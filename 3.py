points = list(map(int, input('input point x and y separated by coma - ').split()))
if points[0] > 0 and points[1] > 0:
    print('1 quarter')
elif points[0] < 0 < points[1]:
    print('2 quarter')
elif points[0] < 0 and points[1] < 0:
    print('3 quarter')
else:
    print('4 quarter')
