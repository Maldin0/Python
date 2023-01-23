'''PSCP Program'''
def main():
    '''BusStop I'''
    bus, stop_loc, count, capacity = [], [], 0, int(input())
    for _ in range(int(input())):
        data = [int(i) for i in input().split()]
        stop_loc.append([data[0], data[1:]])
    for i in sorted(stop_loc, key=lambda x: x[0]):
        count += bus.count(i[0])
        bus = [loc for loc in bus if loc != i[0]]
        for j in i[1]:
            if len(bus) >= capacity:
                break
            if j > i[0]:
                bus.append(j)
    print(count)
main()
