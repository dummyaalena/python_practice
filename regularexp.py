import re
from collections import Counter

file = open('test.txt')
for line in file:
    words = len(re.findall(r'\w+', line)) #counting words
    dots = len(re.findall(r'\.', line)) #counting new lines
    new_line = len(re.findall(r'\n', line)) #counting new lines
    alphabet = len(re.findall(r'[a-zA-Z]',line)) #counting letters
    digits = len(re.findall(r'[0-9]',line)) #counting digits
    counter = Counter(line)
print(words)
print(new_line)
print(alphabet)
print(digits)
print(dots)
# print(counter)