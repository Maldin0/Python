'''PSCP Program'''
def main(books, regs):
    '''8414-Discount 05/11/2022'''
    while regs != 'ENTER':
        books.append(int(regs))
        regs = input()
    print(sum(sorted(books)[int((len(books))//6) if len(books) == 5
                            else int(len(books)//5) if int(len(books)//5) != 3 else 2:]))
main([], input())
