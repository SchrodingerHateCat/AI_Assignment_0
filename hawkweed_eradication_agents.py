""" File name:   hawkweed_eradication_agents.py
    Author:      <your name goes here>
    Date:        <the date goes here>
    Description: This file contains agents which manage and eradicate hawkweed. 
                 It is used in Exercise 4 of Assignment 0.
"""

import random


class HawkweedEradicationAgent:
    """ A simple hawkweed eradication agent. """

    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.

            (HawkweedEradicationAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, hawkweed, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an invalid move will cause the system to stop.

            Changing any of the mutable parameters will have no effect on the operation
            of the system.

            This agent will locally move to the highest hawkweed population, if there is
            is no nearby hawkweed, it will act randomly.

            (HawkweedEradicationAgent, str, [str], [str], { str : float }, float, float, float) -> str
        """
        max_hawkweed = None
        max_move = None
        for move in valid_moves:
            if max_hawkweed is None or hawkweed[move] > max_hawkweed:
                max_hawkweed = hawkweed[move]
                max_move = move

        if not max_hawkweed:
            return random.choice(valid_moves)

        return max_move


# Make a new agent here called SmartHawkweedEradicationAgent, which extends HawkweedEradicationAgent and
# acts a bit more sensibly. Feel free to add other helper functions if needed.

class SmartHawkweedEradicationAgent(HawkweedEradicationAgent):
    def __init__(self, locations, conn):
        """ YOUR CODE HERE. """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, hawkweed, threshold, growth, spread):
        """ YOUR CODE HERE. """
        # simply use A* search, find the highest hawkweed on the map
        # then find the path to this location
        # additionaly use hawkweed / threshold as another rule to find the path

        # in general: agent will find the quickest path to highest hawkweed, at the same time
        # it will choose the way that kill more hawkweed

        target = sorted(hawkweed.items(), key=lambda item:item[1])[-1][0]   # sort hawkweed get the highest
        print('target is :' + target)
        found = False
        openList = [location]                                               
        cameFrom = {location:''}
        costSoFar = {location:0}
        # A* search main loop
        while len(openList) > 0 and not found:
            current = openList[0]
            openList.pop(0)
            if current != '':
                if current == target:                           # find the highest hawkweed
                    found = True
                    #cameFrom[target] = current

                else:
                    for nextPos in self.conn[current]:
                        match = False
                        for locationMatch in costSoFar:         # if this location is aleardy arrived
                            if locationMatch == nextPos:
                                match = True
                        
                        # Here is the core of A* search
                        # the rule is find the lowest cost
                        # costSoFar save the cost so far value to this location
                        # +2 means distance between each location is same (not interested in distance)
                        # hawkweed/threshold display how emergency this location is
                        # with larger hawkweed value, the cost is lower
                        newCost = costSoFar[current] + 2 - hawkweed[nextPos]/threshold
                        if not match:                           #  if this is a new location
                            costSoFar[nextPos] = newCost
                            openList.append(nextPos)
                            cameFrom[nextPos] = current
                        elif newCost < costSoFar[nextPos]:      # if it arrived
                            costSoFar[nextPos] = newCost
                            openList.append(nextPos)
                            cameFrom[nextPos] = current
        path = [target]
        pathFrom = target
        #print(cameFrom)
        while pathFrom != location:
            pathFrom = cameFrom[pathFrom]
            path.append(pathFrom)
        return path[-2]                                         # return the next step
