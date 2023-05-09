# Extracting Data With Regular Expressions


# The basic outline of this problem is to read the file, look for integers using the
# re.findall(), looking for a regular expression of '[0-9]+' and then converting the
# extracted strings to integers and summing up the integers.

import re

# file = open(r"D:\alex_\Documents\Programacion\Cursos\Python for Everybody\3 - Using Python to Access Web Data\regex_sum_876340.txt")
# total = 0
# for line in file:
#     x = re.findall("[0-9]+", line)
#     for n in x:
#         y = int(n)
#         total += y

# print(total)

# Otra forma de hacerlo:
fname = r"D:\alex_\Documents\Programacion\Cursos\Python for Everybody\3 - Using Python to Access Web Data\regex_sum_876340.txt"
print(sum([int(line) for line in (re.findall("[0-9]+", (open(fname).read())))]))
