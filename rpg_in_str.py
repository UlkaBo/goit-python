''' n = 7  m = 3
| | | | | | |
| | | | | | |
| | | | | | |

'''
from random import randrange
n = int(input('Map size n : '))
m = int(input('Map size m : '))
x = int(input('Where am I ? X : '))
y = int(input('Where am I ? Y : '))
portal_x = randrange(n)
portal_y = randrange(m)
direction = 'initially'
while True:
    
    world_map = ''
    for i in range(m):
        row = ''
        for j in range(n):
            if y == i and x == j:
                print(f'moving character {direction} to {x}:{y}')
                row += '|X'
            elif portal_y == i and portal_x == j:
                row += '|O'
                
            else:
                row += '| '
        row += ' \n'
        world_map += row

    print(world_map)
    if x == portal_x and y == portal_y :
        print('I won')
        break
    action = input('Action :  ')
    if action == 'move' :
        direction = input('Direction (up/down/left/right): ')
        if direction == 'up' and y > 0:
            y -= 1
        elif direction == 'down' and y < m-1:
            y += 1
        elif direction == 'left':
            x -= 1
            if x == -1 :
                x = n - 1
        if direction == 'right':
            x += 1
            if x == n :
                x = 0

    
print(' Game over')
