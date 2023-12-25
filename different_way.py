import random
import sys
# from multiprocessing import Pool * next update (don't know how yet lol)


def randomizer(num_low, num_high, target_num):
    global target_hit
    randNum = random.randint(int(num_low), int(num_high))
    print(randNum)
    if randNum == int(target_num):
        target_hit += 1
    else:
        pass


def theory():
    [randomizer(0, 10, 10) for _ in range(100)]
    theory_hit.append(target_hit)


if __name__ == "__main__":
    target_hit = int()
    theory_hit = []
    [theory() for _ in range(1000)]
    print(f"the theory number was hit {sorted(theory_hit)} times")
    sys.exit()










