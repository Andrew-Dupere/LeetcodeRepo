def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    pass



""""
0,0

0,2

3,2

3,0

"""
ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2

#list of touples for each coordinate of the interior rectangle
coords = [(ax1,bx1), (ay1,by1), (ax2,bx2)]


print(max(coords[0]), min(ay2,by1))
