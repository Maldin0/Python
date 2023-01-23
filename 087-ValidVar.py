'''Valid'''
def valid(num):
    '''Valid'''
    rserv = "if", "else", "elif", "while", "for", "True", "False", "continue", "break", \
        "return", "is", "in", "and", "or", "from", "as", "pass", "not", "def", "None"
    for _ in range(num):
        text = input()
        if not(text in rserv) and text.isidentifier() or text[0] == " " or text[-1] == " ":
            val = "Valid"
        else:
            val = "Invalid"
        print(val)
valid(int(input()))
