import random


def alpha_list(num_values, alpha_low, alpha_high):

    final_list = []

    for letter in range(num_values):
        rando = (chr(random.randint(alpha_low, alpha_high)))
        final_list.append(rando)

    for i in range(len(final_list)):
        if final_list[i] > final_list[int((len(final_list)/2)-1)]:
            final_list[i] = final_list[i].upper()
        else:
            pass

    return final_list


user_input_number = eval(
    input('please type an EVEN amount of letters you want: '))

user_input_first_letter = ord(
    input('please type the first letter of the limits(lower case): '))

user_input_last_letter = ord(
    input('please type the last letter of the limits(lower case): '))

print(alpha_list(user_input_number, user_input_first_letter, user_input_last_letter))
