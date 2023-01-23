'''FizzBuzz'''
def fizzbuzz(num):
    '''Is it Fizz or Buzz or Both'''
    for i in range(1, num+1):
        if i%3 == 0 and i%5 == 0:
            text = "FizzBuzz"
        elif i%3 == 0:
            text = "Fizz"
        elif i%5 == 0:
            text = "Buzz"
        else:
            text = i
        print(text)
fizzbuzz(int(input()))
