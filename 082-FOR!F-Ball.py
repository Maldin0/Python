'''Ur gf died of ligma'''
def ligma(shuffle):
    '''ligma balls'''
    shuffle = list(shuffle)
    balls = [1, 0, 0]
    for i in shuffle:
        if i == "A":
            balls[0], balls[1] = balls[1], balls[0]
        elif i == "B":
            balls[1], balls[2] = balls[2], balls[1]
        elif i == "C":
            balls[0], balls[2] = balls[2], balls[0]
    print(balls.index(1)+1)
ligma(input())
