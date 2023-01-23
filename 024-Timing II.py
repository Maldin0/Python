'''hello'''
def main():
    '''hi'''
    seconds = int(input())
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24
    if days < 10000:
        result = "%04d:%02d:%02d:%02d" %(days, hours, minutes, seconds)
    else:
        result = "ERR_:__:__:__"
    print(result)
main()
