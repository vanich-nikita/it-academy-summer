'''Exes and Ohs.
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

s = input("Input string:")
s = s.lower()
o, x = 0, 0
flag = False
for i in s:
    if i == 'o':
        o += 1
    if i == 'x':
        x += 1
    if o == x and x:
        flag = True
print(flag)


'''Isograms.
An isogram is a word that has no repeating letters, consecutive or
non-consecutive.
Implement a function that determines whether a string
that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''

string = input("Input string: ")
flag = True
string = string.lower()
for i in string:
    if string.count(i) > 1:
        flag = False
        break
print(flag)

'''Mumbling.
This time no story, no theory. The examples below show you
how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes
only letters from a..z and A..Z.
'''
string = input("Input string: ")
new_string = ''
n = 1
for i in string:
    new_string += i.upper()
    if n > 1:
        new_string += i.lower() * (n - 1)
    n += 1
    if n <= len(string):
        new_string += '-'
print(new_string)

'''Sum of positive.
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
'''
arr = [-1, 4, 5, -6]
sum = 0
for i in arr:
    if i > 0:
        sum += i
print(sum)

'''Square every digit.
Welcome. In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out,
because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer'''

num = 1234
num1 = str(num)
result_string = ''
for i in num1:
    n = int(i)
    res = n**2
    result_string += str(res)
print(result_string)
