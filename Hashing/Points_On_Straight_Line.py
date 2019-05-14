# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Sample Input :

# (1, 1)
# (2, 2)
# Sample Output :

# 2
# You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])
def maxPoints(self, A, B):
    x = A
    y = B
    hash_map = {}
    max_point = 0
    for i in range(len(x)):
        duplicate = 1
        vertical = 0
        for j in range(i +1 , len(x)):
            if x[i] == x[j]:
                if y[i] == y[j]:
                    duplicate += 1
                else:
                    vertical += 1
            else:
                slope = 0.0 if y[i] == y[j] else 1.0*(y[j] - y[i])/(x[j] - x[i])
                if slope in hash_map:
                    hash_map[slope] += 1
                else:
                    hash_map[slope] = 1
        for count in hash_map.values():
            if count + duplicate > max_point:
                max_point = count + duplicate
        max_point = max(vertical + duplicate, max_point)
        hash_map.clear()
    return max_point
    
