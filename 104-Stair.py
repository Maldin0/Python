'''Stair'''


def main():
    '''Stairway to heaven'''
    dist = int(input())
    step = int(input())
    count = 0
    total_step = 0
    validity = True
    for i in range(step):
        this_step = int(input())
        if this_step > dist:
            validity = False
        elif i == step-1:
            if total_step + this_step > dist:
                count += 2
            elif total_step + this_step <= dist:
                count += 1
        elif this_step == dist:
            count += 1
        else:
            if total_step + this_step < dist:
                total_step += this_step
            elif total_step + this_step == dist:
                count += 1
                total_step = 0
            elif total_step + this_step > dist:
                count += 1
                total_step = this_step
    if not validity:
        print("NO")
    else:
        print(count)


main()
