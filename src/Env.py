# Import routines

import numpy as np
import math
import random

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        #action_space will be in form of (p,q), action_space is all set of possible action in env, it should be list of tuples (p,q)
        self.action_space = [(p,q) for p in range(m) for q in range(m) if p != q]

        #state_space, single state form =(m, d, d), should be a list of state = (m,t,d)
        self.state_space = [(state,time,days) for state in range(m) for time in range(t) for days in range(d)]

        # setting initial state to a random state from state_space
        self.state_init = random.choice(self.state_space)

        # Start the first round
        self.reset()

    ## Encoding state (or state-action) for NN input
    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        state_encod = np.zeros(36, dtype=int)
        state_encod[state[0]]=1
        state_encod[m+state[1]]=1
        state_encod[m+t+state[2]]=1
        return state_encod

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 0:
            requests = np.random.poisson(2)
        if location == 1:
            requests = np.random.poisson(12)
        if location == 2:
            requests = np.random.poisson(4)
        if location == 3:
            requests = np.random.poisson(7)
        if location == 4:
            requests = np.random.poisson(8)

        #max requests can go up to 15 only, upper bound
        if requests >15:
            requests =15
        
        possible_actions_index = random.sample(range(0, (m-1)*m ), requests)
        actions = [self.action_space[i] for i in possible_actions_index]
        
        #appending action, which denote rejecting customer requests
        actions.append((0,0))

        return possible_actions_index,actions   

    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        if action==(0,0):
            return -C

        reward = R*(Time_matrix[action[0]][action[1]][state[1]][state[2]]) - C*(Time_matrix[action[0]][action[1]][state[1]][state[2]] + Time_matrix[state[0]][action[0]][state[1]][state[2]])
        return int(reward)

    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        if action == (0,0):
            nexttime, nextday = self.plusThour(1, state[1], state[2])
            next_state = (state[0], nexttime, nextday)
        else:
            time = Time_matrix[action[0]][action[1]][state[1]][state[2]] + Time_matrix[state[0]][action[0]][state[1]][state[2]] 
            print(time)
            nexttime, nextday = self.plusThour(int(time), state[1], state[2])
            next_state = (action[1], nexttime, nextday)
        return next_state

    def plusThour(self, time, currenttime, currentday):
        if currenttime + time >= 23:
            if currentday == 6:
                return (currenttime+time)%24, 0
            else:
                return (currenttime+time)%24, currentday+1
        else:
            return currenttime+time, currentday

    def reset(self):
        return self.action_space, self.state_space, self.state_init


