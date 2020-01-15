import random as rand
from copy import deepcopy


class Robot:
    def __init__(self, x, y, location):
        self.x = x
        self.y = y
        self.location = location
        self.direction = "up"
        self.power = "on"
        self.dirt_sensor = 0
        self.wall_sensor = 0
        self.home_sensor = 0

    def reset(self, x, y, location):
        self.__init__(x, y, location)


# First Pass Hard Code of env1
env1 = [["Wall ", "Wall ","Wall ", "Wall ", "Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Home ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ", "Wall ","Wall ","Wall ", "Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall "]]

env2 = [["Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall ","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ","Home ","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Dirty","Wall "],
        ["Wall ", "Wall ","Wall ","Wall ", "Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall ","Wall "]]

#print (env2[11][1])
def print_env(env):
    #print env1 out nicely
    for i in range(len(env)):
        for j in range(len(env[i])):
            print(env[i][j], end=' ')
        print()


def number_clean(env):
    clean_count = 0
    for i in range(len(env)):
        for j in range(len(env[i])):
            if(env[i][j] == 'Clean'):
                clean_count +=1

    print("Number of spaces cleaned: ", clean_count)
    return clean_count
#print_env()


def dumb_robot(robot, env):
    # make sure env1 stays constant
    env_copy = deepcopy(env)

    actions = 0
    while(robot.power == 'on'):
        if(robot.dirt_sensor == 1):
            print('cleaning')
            suck(robot, env_copy)
        elif(robot.wall_sensor == 1):
            print('turning right')
            turn_right(robot)
            robot.wall_sensor = 0
        elif(robot.home_sensor == 1):
            print('turning off')
            robot.power = 'off'
        else:
            print('moving forward')
            move_forward(robot, env_copy)

        actions+=1
        check_sensors(robot, env_copy)

    print_env(env_copy)
    print("Actions taken: ", actions)
    cc = number_clean(env_copy)
    return actions, cc


def rand_robot(robot, env):
    # make sure env1 stays constant
    env_copy = deepcopy(env)

    actions = 0
    while(robot.power == 'on'):
        if(robot.dirt_sensor == 1):
            suck(robot, env_copy)
            print('cleaning')
        elif(robot.wall_sensor == 1):
            turn = rand.choice(["left", "right"])
            # turning left or right
            turn_right_left(turn, robot)
            robot.wall_sensor = 0
        elif(robot.home_sensor == 1):
            robot.power = 'off'
            print('turning off')
        else:
            turn = rand.choice(["right", "forward"])
            if turn != "forward":
                turn_right_left(turn, robot)
            else:
                move_forward(robot, env_copy)
                print('moving forward')
        actions+=1
        check_sensors(robot, env_copy)

    print_env(env_copy)
    print("Actions taken: ", actions)
    clean_count = number_clean(env_copy)
    print("\n\n")

    return actions, clean_count


def smart_robot(robot, env):
    # make sure env1 stays constant
    env_copy = deepcopy(env)

    actions = 0
    print(robot.x, robot.y, robot.location)
    while(robot.power == 'on'):
        if(robot.dirt_sensor == 1):
            print('cleaning')
            suck(robot, env_copy)
           # print_env(env_copy)
        elif(check_wall(robot, env_copy) == 2 and robot.direction == 'down' and robot.wall_sensor == 1):
            print("turning right in corner")
            turn_right(robot)
            robot.wall_sensor = 0
        elif(robot.wall_sensor == 1 and robot.y%2 == 1):
            print('turning right')
            turn_right(robot)
            robot.wall_sensor = 0
            robot.location = env_copy[robot.x][robot.y]
        elif(robot.wall_sensor == 1 and robot.y%2 == 0 and robot.direction == 'down'):
            print('turning left')
            turn_left(robot)
            robot.wall_sensor = 0
            robot.location = env_copy[robot.x][robot.y]
        elif(robot.home_sensor == 1):
            print('turning off')
            robot.power = 'off'
        elif(robot.location == 'Clean' and robot.wall_sensor == 0):
            print('moving forward2', robot.x, robot.y)
            #print_env(env_copy1)
            move_forward(robot, env_copy)
        elif(check_wall(robot, env_copy) and robot.y%2 == 0 and robot.direction == 'right'):
            print('turning right2')
            turn_right(robot)
            robot.wall_sensor = 0
        elif(check_wall(robot, env_copy) and robot.y%2 == 1 and robot.direction == 'right'):
            print('turning left2')
            turn_left(robot)
            robot.wall_sensor = 0
        else:
            print('moving forward')
            move_forward(robot, env_copy)

        actions+=1
        check_sensors(robot, env_copy)

    print_env(env_copy)
    print("Actions taken: ", actions)
    cc = number_clean(env_copy)

    return actions, cc


# robot takes left or right turn
def turn_right_left(turn, robot):
    if turn == "left":
        turn_left(robot)
        print('turning left')
    else:
        turn_right(robot)
        print('turning right')


def move_forward(robot, env):
    if(robot.direction == 'up'):
        #print("moving up in the world")
        robot.x -=1
    elif(robot.direction == 'right'):
        robot.y +=1
    elif(robot.direction == 'down'):
        robot.x+=1
    elif(robot.direction == 'left'):
        robot.y-=1
    robot.location = env[robot.x][robot.y]
    print('moved to: ', robot.x, robot.y, robot.location)


def suck(robot, env):
    env[robot.x][robot.y] = 'Clean'
    robot.dirt_sensor = 0


def turn_right(robot):
    if(robot.direction == 'up'):
        robot.direction = 'right'
    elif(robot.direction == 'right'):
        robot.direction = 'down'
    elif(robot.direction == 'down'):
        robot.direction = 'left'
    elif(robot.direction == 'left'):
        robot.direction = 'up'
    print("now facing: ", robot.direction)


def turn_left(robot):
    if(robot.direction == 'up'):
        robot.direction = 'left'
    elif(robot.direction == 'right'):
        robot.direction = 'up'
    elif(robot.direction == 'down'):
        robot.direction = 'right'
    elif(robot.direction == 'left'):
        robot.direction = 'down'
    print("now facing: ", robot.direction)


def check_sensors(robot, env):
    if(robot.location == 'Home '):
        robot.home_sensor = 1
    if(env[robot.x][robot.y] == 'Dirty'):
        robot.dirt_sensor = 1
    if(robot.direction == 'up' and env[robot.x-1][robot.y] == 'Wall '):
        robot.wall_sensor = 1
    elif(robot.direction == 'down' and env[robot.x+1][robot.y] == 'Wall '):
        robot.wall_sensor = 1
    elif(robot.direction == 'right' and env[robot.x][robot.y+1] == 'Wall '):
        robot.wall_sensor = 1
    elif(robot.direction == 'left' and env[robot.x][robot.y-1] == 'Wall '):
        robot.wall_sensor = 1


def check_wall(robot, env):
    num_walls = 0
    if(env[robot.x-1][robot.y] == 'Wall '):
        num_walls += 1
    if(env[robot.x+1][robot.y] == 'Wall '):
        num_walls += 1
    if(env[robot.x][robot.y+1] == 'Wall '):
        num_walls += 1
    if(env[robot.x][robot.y-1] == 'Wall '):
        num_walls += 1

    return num_walls
