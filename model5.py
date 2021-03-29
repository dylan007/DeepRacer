import math


def reward_function(params):
    '''
    Hope to find the racing line 
    '''

    if not params['all_wheels_on_track']:
        return 1e-3

    # penalize non stationary action
    if params['speed'] < 1.33:
        return 1e-3

    reward = 1e-3

    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"])
                  * 100) + (params["speed"]**2)

    return reward
