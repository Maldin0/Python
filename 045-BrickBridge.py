'''BrickBridge'''
def main():
    '''BrickBridge'''
    smolb = int(input())
    bigb = int(input())
    goal = int(input())
    if goal//5 <= bigb and goal%5 <= smolb:
        print(goal%5)
    elif goal//5 > bigb and goal-bigb*5 <= smolb:
        print(goal-bigb*5)
    else:
        print(-1)
main()
