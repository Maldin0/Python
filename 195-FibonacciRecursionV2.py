'''PSCP Program'''
def main(num):
    '''8361-FibonacciRecursionV2 22/10/2022
        - Bypassing maximum recursion depth. One if-condition at a time'''
    def fibbo(num, cache):
        '''find fibbonaci'''
        if num not in cache:
            cache[num] = fibbo(num-1, cache) + fibbo(num-2, cache)
        return cache[num]
    def add_up(i, re1, re2):
        '''Add up'''
        temp1 = fibbo(re1, bypass_dict[i-1])
        temp2 = fibbo(re2, bypass_dict[i-1])
        bypass_dict.append({re1: temp1, re2: temp2})
        i += 1
    bypass_dict = [{0: 0, 1: 1}]
    times = -((num-2)//-996)
    i = 1
    if times <= 1:
        print(fibbo(num, {0: 0, 1: 1}))
    else:
        if times >= 2:
            add_up(i, 997, 998)
            i += 1
        if times >= 3:
            add_up(i, 1993, 1994)
            i += 1
        if times >= 4:
            add_up(i, 2989, 2990)
            i += 1
        if times >= 5:
            add_up(i, 3985, 3986)
            i += 1
        if times >= 6:
            add_up(i, 4981, 4982)
            i += 1
        if times >= 7:
            add_up(i, 5977, 5978)
            i += 1
        if times >= 8:
            add_up(i, 6973, 6974)
            i += 1
        if times >= 9:
            add_up(i, 7969, 7970)
            i += 1
        if times >= 10:
            add_up(i, 8965, 8966)
            i += 1
        if times >= 11:
            add_up(i, 9961, 9962)
            i += 1
        print(fibbo(num, bypass_dict[-1]))

main(int(input()))
