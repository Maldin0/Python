'''PSCP Program'''


def main():
    '''Muddled Menu'''
    menu_store = []
    while True:
        menu_txt = input()
        numbers = menu_txt.find(' #')+1
        if menu_txt == 'DONE':
            break
        if menu_txt == 'CLOSED':
            menu_store.clear()
            break
        if menu_txt == "SOMETHING'S WRONG":
            menu_store.clear()
            continue
        if menu_txt.find("Can't do: ", 0, 10) != -1 and len(menu_txt) > 10:
            # print(menu_txt[10:])
            if menu_txt[10:] in menu_store:
                menu_store.remove(menu_txt[10:])
            continue
        if menu_txt[numbers+1:] == 'N':
            menu_store.append(menu_txt[:numbers-1])
        elif menu_txt[numbers+1:].isnumeric() and len(menu_txt) > 3:
            menu_store.insert(
                int(menu_txt[numbers+1:])-1, menu_txt[:numbers-1])
    print('Full Course:', menu_store, 'Reversed:', list(reversed(menu_store)))


main()
