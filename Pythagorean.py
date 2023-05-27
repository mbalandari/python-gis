import math

x1, y1 = 456456.23, 1279721.064
x2, y2 = 576628.34, 1071740.33

x_dist, y_dist = x1 - x2, y1 - y2
dist_sq = x_dist**2 + y_dist**2
distance = math.sqrt(dist_sq)
print(distance)
