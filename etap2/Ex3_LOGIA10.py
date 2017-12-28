from math import*

class Point(object):
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
        
def robot(track):
    list = []
    cx, cy = 500, 500
    length = len(track)
    if (length > 500):
        return
    listLength = 0
    howMany = 0
    m = 0
    for i in range(0, length):
        if (track[i] == 'N'):
            cy = cy + 1
        elif (track[i] == 'S'):
            cy = cy - 1
        elif (track[i] == 'W'):
            cx = cx - 1
        elif (track[i] == 'E'):
            cx = cx + 1
        else:
            return
        for u in range(0, listLength):
            if (list[u].x == cx & list[u].y == cy):
                m = m + 1
        if (m == 0):
            list.append(Point(cx, cy))
        else:
            howMany = howMany + 1
            m = 0
        listLength = len(list)
    print(howMany)

robot("NNESWWSEE")
