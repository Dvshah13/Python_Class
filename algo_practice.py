# #Bubble Sort
# import random
# import time
#
# startTime = time.time()
#
# l = range(100)
#
# random.shuffle(l)
#
# for i in range(len(l)):
#         for j in range (len(l)-1):
#             if l[j] > l[i]:
#                 l[i],l[j] = l[j],l[i]
# print l
#
# elapsedTime = time.time() - startTime
# print elapsedTime

#Reverse a string
#
# rev_str = "Hello"[::-1]
# print rev_str.lower()
#
# #reverse words in a sentence
# rev_sen = "This is my sentence that I want to reverse"
# spl = rev_sen.split()
# nex = spl[::-1].join()
# print nex

#find largest element in unsorted array
# arr = [3,2,1,5,6,4]
# k = 2
# print arr
# kth_largest_ele = 0
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[i]:
#             arr[i],arr[j] = arr[j],arr[i]
#             kth_largest_ele = arr[-k]
# print kth_largest_ele

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid ...
#
# my_string = ['(', ')', '{', '}', '[', ']']
# my_string = False
# import random
# import string
# mycharacters = ['(', ')', '{', '}', '[', ']']
# right = False
# while right == False:
#     def valid():
#         new = ''.join(random.choice(mycharacters) for n in range(len(mycharacters)))
#         if new == "()[]{}":
#            print "That is valid"
#            right = True
#         else:
#            print "That is not valid"
#         print new
#
# valid()
# mychar = "]}{[(())"
# open_count = 0
# closed_count = 0
# total_count = 0
# # def counter():
#
# for char in mychar:
#     print char
#     if char == '(' or '{' or '[':
#         open_count += 1
#     elif char == ')' or '}' ']':
#         closed_count -= 1
#     total_count = open_count - closed_count
#     print total_count
# if total_count < 0:
#     print "Invalid"
# else:
#     print "Valid"

# mychar = '()()()('
# open_count = 0
# closed_count = 0
# total_count = 0
# done = True
# # def counter():
#
# for char in mychar:
#    print char
#    total_count = open_count + closed_count
#    if char == '(':
#        open_count += 1
#
#    elif char == ')':
#        closed_count -= 1
#
#    total_count = open_count + closed_count
#
#    while total_count < 0:
#        done = False
#        print "Invalid"
#        break
#    if done == True:
#        print "Valid"


# mychar = '))(()('
# open_count = 0
# closed_count = 0
# total_count = 0
# done = True
# # def counter():
#
# for char in mychar:
#    print char
#    total_count = open_count + closed_count
#    if char == '(':
#        open_count += 1
#
#    elif char == ')':
#        closed_count -= 1
#
#    total_count = open_count + closed_count
#
#    while total_count < 0:
#        done = False
#        break
#        if total_count == 0:
#            done = True
#        if total_count != 0:
#            done = False
#
# if done == True:
#     print "Valid"
# else:
#     print "Invalid"




# print total_count
# if total_count < 0:
#    print "Invalid"
# else:
#    print "Valid"






# 1. null or empty string
# 2. white spaces
# 3. +/- sign
# 4. calculate real value
# 5. handle min & max

# str1 = "50 + 60"
# print str1
#
# str2 = "A"
# str3 = "B"
#
# str4 = int(str2) + int(str3)
# print str4

#Damians Solution
# def checkPair(s,pair="()"):
#     unclosedPair = 0
#     for c in s:
#         #counting the opens
#         if c == pair[0]:
#             unclosedPair += 1
#         #close an unclosedPair
#         if c==pair[1]:
#             unclosedPair -= 1
#         if unclosedPair < 0:
#             #started with a closing char, exit
#             return False
#     print "I have %d unclosedPairs" % unclosedPair
#     return True
#
# def checkPairs(s):
#     return checkPair(s) and checkPair(s,"{}") and checkPair(s,"[]")
# print checkPair("{{})())(())[]][]]}")



def convert(s):
    s = s.split()
    for i in s:
        i = float(i)
        print i

convert(s)
