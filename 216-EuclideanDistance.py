'''PSCP Program'''
def main(point, dist):
    '''8393-EuclideanDistance 28/10/2022'''
    for i in range(int(input())):
        point.append([int(i) for i in input().split()])
    for i, j in enumerate(point):
        if i < 1:
            continue
        dist += ((j[0]-point[i-1][0])**2 + (j[1]-point[i-1][1])**2)**0.5
    print("%.02f"%dist)
main([], 0)
