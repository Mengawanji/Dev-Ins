pic = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for elements in pic:
   for items in elements:
       if items == 1:
           print('*', end=' ')
       else:
           print(' ', end=' ')
   print('')
