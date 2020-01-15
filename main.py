import vacuumrobot as v
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
from prettytable import PrettyTable


def main():
    env1_robots = [v.Robot(10, 1, v.env1[10][1]) for i in range(0, 3)]
    env1_action = []
    env1_clean = []

    env2_robots = [v.Robot(11, 1, v.env2[11][1]) for i in range(0, 3)]
    env2_action = []
    env2_clean = []

    # env1, env2
    dumb_data = []
    smart_data = []

    # all robots cleaning the first environment
    for i in env1_robots:
        if env1_robots.index(i) == 0:
            a, c = v.dumb_robot(env1_robots[0], v.env1)
            # append actions, clean count
            dumb_data.append((a, c))

        elif env1_robots.index(i) == 1:
            for j in range(0, 50):
                action_count, clean_count = v.rand_robot(env1_robots[1], v.env1)
                insert_stat(action_count, clean_count, env1_action, env1_clean)
                # reset the robot to initialized values
                env1_robots[1].reset(10, 1, v.env1[10][1])

        elif env1_robots.index(i) == 2:
            a, c = v.smart_robot(env1_robots[2], v.env1)
            smart_data.append((a, c))

    # all robots cleaning the second environment
    for i in env2_robots:
        if env2_robots.index(i) == 0:
            a, c = v.dumb_robot(env2_robots[0], v.env2)
            # append actions, clean count
            dumb_data.append((a, c))

        elif env2_robots.index(i) == 1:
            for j in range(0, 50):
                action_count, clean_count = v.rand_robot(env2_robots[1], v.env2)
                insert_stat(action_count, clean_count, env2_action, env2_clean)
                # reset the robot to initialized values
                env2_robots[1].reset(11, 1, v.env2[11][1])

        elif env2_robots.index(i) == 2:
            a, c = v.smart_robot(env2_robots[2], v.env2)
            smart_data.append((a, c))

    # plot each environment on a scatter plot
    plot_env(env1_action, env1_clean, "Environment 1", "env1")
    plot_env(env2_action, env2_clean, "Environment 2", "env2")

    # find the avgs for random robot for each environment
    print("\nEnvironment 1 - Random Robot")
    action_avg1, clean_avg1 = random_stats(env1_action, env1_clean)
    print("\nEnvironment 2 - Random Robot")
    action_avg2, clean_avg2 = random_stats(env2_action, env2_clean)

    # construct rows for the table
    agent = ["ENV1 Simple", "ENV1 Random", "ENV1 Memory", "ENV2 Simple", "ENV2 Random", "ENV2 Memory"]
    actions_taken = [dumb_data[0][0], action_avg1, smart_data[0][0], dumb_data[1][0], action_avg2, smart_data[1][0]]
    spaces_cleaned = [dumb_data[0][1], clean_avg1, smart_data[0][1], dumb_data[1][1], clean_avg2, smart_data[1][1]]

    # print table
    t = PrettyTable(['Agent', 'Actions Taken', 'Clean Cells'])
    for i in zip(agent, actions_taken, spaces_cleaned):
        t.add_row([i[0], i[1], i[2]])
    print("\nAgent Performance Across Environments")
    print(t)


# plot the environment on a scatter plot
def plot_env(action, clean, title, file):
    plt.plot(action, clean, 'go')
    plt.ylabel('Clean Cells')
    plt.xlabel('Actions taken')
    plt.title(title)

    # trendline
    plt.plot(np.unique(action), np.poly1d(np.polyfit(action, clean, 1))(np.unique(action)))

    # show/save plot
    # plt.show()
    plt.savefig(file, bbox_inches='tight')


def random_stats(action, clean):
    # sort each array and get top 45
    action_sort = deepcopy(action)
    action_sort.sort()
    action_sort = action_sort[5:]

    clean_sort = deepcopy(clean)
    clean_sort.sort()
    clean_sort = clean_sort[5:]

    # get average of random for each environment
    action_avg = round(sum(action_sort)/len(action_sort))
    clean_avg = round(sum(clean_sort)/len(clean_sort))

    # get all values with 90 or better clean
    best = list(zip(action, clean))
    best_clean = [i for i in best if i[1] >= 90]

    # print best clean in a table
    t = PrettyTable(['Actions Taken', 'Clean Cells'])
    for i in best_clean:
        t.add_row([i[0], i[1]])
    print(t)

    return action_avg, clean_avg


def insert_stat(action, clean, a_list, c_list):
    a_list.append(action)
    c_list.append(clean)


if __name__ == "__main__":
    main()


