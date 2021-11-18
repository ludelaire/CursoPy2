def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Lu', 'lastname': 'DelAire'}

    super_list = [
        {'firstname': 'Ninna', 'lastname': 'Hori'},
        {'firstname': 'Tsukiko', 'lastname': 'Omachi'},
        {'firstname': 'Marie', 'lastname': 'Arakawa'},
        {'firstname': 'Freddy', 'lastname': 'Vega'},
        {'firstname': 'Facundo', 'lastname': 'García'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-9, 0, 7, 72, -12],
        'floating_nums': [1.81, 4.5, 3.14]
    }

    for key, value in super_dict.items():
        print(key, ' - ', value)
    
    print(' ')

    for value in super_list:
        print(value)

if __name__ == '__main__':
    main()