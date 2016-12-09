# #exercise 1
#
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
#
# 1. print phonebook_dict['Elizabeth']
# 2. phonebook_dict['Kareem'] = '938-489-1234'
# 3. del phonebook_dict['Alice']
# 4. phonebook_dict['Bob'] = '968-345-2345'
# 5. print phonebook_dict.items()
#
# #exercise 2
# 1.
# 2.
# 3. ramit[0]['friends[0]']['email']
# 4. ramit[0]['friends[1]']['interests']

hello_file = open('programmers_blues.txt')
file_contents = hello_file.read()
print file_contents

def word_count(string):
  my_string = string.lower().split()
  my_dict = {}
  for item in my_string:
    my_dict[item] = my_string.count(item)
    print (my_dict)

word_count(file_contents)
