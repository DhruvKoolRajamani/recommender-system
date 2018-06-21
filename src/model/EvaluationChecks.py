# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:12:33 2018

@author: Steff
"""

query = [[
     ["A","B","C"]
     ,["A"]
     ,["A","B"]
     ,["A","B"]
     ,["A","B"]
     ,["C","D"]
]]

truth = [[
    ["B"]
    ,["B"]
    ,["A"]
    ,["A","C"]
    ,["A","B","C","D"]
    ,["A","B","C","D"]
]]

# MeanRecall:
# ---------
# 1.0
# 0.0
# 1.0
# 0.5
# 0.5
# 0.5
# = 3.5/6 = 0.583

# MeanPrecision:
# ---------
# 0.33
# 0.0
# 0.5
# 0.5
# 1.0
# 1.0
# = 3.33/6 = 0.556

# MAP:
# ---------
# 0.5
# 0.0
# 1.0
# (1)/2 = 0.5
# (1+1)/4 = 0.5
# (1+1)/4 = 0.5
# = 3/6 = 0.5

print("Computing Recall.")
from MeanRecallEvaluation import MeanRecallEvaluation
evaluation = MeanRecallEvaluation()
ev_recall = round(evaluation.evaluate(query, truth),3)

print("Computing Precision.")
from MeanPrecisionEvaluation import MeanPrecisionEvaluation
evaluation = MeanPrecisionEvaluation()
ev_precision = round(evaluation.evaluate(query, truth),3)

print("Computing MAP.")
from MAPEvaluation import MAPEvaluation
evaluation = MAPEvaluation()
ev_map = evaluation.evaluate(query, truth)

print("Recall: {}, Precision: {}, MAP: {}".format(ev_recall,ev_precision,ev_map))