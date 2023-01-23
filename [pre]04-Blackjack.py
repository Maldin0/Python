"""I don't wanna play cards anymore"""
def checkpoint(card):#check แต้มการ์ด
    """Check value of cards"""
    global point
    if card.isnumeric() == True:#ถ้าเป็นตัวเลขเอาแต้มบวกเลย
        point += int(card)
    elif card == "J" or card == "Q" or card == "K":#ถ้าเป็น J Q K แต้มบวก 10
        point += 10
    elif card == "A":#ถ้าเป็น A ให้เช็คเงื่อนไขต่อ
        if point + 11 > 21:#ถ้า A เป็น 11 แล้วแต้มเกิน 21 ให้ A เป็น 1
            point += 1
        elif point + 11 <= 21:#ถ้า A เป็น 11 แล้วแต้ม <= 21 ให้ A เป็น 11
            point += 11
    return point
def main():
    """Main"""
    global point
    numcard = int(input())#input จำนวน cards
    point = 0
    if numcard == 2:#ถ้ามีcards 2 ใบ input 2 ใบ
        card1 = input().upper()
        card2 = input().upper()
        checkpoint(card1)#เช็คแต้ม ใบแรก
        checkpoint(card2)#เช็คแต้มใบสอง
    elif numcard == 3:#ถ้ามีcards 3 ใบ input 3 ใบ
        card1 = input().upper()
        card2 = input().upper()
        card3 = input().upper()
        checkpoint(card1)#เช็คแต้มใบแรก
        checkpoint(card2)#เช็คแต้มใบสอง
        checkpoint(card3)#เช็คแต้มใบสอง
    print(point)
main()