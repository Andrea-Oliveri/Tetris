# -*- coding: utf-8 -*-


class Score:
    """Class Score. Class dealing with updating of the score."""

    def __init__(self):
        """Constructor for the class Score."""
        self._score = 0
        self._back_to_back = False
        
        
    def _get_score(self):
        """Special function that allows to get the attribute _score from the exterior."""
        return self._score
    
    
    """Definition of a properties for parameter _score. This parameter can
    only be get from the exteriour, not set nor deleted."""
    score = property(_get_score)
        
        
    def add_to_score(self, action_type, parameters):
        """Adds points to the score based on the action type and data in parameters dictionary."""
                    
        if action_type == "single":
            self._score += 100 * parameters["level"]
            self._back_to_back = False
            
        elif action_type == "double":
            self._score += 300 * parameters["level"]
            self._back_to_back = False
            
        elif action_type == "triple":
            self._score += 500 * parameters["level"]
            self._back_to_back = False
            
        elif action_type == "tetris":
            if self._back_to_back:
                self._score += 1200 * parameters["level"]
            else:
                self._score += 800 * parameters["level"]
            self._back_to_back = True
            
#        elif action_type == "tspin_mini_no_lines":
#            self._score += 100 * parameters["level"]
            
        elif action_type == "tspin_no_lines":
            self._score += 400 * parameters["level"]
            
#        elif action_type == "tspin_mini_single":
#            if self._back_to_back:
#                self._score += 300 * parameters["level"]
#            else:
#                self._score += 200 * parameters["level"]
#            self._back_to_back = True
            
        elif action_type == "tspin_single":
            if self._back_to_back:
                self._score += 1200 * parameters["level"]
            else:
                self._score += 800 * parameters["level"]
            self._back_to_back = True
            
#        elif action_type == "tspin_mini_double":
#            if self._back_to_back:
#                self._score += 600 * parameters["level"]
#            else:
#                self._score += 400 * parameters["level"]
#            self._back_to_back = True
            
        elif action_type == "tspin_double":
            if self._back_to_back:
                self._score += 1800 * parameters["level"]
            else:
                self._score += 1200 * parameters["level"]
            self._back_to_back = True
            
        elif action_type == "tspin_triple":
            if self._back_to_back:
                self._score += 2400 * parameters["level"]
            else:
                self._score += 1600 * parameters["level"]
            self._back_to_back = True
            
        elif action_type == "soft_drop":
            self._score += parameters["n_lines"]
                
        elif action_type == "hard_drop":
            self._score += 2 * parameters["n_lines"]
           
        else:
            raise ValueError(f"Invalid attribute value for action_type: {action_type}")
            
            
    def add_perfect_bonus_to_score(self, n_lines, level):
        """Adds points for perfect bonus to the score based on the number of cleared lines."""
        
        if n_lines == 1:
            self._score += 800 * level
            
        elif n_lines == 2:
            self._score += 1200 * level
            
        elif n_lines == 3:
            self._score += 1800 * level
            
        elif n_lines == 4:
            if self._back_to_back:
                self._score += 3200 * level
            else:
                self._score += 2000 * level