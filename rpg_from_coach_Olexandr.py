from random import randint


def generate_map(x, y, portal_x, portal_y):

    print(x, y)
    print(portal_x, portal_y)

    world_map = []

    for i in range(MAP_SIZE_M):      

        row = []

        for j in range(MAP_SIZE_N):    
                                                             
            row.append(' ')

        world_map.append(row)
    
    world_map[y][x] = 'X'
    world_map[portal_y][portal_x] = 'O'

    return world_map


def print_map(world_map):

    for row in world_map:
        print(f'|{"|".join(row)}|')


def initialize_configs(manual=False):

    if manual:
        n = int(input('Map size n: '))
        m = int(input('Map size m: '))

        x = int(input('Player x: '))
        y = int(input('Player y: '))

        portal_x, portal_y = randint(0, n - 1), randint(0, m - 1)
    else:
        n, m = randint(5, 10), randint(5, 10)
        x, y = randint(0, n - 1), randint(0, m - 1)
        portal_x, portal_y = randint(0, n - 1), randint(0, m - 1)

    return n, m, x, y, portal_x, portal_y


def move(direction, x, y):

    if direction == 'up' and y > 0:
        y -= 1
    elif direction == 'down' and y < MAP_SIZE_M - 1:
        y += 1
    elif direction == 'left':
        x -= 1
        x = MAP_SIZE_N - 1 if x < 0 else x
    elif direction == 'right':
        x += 1
        x = 0 if x == MAP_SIZE_N else x
    else:
        raise ValueError('Wrong direction. Please try again.')

    print(f'Moving character {direction} to {x}:{y}')

    return x, y


if __name__ == '__main__':

    manual = input('Auto configs? ')
    MAP_SIZE_N, MAP_SIZE_M, x, y, portal_x, portal_y = initialize_configs(manual)

    while True:
        
        world_map = generate_map(x, y, portal_x, portal_y)
        print_map(world_map)

        if x == portal_x and y == portal_y:
            print('You won!')
            break

        action = input('Action: ')

        if action == 'move': 
            direction = input('Direction: ')

            try:
                x, y = move(direction, x, y)
            except ValueError as error:
                print(error)

        elif action == 'exit':
            break
        else:
            print('Wrong action. Please try again.')

    print('Game Over')
