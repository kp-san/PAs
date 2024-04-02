# PA1 Code

import random
import time

def one_dimensional_moves(steps):
    position = 0
    counter = 0
    for i in range(steps):
        position += random.choice([-1, 1])
        if position == 0:
            counter = 1
            break
    return counter

def two_dimensional_moves(steps):
    position = [0, 0]
    counter = 0
    for i in range(steps):
        axis = random.choice([0, 1])
        direction = random.choice([-1, 1])
        position[axis] += direction
        if position == [0, 0]:
            counter = 1
            break
    return counter

def three_dimensional_moves(steps):
    position = [0, 0, 0]
    counter = 0
    for i in range(steps):
        axis = random.choice([0, 1, 2])
        direction = random.choice([-1, 1])
        position[axis] += direction
        if position == [0, 0, 0]:
            counter = 1
            break
    return counter

def run_experiment(dimension, steps, trials):
    count_returned_origin = 0
    start_time = time.time()
    
    for i in range(trials):
        if dimension == 1:
            count_returned_origin += one_dimensional_moves(steps)
        elif dimension == 2:
            count_returned_origin += two_dimensional_moves(steps)
        elif dimension == 3:
            count_returned_origin += three_dimensional_moves(steps)
    
    end_time = time.time()
    run_time = end_time - start_time
    
    return (count_returned_origin / trials) * 100, run_time

def main():
    dimensions = [1, 2, 3]
    steps_list = [20, 200, 2000, 20000, 200000, 2000000]
    trials = 100

    print("Percentages of time particle returned to origin:")
    print("Number of steps:", end=" ")
    for steps in steps_list:
        print(steps, end=" ")
    print()

    for dimension in dimensions:
        print(f"{dimension}D", end=" ")
        for steps in steps_list:
            percentage, i = run_experiment(dimension, steps, trials)
            print(f"{percentage:.2f}%", end=" ")
        print()

    print("\nRun time (seconds):")
    print("Number of steps:", end=" ")
    for steps in steps_list:
        print(steps, end=" ")
    print()

    for dimension in dimensions:
        if dimension == 3:
            print(f"{dimension}D", end=" ")
            for steps in steps_list:
                i, run_time = run_experiment(dimension, steps, trials)
                print(f"{run_time:.6f}", end=" ")
            print()

main()
