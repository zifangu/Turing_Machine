# Turing_Machine

tm.py will read in a text file called tm.txt and construct a theoretical turing machine. Then it reads in input.txt to determine whether each input strings can be accepted or not by the turing machine. The result is reflected in output.txt as each line contains the result "accetpt" or "reject" for every line in input.txt.

Files "tm.txt" and "tm copy.txt" are different test files for tm.py. Both test cases produced consisent answers identical to the results from manually contructed turing machines.

tm.txt structure:
 Line 1: the states of the Turing machine (separated by commas, and ‘accept’ and ‘reject’ will always be states)
 Line 2: the input alphabet (separated by commas, if there is more than one symbol)
 Line 3: the tape alphabet (separated by commas, if there is more than one symbol, and assume that ‘_’ represents a blank space on the tape)
 Line 4: the starting state of the Turing machine
 Line 5 and onward: the transition rules, where each rule takes the form a,b,c,d,e (where being in state a and reading symbol b on the tape will write a c to that location, move to new state d, and move the read/write head in direction e)

