"""[Pre] Blackjack"""
def main(numcard):
    """main"""
    num = []
    ace = 0
    ans = []
    for _ in range(numcard):
        num = input().upper()
        if num == "A":
            ace += 1
        if ace == 1:
            num = 11
            ace += 1
        elif num == "A" and ace > 1:
            num = 1
        if num == "J" or num == "Q" or num == "K":
            num = 10
        else:
            num = int(num)
        ans += [num]
    if ace > 1 and sum(ans) > 21:
        print(sum(ans)-10)
    else:
        print(sum(ans))
main(int(input()))
