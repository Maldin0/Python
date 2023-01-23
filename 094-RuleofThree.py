'''Huhuhahhahuhdue'''
def main(num):
    '''Huhahuhehuehahha'''
    ngpc = 0
    ncost = 0
    ngrams = 0
    # cost = []
    # grams = []
    # gramspercost = []
    # for _ in range(num):
    #     cost.append(float(input()))
    #     grams.append(float(input()))
    # for i in range(num):
    #     gramspercost.append(grams[i]/cost[i])
    # worthiestcost = cost[gramspercost.index(max(gramspercost))]
    # worthiestgrams = grams[gramspercost.index(max(gramspercost))]
    for _ in range(num):
        cost = float(input())
        grams = float(input())
        gramspercost = grams/cost
        if ngpc < gramspercost:
            ngpc = gramspercost
            ncost = cost
            ngrams = grams
        elif ngpc == gramspercost and ncost > cost:
            ncost = cost
            ngrams = grams
    print("%.02f %.02f" %(ncost, ngrams))
main(int(input()))
