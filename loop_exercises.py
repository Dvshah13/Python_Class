# #1 to 10
# for number in range(1,11):
#     print number

#n to m
# start = int(raw_input("Pick a number to start from "))
# finish = int(raw_input("Pick a number to end on "))
# print "Start from: %d" % start
# print "End on: %d" % finish
# for number in range(start,finish+1):
#     print number

#odd numbers
# for number in range(1,11):
#     if number % 2 > 0:
#         print number

#print a square
# size = 5
# for i in range(size):
#     print ('*' * size)

#print a squareII
# size = int(raw_input("How big is your square? "))
# for i in range(size):
#     print ('*' * size)

#print a box
# height = int(raw_input("Give me a height: "))
# width = int(raw_input("Give me a width: "))
# for i in range(height):
#     if i in[0]:
#         print("*" * width)
#     elif i in[height-1]:
#         print("*" * width)
#     else:
#         print("*"+ " "* (width-2) + "*")
# input()

#print a triangle
# def pyramid(rows):
#     for i in range(rows):
#         print ' '*(rows-i-1) + '*'*(2*i+1)
# pyramid(4)

#print a triangle II
# rows = int(raw_input("How many rows would you like to print?: "))
# def pyramid(rows):
#      for i in range(rows):
#          print ' '*(rows-i-1) + '*'*(2*i+1)
# pyramid(rows)

#multiplication table
# for i in range(1,11):
#     for j in range(1,11):
#         print i," x ",j," = ",j*i
