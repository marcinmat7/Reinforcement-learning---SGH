# Wyświetla tor, rakietkę i odległości


#siec = {'a1': 5, 'a2': 7, 'a3': 2, 'a4': 2, , 'a5': 3}
linewidth = 5
stop = False

decision = "p"
czubek = (0, 0)
ba0= (0,0)
baP60= (0,0)
baP30= (0,0)
baM30= (0,0)
baM60= (0,0)
deltacircleroot = 0
deltacircle = 0
anglecorrect = 0
a0 = 0
b0 = 0
ba = (0,0)


def getcoord(line1):
    point1 = (line1[0][0], 1080 - line1[0][1])
    point2 = (line1[1][0], 1080 - line1[1][1])
    a = (point1[1] - point2[1]) / (point1[0] - point2[1])
    b = point1[1] - a * point1[0]
    coord = (a, b)
    return coord

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



par1 = getcoord(line1)
par2 = getcoord(line2)

par5 = getcoord(line5)
par6 = getcoord(line6)


import os
# Get the current working directory
cwd = os.getcwd()
cwd = '/home/marcin/Pulpit/rakietka_v0.1/figures'
print(cwd)
# Set the current working directory
os.chdir(cwd)

pygame.init()
print(pygame.__version__)

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Tutorial 1')
bc = pygame.image.load("bg2.jpg").convert()
#pygame.draw.circle(screen, (255, 255, 255), (500,500), 20, 10)
ship = pygame.image.load("rocket.png").convert_alpha()
w, h = ship.get_size()
box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
box_rotate = [p.rotate(90) for p in box]
#drawHouse(x, y, width, height, screen, color)
min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
#list = [(1,1),(1,100),(100,1)]
distance = 0

#TEXT
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
angle = -90
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
#coord = [50,50]

#coord = [1000,140]
coord = [800,350]
a = coord
tekst1 = 1
math.radians(angle)
if stop == False:
    ship2 = pygame.transform.rotate(ship, angle)
#player_rect = ship2.get_rect()
#player_rect.center = coord

box = pygame.Rect(10, 10, 50, 50)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    keys = pygame.key.get_pressed()

    if stop == False:

        if keys[pygame.K_d]:
            coord[0] += 1
        if keys[pygame.K_s]:
            coord[1] += 1
        if keys[pygame.K_w]:
            coord[1] -= 2*math.cos(math.radians(angle))
            coord[0] -= 2*math.sin(math.radians(angle))
        if keys[pygame.K_a]:
            coord[0] -= 1
        if keys[pygame.K_q] or decision == "l":
            angle = (angle + 1) % 360
        if keys[pygame.K_e] or decision == "r":
            angle = (angle - 1) % 360
            #angle = 90
    if keys[pygame.K_p] :
        sys.exit(0)


    #if stop == False:
        #coord[1] -= 3*math.cos(math.radians(angle))
        #coord[0] -= 3*math.sin(math.radians(angle))






    #pygame.draw.circle(screen, (255, 255, 255), (700, 700), 500, 5)
    #list = [(100, 100), (100, 200), (200, 300)]

    if stop == False:
        anglecorrect =  (angle + 90) % 360

        x_rocket = coord[0]
        y_rocket = 1080 - coord[1]

        x_p = (y_rocket - x_rocket * math.tan(math.radians(90 + angle)) - par1[1]) / \
              (par1[0] - math.tan(math.radians(90 + angle)))
        y_p = par1[0] * x_p + par1[1]
        # ba0 = (0,0)
        # ba1 = (0, 0)
        distsqP60 = (czubek[0] - baP60[0]) ** 2 + (1050 - czubek[1] - baP60[1]) ** 2
        distsqP30 = (czubek[0] - baP30[0]) ** 2 + (1050 - czubek[1] - baP30[1]) ** 2
        distsq0 = (czubek[0] - ba0[0]) ** 2 + (1050 - czubek[1] - ba0[1]) ** 2
        distsqM30 = (czubek[0] - baM30[0]) ** 2 + (1050 - czubek[1] - baM30[1]) ** 2
        distsqM60 = (czubek[0] - baM60[0]) ** 2 + (1050 - czubek[1] - baM60[1]) ** 2

    #if min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) < 10:
    #    stop = True

    #if min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) == distsqP60 or min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) == distsqP30:
    #   decision = "r"

    #if min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) == distsqM30 or min(distsqP60, distsqP30, distsq0, distsqM30, distsqM60) == distsqM60:
    #    decision = "l"

    #dista = 100
    #if math.sqrt(distsq0) > 200 and math.sqrt(distsqP60) > dista and math.sqrt(distsqP30) > dista and math.sqrt(distsqM60) > dista and math.sqrt(distsqM30) > dista :
    #    decision = "p"

    #ran1 = random()
    #ran2 = random()
    #ran3 = random()

    #if ran1 > ran2 and ran1 > ran3:
    #    decision = "l"

    #if ran2 > ran1 and ran2 > ran3:
    #    decision = "r"

    #if ran3 > ran2 and ran3 > ran1:
    #    decision = "p"

    dist = str(round(math.sqrt(distsq0), 2))
    tekst0 = "Dist: " + dist

    dist = str(round(math.sqrt(distsqP60), 2))
    tekstP60 = "Dist: " + dist

    dist = str(round(math.sqrt(distsqP30), 2))
    tekstP30 = "Dist: " + dist

    dist = str(round(math.sqrt(distsqM30), 2))
    tekstM30 = "Dist: " + dist

    dist = str(round(math.sqrt(distsqM60), 2))
    tekstM60 = "Dist: " + dist
    if stop == False:
        # tekst1 = str((deltacircleroot, a0, b0, angle, x_p, y_p))
        x_p = (y_rocket - x_rocket * math.tan(math.radians(90 + angle)) - par2[1]) / \
              (par2[0] - math.tan(math.radians(90 + angle)))
        y_p = par1[0] * x_p + par1[1]


            # tekst2 = str(( angle,  x_p, y_p))
        text0 = font.render(str(tekst0), True, green, blue)
        textP30 = font.render(str(tekstP30), True, green, blue)
        textP60 = font.render(str(tekstP60), True, green, blue)
        textM30 = font.render(str(tekstM30), True, green, blue)
        textM60 = font.render(str(tekstM60), True, green, blue)

        screen.blit(bc, [0, 0])
        screen.blit(text0, textRect0)
        screen.blit(textP30, textRectP30)
        screen.blit(textP60, textRectP60)
        screen.blit(textM30, textRectM30)
        screen.blit(textM60, textRectM60)

        # Laser:
        delta = (50 * math.sin(math.radians(angle)), 50 * math.cos(math.radians(angle)))
        delta2 = (500 * math.sin(math.radians(angle)), 500 * math.cos(math.radians(angle)))
        xx = coord[0] - delta[0]
        yy = coord[1] - delta[1]
        czubek = [xx, yy]
        # coordsrodek = coord
        # coord = czubek
        # pygame.draw.line(screen, (255, 0, 0), czubek, (coord[0] - delta2[0], coord[1] - delta2[1]) , 3)

        a0 = math.tan(math.radians(anglecorrect))
        b0 = (1050 - czubek[1] - czubek[0] * a0)

        a0 = math.tan(math.radians(anglecorrect))
        b0 = (1050 - czubek[1] - czubek[0] * a0)
        ba0 = crosspointsfunction(anglecorrect, coord, czubek)

        a0 = math.tan(math.radians(anglecorrect + 30))
        b0 = (1050 - czubek[1] - czubek[0] * a0)
        baP30 = crosspointsfunction(anglecorrect +30, coord, czubek)

        a0 = math.tan(math.radians(anglecorrect + 60))
        b0 = (1050 - czubek[1] - czubek[0] * a0)
        baP60 = crosspointsfunction(anglecorrect + 60, coord, czubek)

        a0 = math.tan(math.radians(anglecorrect - 30))
        b0= (1050 - czubek[1] - czubek[0] * a0)
        baM30  = crosspointsfunction(anglecorrect - 30, coord, czubek)

        a0 = math.tan(math.radians(anglecorrect - 60))
        b0 = (1050 - czubek[1] - czubek[0] * a0)
        baM60 = crosspointsfunction(anglecorrect - 60, coord, czubek)

    pygame.draw.circle(screen, (255, 255, 255), (round(ba0[0]), round(1050 - ba0[1])), 10, 0)
    pygame.draw.circle(screen, (255, 255, 255), (round(baP30[0]), round(1050 - baP30[1])), 10, 0)
    pygame.draw.circle(screen, (255, 255, 255), (round(baP60[0]), round(1050 - baP60[1])), 10, 0)
    pygame.draw.circle(screen, (255, 255, 255), (round(baM30[0]), round(1050 - baM30[1])), 10, 0)
    pygame.draw.circle(screen, (255, 255, 255), (round(baM60[0]), round(1050 - baM60[1])), 10, 0)


    pygame.draw.line(screen, (255, 0, 0), line1[0], line1[1], linewidth)
    pygame.draw.line(screen, (255, 0, 0), line2[0], line2[1], linewidth)

    pygame.draw.line(screen, (255, 0, 0), line5[0], line5[1], linewidth)
    pygame.draw.line(screen, (255, 0, 0), line6[0], line6[1], linewidth)

    pygame.draw.line(screen, (255, 0, 0), line9[0], line9[1], linewidth)
    pygame.draw.line(screen, (255, 0, 0), line10[0], line10[1], linewidth)

    pygame.draw.line(screen, (255, 0, 0), line13[0], line13[1], linewidth)
    pygame.draw.line(screen, (255, 0, 0), line14[0], line14[1], linewidth)

    pygame.draw.line(screen, (255, 0, 0), line17[0], line17[1], linewidth)
    pygame.draw.line(screen, (255, 0, 0), line18[0], line18[1], linewidth)

    pygame.draw.line(screen, (255, 0, 0), line21[0], line21[1], linewidth)
    pygame.draw.line(screen, (255, 0, 0), line22[0], line22[1], linewidth)

    pygame.draw.line(screen, (255, 0, 0), line25[0], line25[1], linewidth)
    pygame.draw.line(screen, (255, 0, 0), line26[0], line26[1], linewidth)

    # circle 3
    #pygame.draw.circle(screen, (255, 0, 0), (240, 1050 - 250), 30, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(210, 1050-250-30, 60, 60), math.radians(-180), math.radians(0), linewidth)
    # circle 4
    #pygame.draw.circle(screen, (255, 0, 0), (240, 1050 - 250), 230, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(240 - 230, 1050-250-230, 460, 460), math.radians(-180), math.radians(0), linewidth)
    # circle 7
    #pygame.draw.circle(screen, (255, 0, 0), (520, 1050 - 550), 50, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(520 - 50, 1050 - 550 - 50, 100, 100), math.radians(-270),
                    math.radians(-180), linewidth)
    # circle 8
    #pygame.draw.circle(screen, (255, 0, 0), (520, 1050 - 550), 250, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(520 - 250, 1050 - 550 - 250, 500, 500), math.radians(-270),
                    math.radians(-180), linewidth)
    # circle 11
    #pygame.draw.circle(screen, (255, 0, 0), (1000, 1050 - 550), 50, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1000 - 50, 1050 - 550 - 50, 100, 100), math.radians(0),
                    math.radians(90), linewidth)
    # circle 12
    #pygame.draw.circle(screen, (255, 0, 0), (1000, 1050 - 550), 250, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1000 - 250, 1050 - 550 - 250, 500, 500), math.radians(0),
                    math.radians(90), linewidth)
    # circle 15
    #pygame.draw.circle(screen, (255, 0, 0), (1280, 1050 - 250), 230, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1280 - 230, 1050 - 250 - 230, 460, 460), math.radians(-180),
                    math.radians(-90), linewidth)
    # circle 16
    #pygame.draw.circle(screen, (255, 0, 0), (1280, 1050 - 250), 30, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1280 - 30, 1050 - 250 - 30, 60, 60), math.radians(-180),
                    math.radians(-90), linewidth)
    # circle 19
    #pygame.draw.circle(screen, (255, 0, 0), (1670, 1050 - 250), 230, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1670 - 230, 1050 - 250 - 230, 460, 460), math.radians(-90),
                    math.radians(0), linewidth)
    # circle 20
    #pygame.draw.circle(screen, (255, 0, 0), (1670, 1050 - 250), 30, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1670 - 30, 1050 - 250 - 30, 60, 60), math.radians(-90),
                    math.radians(0), linewidth)
    # circle 23
    #pygame.draw.circle(screen, (255, 0, 0), (1500, 1050 - 620), 400, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1500 - 400, 1050 - 620 - 400, 800, 800), math.radians(0),
                    math.radians(90), linewidth)
    # circle 24
    #pygame.draw.circle(screen, (255, 0, 0), (1500, 1050 - 620), 200, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1500 - 200, 1050 - 620 - 200, 400, 400), math.radians(0),
                    math.radians(90), linewidth)
    # circle 27
    #pygame.draw.circle(screen, (255, 0, 0), (410, 1050 - 620), 400, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(410 - 400, 1050 - 620 - 400, 800, 800), math.radians(-270),
                    math.radians(-180), linewidth)
    # circle 28
    #pygame.draw.circle(screen, (255, 0, 0), (410, 1050 - 620), 200, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(410 - 200, 1050 - 620 - 200, 400, 400), math.radians(-270),
                    math.radians(-180), linewidth)

    blitRotate(screen, ship, coord, (50, 50), angle)

    pygame.display.flip()



