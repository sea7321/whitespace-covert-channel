"""
Filename: sender.py
Author: Savannah Alfaro, sea2985
"""
# Standard Imports
import sys


def encode(character):
    """
    Encodes a character using tabs and spaces from the binary value.
    :param character: (char) the character to encode
    :return: (str) the encoded character
    """
    encoded_letter = ""
    binary_letter = format(ord(character), '07b')

    # transforms 1s and 0s into tabs and spaces
    for digit in binary_letter:
        if digit == "1":
            encoded_letter += "\t"
        elif digit == "0":
            encoded_letter += " "
    return encoded_letter


def send(output_filename):
    """
    Sends a hidden message and writes it to an output file.
    :param output_filename: (str) the output filename
    :return: None
    """
    message = input("Enter your hidden message: ")
    encoded_message = ""

    # encode each hidden message character at the end of each line of the message
    for index in range(0, len(message)):
        line = input("Enter line #{} of the message: ".format(index + 1))
        line += encode(message[index])
        encoded_message += line

        # append a newline character
        if index != (len(message) - 1):
            encoded_message += "\n"

    # write message to an output file
    with open(output_filename, "w") as file:
        file.write(encoded_message)


def main():
    # get output filename and call send
    output_filename = sys.argv[1]
    send(output_filename)


if __name__ == "__main__":
    main()
