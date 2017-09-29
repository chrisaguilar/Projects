"""
Classic Algorithm 03: Closest Pair Problem.

The closest pair of points problem or closest pair problem is a problem of
computational geometry: given n points in metric space, find a pair of points
with the smallest distance between them.
"""

from math import sqrt


def dist(p_1, p_2):
    """Calculate the distance between p_1 and p_2."""
    x_1, y_1 = p_1
    x_2, y_2 = p_2
    return sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)


def closest_pair(points):
    """Find the closest pair in an array of given points."""
    count = len(points)
    min_dist = float('inf')
    for i in range(count):
        for j in range(i + 1, count):
            point_1 = points[i]
            point_2 = points[j]
            if dist(point_1, point_2) < min_dist:
                min_dist = dist(point_1, point_2)
                closest = (point_1, point_2)
    return closest


print(closest_pair([(1, 5), (-2, 4), (-6, 3), (1.4, 8)]))
tst = closest_pair([(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)])

print(sqrt((tst[1][0] - tst[0][0])**2 + (tst[1][1] - tst[0][1])**2))
