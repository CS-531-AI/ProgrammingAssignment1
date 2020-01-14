import vacuumrobot as r


def main():
    # robot1 = r.Robot(10, 1, r.env1[10][1])
    # r.dumb_robot(robot1, r.env1)

    #robot2 = r.Robot(10, 1, r.env1[10][1])
    #r.rand_robot(robot2, r.env1)

    robot3 = r.Robot(10, 1, r.env1[10][1])
    r.smart_robot(robot3, r.env1)

    #robot4 = r.Robot(11, 1, r.env2[11][1])
    #r.dumb_robot(robot4, r.env2)

    #robot5 = r.Robot(11, 1, r.env2[11][1])
    #r.rand_robot(robot5, r.env2)

    #robot6 = r.Robot(11, 1, r.env2[11][1])
    #r.smart_robot(robot6, r.env2)

    
if __name__ == "__main__":
    main()


