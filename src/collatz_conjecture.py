#-*- coding: utf-8 -*-
import sys

def decompose_number(number):
    counter = 1
    while (number > 1):
        if int(number) % 2 == 0:
            number = number/2
        else:
            number = (3 * number) + 1
        counter = counter + 1
    return counter

def execute(number):
    larger_sequence_number = 0
    larger_sequence = 0
    for i in range(number):
        sequence = decompose_number(i)
        if sequence > larger_sequence:
            larger_sequence = sequence
            larger_sequence_number = i
    print larger_sequence_number

def main():
    number = int(sys.argv[1])
    execute(number)

if __name__ == '__main__':
    main()