'''IDK im average android enjoyers'''


def main():
    '''iPhone 13 Again'''
    phone = ('iPhone 13 mini', 'iPhone 13',
             'iPhone 13 Pro', 'iPhone 13 Pro Max')
    storage = ('128 GB', '256 GB', '512 GB', '1 TB')
    pricing = (('25900', '29900', '37900'), ('29900', '33900', '41900'),
               ('38900', '42900', '50900', '58900'), ('42900', '46900', '54900', '62900'))
    try:
        model, stor = input(), input()
        print(pricing[phone.index(model.rstrip())][storage.index(stor)])
    except (ValueError, IndexError) as _:
        print('Not Available')


main()
