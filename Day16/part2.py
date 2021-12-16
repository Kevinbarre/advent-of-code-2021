import math


def parse_packet(packet):
    version = int(packet[:3], base=2)
    packet_type = int(packet[3:6], base=2)
    packet = packet[6:]

    if packet_type == 4:
        # Litteral value
        value, packet = parse_litteral_value(packet)
        return (version, packet_type, value), packet
    else:
        # Operator
        subpackets, packet = parse_operator(packet)
        return (version, packet_type, subpackets), packet


def parse_litteral_value(packet):
    value_binary = ''
    nb_loops = 1
    while True:
        first_bit = packet[0]
        value_binary += packet[1:5]
        packet = packet[5:]
        if first_bit == '1':
            # Not the last group, keep reading
            nb_loops += 1
            continue
        else:
            # Last group, end of packet
            return int(value_binary, base=2), packet


def parse_operator(packet):
    length_type_id = packet[0]
    packet = packet[1:]

    if length_type_id == '0':
        # Next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
        total_length = int(packet[:15], base=2)
        packet = packet[15:]
        return parse_subpackets_by_length(total_length, packet)
    else:
        # Next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
        nb_sub_packets = int(packet[:11], base=2)
        packet = packet[11:]
        return parse_subpackets_by_number(nb_sub_packets, packet)


def parse_subpackets_by_length(length, packet):
    subpackets_binary = packet[:length]
    packet = packet[length:]
    subpackets = []
    while subpackets_binary:
        subpacket, subpackets_binary = parse_packet(subpackets_binary)
        subpackets.append(subpacket)

    return subpackets, packet


def parse_subpackets_by_number(nb, packet):
    subpackets = []
    for i in range(nb):
        subpacket, packet = parse_packet(packet)
        subpackets.append(subpacket)

    return subpackets, packet


def sum_packet_versions(packet):
    """Sum versions of a parsed packet"""
    version, packet_type, subpackets = packet
    if packet_type == 4:
        # Litteral value, return version
        return version
    else:
        # Return version plus sum of subpackets versions
        return version + sum(sum_packet_versions(subpacket) for subpacket in subpackets)


def compute_packet_expression(packet):
    """Compute expression of a parsed packet"""
    # print("Packet", packet)
    _, packet_type, subpackets = packet
    # print("Packet type", packet_type)
    # print("Subpackets", subpackets)
    if packet_type == 4:
        # Litteral value, return value contained in subpackets
        return subpackets
    elif packet_type == 0:
        # Sum packets
        return sum(compute_packet_expression(subpacket) for subpacket in subpackets)
    elif packet_type == 1:
        # Product packets
        return math.prod(compute_packet_expression(subpacket) for subpacket in subpackets)
    elif packet_type == 2:
        # Minimum packets
        return min(compute_packet_expression(subpacket) for subpacket in subpackets)
    elif packet_type == 3:
        # Maximum packets
        return max(compute_packet_expression(subpacket) for subpacket in subpackets)
    elif packet_type == 5:
        # Greater than packets
        first, second = (compute_packet_expression(subpacket) for subpacket in subpackets)
        return 1 if first > second else 0
    elif packet_type == 6:
        # Less than packets
        first, second = (compute_packet_expression(subpacket) for subpacket in subpackets)
        return 1 if first < second else 0
    elif packet_type == 7:
        # Equal to packets
        first, second = (compute_packet_expression(subpacket) for subpacket in subpackets)
        return 1 if first == second else 0
    else:
        raise TypeError


hex_input = input()
main_packet = int(hex_input, base=16)
main_packet = format(main_packet, '0b').zfill(
    len(hex_input) * 4)  # Binary representation with padded 0 to reach multiples of 4
# print(main_packet)

main_packet, _ = parse_packet(main_packet)
print(main_packet)

print("Result:", compute_packet_expression(main_packet))
