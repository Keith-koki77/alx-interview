#!/usr/bin/python3
"""
Python script for UTF-8 Validation
"""


def validUTF8(data):
    # Count of consecutive 1s in the most significant bits
    num_bytes = 0

    for num in data:
        # Check if the current number is a continuation byte
        if num >> 7 == 1 and (num >> 6) & 1 == 0:
            if num_bytes == 0:
                return False  # Invalid sequence
            num_bytes -= 1
        elif num >> 7 == 0:
            if num_bytes > 0:
                return False  # Incomplete sequence
        elif num >> 6 == 0b10:
            if num_bytes == 0:
                return False  # Misplaced continuation byte
            num_bytes -= 1
        elif num >> 5 == 0b110:
            num_bytes = 1
        elif num >> 4 == 0b1110:
            num_bytes = 2
        elif num >> 3 == 0b11110:
            num_bytes = 3
        else:
            return False  # Invalid leading byte

    return num_bytes == 0
