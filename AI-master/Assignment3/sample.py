# sample.py for CS4341 Assignment 3
# @author Everett Harding
# @author Kenedi Heather
# @author Dean Schifilliti
# @author Dan Seaman

import sys
from probabilities import *
import statistics
import numpy as np
import scipy as sp
import scipy.stats
 
name, status = sys.argv[1].split('=')
name = name.lower()
 
if status.lower() == 'true':
    status = True
elif status.lower() == 'false':
    status = False
else: status = status.upper()
 
inputNode = [name, status]
runs = int(sys.argv[2])
 
 
givens = {} 
i = 3
 
while i < len(sys.argv):
    name, status =  sys.argv[i].split('=')
    if status.lower() == 'true':
        status = True
    elif status.lower() == 'false':
        status = False

    if type(status) is str:
        givens[name.lower()] = status.upper()
    else:
        givens[name.lower()] = status
    
    i+=1


iterations = 0
acceptedResults = []
numbers = []
accepted = 0
acceptedMatch = 0
while iterations < runs:
    nodeValues = generateGraph() #humidity, temperature, day, icy, snow, cloudy, exams, stress
    acceptNode = True
    
    for node in nodeValues:
        if node in givens and nodeValues[node][0] != givens[node]:
            acceptNode = False
    
    if acceptNode:
        acceptedResults.append(nodeValues[inputNode[0]][0])
        numbers.append(nodeValues[inputNode[0]][1])
        queryNode = inputNode[0]
        queryStatus = inputNode[1]
        if nodeValues[queryNode][0] == queryStatus:
            acceptedMatch +=1

    iterations += 1

valid = 0
if len(acceptedResults) != 0:
    valid = acceptedMatch/len(acceptedResults)


#from StackOverflow user "shasan":
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    #return h
    return m, h, m-h, m+h


print("Samples completed: ", runs)
print("Accepted samples: ", len(acceptedResults))
print("Accepted valid results: ", acceptedMatch)
print("P(",inputNode[0],") = ", valid)
if len(numbers) > 1:
    stats = mean_confidence_interval(numbers)
    print("Mean: ", stats[0])
    print("Standard Deviation: ", statistics.stdev(numbers))
    print("95% confidnce intervals: Mean +/- ", stats[1], " ->", stats[2:])
else:
    print("Not enough accepted values to calculate statistics")
