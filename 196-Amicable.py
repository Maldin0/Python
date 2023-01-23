'''PSCP Program'''
def main(num):
    '''8362-Amicable 23/10/2022'''
    total = {}
    caching = {}
    def sum_of_divisors(num):
        '''Cacheable function -- with optimised algorithm'''
        temp = 1
        for k in range(2, int(num**0.5)+1):
            if num % k == 0:
                temp += k + num // k
        return temp
    if num > 75000:
        for i in range(220, num):
            temp_a = sum_of_divisors(i)
            if i == sum_of_divisors(temp_a) and i != temp_a and i not in total:
                total[i] = 1
                total[temp_a] = 1
    else:
        for i in range(220, num):
            if i not in caching:
                caching[i] = sum_of_divisors(i)
                temp_a = caching[i]

            if caching[i] not in caching:
                caching[temp_a] = sum_of_divisors(temp_a)

            if i == caching[temp_a] and i != temp_a and i not in total:
                total[i] = 1
                total[temp_a] = 1
    print(sum(total))
main(int(input()))
