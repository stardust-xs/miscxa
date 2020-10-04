# import random
# from typing import List


# def alpha_list(letters: int,
#                start: int,
#                stop: int,
#                randomize: bool = True) -> List[str]:
#   """
#   Return list of evenly* distributed characters with mixed cases.

#   Args:
#     letters: Maximum number of characters required in the list.
#     start: Starting ordinal range.
#     stop: Stopping ordinal range.
#     randomize: Boolean to return random sequence.

#   Returns:
#     List of characters split in upper and lower cases.
#   """
#   chars = []

#   for idx in range(letters):
#     temp = (chr(random.randint(start, stop)))
#     chars.append(temp.upper() if idx % 2 else temp)

#   if randomize:
#     random.shuffle(chars)

#   return chars


# number = int(input("Please enter even amount of characters you want: "))
# first = ord(input("Please type the first character of the limits in lowercase "
#                   "[ex: a]: "))
# last = ord(input("Please type the last character of the limits in lowercase "
#                  "[ex: z]: "))

# print(alpha_list(number, first, last))


# dt = {'Congress': {'April': '5.902',
#                    'August': '5.925',
#                    'January': '5.881',
#                    'February': '5.888',
#                    'July': '5.920',
#                    'June': '5.910',
#                    'March': '5.896',
#                    'May': '5.906',
#                    'November': '5.942',
#                    'October': '5.938',
#                    'September': '5.933'},
#       'Entity': {'April': '64.320',
#                  'August': '64.642',
#                  'December': '64.825',
#                  'January': '63.965',
#                  'February': '64.089',
#                  'June': '64.509',
#                  'March': '64.221',
#                  'May': '64.404',
#                  'October': '64.757',
#                  'September': '64.690'}
#                  }

#       # months = {"January", "February", "March", "April", "May", "June", "July",
#       #           "August", "September", "October", "November", "December"}
#       # temp = set(dt.keys())
#       # s = (months - temp)

#       # for idx in s:
# #   dt[idx] = "NaN"

# # print(dt)

# months = {"January", "February", "March", "April", "May", "June", "July",
#           "August", "September", "October", "November", "December"}


# def fill_months(dictionary: dict, replace: str = "NaN") -> dict:
#   """
#   Fill missing months with some replacement string (default: NaN).
  
#   Args:
#     dictionary: Dictionary which has the missing months.
#     replace: Values to be added for the missing months.

#   Returns:
#     Dictionary with missing month and some string value.  
#   """
#   for idx in (months - set(dictionary.keys())):
#     dictionary[idx] = replace
#   return dictionary


# # print(fill_months(dt["Congress"]))

# from datetime import datetime

# start_date = "2015 June 12 16:00 GMT"
# # date = datetime.strptime(start_date[:-10], '%Y %B %d')
# # a = date.strftime('%Y-%d-%m')
# # print(a)

# from dateutil import parser

# print(parser.parse(start_date).strftime("%Y-%d-%m"))


# words = ["the", "cat", "dog", "fish", "runs"]
# sentences = ["the dog and cat are friends",
#              "the dog runs all the time",
#              "the dog eats fish",
#              "I love to eat fish",
#              "Granola is yummy too"]
# output = ["",
#           "the dog and cat are friends",
#           "the dog eats fish",
#           "I love to eat fish",
#           "the dog runs all the time"]
# # omitted = ["Granola is yummy too"]


# dataset = {}
# copy = []
# freq = 0

# for word in words:
#   for sentence in sentences:
#     if word in sentence and sentence not in dataset.values():
#       dataset[word] = sentence

#     freq = 0

# print(dataset)

# {'the': 'the dog eats fish',
#  'cat': 'the dog and cat are friends',
#  'dog': 'the dog runs all the time',
#  'fish': 'I love to eat fish'}
# x = 'the dog runs all the time'
# print(x.count('the'))

# import datetime as dt

# toadd = dt.timedelta(minutes=10)
# starttime = dt.datetime.now()
# endtime = starttime + toadd




# from datetime import datetime, timedelta

# start_time = datetime.now().replace(microsecond=0)
# end_time = start_time + timedelta(minutes=10)

# print(f"Start time is {start_time} and End time is {end_time}")


# items = {
#     'flour': [20, 10, 15, 8, 32, 15],
#     'beef': [3, 4, 2, 8, 2, 4],
#     'bread': [2, 3, 3],
#     'cc': [0.3, 0.5, 0.8, 0.3, 1]
# }

# print([idx[2] for idx in items.values() if len(idx) >= 3])
