""" File name:   hawkweed_scenario.py
    Author: Zhengduo Zhu
    Date: 4/03/2021
    Description: This file represents a scenario simulating the spread of 
                 hawkweed through Kosciuszko National Park and its
                 surroundings. It should be implemented for Part 1 of 
                 Exercise 4 of Assignment 0.

                 See the lab notes for a description of its contents.
"""
import copy

class HawkweedScenario:
    def __init__(self):
        """ YOUR CODE HERE. """
        self.locations = []
        self.hawkweed = {}
        self.conn = {}

    def read_scenario_file(self, path_to_scenario_file):
        """ YOUR CODE HERE. """
        # try to open the file can read
        try:
            with open(path_to_scenario_file) as scenario_file:
                for line in scenario_file:
                    category = line.split()[0]                      # set first string as category
                    if category == 'threshold':                     # save threshold as float
                        self.threshold = float(line.split()[1])
                    elif category == 'growth':                      # save growth as float
                        self.growth = float(line.split()[1])
                    elif category == 'spread':                      # save spread as float
                        self.spread = float(line.split()[1])
                    elif category == 'location':
                        self.locations.append(line.split()[1])
                        if line.split()[1] not in self.hawkweed:    # check loaction exist in hawkweed
                            self.hawkweed[line.split()[1]] = 0      # set default value to 0
                        if line.split()[1] not in self.conn:        # check location exist in connection
                            self.conn[line.split()[1]] = set()      # set default value to empty set
                    elif category == 'start':                       # save start location as location
                        self.location = line.split()[1]
                    elif category == 'hawkweed':                    # write hawkweed value
                        self.hawkweed[line.split()[1]] = float(line.split()[2])
                    elif category == 'conn':
                        loc1 = line.split()[1]
                        loc2 = line.split()[2]
                        if loc1 not in self.conn:                   # check existing
                            self.conn[loc1] = set()
                        if loc2 not in self.conn:
                            self.conn[loc2] = set()
                        self.conn[loc1].add(loc2)                   # save value
                        self.conn[loc2].add(loc1)
            return True
        except IOError:
            print("IOError")
            return False


    def valid_moves(self):
        """ YOUR CODE HERE. """
        movement = copy.deepcopy(self.conn[self.location])
        movement.add(self.location)
        return list(movement)

    def move(self, loc):
        """ YOUR CODE HERE. """
        validMove = self.valid_moves()
        if loc not in validMove:
            raise ValueError
        else:
            self.location = loc
            self.hawkweed[self.location] = 0

    def spread_hawkweed(self):
        """ YOUR CODE HERE. """
        result = copy.deepcopy(self.hawkweed)
        for key in self.hawkweed:
            if key != self.location:
                if self.hawkweed[key] >= self.threshold:
                    spreadList = self.conn[key]
                    for spreadItem in spreadList:
                        if spreadItem != self.location:
                            result[spreadItem] = result[spreadItem] + self.spread * self.hawkweed[key]
                result[key] = result[key] + self.growth * self.hawkweed[key]
        self.hawkweed = result