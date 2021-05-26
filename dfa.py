""" File name:   dfa.py
    Author:      <Zhengduo Zhu>
    Date:        <3/03/2021>
    Description: This file defines a function which reads in
                 a DFA described in a file and builds an appropriate datastructure.

                 There is also another function which takes this DFA and a word
                 and returns if the word is accepted by the DFA.

                 It should be implemented for Exercise 3 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""


def load_dfa(path_to_dfa_file):
    """ This function reads the DFA in the specified file and returns a
        data structure representing it. It is up to you to choose an appropriate
        data structure. The returned DFA will be used by your accepts_word
        function. Consider using a tuple to hold the parts of your DFA, one of which
        might be a dictionary containing the edges.

        We suggest that you return a tuple containing the names of the start
        and accepting states, and a dictionary which represents the edges in
        the DFA.

        (str) -> Object
    """

    # YOUR CODE HERE
    
    # initialize container
    initial = []
    accepting = []
    transition = {}
    output = {}

    # open the .dfa file and read as line   
    with open(path_to_dfa_file) as dfa_file:
        for line in dfa_file:
            category = line.split()[0]                          # category display the category of lines
            if category == "initial":                           # if it is initial then save from second string
                for word in line.split()[1:]:
                    initial.append(word)
            elif category == "accepting":                       # same as initial 
                for word in line.split()[1:]:
                    accepting.append(word)
            elif category == "transition":                      # save as a dictionary
                key = line.split()[1]+' '+line.split()[3]       # the key is start node and transition value
                value = line.split()[2]                         # the value is end node
                transition[key] = value
            else:
                print("wrong form")
    
    # put all the variables into output
    output['initial'] = initial
    output['accepting'] = accepting
    output['transition'] = transition
    return output
    



def accepts_word(dfa, word):
    """ This function takes in a DFA (that is produced by your load_dfa function)
        and then returns True if the DFA accepts the given word, and False
        otherwise.

        (Object, str) -> bool
    """

    # YOUR CODE HERE

    # read data from dfa
    initial = dfa['initial']
    accepting = dfa['accepting']
    transition = dfa['transition']

    # initialize state
    state = initial[0]

    # start looping
    for i in range(len(word)+1):
        # come to end
        if i == len(word):
            if state in accepting:
                return True
            else:
                return False
        key = state + ' ' + word[i]
        # check edges
        if key in transition:
            state = transition[key]
        else:
            return False