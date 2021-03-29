import math
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    if not params['all_wheels_on_track']:
        return 1e-3
    
    rewards = dict.fromkeys(['speed','heading','steering'],0.0)
    weights = dict.fromkeys(['speed','heading','steering'],1000.0)
    weights['steering'] = 500.0
    weights['speed'] = 1500.0
        
    next_waypoint = params['waypoints'][params['closest_waypoints'][1]]
    prev_waypoint = params['waypoints'][params['closest_waypoints'][0]]
    
    ideal_direction = math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0])
    ideal_direction = math.degrees(ideal_direction)
    
    direction_offset = abs(ideal_direction - params['heading'])
    direction_offset = min(direction_offset, 360 - direction_offset)
    
    rewards['heading'] = (1 - direction_offset/180.0) * weights['heading']
    
    rewards['steering'] = (1 - (abs(params['steering_angle'] - direction_offset))/180.0) * weights['steering']
    
    rewards['speed'] = params['speed'] * params['speed']
    return sum(rewards.values())