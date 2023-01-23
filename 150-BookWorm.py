'''PSCP Program'''
def main():
    '''Book Worm'''
    for _ in range(int(input())):
        time = float(input())
        books = int(input())
        each_books = []
        read = 0
        for _ in range(books):
            each_books.append(float(input()))
        for i in sorted(each_books):
            time -= i
            if time >= 0:
                read += 1
            else:
                break
        print(read)
main()
