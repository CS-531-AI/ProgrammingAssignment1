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

#print(env1[10][1])

class Robot:
  def __init__(self, x, y, location, direction, power):
    self.x = x
    self.y = y
    self.location = location
    self.direction = direction
    self.power = power
    self.dirt_sensor = 0
    self.wall_sensor = 0
    self.home_sensor = 0

robot1 = Robot(10, 1, env1[10][1], 'up', 'on')

#print(robot1.location, robot1.direction)
#print(robot1.x, robot1.y)

def print_env():
#print env1 out nicely
    for i in range(len(env1)):
        for j in range(len(env1[i])):
            print(env1[i][j], end=' ')
        print()

#print_env()

def dumb_robot(robot1, env1):
    #move_forward(robot1)
    #suck(robot1, env1)
    #print_env()
    #turn_right(robot1)
    #turn_left(robot1)
    while(robot1.power == 'on'):
        #print_env()
        if(robot1.dirt_sensor == 1):
            print('cleaning')
            suck(robot1, env1)
        elif(robot1.wall_sensor == 1):
            print('turning right')
            turn_right(robot1)
            robot1.wall_sensor = 0
        elif(robot1.home_sensor == 1):
            print('turning off')
            robot1.power = 'off'
        else:
            print('moving forward')
            move_forward(robot1)

        check_sensors(robot1, env1)
    
def move_forward(robot1):
    if(robot1.direction == 'up'):
        #print("moving up in the world")
        robot1.x -=1
    elif(robot1.direction == 'right'):
        robot1.y +=1
    elif(robot1.direction == 'down'):
        robot1.x+=1
    elif(robot1.direction == 'left'):
        robot1.y-=1
    robot1.location = env1[robot1.x][robot1.y]

def suck(robot1, env1):
    env1[robot1.x][robot1.y] = 'Clean'
    robot1.dirt_sensor = 0

def turn_right(robot1):
    if(robot1.direction == 'up'):
         robot1.direction = 'right'
    elif(robot1.direction == 'right'):
        robot1.direction = 'down'
    elif(robot1.direction == 'down'):
        robot1.direction = 'left'
    elif(robot1.direction == 'left'):
        robot1.direction = 'up'
    print("now facing: ", robot1.direction)

def turn_left(robot1):
    if(robot1.direction == 'up'):
         robot1.direction = 'left'
    elif(robot1.direction == 'right'):
        robot1.direction = 'up'
    elif(robot1.direction == 'down'):
        robot1.direction = 'right'
    elif(robot1.direction == 'left'):
        robot1.direction = 'down'
    print("now facing: ", robot1.direction)

def check_sensors(robot1, env1):
    if(robot1.location == 'Home '):
        robot1.home_sensor = 1
    if(env1[robot1.x][robot1.y] == 'Dirty'):
        robot1.dirt_sensor = 1
    if(robot1.direction == 'up' and env1[robot1.x-1][robot1.y] == 'Wall '):
        robot1.wall_sensor = 1
    elif(robot1.direction == 'down' and env1[robot1.x+1][robot1.y] == 'Wall '):
        robot1.wall_sensor = 1
    elif(robot1.direction == 'right' and env1[robot1.x][robot1.y+1] == 'Wall '):
        robot1.wall_sensor = 1
    elif(robot1.direction == 'left' and env1[robot1.x][robot1.y-1] == 'Wall '):
        robot1.wall_sensor = 1
        
    

dumb_robot(robot1, env1)

#robot 1 pseudocode 
    #Starts in bottom left
    #if on dirty tile, clean tile
    #if facing wall turn right
    #if on home space, turn off
#main things to figure out 1) how to get robot to clean inner rows (this will just sweep the outside), 2) should the robot turn off the first time it reaches home? are we allowed to have a home counter i.e., the 3rd time the robot reaches home it turns off, this would also prevent the robot turning off on its first move
    
    
