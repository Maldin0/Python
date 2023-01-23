'''PSCP Program'''
def main():
    '''8386-Scout 05/11/2022'''
    for _ in range(int(input())):
        params, eggs = [int(i) for i in input().split()], sorted([int(i) for i in input().split()])
        egg_mass, count = 0, 0
        for i in eggs:
            egg_mass += i
            if egg_mass <= params[2] and count + 1 <= params[1]:
                count += 1
            else:
                break
        print(count)
main()
