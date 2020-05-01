#!/usr/bin/env python3

"""
Author: Zifan(Ivan) Gu

tm.txt structure:
 Line 1: the states of the Turing machine (separated by commas, and ‘accept’ and ‘reject’ will always be states)
 Line 2: the input alphabet (separated by commas, if there is more than one symbol)
 Line 3: the tape alphabet (separated by commas, if there is more than one symbol, and assume that ‘_’ represents a blank space on the tape)
 Line 4: the starting state of the Turing machine
 Line 5 and onward: the transition rules, where each rule takes the form a,b,c,d,e (where being in state a and reading symbol b on the tape will write a c to that location, move to new state d, and move the read/write head in direction e)

Algorithm:
    1. Read in tm.txt
    2. Collect starting state from line 4, no final states needs to be connected. It's embedded in the transition rules.
    3. Form line 5 and onward: 2-tuple and 3-tuple
    4. 2-tuple: (a, b). If in state a, and read in char b, execute the 3-tuple
    5. 3-tuple: (c, d, e). c is the character replacing b d is the new state, e is where the next pointer goes to (either R or L)
    6. If within the execution a state of "accept" or "reject" is reached, return the function immediately.
"""


def open_file(filename):
    file = open(filename, "r")
    content = file.readlines()
    file.close()
    return content

def tm_process(start_state, string, dict):
    """
    :param start_state: the initial state of the turing machine
    :param string: the input string
    :param dict: 2-tuple is the key, 3-tuple is the value
    :return: either "accept" or "reject"
    """
    pro_list = list(string)
    # randomly chose a number to put "_"(blank space) on the tape
    for i in range(5):
        pro_list.append("_")

    counter = 0
    curr_state = start_state
    while counter < len(pro_list):
        # given the 2-tuple, find the value of the 3-tuple
        temp_tuple = dict.get((curr_state, pro_list[counter]))

        # if value to the key exist, execute 3-tuple
        if temp_tuple is not None:
            # print("location:", counter)

            # overrwrite the value on the tape
            pro_list[counter] = temp_tuple[0]

            # set the current state
            curr_state = temp_tuple[1]

            # check if the state is "accept", if so, return the state
            if curr_state == "accept":
                return curr_state
            # else, move the read/write pin to the left or right accordingly
            if temp_tuple[2] == 'R':
                counter += 1
            else:
                counter -= 1

        # if no dictionary value, immediately return "reject"
        else:
            # print("location reject:", counter)
            return "reject"




def main():
    # read in "tm.txt" which contains information listed in the above documentation
    tm = open_file("tm.txt")
    start_state = ""
    tm_dictionary = {}
    counter = 0

    for line in tm:
        line = line.strip()
        if counter == 3:
            start_state = line
        elif counter > 3:
            temp = line.split(",")
            # print(temp)
            tm_dictionary[(temp[0], temp[1])] = (temp[2], temp[3], temp[4])

        counter += 1
    # print("start:", start_state)
    # print("tm:", tm_dictionary)

    # read in input.txt and extract the strings to be processed
    trans_states = open_file("input.txt")
    transition = []
    for line in trans_states:
        line = line.strip()
        transition.append(line)

    # append the result of turing machine processing to the list and write to "output.txt"
    result_list = []
    for i in transition:
        result_list.append(tm_process(start_state, i, tm_dictionary))

    output = open("output.txt", "w+")
    count = 1
    for i in result_list:
        if count != len(result_list):
            output.write(i)
            output.write("\n")
        else:
            output.write(i)
        count += 1


main()
