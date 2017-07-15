# probabilties.py for CS4341 Assignment 3
# @author Everett Harding
# @author Kenedi Heather
# @author Dean Schifilliti
# @author Dan Seaman

from random import random
 
def generateHumidity():
    ran = random()
    if ran < .2:
        return "LOW", ran 
    elif ran >= .2 and ran < .7:
        return "MEDIUM", ran
    else:
        return "HIGH", ran
 
def generateTemperature():
    ran = random()
    if ran < .1:
        return "WARM", ran
    elif ran >= .1 and ran < .5:
        return "MILD", ran
    else:
        return "COLD", ran
 
def generateIcy(humidity, temperature):
    ran = random()
    humidity = humidity_state[humidity];
    humidity = temperature_state[temperature];
    if humidity == 0 and temperature == 0:
        if ran < .001:
            return True, ran
        else:
            return False, ran
    elif humidity == 0 and temperature == 1:
        if ran < .01:
            return True, ran
        else:
            return False, ran
    elif humidity == 0 and temperature == 2:
        if ran < .05:
            return True, ran
        else:
            return False, ran
    elif humidity == 1 and temperature == 0:
        if ran < .001:
            return True, ran
        else:
            return False, ran
    elif humidity == 1 and temperature == 1:
        if(ran < .03):
            return True, ran
        else:
            return False, ran
    elif humidity == 1 and temperature == 2:
        if ran < .2:
            return True, ran
        else:
            return False, ran
    elif humidity == 2 and temperature == 0:
        if ran < .005:
            return True, ran
        else:
            return False, ran
    elif humidity == 2 and temperature == 1:
        if ran < .01:
            return True, ran
        else:
            return False, ran
    else:
        if ran < .35:
            return True, ran
        else:
            return False, ran
 
def generateSnow(humidity, temperature):
    ran = random()
    humidity = humidity_state[humidity];
    temperature = temperature_state[temperature];
    if humidity == 0 and temperature == 0:
        if ran < .0001:
            return True, ran
        else:
            return False, ran
    elif humidity == 0 and temperature == 1:
        if ran < .001:
            return True, ran
        else:
            return False, ran
    elif humidity == 0 and temperature == 2:
        if ran < .1:
            return True, ran
        else:
            return False, ran
    elif humidity == 1 and temperature == 0:
        if ran < .0001:
            return True, ran
        else:
            return False, ran
    elif humidity == 1 and temperature == 1:
        if ran < .0001:
            return True, ran
        else:
            return False, ran
    elif humidity == 1 and temperature == 2:
        if ran < .25:
            return True, ran
        else:
            return False, ran
    elif humidity == 2 and temperature == 0:
        if ran < .0001:
            return True, ran
        else:
            return False, ran
    elif humidity == 2 and temperature == 1:
        if ran < .001:
            return True, ran
        else:
            return False, ran
    elif humidity == 2 and temperature == 2:
        if ran < .4:
            return True, ran
        else:
            return False, ran
 
def generateDay():
    ran = random()
    if ran > .2:
        return "WEEKDAY", ran
    else:
        return "WEEKEND", ran
 
def generateCloudy(snow):
    ran = random()
    if snow:
        if ran < .9:
            return True, ran
        else:
            return False, ran
    else:
        if ran < .3:
            return True, ran
        else:
            return False, ran
 
def generateExams(snow, day):
    ran = random()
    day = day_state[day]
    if not snow and day == 1:
        if ran < .001:
            return True, ran
        else:
            return False, ran
    elif not snow and day == 0:
        if ran < .1:
            return True, ran
        else:
            return False, ran
    elif snow and day == 1:
        if ran < .0001:
            return True, ran
        else:
            return False, ran
    else:
        if ran < .3:
            return True, ran
        else:
            return False, ran
 
def generateStress(snow, exams):
    ran = random()
    if not snow and not exams:
        if ran < .01:
            return "HIGH", ran
        else:
            return "LOW", ran
    elif not snow and exams:
        if ran < .2:
            return "HIGH", ran
        else:
            return "LOW", ran
    elif snow and not exams:
        if ran < .1:
            return "HIGH", ran
        else:
            return "LOW", ran
    else:
        if ran < .5:
            return "HIGH", ran 
        else:
            return "LOW", ran
 
 
humidity_state = {"LOW" : 0, "MEDIUM":1, "HIGH" : 2}
temperature_state = {"WARM" : 0, "MILD" : 1, "COLD" : 2}
day_state = {"WEEKDAY" : 0, "WEEKEND" : 1}
stress_state = {"LOW" : 0, "HIGH" : 1}

#returns the state of all the nodes in the graph as a list ordered:
# humidity, temperature, day, icy, snow, cloudy, exams, stress

def generateGraph():
    nodeValues = {} 
    nodeValues['humidity'] = list(generateHumidity()) #String: LOW, MEDIUM, HIGH
    nodeValues['temperature'] = list(generateTemperature()) #String: COLD, MILD, WARM
    nodeValues['day'] = list(generateDay()) #String: WEEKEND, WEEKDAY
    nodeValues['icy'] = list(generateIcy(nodeValues['humidity'][0], nodeValues['temperature'][0])) #Boolean: True, False
    nodeValues['snow'] = list(generateSnow(nodeValues['humidity'][0], nodeValues['temperature'][0])) #Boolean: True, False
    nodeValues['cloudy'] = list(generateCloudy(nodeValues['snow'][0])) #Boolean: True, False
    nodeValues['exams'] = list(generateExams(nodeValues['snow'][0], nodeValues['day'][0])) #Boolean: True, False
    nodeValues['stress'] = list(generateStress(nodeValues['snow'][0], nodeValues['exams'][0])) #String: LOW, HIGH
    #print(nodeValues)
    return nodeValues

# i = 0
# while i < 100:
#     print(generateGraph())
#     i +=1

#     print(generateGraph())
