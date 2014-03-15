'''
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order.
'''

s = 'azcbobobegghakl'
copy = s

strings = []
while copy != '':
    word = ''
    for char in copy:
        word += char
        strings.append(word)
    copy = copy[1:]

unique = list(set(strings))
words = {}
for word in unique:
    words.update({word: len(word)})

for key in words.keys():
    if key != ''.join(sorted(key)):
        del words[key]
longest_alphabetical_substrings = []
for key, value in words.items():
    if words[key] == max(words.values()):
        longest_alphabetical_substrings.append(key)
        
final_dict = {}

for x in longest_alphabetical_substrings:
    final_dict.update({x: s.index(x)})

for key, value in final_dict.items():
    if final_dict[key] == min(final_dict.values()):
        print 'Longest substring in alphabetical order is: ' + key    
