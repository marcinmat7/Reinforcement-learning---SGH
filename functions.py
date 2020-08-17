
def crosspointsfunction(anglecorrect, coord, czubek):
    crosspoints = [(0, 0)]
    # if(coord[1] <= 1050 - 820):
    if (1050 - coord[1] > 815):
        crosspoints = [(0, 0)]
        crosspoints = crosspoints.__add__([circle23a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([circle24a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([line25a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([line26a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([circle27a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([circle28a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([line1a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([line2a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([circle3a(czubek[0], czubek[1], anglecorrect)])
        crosspoints = crosspoints.__add__([circle4a(czubek[0], czubek[1], anglecorrect)])

    if (1050 - coord[1] <= 815):

        if (coord[0] < 220):
            crosspoints = crosspoints.__add__([line25a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line26a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle27a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle28a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line1a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line2a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle3a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle4a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line5a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line6a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle7a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle8a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line9a(czubek[0], czubek[1], anglecorrect)])

        if (220 <= coord[0] < 540):
            crosspoints = [(0, 0)]
            crosspoints = crosspoints.__add__([line1a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line2a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle3a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle4a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line5a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line6a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle7a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle8a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line9a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line10a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle11a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle12a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line13a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line14a(czubek[0], czubek[1], anglecorrect)])

        if (540 <= coord[0] < 1300):
            crosspoints = [(0, 0)]
            crosspoints = crosspoints.__add__([line5a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line6a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle7a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle8a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line9a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line10a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle11a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle12a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line13a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line14a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle15a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle16a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line17a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line18a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle19a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle20a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line21a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line22a(czubek[0], czubek[1], anglecorrect)])

        if (1300 <= coord[0]):
            crosspoints = [(0, 0)]
            crosspoints = crosspoints.__add__([line13a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line14a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle15a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle16a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line17a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line18a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle19a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle20a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line21a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line22a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle23a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([circle24a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line25a(czubek[0], czubek[1], anglecorrect)])
            crosspoints = crosspoints.__add__([line26a(czubek[0], czubek[1], anglecorrect)])

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




def getcoord(line1):
    point1 = (line1[0][0], 1080 - line1[0][1])
    point2 = (line1[1][0], 1080 - line1[1][1])
    a = (point1[1] - point2[1]) / (point1[0] - point2[1])
    b = point1[1] - a * point1[0]
    coord = (a, b)
    return coord


def line25a(coord1, coord2, anglea):
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

def line26a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0

    if (1050 - coord1 < 820 ):
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




def circle27a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 620 + a0 * 410
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 400 * 400)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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


def circle28a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 620 + a0 * 410
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 200 * 200)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
    a1a = a0a
    b1a = b0a - 620 + a0a * 410

    if 90 < anglea < 180:
        return((0,0))

    if 180 < anglea < 270:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 410

        if (x1a <= 410 and y1a >= 620 and coord0 > 210):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if anglea < 90 or 270 < anglea:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 620
        x1a = x1a + 410

        if (x1a <= 410 and y1a >= 620 and coord0 < x1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def line1a(coord0, coord1, anglea):
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


def line2a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0

    if(coord0 > 210):
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



def circle3a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 250 + a0 * 240
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 30 * 30)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
    a1a = a0a
    b1a = b0a - 250 + a0a * 240

    if (0 < anglea and anglea < 90):

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord0 <= x1a and 1050 - coord1 <= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if (90 < anglea and anglea < 180):

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord0 >= x1a and 1050 - coord1 <= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if (180 < anglea and anglea < 270):

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord0 >= x1a and 1050 - coord1 >= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if (270 < anglea and anglea < 360):

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 250
        x1a = x1a + 240

        if (y1a <= 250 and coord0 <= x1a and coord1 >= y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def circle4a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 250 + a0 * 240
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 230 * 230)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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

def line5a(coord0, coord1, anglea):

    if(coord0 > 470):
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

def line6a(coord0, coord1, anglea):

    if (coord0 < 270):
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

def circle8a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 550 + a0 * 520
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 250 * 250)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
    a1a = a0a
    b1a = b0a - 550 + a0a * 520

    if anglea < 90 or anglea > 270:

        x1a = (- 2 * a1a * b1a + math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 520

        if (y1a >= 550 and x1a <= 520 and coord0 <= x1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if anglea > 90 and anglea < 270:

        x1a = (- 2 * a1a * b1a - math.sqrt(deltacircle1)) / (2 * (a1a * a1a + 1))
        y1a = x1a * a1a + b1a + 550
        x1a = x1a + 520

        if (y1a >= 550 and x1a <= 520 and coord0 >= x1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))

def circle7a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 550 + a0 * 520
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 50 * 50)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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


def line9a(coord0, coord1, anglea):

    if (1050 - coord1 > 800 ):
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

def line10a(coord0, coord1, anglea):

    if (1050 - coord1 < 600 ):
        return ((0, 0))

    a1 = a0
    b1 = b0
    if( 180 < anglea ):
        xp = (600 - b1) / a1
        if xp < 520 or 1000 < xp:
            return((0,0))
        try:
            return (xp, 600)
        except ZeroDivisionError:
            return ((0, 0))
    else:
        return(((0, 0)))


def circle11a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 550 + a0 * 1000
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 50 * 50)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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



def circle12a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 550 + a0 * 1000
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 250 * 250)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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


def line13a(coord0, coord1, anglea):

    if (coord0 < 1050):
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


def line14a(coord0, coord1, anglea):

    if (coord0 > 1250):
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



def circle16a(coord0, coord1, anglea):
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

        if (y1a <= 250 and x1a <= 1280 and coord0 > x1a and 1050 - coord1 < y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    if  180 < anglea < 270:
        return ((0, 0))

    return ((0, 0))


def circle15a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 250 + a0 * 1280
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 230 * 230)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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


def line17a(coord0, coord1, anglea):
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


def line18a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0

    if(1050 - coord1 >220 ):
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


def circle19a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 250 + a0 * 1670
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 230 * 230)
    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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

def circle20a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 250 + a0 * 1670
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 30 * 30)

    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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

        if (y1a <= 250 and x1a >= 1670 and coord0 > x1a and 1050 - coord1 < y1a):
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))



def line21a(coord0, coord1, anglea):
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


def line22a(coord0, coord1, anglea):

    if (coord0 < 1700):
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



def circle23a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 620 + a0 * 1500
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 400 * 400)

    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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

def circle24a(coord0, coord1, anglea):
    a1 = a0
    b1 = b0 - 620 + a0 * 1500
    deltacircle1 = 4 * a1 * a1 * b1 * b1 - 4 * (a1 * a1 + 1) * (b1 * b1 - 200 * 200)

    if (deltacircle1 < 0):
        return ((0, 0))

    a0a = math.tan(math.radians(anglea))
    b0a = (1050 - coord1 - coord0 * a0a)
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

        if (y1a >= 620 and x1a >= 1500) and x1a < coord0:
            return ((x1a, y1a))
        else:
            return ((0, 0))

    return ((0, 0))


def przeciecie(linepar, coord, ang):
    return zip(numpy.linspace(p1[0], p2[0], parts+1), numpy.linspace(p1[1], p2[1], parts+1))

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1), numpy.linspace(p1[1], p2[1], parts+1))

#round(list(getEquidistantPoints((0,0), (1,2), 10)))

def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height),
        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

    # draw rectangle around the image
    #pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)

