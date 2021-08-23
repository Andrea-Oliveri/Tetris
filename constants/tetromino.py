# -*- coding: utf-8 -*-

from constants.gui import REFRESH_PERIOD

# Constant defined as the maps of each tetromino for each rotation
MAPS = { "I": { "DEG_0"  : ((0,0,0,0),
                            (1,1,1,1),
                            (0,0,0,0),
                            (0,0,0,0)) ,
                
                "DEG_90" : ((0,0,1,0),
                            (0,0,1,0),
                            (0,0,1,0),
                            (0,0,1,0)) ,
                
                "DEG_180": ((0,0,0,0),
                            (0,0,0,0),
                            (1,1,1,1),
                            (0,0,0,0)) ,
                
                "DEG_270": ((0,1,0,0),
                            (0,1,0,0),
                            (0,1,0,0),
                            (0,1,0,0)) } ,
        
        
         "L": { "DEG_0"  : ((0,0,1),
                            (1,1,1),
                            (0,0,0)),
                
                "DEG_90" : ((0,1,0),
                            (0,1,0),
                            (0,1,1)),
                
                "DEG_180": ((0,0,0),
                            (1,1,1),
                            (1,0,0)),
                
                "DEG_270": ((1,1,0),
                            (0,1,0),
                            (0,1,0)) } ,
        
        
         "Z": { "DEG_0"  : ((1,1,0),
                            (0,1,1),
                            (0,0,0)) ,
                
                "DEG_90" : ((0,0,1),
                            (0,1,1),
                            (0,1,0)) ,
                
                "DEG_180": ((0,0,0),
                            (1,1,0),
                            (0,1,1)) ,
                
                "DEG_270": ((0,1,0),
                            (1,1,0),
                            (1,0,0)) } ,
        
        
         "J": { "DEG_0"  : ((1,0,0),
                            (1,1,1),
                            (0,0,0)),
                
                "DEG_90" : ((0,1,1),
                            (0,1,0),
                            (0,1,0)),
                
                "DEG_180": ((0,0,0),
                            (1,1,1),
                            (0,0,1)),
                
                "DEG_270": ((0,1,0),
                            (0,1,0),
                            (1,1,0)) } ,
        
        
         "T": { "DEG_0"  : ((0,1,0),
                            (1,1,1),
                            (0,0,0)) ,
                
                "DEG_90" : ((0,1,0),
                            (0,1,1),
                            (0,1,0)) ,
                
                "DEG_180": ((0,0,0),
                            (1,1,1),
                            (0,1,0)) ,
                
                "DEG_270": ((0,1,0),
                            (1,1,0),
                            (0,1,0)) } ,
         
         
         "O": { "DEG_0"  : ((1,1),
                            (1,1)) ,
                
                "DEG_90" : ((1,1),
                            (1,1)) ,
                
                "DEG_180": ((1,1),
                            (1,1)) ,
                
                "DEG_270": ((1,1),
                            (1,1)) } ,
         
         
         "S": { "DEG_0"  : ((0,1,1),
                            (1,1,0),
                            (0,0,0)) ,
                
                "DEG_90" : ((0,1,0),
                            (0,1,1),
                            (0,0,1)) ,
                
                "DEG_180": ((0,0,0),
                            (0,1,1),
                            (1,1,0)) ,
                
                "DEG_270": ((1,0,0),
                            (1,1,0),
                            (0,1,0)) }

        }


# Constant defined as the tests to perform for the Super Rotation System
ROTATION_TESTS = { "I": { ("DEG_0"  , "DEG_90" )  : ((0,0), (-2,0), (+1,0), (-2,-1), (+1,+2)),
                          ("DEG_90" , "DEG_0"  )  : ((0,0), (+2,0), (-1,0), (+2,+1), (-1,-2)),
                          ("DEG_90" , "DEG_180")  : ((0,0), (-1,0), (+2,0), (-1,+2), (+2,-1)),
                          ("DEG_180", "DEG_90" )  : ((0,0), (+1,0), (-2,0), (+1,-2), (-2,+1)),
                          ("DEG_180", "DEG_270")  : ((0,0), (+2,0), (-1,0), (+2,+1), (-1,-2)),
                          ("DEG_270", "DEG_180")  : ((0,0), (-2,0), (+1,0), (-2,-1), (+1,+2)),
                          ("DEG_270", "DEG_0"  )  : ((0,0), (+1,0), (-2,0), (+1,-2), (-2,+1)),
                          ("DEG_0"  , "DEG_270")  : ((0,0), (-1,0), (+2,0), (-1,+2), (+2,-1)) } ,
         
        
                   "L": { ("DEG_0"  , "DEG_90" )  : ((0,0), (-1,0), (-1,+1), (0,-2), (-1,-2)),
                          ("DEG_90" , "DEG_0"  )  : ((0,0), (+1,0), (+1,-1), (0,+2), (+1,+2)),
                          ("DEG_90" , "DEG_180")  : ((0,0), (+1,0), (+1,-1), (0,+2), (+1,+2)),
                          ("DEG_180", "DEG_90" )  : ((0,0), (-1,0), (-1,+1), (0,-2), (-1,-2)),
                          ("DEG_180", "DEG_270")  : ((0,0), (+1,0), (+1,+1), (0,-2), (+1,-2)),
                          ("DEG_270", "DEG_180")  : ((0,0), (-1,0), (-1,-1), (0,+2), (-1,+2)),
                          ("DEG_270", "DEG_0"  )  : ((0,0), (-1,0), (-1,-1), (0,+2), (-1,+2)),
                          ("DEG_0"  , "DEG_270")  : ((0,0), (+1,0), (+1,+1), (0,-2), (+1,-2)) }
          
                 }
ROTATION_TESTS["Z"] = ROTATION_TESTS["J"] = ROTATION_TESTS["T"] = ROTATION_TESTS["S"] = ROTATION_TESTS["L"]


# Constant defined as the speed at which tetrominos fall for different levels in G.
# It is then rescaled to account for frame rates different from 60 Hz.
GRAVITY = { 1: 0.01667,  2: 0.021017, 3: 0.026977, 4: 0.035256, 5: 0.04693,
            6: 0.06361,  7: 0.0879,   8: 0.1236,   9: 0.1775,  10: 0.2598,
           11: 0.388,   12: 0.59,    13: 0.92,    14: 1.46,    15: 2.36 }

GRAVITY = {k: v * 60 * REFRESH_PERIOD * 1e-3 for k, v in GRAVITY.items()}


# Constant defining the soft drop factor applied to gravity.
SOFT_DROP_FACTOR = 20


# Constant defining the hard drop speed in G.
HARD_DROP_GRAVITY = 20