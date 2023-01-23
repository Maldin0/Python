'''PSCP Program'''
def main():
    '''8364-PedPonFire 24/10/2022'''
    ducks = []
    matched = []
    count = 0

    for _ in range(int(input())):
        ducks.append(int(input()))
    required = int(input())
    min_ducks = min(ducks)

    for i in set(ducks.copy()):
        if i > required or i + min_ducks > required:
            ducks.remove(i)

    count_i = ducks.count(int(required / 2)) if required % 2 == 0 else 0
    if count_i >= 2:
        count += ((count_i - 1) * count_i) / 2
        ducks = list(filter(lambda x: x != int(required / 2), ducks))

    for i in sorted(set(ducks)):
        if i >= required / 2:
            break
        check = required - i
        count_i = ducks.count(i)
        if i not in matched and ducks.count(check):
            count += count_i * ducks.count(check)
            matched.append(check)
    print('%d' % count)

main()
