# def is_number_or_letter(some_string):
#     numbers = [int(number) for number in some_string if number.isnumeric()]
#     letters = [letter for letter in some_string if not letter.isnumeric()]
#     return numbers, letters
#
# def take_skip(some_numbers):
#     take = [some_numbers[number] for number in range(len(some_numbers)) if number % 2 == 0]
#     skip = [some_numbers[number] for number in range(len(some_numbers)) if number % 2 != 0]
#     return take, skip
#
# def take_skip_string(some_letters, take, skip):
#     some_letters = "".join(some_letters)
#     take_string = []
#     skip_string = []
#     skip_index = 0
#     counter = 0
#     while counter < len(some_letters):
#         inner_counter = 0
#         for take_element in range(skip_index, len(take)):
#             if some_letters[:take[take_element]] != "":
#                 take_string.append(some_letters[:take[take_element]])
#             counter += take[take_element]
#             inner_counter = take[take_element]
#             some_letters = some_letters[inner_counter:]
#             for skip_element in range(skip_index, len(skip)):
#                 inner_counter = 0
#                 test = skip[skip_element]
#                 if some_letters[:skip[skip_element]] != "":
#                     skip_string.append(some_letters[:skip[skip_element]])
#                 counter += skip[skip_element]
#                 inner_counter = skip[skip_element]
#                 some_letters = some_letters[inner_counter:]
#                 skip_index += 1
#                 break
#     return take_string
#
#
# input_string = [*input()]
# numbers_list, letters_list = is_number_or_letter(input_string)
# take_list, skip_list = take_skip(numbers_list)
# print("".join(take_skip_string(letters_list, take_list,skip_list)))


def is_number_or_letter(some_string):
    numbers = [int(number) for number in some_string if number.isnumeric()]
    letters = [letter for letter in some_string if not letter.isnumeric()]
    return numbers, letters

def list_decoder(some_letters, some_numbers):
    some_letters = "".join(some_letters)
    take_string = []
    for element_index in range(len(some_numbers)):
        if element_index % 2 == 0:
            if some_letters[:some_numbers[element_index]] != "":
                take_string.append(some_letters[:some_numbers[element_index]])
            some_letters = some_letters[some_numbers[element_index]:]
        else:
            some_letters = some_letters[some_numbers[element_index]:]
    return "".join(take_string)

input_string = [*input()]
numbers_list, letters_list = is_number_or_letter(input_string)
print(list_decoder(letters_list, numbers_list))
