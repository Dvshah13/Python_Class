# #uppercase a string
# my_string = "deepak v shah"
# print my_string.upper()
#
# #capitalize a string
# my_string = "this is my string to be used in the problem"
# my_string = my_string[:1].upper() + my_string[1:]
# print my_string

# #reverse a string
# my_string = "good afternoon everyone"
# print my_string[::-1]

#Caesar cipher
# L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
# I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#
# key = 13
# plaintext = "lbh zhfg hayrnea jung lbh unir yrnearq"
#
# ciphertext = ""
# for c in plaintext.upper():
#     if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
#     else: ciphertext += c
#
# print ciphertext


#Leetspeak
# paragraph = "leet".upper()
# leetmsg = paragraph
# leetwords = "AEGIOST"
# for letter in paragraph:
#     if letter in leetwords:
#         leetmsg = leetmsg.replace('A', str(4))
#         leetmsg = leetmsg.replace('E', str(3))
#         leetmsg = leetmsg.replace('G', str(6))
#         leetmsg = leetmsg.replace('I', str(1))
#         leetmsg = leetmsg.replace('O', str(0))
#         leetmsg = leetmsg.replace('S', str(5))
#         leetmsg = leetmsg.replace('T', str(7))
# print leetmsg

#Long-long vowels
# word = "Spoon"
# long_word = word
# vowel = "aa","ee","ii","oo","uu"
# for letters in word:
#     if letters in vowel:
#         long_word = long_word.replace("aa", "aaaaa")
#         long_word = long_word.replace("ee", "eeeee")
#         long_word = long_word.replace("ii", "iiiii")
#         long_word = long_word.replace("oo", "ooooo")
#         long_word = long_word.replace("uu", "uuuuu")
# print long_word
