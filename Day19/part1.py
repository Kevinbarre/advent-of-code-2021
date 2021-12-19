import itertools
import sys
from pprint import pprint

NB_MATCHING_BEACONS = 12
NB_MATCHING_VECTORS = NB_MATCHING_BEACONS * (NB_MATCHING_BEACONS - 1) // 2


class Vector:
    def __init__(self, x, y, z, a, b):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z) or (
                self.x == -other.x and self.y == -other.y and self.z == -other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z)) + hash((-self.x, -self.y, -self.z))

    def __repr__(self):
        return "Vector(x=%r, y=%r, z=%r, a=%r, b=%r)" % (self.x, self.y, self.z, self.a, self.b)

    def __str__(self):
        return "({},{},{}) from a:{} and b:{}".format(self.x, self.y, self.z, self.a, self.b)


class Scanner:
    def __init__(self, name):
        self.name = name
        self.beacons = set()
        self.vectors = set()
        self.orientations = []

    def __repr__(self):
        return "Scanner(name=%r, beacons=%r, vectors=%r)" % (self.name, self.beacons, self.vectors)

    def __str__(self):
        return "Scanner {} - Beacons: [{}]. Vectors: [{}]".format(self.name, self.beacons, self.vectors)

    def compute_vectors(self):
        for first, second in itertools.combinations(self.beacons, 2):
            vector = Vector(*(first[i] - second[i] for i in range(3)), first, second)
            self.vectors.add(vector)

    def get_orientations(self):
        # Compute orientations only once
        if not self.orientations:
            # Iterate over all possible rotations
            for rotation in ROTATIONS:
                orientation = Scanner(self.name)
                # Get new coordinates after rotation for each beacon
                orientation.beacons.update(rotation(x, y, z) for x, y, z in self.beacons)
                # Compute vectors of this orientation
                orientation.compute_vectors()
                # Add it to the list
                self.orientations.append(orientation)
        return self.orientations


ROTATIONS = [
    # Positive x
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (x, z, -y),
    # Negative x
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -z, -y),
    # Positive y
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (y, x, -z),
    # Negative y
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -x, -z),
    # Positive z
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (z, y, -x),
    # Negative z
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -y, -x)
]


def extract_scanner_beacons_into_main_scanner(extracted_scanner):
    # print("Main scanner vectors: {}".format(main_scanner.vectors))
    # print("Extracted scanner vectors: {}".format(extracted_scanner.vectors))
    intersection = main_scanner.vectors.intersection(extracted_scanner.vectors)
    # print("Intersection size {} for extracted scanner {}".format(len(intersection), extracted_scanner.name))
    if len(intersection) >= NB_MATCHING_VECTORS:
        # print("Intersection with enough matching elements:")
        # pprint(intersection)
        # Found a matching scanner
        # Get first vector of intersection, to find coordinates of extracted_scanner from main scanner point of view
        any_scanner_vector = intersection.pop()  # Don't know from which set this comes from !
        # Need to research it in both scanners
        main_scanner_vector = next(v for v in main_scanner.vectors if v == any_scanner_vector)
        extracted_scanner_vector = next(v for v in extracted_scanner.vectors if v == any_scanner_vector)

        # print("Vector for main scanner", main_scanner_vector)
        # print("Vector for extracted scanner", extracted_scanner_vector)

        # Check if scanners are both built from same origin AB
        # OO' = OA + AO'
        origins_vector_from_a = tuple(main_scanner_vector.a[i] - extracted_scanner_vector.a[i] for i in range(3))
        origins_vector_from_b = tuple(main_scanner_vector.b[i] - extracted_scanner_vector.b[i] for i in range(3))

        if not origins_vector_from_a == origins_vector_from_b:
            # A and B are reversed
            origins_vector_from_a = tuple(main_scanner_vector.a[i] - extracted_scanner_vector.b[i] for i in range(3))
            # origins_vector_from_b = (main_scanner_vector.b[i] - extracted_scanner_vector.a[i] for i in range(3))
        print("Coordinates of origin of extracted scanner {} are:".format(extracted_scanner.name), origins_vector_from_a)

        # Extract all beacons to the main_scanner coordinates
        new_beacons = set()
        for beacon in extracted_scanner.beacons:
            beacon_for_main_scanner = tuple(origins_vector_from_a[i] + beacon[i] for i in range(3))
            # print("Beacon for main scanner:", beacon_for_main_scanner)
            new_beacons.add(beacon_for_main_scanner)
        # Add new beacons to main scanner
        main_scanner.beacons.update(new_beacons)
        # Need to recompute all vectors for new beacons to add to main scanner
        for first, second in itertools.combinations(new_beacons, 2):
            vector = Vector(*(first[i] - second[i] for i in range(3)), first, second)
            main_scanner.vectors.add(vector)

        return True
    return False


scanners = []
scanner_count = 0
current_scanner = Scanner(scanner_count)
for line in sys.stdin:
    if line.startswith('---'):
        # Next line is a scanner
        continue
    elif line == '\n':
        # Empty line, end of current_scanner
        scanners.append(current_scanner)
        scanner_count += 1
        current_scanner = Scanner(scanner_count)
        continue
    else:
        # Coordinates
        current_scanner.beacons.add(tuple(map(int, line.rstrip('\n').split(','))))

# Final scanner to add
scanners.append(current_scanner)

for scanner in scanners:
    scanner.compute_vectors()

# pprint(scanners)
main_scanner = scanners.pop(0)

# for main_scanner_orientation in main_scanner.get_orientations():
#     print(main_scanner_orientation)

while scanners:
    scanner_removed = False
    # Find other scanner matching 12 vectors of main scanner
    for scanner in scanners:
        for scanner_orientation in scanner.get_orientations():
            if extract_scanner_beacons_into_main_scanner(scanner_orientation):
                scanner_removed = True
                break

        if scanner_removed:
            # No need for scanner anymore, remove it from scanners
            # print("Remove scanner", scanner.name)
            scanners.remove(scanner)
            # Start again with the whole list of remaining scanners
            break

    if not scanner_removed:
        print("ERROR: Infinite loop reached, we just break to exit")
        break

# print(main_scanner)
print("Result:", len(main_scanner.beacons))
