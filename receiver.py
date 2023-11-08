"""
Filename: receiver.py
Author: Savannah Alfaro, sea2985
"""
# Standard Imports
import sys


def decode(binary_letter):
    """
    Decodes a letter from its binary value to its character representation.
    :param binary_letter: (str) the binary letter
    :return: (str) the decoded letter
    """
    return chr(int(binary_letter, 2))


def receive(input_filename):
    """
    Decodes and prints a hidden message from an input file.
    :param input_filename: (str) the input filename
    :return: None
    """
    decoded_message = ""
    with open(input_filename, "r") as file:
        for line in file.readlines():
            binary_letter = ""
            whitespace = line.strip("\n")[-7:]

            # transforms tabs and spaces into 1s and 0s
            for character in whitespace:
                if character == "\t":
                    binary_letter += "1"
                elif character == " ":
                    binary_letter += "0"
                else:
                    continue

            # decodes and appends whitespace of length 7
            if len(binary_letter) == 7:
                decoded_message += decode(binary_letter)
    print(decoded_message)


def main():
    # get input filename and call receive
    input_filename = sys.argv[1]
    receive(input_filename)


if __name__ == "__main__":
    main()
