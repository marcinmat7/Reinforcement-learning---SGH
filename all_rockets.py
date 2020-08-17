import os
import numpy as np
import pandas as pd
import pygame, sys, math, numpy
from decide_one_layer import *
from decide import *
# from lines import *
from drawlines import *
from functions import *
# Get the current working directory
# cwd = os.getcwd()
cwd = '/home/marcin/Pulpit/rakietka/rakietka_v0.1'

coord_init = [1500, 140]
run = 5
parameters = "Parameters"
pokolenie = 2
anglesmall = 10
anglebig = 20
speed = 5
anglechange = 3

inputpath = '/home/marcin/Pulpit/rakietka_v0.1/' + parameters + '/Pokolenie_' + str(pokolenie) + '/run_' + str(run) + '.csv'
pars = pd.read_csv(inputpath)

pars1a = pars.iloc[0:30, 1]
pars1b = pars.iloc[30:48, 1]
pars2a = pars.iloc[0:30, 2]
pars2b = pars.iloc[30:48, 2]
pars3a = pars.iloc[0:30, 3]
pars3b = pars.iloc[30:48, 3]
pars4a = pars.iloc[0:30, 4]
pars4b = pars.iloc[30:48, 4]
pars5a = pars.iloc[0:30, 5]
pars5b = pars.iloc[30:48, 5]
pars6a = pars.iloc[0:30, 6]
pars6b = pars.iloc[30:48, 6]
pars7a = pars.iloc[0:30, 7]
pars7b = pars.iloc[30:48, 7]
pars8a = pars.iloc[0:30, 8]
pars8b = pars.iloc[30:48, 8]
pars9a = pars.iloc[0:30, 9]
pars9b = pars.iloc[30:48, 9]
pars10a = pars.iloc[0:30, 10]
pars10b = pars.iloc[30:48, 10]

#
# pars1a = np.random.normal(0, 0.1, 30)
# pars2a = np.random.normal(0, 0.1, 30)
# pars3a = np.random.normal(0, 0.1, 30)
# pars4a = np.random.normal(0, 0.1, 30)
# pars5a = np.random.normal(0, 0.1, 30)
# pars6a = np.random.normal(0, 0.1, 30)
# pars7a = np.random.normal(0, 0.1, 30)
# pars8a = np.random.normal(0, 0.1, 30)
# pars9a = np.random.normal(0, 0.1, 30)
# pars10a = np.random.normal(0, 0.1, 30)
#
# pars1b = np.random.normal(0, 0.1, 18)
# pars2b = np.random.normal(0, 0.1, 18)
# pars3b = np.random.normal(0, 0.1, 18)
# pars4b = np.random.normal(0, 0.1, 18)
# pars5b = np.random.normal(0, 0.1, 18)
# pars6b = np.random.normal(0, 0.1, 18)
# pars7b = np.random.normal(0, 0.1, 18)
# pars8b = np.random.normal(0, 0.1, 18)
# pars9b = np.random.normal(0, 0.1, 18)
# pars10b = np.random.normal(0, 0.1, 18)



# import csv
#
# with open('/home/marcin/Pulpit/rakietka/Parameters/Pokolenie_0/run_1.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     dates = []
#     colors = []
#     for row in readCSV:
#         color = row[3]
#         date = row[0]



cwd = '/home/marcin/Pulpit/rakietka_v0.1/figures'
decision = 0





# ###############################################3
pars = pars = np.random.normal(0, 0.1, 15)
def crosspointsfunction(anglecorrect, coord):
    crosspoints = [(0, 0)]
    # if(coord[1] <= 1050 - 820):
    if (1050 - coord[1] > 815):
        crosspoints = [(0, 0)]
        crosspoints = crosspoints.__add__([circle23a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([circle24a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([line25a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([line26a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([circle27a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([circle28a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([line1a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([line2a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([circle3a(coord, anglecorrect)])
        crosspoints = crosspoints.__add__([circle4a(coord, anglecorrect)])

    if (1050 - coord[1] <= 815):

        if (coord[0] < 220):
            crosspoints = crosspoints.__add__([line25a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line26a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle27a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle28a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line1a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line2a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle3a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle4a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line5a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line6a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle7a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle8a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line9a(coord, anglecorrect)])

        if (220 <= coord[0] < 540):
            crosspoints = [(0, 0)]
            crosspoints = crosspoints.__add__([line1a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line2a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle3a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle4a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line5a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line6a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle7a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle8a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line9a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line10a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle11a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle12a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line13a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line14a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle28a(coord, anglecorrect)])

        if (540 <= coord[0] < 1300):
            crosspoints = [(0, 0)]
            crosspoints = crosspoints.__add__([line5a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line6a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle7a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle8a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line9a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line10a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle11a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle12a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line13a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line14a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle15a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle16a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line17a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line18a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle19a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle20a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line21a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line22a(coord, anglecorrect)])

        if (1300 <= coord[0]):
            crosspoints = [(0, 0)]
            crosspoints = crosspoints.__add__([line13a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line14a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle15a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle16a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line17a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line18a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle19a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle20a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line21a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line22a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle23a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([circle24a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line25a(coord, anglecorrect)])
            crosspoints = crosspoints.__add__([line26a(coord, anglecorrect)])

    ba = list(filter(lambda a: a != (0, 0), crosspoints))
    ba = list(filter(lambda a: a != None, ba))
    if ba == [None] or ba == []:
        ba = [(0, 0)]
    # ba = [(3,1), (0,1), (1,0)]
    ba = sorted(ba, key=lambda k: [k[0], k[1]])

    if (anglecorrect < 90 or 270 < anglecorrect):
        ba = ba[0]
    if (90 <= anglecorrect <= 270):
        ba.reverse()
        ba = ba[0]
    return(ba)

def croospointcheck(point):

    if 0 < anglecorrect < 90 and coord[0] < point[0] and coord[1] < point[1]:
        return(point)

    if 90 < anglecorrect < 180 and point[0] < coord[0] and coord[1] < point[1]:
        return(point)

    if 180 < anglecorrect < 270 and coord[0] < point[0] and point[1] < coord[1]:
        return(point)

    if 270 < anglecorrect < 360 and point[0] < coord[0] and point[1]< coord[1]:
        return(point)

    return((0,0))

def line25a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0
    if(0 < anglea < 180):
        xp = (1050 - 30 - b1) / a1
        if xp < 410 or 1500 < xp:
            return((0,0))
        try:
            return (xp, 1050 - 30)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))

def line26a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0

    if (1050 - coord[1] < 820 ):
        return((0,0))
    if (anglea > 180 and anglea < 360):
        xp = (1050 - (1050 - 820) - b1) / a1
        if xp < 410 or 1500 < xp:
            return ((0, 0))
        try:
            return (xp, 820)
        except ZeroDivisionError:
            return ((0, 0))
        #else:
        #    return ((0, 0))




def circle27a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 620 + a0 * 410
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 400 * 400)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 620 + a0a * 410

    if 90 < anglea and anglea < 270:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 410

        if (x1a <= 410 and y1a >= 620):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if anglea < 90 or 270 < anglea:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 410

        if (x1a <= 410 and y1a >= 620):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def circle28a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 620 + a0 * 410
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 200 * 200)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 620 + a0a * 410

    if 90 < anglea < 180:
        return((0,0))

    if 180 < anglea < 270:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 410

        if (x1a <= 410 and y1a >= 620 and coord[0] > 210):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if anglea < 90 or 270 < anglea:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 410
        #
        if (x1a <= 410 and y1a >= 620 and coord[0] < x1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def line1a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0
    if(90 < anglea and anglea < 270):
        xp = 10
        yp = xp * a1 + b1
        if yp > 620 or yp < 250:
            return((0,0))
        try:
            return (10, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))


def line2a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0

    if(coord[0] > 210):
        return((0,0))

    if(anglea < 90 or 270 < anglea):
        xp = 210
        yp = xp * a1 + b1
        if yp > 620 or yp < 250:
            return((0,0))
        try:
            return (210, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))



def circle3a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 250 + a0 * 240
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 30 * 30)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 250 + a0a * 240

    if (0 < anglea and anglea < 90):

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord[0] <= x1a and 1050 - coord[1] <= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if (90 < anglea and anglea < 180):

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord[0] >= x1a and 1050 - coord[1] <= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if (180 < anglea and anglea < 270):

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord[0] >= x1a and 1050 - coord[1] >= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if (270 < anglea and anglea < 360):

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord[0] <= x1a and coord[1] >= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def circle4a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 250 + a0 * 240
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 230 * 230)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 250 + a0a * 240

    if anglea < 90 or anglea > 270:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if anglea > 90 and anglea < 270:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))

def line5a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    if(coord[0] > 470):
        return((0,0))
    a1 = a0
    b1 = b0
    if(anglea < 90 or 270 < anglea):
        xp = 470
        yp = xp * a1 + b1
        if yp > 550 or yp < 250:
            return((0,0))
        try:
            return (470, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))

def line6a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    if (coord[0] < 270):
        return ((0, 0))

    a1 = a0
    b1 = b0
    if(90 < anglea and anglea < 270 ):
        xp = 270
        yp = xp * a1 + b1
        if yp > 550 or yp < 250:
            return((0,0))
        try:
            return (270, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))

def circle8a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 550 + a0 * 520
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 250 * 250)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 550 + a0a * 520

    if anglea < 90 or anglea > 270:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 520

        if (y1a >= 550 and x1a <= 520 and coord[0] <= x1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if anglea > 90 and anglea < 270:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 520

        if (y1a >= 550 and x1a <= 520 and coord[0] >= x1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))

def circle7a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 550 + a0 * 520
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 50 * 50)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 550 + a0a * 520

    if anglea < 90 or anglea > 270:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 520

        if (y1a >= 550 and x1a <= 520):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if anglea > 90 and anglea < 270:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 520

        if (y1a >= 550 and x1a <= 520):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def line9a(coord, anglea):

    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    if (1050 - coord[1] > 800 ):
        return ((0, 0))


    a1 = a0
    b1 = b0
    if( 0 < anglea and anglea < 180):
        xp = (800 - b1) / a1
        if xp < 520 or 1000 < xp:
            return((0,0))
        try:
            return (xp, 800)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))

def line10a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)

    if (1050 - coord[1] < 600 ):
        return ((0, 0))

    a1 = a0
    b1 = b0
    if(0 < anglea and 180 < anglea and anglea < 360 ):
        xp = (600 - b1) / a1
        if xp < 520 or 1000 < xp:
            return((0,0))
        try:
            return (xp, 600)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))


def circle11a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 550 + a0 * 1000
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 50 * 50)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 550 + a0a * 1000

    if  0 < anglea < 90 :
        return ((0, 0))

    if 90 < anglea < 270:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 1000

        if (y1a >= 550 and x1a >= 1000):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if 270 < anglea < 360:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 1000

        if (y1a >= 550 and x1a >= 1000):
            return ((x1a, y1a))
        else:
            return ((0, 0))


    return ((0, 0))



def circle12a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 550 + a0 * 1000
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 250 * 250)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 550 + a0a * 1000

    if anglea < 90 or 270 < anglea:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 1000

        if (y1a >= 550 and x1a >= 1000):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if 90 < anglea < 270:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 1000

        if (y1a >= 550 and x1a >= 1000):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def line13a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    if (coord[0] < 1050):
        return ((0, 0))

    a1 = a0
    b1 = b0
    if(90 < anglea < 270):
        xp = 1050
        yp = xp * a1 + b1
        if yp > 550 or yp < 250:
            return((0,0))
        try:
            return (1050, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))


def line14a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    if (coord[0] > 1250):
        return ((0, 0))

    a1 = a0
    b1 = b0
    if(anglea < 90 or 270 < anglea):
        xp = 1250
        yp = xp * a1 + b1
        if yp > 550 or yp < 250:
            return((0,0))
        try:
            return (1250, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))



def circle16a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 250 + a0 * 1280
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 30 * 30)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 250 + a0a * 1280

    if  anglea < 90 or 270 < anglea:
        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1280

        if (y1a <= 250 and x1a <= 1280):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if 90 < anglea < 180:
        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1280

        if (y1a <= 250 and x1a <= 1280 and coord[0] > x1a and 1050 - coord[1] < y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if  180 < anglea < 270:
        return ((0, 0))

    return ((0, 0))


def circle15a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 250 + a0 * 1280
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 230 * 230)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 250 + a0a * 1280

    if  anglea < 90 or 270 < anglea:
        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1280

        if (y1a <= 250 and x1a <= 1280):
            return ((x1a, y1a))
        else:
            return ((0, 0))


    if  90 < anglea < 270:
        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1280

        if (y1a <= 250 and x1a <= 1280):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def line17a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0
    if( 180 < anglea < 360 ):
        xp = (20 - b1) / a1
        if xp < 1280 or 1670 < xp:
            return((0,0))
        try:
            return (xp, 20)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))


def line18a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0

    if(1050 - coord[1] >220 ):
        return((0,0))

    if(0 < anglea < 180):
        xp = (220 - b1) / a1
        if xp < 1280 or 1670 < xp:
            return((0,0))
        try:
            return (xp, 220)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))


def circle19a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 250 + a0 * 1670
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 230 * 230)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 250 + a0a * 1670

    if  anglea < 90 or 270 < anglea:
        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1670

        if (y1a <= 250 and x1a >= 1670):
            return ((x1a, y1a))
        else:
            return ((0, 0))


    if  90 < anglea < 270:
        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1670

        if (y1a <= 250 and x1a >= 1670):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))

def circle20a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 250 + a0 * 1670
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 30 * 30)

    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 250 + a0a * 1670


    if  0 < anglea < 90:
        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1670

        if (y1a <= 250 and x1a >= 1670):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if 270 < anglea < 360:
        return ((0, 0))

    if  90 < anglea < 270:
        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 1670

        if (y1a <= 250 and x1a >= 1670 and coord[0] > x1a and 1050 - coord[1] < y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))



def line21a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0
    if(anglea < 90 or 270 < anglea):
        xp = 1900
        yp = xp * a1 + b1
        if yp < 250 or 620 < yp:
            return((0,0))
        try:
            return (1900, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))


def line22a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    if (coord[0] < 1700):
        return ((0, 0))

    a1 = a0
    b1 = b0
    if(90 < anglea < 270):
        xp = 1700
        yp = xp * a1 + b1
        if yp < 250 or 620 < yp:
            return((0,0))
        try:
            return (1700, yp)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))



def circle23a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 620 + a0 * 1500
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 400 * 400)

    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 620 + a0a * 1500


    if  anglea < 90 or 270 < anglea :
        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 1500

        if (y1a >= 620 and x1a >= 1500):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if  90 < anglea < 180:
        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 1500

        if (y1a >= 620 and x1a >= 1500):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))

def circle24a(coord, anglea):
    a0 = math.tan(math.radians(anglea))
    b0 = (1050 - coord[1] - coord[0] * a0)
    a1 = a0
    b1 = b0 - 620 + a0 * 1500
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 200 * 200)

    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord[1] - coord[0] * a0a)
    a1a = a0a
    b1a = b0a - 620 + a0a * 1500

    if anglea < 90 :
        return ((0, 0))

    if  270 < anglea :
        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 1500

        if (y1a >= 620 and x1a >= 1500):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if  90 < anglea < 270:
        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 1500

        if (y1a >= 620 and x1a >= 1500) and x1a < coord[0]:
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))





# ##########################################################

linewidth = 5
# Set the current working directory
os.chdir(cwd)
angle = pd.Series([-90, -90, -90, -90, -90, -90, -90, -90, -90, -90])
# angle = pd.Series([90, 90, 90, 90, 90, 90, 90, 90, 90, 90])
pygame.init()
#print(pygame.__version__)


screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption('SGH')
bc = pygame.image.load("bg2.jpg").convert()
meta = pygame.image.load("meta.jpg").convert()
# ship = pygame.image.load("rocket.png").convert_alpha()
# w, h = ship.get_size()
# box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
# box_rotate = [p.rotate(90) for p in box]

# min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
# max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
czubek = (0, 0)
ba0= (0,0)
baP60= (0,0)
baP30= (0,0)
baM30= (0,0)
baM60= (0,0)
#distance = 0
font = pygame.font.Font('freesansbold.ttf', 32)
# Initial settings
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# angle = 90
# ship = pygame.image.load("rocket.png").convert_alpha()
# Initial coordinates:


# coord_init = [1500, 140]
# coord1 = coord_init
# coord2 = coord_init
# coord3 = coord_init
# coord4 = coord_init
# coord5 = coord_init
# coord6 = coord_init
# coord7 = coord_init
# coord8 = coord_init
# coord9 = coord_init
# coord10 = coord_init


coord1 = [800,350]
coord2 = [800,350]
coord3 = [800,350]
coord4 = [800,350]
coord5 = [800,350]
coord6 = [800,350]
coord7 = [800,350]
coord8 = [800,350]
coord9 = [800,350]
coord10 = [800,350]


# coord2 = [1500,140]
# coord3 = [1500,140]
# coord4 = [1500,140]
# coord5 = [1500,140]
# coord6 = [1500,140]
# coord7 = [1500,140]
# coord8 = [1500,140]
# coord9 = [1500,140]
# coord10 = [1500,140]

pygame.init()
print(pygame.__version__)
# box = pygame.Rect(10, 10, 50, 50)
pygame.display.flip()
stop = False
# decision = "z"

# keys = pygame.key.get_pressed()
# if keys[pygame.K_p]:
#     sys.exit(0)
text0 = font.render(str(angle), True, green, blue)
textP30 = font.render(str(angle), True, green, blue)
textP60 = font.render(str(angle), True, green, blue)
textM30 = font.render(str(angle), True, green, blue)
textM60 = font.render(str(angle), True, green, blue)
# create a rectangular object for the
# text surface object
textRect0 = text0.get_rect()
textRectP30 = textP30.get_rect()
textRectP60 = textP60.get_rect()
textRectM30 = textM30.get_rect()
textRectM60 = textM60.get_rect()
X = 1300
Y = 1000
# set the center of the rectangular object.
textRect0.center = (X // 2, Y // 2)
X = 1100
Y = 1100
textRectP30.center = (X // 2, Y // 2)
X = 900
Y = 1200
textRectP60.center = (X // 2, Y // 2)
X = 1500
Y = 1100
textRectM30.center = (X // 2, Y // 2)
X = 1700
Y = 1200
textRectM60.center = (X // 2, Y // 2)
decision = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
zeros = [1,1,1,1,1,1,1,1,1,1]

# pars1a = np.random.normal(0, 0.1, 30)
# pars2a = np.random.normal(0, 0.1, 30)
# pars3a = np.random.normal(0, 0.1, 30)
# pars4a = np.random.normal(0, 0.1, 30)
# pars5a = np.random.normal(0, 0.1, 30)
# pars6a = np.random.normal(0, 0.1, 30)
# pars7a = np.random.normal(0, 0.1, 30)
# pars8a = np.random.normal(0, 0.1, 30)
# pars9a = np.random.normal(0, 0.1, 30)
# pars10a = np.random.normal(0, 0.1, 30)
#
# pars1b = np.random.normal(0, 0.1, 18)
# pars2b = np.random.normal(0, 0.1, 18)
# pars3b = np.random.normal(0, 0.1, 18)
# pars4b = np.random.normal(0, 0.1, 18)
# pars5b = np.random.normal(0, 0.1, 18)
# pars6b = np.random.normal(0, 0.1, 18)
# pars7b = np.random.normal(0, 0.1, 18)
# pars8b = np.random.normal(0, 0.1, 18)
# pars9b = np.random.normal(0, 0.1, 18)
# pars10b = np.random.normal(0, 0.1, 18)







while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        sys.exit(0)
    if keys[pygame.K_m]:
        sys.exit(0)
    # decision = pd.Series([1,1,2])

    # isone = decision == 1
    # isone = pd.Series(decision)
    # decisionfinal = pd.Series(decision)
    # (decisionfinal - 1) * 2

    # decisionfinal
    # which(isone == True)
    # isthree = decision == 3
    # isthree = pd.Series(isthree)

    # dec1 = int(isone)
    # dec3 = int(isthree)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        sys.exit(0)
    # decision = 0
    if keys[pygame.K_z]:
        # df = pd.DataFrame(cars, columns=['Brand', 'Price'])


        sciezka = '/home/marcin/Pulpit/rakietka_v0.1/' + parameters + '/Pokolenie_' + str(pokolenie) + '/run_' + str(run) + '_results.csv'
        a = pd.DataFrame([coord1, coord2, coord3, coord4, coord5, coord6, coord7, coord8, coord9, coord10])
        a.to_csv(sciezka, index=True, header=True)


        sys.exit(0)
    # keys[pygame.K_q] |
    # keys[pygame.K_e] |

    angle = angle + (decision - 2) * anglechange
    # angle[decisionfinal == 1] = (angle[decisionfinal == 1] + 2)
    # angle[decisionfinal == 3] = (angle[decisionfinal == 3] - 2)
    angle = angle % 360

    if zeros[0]:
        coord1[1] -= speed * math.cos(math.radians(angle[0])) * zeros[0]
        coord1[0] -= speed * math.sin(math.radians(angle[0])) * zeros[0]

    if zeros[1]:
        coord2[1] -= speed * math.cos(math.radians(angle[1])) * zeros[1]
        coord2[0] -= speed * math.sin(math.radians(angle[1])) * zeros[1]

    if zeros[2]:
        coord3[1] -= speed * math.cos(math.radians(angle[2])) * zeros[2]
        coord3[0] -= speed * math.sin(math.radians(angle[2])) * zeros[2]

    if zeros[3]:
        coord4[1] -= speed * math.cos(math.radians(angle[3])) * zeros[3]
        coord4[0] -= speed * math.sin(math.radians(angle[3])) * zeros[3]

    if zeros[4]:
        coord5[1] -= speed * math.cos(math.radians(angle[4])) * zeros[4]
        coord5[0] -= speed * math.sin(math.radians(angle[4])) * zeros[4]

    if zeros[5]:
        coord6[1] -= speed * math.cos(math.radians(angle[5])) * zeros[5]
        coord6[0] -= speed * math.sin(math.radians(angle[5])) * zeros[5]

    if zeros[6]:
        coord7[1] -= speed * math.cos(math.radians(angle[6])) * zeros[6]
        coord7[0] -= speed * math.sin(math.radians(angle[6])) * zeros[6]

    if zeros[7]:
        coord8[1] -= speed * math.cos(math.radians(angle[7])) * zeros[7]
        coord8[0] -= speed * math.sin(math.radians(angle[7])) * zeros[7]

    if zeros[8]:
        coord9[1] -= speed * math.cos(math.radians(angle[8])) * zeros[8]
        coord9[0] -= speed * math.sin(math.radians(angle[8])) * zeros[8]

    if zeros[9]:
        coord10[1] -= speed * math.cos(math.radians(angle[9])) * zeros[9]
        coord10[0] -= speed * math.sin(math.radians(angle[9])) * zeros[9]

    anglecorrect = (angle + 90) % 360
    anglecorrect = anglecorrect.astype(int)

    ba0 = crosspointsfunction(anglecorrect[0], coord1)
    baP30 = crosspointsfunction((anglecorrect[0] + anglesmall) % 360, coord1)
    baP60 = crosspointsfunction((anglecorrect[0] + anglebig) % 360, coord1)
    baM30  = crosspointsfunction((anglecorrect[0] - anglesmall) % 360, coord1)
    baM60 = crosspointsfunction((anglecorrect[0] - anglebig) % 360, coord1)

    distsqP60 = (coord1[0] - baP60[0]) ** 2 + (1050 - coord1[1] - baP60[1]) ** 2
    distsqP30 = (coord1[0] - baP30[0]) ** 2 + (1050 - coord1[1] - baP30[1]) ** 2
    distsq0 = (coord1[0] - ba0[0]) ** 2 + (1050 - coord1[1] - ba0[1]) ** 2
    distsqM30 = (coord1[0] - baM30[0]) ** 2 + (1050 - coord1[1] - baM30[1]) ** 2
    distsqM60 = (coord1[0] - baM60[0]) ** 2 + (1050 - coord1[1] - baM60[1]) ** 2

    distances1 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]


    # ba0 = crosspointsfunction(anglecorrect[1], coord2)
    # baP30 = crosspointsfunction((anglecorrect[1] + anglesmall) % 360, coord2)
    # baP60 = crosspointsfunction((anglecorrect[1] + anglebig) % 360, coord2)
    # baM30  = crosspointsfunction((anglecorrect[1] - anglesmall) % 360, coord2)
    # baM60 = crosspointsfunction((anglecorrect[1] - anglebig) % 360, coord2)
    #
    # distsqP60 = (coord2[0] - baP60[0]) ** 2 + (1050 - coord2[1] - baP60[1]) ** 2
    # distsqP30 = (coord2[0] - baP30[0]) ** 2 + (1050 - coord2[1] - baP30[1]) ** 2
    # distsq0 = (coord2[0] - ba0[0]) ** 2 + (1050 - coord2[1] - ba0[1]) ** 2
    # distsqM30 = (coord2[0] - baM30[0]) ** 2 + (1050 - coord2[1] - baM30[1]) ** 2
    # distsqM60 = (coord2[0] - baM60[0]) ** 2 + (1050 - coord2[1] - baM60[1]) ** 2
    # distances2 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]
    #

    ba0 = crosspointsfunction(anglecorrect[1], coord2)
    baP30 = crosspointsfunction((anglecorrect[1] + anglesmall) % 360, coord2)
    baP60 = crosspointsfunction((anglecorrect[1] + anglebig) % 360, coord2)
    baM30  = crosspointsfunction((anglecorrect[1] - anglesmall) % 360, coord2)
    baM60 = crosspointsfunction((anglecorrect[1] - anglebig) % 360, coord2)
    distsqP60 = (coord2[0] - baP60[0]) ** 2 + (1050 - coord2[1] - baP60[1]) ** 2
    distsqP30 = (coord2[0] - baP30[0]) ** 2 + (1050 - coord2[1] - baP30[1]) ** 2
    distsq0 = (coord2[0] - ba0[0]) ** 2 + (1050 - coord2[1] - ba0[1]) ** 2
    distsqM30 = (coord2[0] - baM30[0]) ** 2 + (1050 - coord2[1] - baM30[1]) ** 2
    distsqM60 = (coord2[0] - baM60[0]) ** 2 + (1050 - coord2[1] - baM60[1]) ** 2
    distances2 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]
    # a1 = ba0
    # a2 = baP30
    # a3 = baP60
    # a4 = baM30
    # a5 = baM60

    ba0 = crosspointsfunction(anglecorrect[2], coord3)
    baP30 = crosspointsfunction((anglecorrect[2] + anglesmall) % 360, coord3)
    baP60 = crosspointsfunction((anglecorrect[2] + anglebig) % 360, coord3)
    baM30  = crosspointsfunction((anglecorrect[2] - anglesmall) % 360, coord3)
    baM60 = crosspointsfunction((anglecorrect[2] - anglebig) % 360, coord3)
    distsqP60 = (coord3[0] - baP60[0]) ** 2 + (1050 - coord3[1] - baP60[1]) ** 2
    distsqP30 = (coord3[0] - baP30[0]) ** 2 + (1050 - coord3[1] - baP30[1]) ** 2
    distsq0 = (coord3[0] - ba0[0]) ** 2 + (1050 - coord3[1] - ba0[1]) ** 2
    distsqM30 = (coord3[0] - baM30[0]) ** 2 + (1050 - coord3[1] - baM30[1]) ** 2
    distsqM60 = (coord3[0] - baM60[0]) ** 2 + (1050 - coord3[1] - baM60[1]) ** 2
    distances3 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    ba0 = crosspointsfunction(anglecorrect[3], coord4)
    baP30 = crosspointsfunction((anglecorrect[3] + anglesmall) % 360, coord4)
    baP60 = crosspointsfunction((anglecorrect[3] + anglebig) % 360, coord4)
    baM30  = crosspointsfunction((anglecorrect[3] - anglesmall) % 360, coord4)
    baM60 = crosspointsfunction((anglecorrect[3] - anglebig) % 360, coord4)
    distsqP60 = (coord4[0] - baP60[0]) ** 2 + (1050 - coord4[1] - baP60[1]) ** 2
    distsqP30 = (coord4[0] - baP30[0]) ** 2 + (1050 - coord4[1] - baP30[1]) ** 2
    distsq0 = (coord4[0] - ba0[0]) ** 2 + (1050 - coord4[1] - ba0[1]) ** 2
    distsqM30 = (coord4[0] - baM30[0]) ** 2 + (1050 - coord4[1] - baM30[1]) ** 2
    distsqM60 = (coord4[0] - baM60[0]) ** 2 + (1050 - coord4[1] - baM60[1]) ** 2
    distances4 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    ba0 = crosspointsfunction(anglecorrect[4], coord5)
    baP30 = crosspointsfunction((anglecorrect[4] + anglesmall) % 360, coord5)
    baP60 = crosspointsfunction((anglecorrect[4] + anglebig) % 360, coord5)
    baM30  = crosspointsfunction((anglecorrect[4] - anglesmall) % 360, coord5)
    baM60 = crosspointsfunction((anglecorrect[4] - anglebig) % 360, coord5)
    distsqP60 = (coord5[0] - baP60[0]) ** 2 + (1050 - coord5[1] - baP60[1]) ** 2
    distsqP30 = (coord5[0] - baP30[0]) ** 2 + (1050 - coord5[1] - baP30[1]) ** 2
    distsq0 = (coord5[0] - ba0[0]) ** 2 + (1050 - coord5[1] - ba0[1]) ** 2
    distsqM30 = (coord5[0] - baM30[0]) ** 2 + (1050 - coord5[1] - baM30[1]) ** 2
    distsqM60 = (coord5[0] - baM60[0]) ** 2 + (1050 - coord5[1] - baM60[1]) ** 2
    distances5 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    ba0 = crosspointsfunction(anglecorrect[5], coord6)
    baP30 = crosspointsfunction((anglecorrect[5] + anglesmall) % 360, coord6)
    baP60 = crosspointsfunction((anglecorrect[5] + anglebig) % 360, coord6)
    baM30  = crosspointsfunction((anglecorrect[5] - anglesmall) % 360, coord6)
    baM60 = crosspointsfunction((anglecorrect[5] - anglebig) % 360, coord6)
    distsqP60 = (coord6[0] - baP60[0]) ** 2 + (1050 - coord6[1] - baP60[1]) ** 2
    distsqP30 = (coord6[0] - baP30[0]) ** 2 + (1050 - coord6[1] - baP30[1]) ** 2
    distsq0 = (coord6[0] - ba0[0]) ** 2 + (1050 - coord6[1] - ba0[1]) ** 2
    distsqM30 = (coord6[0] - baM30[0]) ** 2 + (1050 - coord6[1] - baM30[1]) ** 2
    distsqM60 = (coord6[0] - baM60[0]) ** 2 + (1050 - coord6[1] - baM60[1]) ** 2
    distances6 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    ba0 = crosspointsfunction(anglecorrect[6], coord7)
    baP30 = crosspointsfunction((anglecorrect[6] + anglesmall) % 360, coord7)
    baP60 = crosspointsfunction((anglecorrect[6] + anglebig) % 360, coord7)
    baM30  = crosspointsfunction((anglecorrect[6] - anglesmall) % 360, coord7)
    baM60 = crosspointsfunction((anglecorrect[6] - anglebig) % 360, coord7)
    distsqP60 = (coord7[0] - baP60[0]) ** 2 + (1050 - coord7[1] - baP60[1]) ** 2
    distsqP30 = (coord7[0] - baP30[0]) ** 2 + (1050 - coord7[1] - baP30[1]) ** 2
    distsq0 = (coord7[0] - ba0[0]) ** 2 + (1050 - coord7[1] - ba0[1]) ** 2
    distsqM30 = (coord7[0] - baM30[0]) ** 2 + (1050 - coord7[1] - baM30[1]) ** 2
    distsqM60 = (coord7[0] - baM60[0]) ** 2 + (1050 - coord7[1] - baM60[1]) ** 2
    distances7 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    ba0 = crosspointsfunction(anglecorrect[7], coord8)
    baP30 = crosspointsfunction((anglecorrect[7] + anglesmall) % 360, coord8)
    baP60 = crosspointsfunction((anglecorrect[7] + anglebig) % 360, coord8)
    baM30  = crosspointsfunction((anglecorrect[7] - anglesmall) % 360, coord8)
    baM60 = crosspointsfunction((anglecorrect[7] - anglebig) % 360, coord8)
    distsqP60 = (coord8[0] - baP60[0]) ** 2 + (1050 - coord8[1] - baP60[1]) ** 2
    distsqP30 = (coord8[0] - baP30[0]) ** 2 + (1050 - coord8[1] - baP30[1]) ** 2
    distsq0 = (coord8[0] - ba0[0]) ** 2 + (1050 - coord8[1] - ba0[1]) ** 2
    distsqM30 = (coord8[0] - baM30[0]) ** 2 + (1050 - coord8[1] - baM30[1]) ** 2
    distsqM60 = (coord8[0] - baM60[0]) ** 2 + (1050 - coord8[1] - baM60[1]) ** 2
    distances8 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    ba0 = crosspointsfunction(anglecorrect[8], coord9)
    baP30 = crosspointsfunction((anglecorrect[8] + anglesmall) % 360, coord9)
    baP60 = crosspointsfunction((anglecorrect[8] + anglebig) % 360, coord9)
    baM30  = crosspointsfunction((anglecorrect[8] - anglesmall) % 360, coord9)
    baM60 = crosspointsfunction((anglecorrect[8] - anglebig) % 360, coord9)
    distsqP60 = (coord9[0] - baP60[0]) ** 2 + (1050 - coord9[1] - baP60[1]) ** 2
    distsqP30 = (coord9[0] - baP30[0]) ** 2 + (1050 - coord9[1] - baP30[1]) ** 2
    distsq0 = (coord9[0] - ba0[0]) ** 2 + (1050 - coord9[1] - ba0[1]) ** 2
    distsqM30 = (coord9[0] - baM30[0]) ** 2 + (1050 - coord9[1] - baM30[1]) ** 2
    distsqM60 = (coord9[0] - baM60[0]) ** 2 + (1050 - coord9[1] - baM60[1]) ** 2
    distances9 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    ba0 = crosspointsfunction(anglecorrect[9], coord10)
    baP30 = crosspointsfunction((anglecorrect[9] + anglesmall) % 360, coord10)
    baP60 = crosspointsfunction((anglecorrect[9] + anglebig) % 360, coord10)
    baM30  = crosspointsfunction((anglecorrect[9] - anglesmall) % 360, coord10)
    baM60 = crosspointsfunction((anglecorrect[9] - anglebig) % 360, coord10)
    distsqP60 = (coord10[0] - baP60[0]) ** 2 + (1050 - coord10[1] - baP60[1]) ** 2
    distsqP30 = (coord10[0] - baP30[0]) ** 2 + (1050 - coord10[1] - baP30[1]) ** 2
    distsq0 = (coord10[0] - ba0[0]) ** 2 + (1050 - coord10[1] - ba0[1]) ** 2
    distsqM30 = (coord10[0] - baM30[0]) ** 2 + (1050 - coord10[1] - baM30[1]) ** 2
    distsqM60 = (coord10[0] - baM60[0]) ** 2 + (1050 - coord10[1] - baM60[1]) ** 2
    distances10 = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

    zerosold = pd.Series(zeros)
    zeros = [min(distances1), min(distances2), min(distances3), min(distances4), min(distances5), min(distances6), min(distances7), min(distances8), min(distances9),min(distances10)]
    # zeros = [1,2,3]
    zeros = pd.Series(zeros) > 20
    zeros = zeros * zerosold
    zeros = zeros.astype(int)


    # decision1 = decideone(pars1, distances1)
    # decision2 = decideone(pars2, distances2)
    # decision3 = decideone(pars3, distances3)
    # decision4 = decideone(pars4, distances4)
    # decision5 = decideone(pars5, distances5)
    # decision6 = decideone(pars6, distances6)
    # decision7 = decideone(pars7, distances7)
    # decision8 = decideone(pars8, distances8)
    # decision9 = decideone(pars9, distances9)
    # decision10 = decideone(pars10, distances10)


    decision1 = decidetwo(pars1a, pars1b, distances1)
    decision2 = decidetwo(pars2a, pars2b, distances2)
    decision3 = decidetwo(pars3a, pars3b, distances3)
    decision4 = decidetwo(pars4a, pars4b, distances4)
    decision5 = decidetwo(pars5a, pars5b, distances5)
    decision6 = decidetwo(pars6a, pars6b, distances6)
    decision7 = decidetwo(pars7a, pars7b, distances7)
    decision8 = decidetwo(pars8a, pars8b, distances8)
    decision9 = decidetwo(pars9a, pars9b, distances9)
    decision10 = decidetwo(pars10a, pars10b, distances10)

    decision = pd.Series([decision1,
                          decision2,
                          decision3,
                          decision4,
                          decision5,
                          decision6,
                          decision7,
                          decision8,
                          decision9,
                          decision10
                          ])
    #
    # distsqP60 = (coord[0] - baP60[0]) ** 2 + (1050 - coord[1] - baP60[1]) ** 2
    # distsqP30 = (coord[0] - baP30[0]) ** 2 + (1050 - coord[1] - baP30[1]) ** 2
    # distsq0 = (coord[0] - ba0[0]) ** 2 + (1050 - coord[1] - ba0[1]) ** 2
    # distsqM30 = (coord[0] - baM30[0]) ** 2 + (1050 - coord[1] - baM30[1]) ** 2
    # distsqM60 = (coord[0] - baM60[0]) ** 2 + (1050 - coord[1] - baM60[1]) ** 2

    # distances = [distsqP60, distsqP30, distsq0, distsqM30, distsqM60]

# Algorithm
#     if min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) < 10:
#         stop = True

    # if min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) == distsqP60 or min(distsqP60, distsqP30, distsq0,
    #                                                                                 distsqM30, distsqM60) == distsqP30:
    #     decision = 1
    #
    # if min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) == distsqM30 or min(distsqP60, distsqP30, distsq0,
    #                                                                                 distsqM30, distsqM60) == distsqM60:
    #     decision = 3
    #
    # dista = 100
    # if math.sqrt(distsq0) > 200 and math.sqrt(distsqP60) > dista and math.sqrt(distsqP30) > dista and math.sqrt(
    #         distsqM60) > dista and math.sqrt(distsqM30) > dista:
    #     decision = 2

    # decision = decideone(pars, distances)

# Algorithm end

    # tekst0 = "Dist: " + str(distances2)
    # tekst0 = "Dist: " + str(round(distances8[0]))

        # tekst0 = "Dist: " + str(decision)
    # tekstP60 = "Dist: " + str(decision2)
    # tekstP30 = "Dist: " + str(decision3)
        # tekstM30 = "Dist: " + str(round(math.sqrt(distsqM30), 2))
        # tekstM60 = "Dist: " + str(round(math.sqrt(distsqM60), 2))

    # dist = str(anglecorrect[1])
    # tekst0 = "Dist: " + dist
    screen.blit(bc, [0, 0])
    screen.blit(meta, [800 - 43, 250], )
    # text0 = font.render(str(tekst0), True, green, blue)
    # textP30 = font.render(str(tekstP30), True, green, blue)
    # textP60 = font.render(str(tekstP60), True, green, blue)
        # textM30 = font.render(str(tekstM30), True, green, blue)
        # textM60 = font.render(str(tekstM60), True, green, blue)

    # screen.blit(text0, textRect0)
    # screen.blit(textP30, textRectP30)
    # screen.blit(textP60, textRectP60)
        # screen.blit(textM30, textRectM30)
        # screen.blit(textM60, textRectM60)

        # screen.blit(text0, textRect0)

    # pygame.draw.circle(screen, (255, 255, 255), (round(ba0[0]), round(1050 - ba0[1])), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (round(baP30[0]), round(1050 - baP30[1])), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (round(baP60[0]), round(1050 - baP60[1])), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (round(baM30[0]), round(1050 - baM30[1])), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (round(baM60[0]), round(1050 - baM60[1])), 10, 0)

    # pygame.draw.circle(screen, (255, 255, 255), (int(round(ba0[0])), int(round(1050 - ba0[1]))), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (int(round(baP30[0])), int(round(1050 - baP30[1]))), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (int(round(baP60[0])), int(round(1050 - baP60[1]))), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (int(round(baM30[0])), int(round(1050 - baM30[1]))), 10, 0)
    # pygame.draw.circle(screen, (255, 255, 255), (int(round(baM60[0])), int(round(1050 - baM60[1]))), 10, 0)
    #
    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord1[0])), int(round(coord1[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord1[0]), round(coord1[1])), (coord1[0] - round(10 * math.sin(math.radians(angle[0]))), round(coord1[1]) - round(10 * math.cos(math.radians(angle[0])))), 1)
    # #
    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord2[0])), int(round(coord2[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord2[0]), round(coord2[1])), (coord2[0] - round(10 * math.sin(math.radians(angle[1]))), round(coord2[1]) - round(10 * math.cos(math.radians(angle[1])))), 1)
    #
    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord3[0])), int(round(coord3[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord3[0]), round(coord3[1])), (coord3[0] - round(10 * math.sin(math.radians(angle[2]))), round(coord3[1]) - round(10 * math.cos(math.radians(angle[2])))), 1)
    #
    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord4[0])), int(round(coord4[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord4[0]), round(coord4[1])), (coord4[0] - round(10 * math.sin(math.radians(angle[3]))), round(coord4[1]) - round(10 * math.cos(math.radians(angle[3])))), 1)

    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord5[0])), int(round(coord5[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord5[0]), round(coord5[1])), (coord5[0] - round(10 * math.sin(math.radians(angle[4]))), round(coord5[1]) - round(10 * math.cos(math.radians(angle[4])))), 1)
    #
    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord6[0])), int(round(coord6[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord6[0]), round(coord6[1])), (coord6[0] - round(10 * math.sin(math.radians(angle[5]))), round(coord6[1]) - round(10 * math.cos(math.radians(angle[5])))), 1)

    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord7[0])), int(round(coord7[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord7[0]), round(coord7[1])), (coord7[0] - round(10 * math.sin(math.radians(angle[6]))), round(coord7[1]) - round(10 * math.cos(math.radians(angle[6])))), 1)
    #
    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord8[0])), int(round(coord8[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord8[0]), round(coord8[1])), (coord8[0] - round(10 * math.sin(math.radians(angle[7]))), round(coord8[1]) - round(10 * math.cos(math.radians(angle[7])))), 1)

    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord9[0])), int(round(coord9[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord9[0]), round(coord9[1])), (coord9[0] - round(10 * math.sin(math.radians(angle[8]))), round(coord9[1]) - round(10 * math.cos(math.radians(angle[8])))), 1)

    pygame.draw.circle(screen, (255, 255, 255), (int(round(coord10[0])), int(round(coord10[1]))), 3, 3)
    pygame.draw.line(screen, (255, 255, 255), (round(coord10[0]), round(coord10[1])), (coord10[0] - round(10 * math.sin(math.radians(angle[9]))), round(coord10[1]) - round(10 * math.cos(math.radians(angle[9])))), 1)
    #

    drawlines(screen, linewidth)

    pygame.display.flip()


# coord1 = [1000,140]
# coord2 = [1000,140]
# coord3 = [1000,140]
# coord4 = [1000,140]
# coord5 = [1000,140]
# coord6 = [1000,140]
# coord7 = [1000,140]
# coord8 = [1000,140]
# coord9 = [1000,140]
# coord10 = [1000,140]

# res1 = pd.DataFrame(coord1, coord2)
# res2 = pd.DataFrame(coord3, coord4)
# res3 = pd.DataFrame(coord5, coord6)
# res4 = pd.DataFrame(coord7, coord8)
# res5 = pd.DataFrame(coord9, coord10)
# rbind(res1, res2)
# []
# res = pd.DataFrame(res1, res2)
#
#
# a = pd.DataFrame([coord1, coord2, coord3, coord4, coord5, coord6, coord7, coord8, coord9, coord10])
#

# res.to_csv(sciezka, index=True, header=True)