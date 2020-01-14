import random as rand


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

#First Pass Hard Code of env1
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


def print_env(env):
    #print env1 out nicely
    for i in range(len(env)):
        for j in range(len(env[i])):
            print(env[i][j], end=' ')
        print()


def number_clean():
    clean_count = 0
    for i in range(len(env1)):
        for j in range(len(env1[i])):
            if(env1[i][j] == 'Clean'):
                clean_count +=1

    print("Number of spaces cleaned: ", clean_count)
#print_env()

def dumb_robot(robot, env1):
    #move_forward(robot)
    #suck(robot, env1)
    #print_env()
    #turn_right(robot)
    #turn_left(robot)
    actions = 0
    while(robot.power == 'on'):
        if(robot.dirt_sensor == 1):
            print('cleaning')
            suck(robot, env1)
        elif(robot.wall_sensor == 1):
            print('turning right')
            turn_right(robot)
            robot.wall_sensor = 0
        elif(robot.home_sensor == 1):
            print('turning off')
            robot.power = 'off'
        else:
            print('moving forward')
            move_forward(robot)

        actions+=1
        check_sensors(robot, env1)

    print_env()
    print("Actions taken: ", actions)
    number_clean()

def rand_robot(robot, env1):
    actions = 0
    while(robot.power == 'on'):
        if(robot.dirt_sensor == 1):
            suck(robot, env1)
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
                move_forward(robot)
                print('moving forward')
        actions+=1
        check_sensors(robot, env1)

    print_env(env1)
    print("Actions taken: ", actions)
    number_clean()

def smart_robot(robot, env):
    actions = 0
    while(robot.power == 'on'):
        if(robot.dirt_sensor == 1):
            print('cleaning')
            suck(robot, env)
        elif(robot.x == 10 and robot.y == 10 and robot.direction == 'right'):
            #hardcode to get robot out of the corner part 1
            print('turning left3')
            turn_left(robot)
            robot.wall_sensor = 0
        elif(check_wall(robot, env) and robot.y == 10 and robot.direction == 'up'):
            #hardcode to get robot out of the corner part 2
            print('turning left4')
            turn_left(robot)
            robot.wall_sensor = 0
        elif(robot.wall_sensor == 1 and robot.y%2 == 1):
            print('turning right')
            turn_right(robot)
            robot.wall_sensor = 0
            robot.location = env[robot.x][robot.y]
        elif(robot.wall_sensor == 1 and robot.y%2 == 0 and robot.direction == 'down'):
            print('turning left')
            turn_left(robot)
            robot.wall_sensor = 0
            robot.location = env[robot.x][robot.y]
        elif(robot.home_sensor == 1):
            print('turning off')
            robot.power = 'off'
        elif(robot.location == 'Clean' and robot.wall_sensor == 0):
            print('moving forward2', robot.x, robot.y)
            #print_env(env1)
            move_forward(robot)
        elif(check_wall(robot, env) and robot.y%2 == 0 and robot.direction == 'right'):
            print('turning right2')
            turn_right(robot)
            robot.wall_sensor = 0
        elif(check_wall(robot, env) and robot.y%2 == 1 and robot.direction == 'right'):
            print('turning left2')
            turn_left(robot)
            robot.wall_sensor = 0
        else:
            print('moving forward')
            move_forward(robot)

        actions+=1
        check_sensors(robot, env)

    print_env(env)
    print("Actions taken: ", actions)
    number_clean()
# robot takes left or right turn
def turn_right_left(turn, robot):
    if turn == "left":
        turn_left(robot)
        print('turning left')
    else:
        turn_right(robot)
        print('turning right')


def move_forward(robot):
    if(robot.direction == 'up'):
        #print("moving up in the world")
        robot.x -=1
    elif(robot.direction == 'right'):
        robot.y +=1
    elif(robot.direction == 'down'):
        robot.x+=1
    elif(robot.direction == 'left'):
        robot.y-=1
    robot.location = env1[robot.x][robot.y]


def suck(robot, env1):
    env1[robot.x][robot.y] = 'Clean'
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
    if(env1[robot.x][robot.y] == 'Dirty'):
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
    if(env[robot.x-1][robot.y] == 'Wall '):
        return True
    elif(env[robot.x+1][robot.y] == 'Wall '):
        return True
    elif(env[robot.x][robot.y+1] == 'Wall '):
        return True
    elif(env[robot.x][robot.y-1] == 'Wall '):
        return True
    else:
        return False

