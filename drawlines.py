def drawlines(screen, linewidth):
    import pygame, sys, math, numpy
    line1 = [(10, 1050 - 620), (10, 1050 - 250)]
    line2 = [(210, 1050 - 620), (210, 1050 - 250)]

    line5 = [(470, 1050 - 250), (470, 1050 - 550)]
    line6 = [(270, 1050 - 250), (270, 1050 - 550)]

    line9 = [(520, 1050 - 600), (1000, 1050 - 600)]
    line10 = [(520, 1050 - 800), (1000, 1050 - 800)]

    line13 = [(1050, 1050 - 250), (1050, 1050 - 550)]
    line14 = [(1250, 1050 - 250), (1250, 1050 - 550)]

    line17 = [(1280, 1050 - 20), (1670, 1050 - 20)]
    line18 = [(1280, 1050 - 220), (1670, 1050 - 220)]

    line21 = [(1900, 1050 - 620), (1900, 1050 - 250)]
    line22 = [(1700, 1050 - 620), (1700, 1050 - 250)]

    line25 = [(410, 1050 - 1020), (1500, 1050 - 1020)]
    line26 = [(410, 1050 - 820), (1500, 1050 - 820)]

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
    # pygame.draw.circle(screen, (255, 0, 0), (240, 1050 - 250), 30, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(210, 1050 - 250 - 30, 60, 60), math.radians(-180), math.radians(0),
                    linewidth)
    # circle 4
    # pygame.draw.circle(screen, (255, 0, 0), (240, 1050 - 250), 230, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(240 - 230, 1050 - 250 - 230, 460, 460), math.radians(-180),
                    math.radians(0), linewidth)
    # circle 7
    # pygame.draw.circle(screen, (255, 0, 0), (520, 1050 - 550), 50, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(520 - 50, 1050 - 550 - 50, 100, 100), math.radians(-270),
                    math.radians(-180), linewidth)
    # circle 8
    # pygame.draw.circle(screen, (255, 0, 0), (520, 1050 - 550), 250, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(520 - 250, 1050 - 550 - 250, 500, 500), math.radians(-270),
                    math.radians(-180), linewidth)
    # circle 11
    # pygame.draw.circle(screen, (255, 0, 0), (1000, 1050 - 550), 50, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1000 - 50, 1050 - 550 - 50, 100, 100), math.radians(0),
                    math.radians(90), linewidth)
    # circle 12
    # pygame.draw.circle(screen, (255, 0, 0), (1000, 1050 - 550), 250, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1000 - 250, 1050 - 550 - 250, 500, 500), math.radians(0),
                    math.radians(90), linewidth)
    # circle 15
    # pygame.draw.circle(screen, (255, 0, 0), (1280, 1050 - 250), 230, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1280 - 230, 1050 - 250 - 230, 460, 460), math.radians(-180),
                    math.radians(-90), linewidth)
    # circle 16
    # pygame.draw.circle(screen, (255, 0, 0), (1280, 1050 - 250), 30, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1280 - 30, 1050 - 250 - 30, 60, 60), math.radians(-180),
                    math.radians(-90), linewidth)
    # circle 19
    # pygame.draw.circle(screen, (255, 0, 0), (1670, 1050 - 250), 230, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1670 - 230, 1050 - 250 - 230, 460, 460), math.radians(-90),
                    math.radians(0), linewidth)
    # circle 20
    # pygame.draw.circle(screen, (255, 0, 0), (1670, 1050 - 250), 30, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1670 - 30, 1050 - 250 - 30, 60, 60), math.radians(-90),
                    math.radians(0), linewidth)
    # circle 23
    # pygame.draw.circle(screen, (255, 0, 0), (1500, 1050 - 620), 400, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1500 - 400, 1050 - 620 - 400, 800, 800), math.radians(0),
                    math.radians(90), linewidth)
    # circle 24
    # pygame.draw.circle(screen, (255, 0, 0), (1500, 1050 - 620), 200, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(1500 - 200, 1050 - 620 - 200, 400, 400), math.radians(0),
                    math.radians(90), linewidth)
    # circle 27
    # pygame.draw.circle(screen, (255, 0, 0), (410, 1050 - 620), 400, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(410 - 400, 1050 - 620 - 400, 800, 800), math.radians(-270),
                    math.radians(-180), linewidth)
    # circle 28
    # pygame.draw.circle(screen, (255, 0, 255), (410, 1050 - 620), 200, 3)
    pygame.draw.arc(screen, (255, 0, 0), pygame.Rect(410 - 200, 1050 - 620 - 200, 400, 400), math.radians(-270),
                    math.radians(-180), linewidth)
    return(0)
