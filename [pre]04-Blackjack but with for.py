"""I don't wanna play cards anymore"""
def main():
    """Poker is good tbh"""
    numcard = int(input())
    point = 0
    ace = 0
    card = []
    for _ in range(numcard):
        card.append(input().upper())
    for j in card:
        if j.isnumeric() == True:
            point += int(j)
        elif j == "J" or j == "Q" or j == "K":
            point += 10
        elif j == "A":
            point += 11
            ace += 1
    for _ in range(ace):
        if point > 21 and ace > 0:
            point -= 10
            ace -= 1
    print(point)
main()
