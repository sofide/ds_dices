black_dice = [0, 1, 1, 1, 2, 2]
blue_dice = [1, 1, 2, 2, 2, 3]
orange_dice = [1, 2, 2, 3, 3, 4]


def convert_string_to_dict_dices(string_input):
    dices_str_list = string_input.split()

    if not dices_str_list:
        raise ValueError()

    try:
        dices_int_list = [int(n) for n in dices_str_list]
    except ValueError as err:
        raise err

    if len(dices_int_list) < 3:
        for n in range(3-len(dices_int_list)):
            dices_int_list.append(0)

    dices_dict = {
        'black': dices_int_list[0],
        'blue': dices_int_list[1],
        'orange': dices_int_list[2]}

    return dices_dict


def input_dices():
    print('Insert your dices set with the next format:')
    print('First number: black dices')
    print('Second number: blue dices')
    print('Third number: orange dices')
    print('Each number has to be separeted by an espace')
    print('You can ommit second and/or third number')

    while True:
        input_dices = input('Your dices set: ')

        try:
            print('trying')
            dices_dict = convert_string_to_dict_dices(input_dices)
            # desde acaaa print
            break
        except ValueError:
            print('INVALID INPUT')
            print('Please enter a correct input')
            print('For example "1 2" for one black and two blue dices')

    print('Excelent! Your set dice is:')
    for k, v in dices_dict.items():
        print(k, ': ', v)


input_dices()
