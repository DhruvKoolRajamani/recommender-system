# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:31:50 2018

@author: Steff
"""

from AbstractClasses import AbstractEvaluation

class MeanPrecisionEvaluation(AbstractEvaluation):
    
    def __init__(self,none_value=1):
        self.none_value = none_value
    
    def evaluate(self,recommendation,truth):
        """
        Calculates the fraction of attended conferences that were recommended.
        
        Args:
            recommendation (list): The list of recommendations returned 
                                    by the model.
            truth (list): The test set list of conferences attended
        
        Returns:
            int: #recommended and attended conferences / #attended conferences
            
        """
        precision = 0
        size = len(recommendation[0])
        for i in range(size):
            if recommendation[0][i] is None:
                precision += self.none_value
            elif truth[0][i] is None:
                precision += 0
            else:
                q_s = set(recommendation[0][i])
                t_s = set(truth[0][i])
                precision += len(q_s.intersection(t_s)) / len(q_s)
            
        return precision/size