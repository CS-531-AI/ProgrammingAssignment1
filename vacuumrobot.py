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


def print_env():
    #print env1 out nicely
    for i in range(len(env1)):
        for j in range(len(env1[i])):
            print(env1[i][j], end=' ')
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

    print_env()
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

def check_sensors(robot, env1):
    if(robot.location == 'Home '):
        robot.home_sensor = 1
    if(env1[robot.x][robot.y] == 'Dirty'):
        robot.dirt_sensor = 1
    if(robot.direction == 'up' and env1[robot.x-1][robot.y] == 'Wall '):
        robot.wall_sensor = 1
    elif(robot.direction == 'down' and env1[robot.x+1][robot.y] == 'Wall '):
        robot.wall_sensor = 1
    elif(robot.direction == 'right' and env1[robot.x][robot.y+1] == 'Wall '):
        robot.wall_sensor = 1
    elif(robot.direction == 'left' and env1[robot.x][robot.y-1] == 'Wall '):
        robot.wall_sensor = 1