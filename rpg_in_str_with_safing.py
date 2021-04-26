''' n = 7  m = 3
| | | | | | |
| | | | | | |
| | | | | | |

'''
from random import randrange

def serialize_game_data(n,m,x,y, portal_x, portal_y):
    return f'{n}\n{m}\n{x}\n{y}\n{portal_x}\n{portal_y}'

def deserialize_game_data(serialized_game_data):

    n, m, x, y, portal_x, portal_y = map(int, serialized_game_data.split())
    return n, m, x, y, portal_x, portal_y

def save_game( serialized_game_data):
    print("Saving game ...")
    with open('save.txt', 'w') as file:
        file.write(serialize_game_data(x,y, portal_x, portal_y))
    print("The game has been saved")


def load_game():
    print("Loading game ...")
    with open('save.txt', 'r') as file:
        serialized_game_data = file.read()
    print("The game has been loaded")
    return serialized_game_data

def general_map(x, y, portal_x, portal_y):
    world_map = []
    for i in range(MAP_SIZE_M):
        row = []
        for j in range(MAP_SIZE_N):
            row.append(' ')
        world_map.append(row)
    world_map[x][y] = 'X'
    world_map[portal_x][portal_y] = '0'
    return world_map

def print_map(world_map):
    for el in world_map :
        print(f"|{'|'.join(el)}|")

def move(direction, x, y):
    
    if direction == 'up' and y > 0:
        y -= 1
    elif direction == 'down' and y < MAP_SIZE_M-1:
        y += 1
    elif direction == 'left':
        x -= 1
        if x == -1 :
            x = MAP_SIZE_N - 1
    elif direction == 'right':
        x += 1
        if x == MAP_SIZE_N :
            x = 0
    else:
         raise ValueError("Wrong direction")
    print(f'moving character {direction} to {x}:{y}')
    return x, y


def initialize_config(auto = True):
    if auto :
        n = int(input('Map size n : '))
        m = int(input('Map size m : '))
        x = int(input('Where am I ? X : '))
        y = int(input('Where am I ? Y : '))    
        portal_x = randrange(n)
        portal_y = randrange(m)
        direction = 'initially'

    else:   
        n, m = randrange(3,10) , randrange(3, 10)
        x, y = randrange(n) , randrange(m)

        portal_x, portal_y = randrange(n), randrange(m)

        direction = 'initially'

    
    return n, m, x, y, portal_x, portal_y

if __name__ == '__main__':
    MAP_SIZE_N, MAP_SIZE_M, x, y, portal_x, portal_y =  initialize_config(input())
    print(MAP_SIZE_N, MAP_SIZE_M)
    print(x, y)
    print(portal_x, portal_y )
    while True:
        
        world_map = general_map(x, y, portal_x, portal_y)
        print_map(world_map)
        
        if x == portal_x and y == portal_y :
            print('I won')
            break
        action = input('Action :  ')
        if action == 'move' :
            try:
                direction = input('Direction (up/down/left/right): ')
                x, y =  move(direction, x, y)       
            except ValueError as error:
                print(error)
        elif action == 'save':
            serialized_game_data = serialize_game_data(MAP_SIZE_N,MAP_SIZE_M,x,y, portal_x, portal_y)
            save_game(serialized_game_data)
        elif action == 'load':
            serialized_game_data = load_game()
            MAP_SIZE_N,MAP_SIZE_M,x,y, portal_x, portal_y = deserialize_game_data(serialized_game_data)
        elif action =='quit':
            break
            
    
    print(' Game over')
