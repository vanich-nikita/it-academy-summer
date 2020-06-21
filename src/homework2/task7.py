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
o = s.count('o')
x = s.count('x')
if o == x:
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
string1 = string
my_set = set(string1)
if len(string) != len(my_set):
    flag = False

"""for i in string:
    if string.count(i) > 1:
        flag = False
        break
"""

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


'''
Given a triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
Note: your code should be optimized to handle big inputs.
'''

n = int(input("Enter n: "))
list = []
for i in range(n * (n - 1) + 1, n * (n + 1), 2):
    list.append(i)

print(list)


'''
Given a list lst and a number N, create a new list that contains each number
of lst at most N times without reordering. For example if N = 2, and
the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2]
since this would lead to 1 and 2 being in the result 3 times,
and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
'''

initial_list = [20, 37, 20, 21]
secondary_list = []

max_e = 1
for i in initial_list:
    if secondary_list.count(i) <= max_e - 1:
        secondary_list.append(i)
    else:
        continue
print(secondary_list)

'''
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]

n_floor=int(input("Enter number of floors: "))
result = []
width = (n_floor * 2) - 1
for x in range(1, 2 * n_floor, 2):
    stars = x * '*'
    line = stars.center(width)
    result.append(line)

print(result)
'''

n_floor = int(input("Enter number of floors: "))
result = []

for i in range(1, n_floor + 1):
    stars = '*' * (2 * i - 1)
    space = ' ' * (n_floor - i)
    result.append(space + stars + space)
print(result)

'''
Complete the solution so that the function will break up camel casing,
using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
'''

string = input("Input string: ")
new_string = ""
for i in string:
    if i.islower():
        new_string += i
    else:
        new_string += " " + i
print(new_string)

'''
The goal of this exercise is to convert a string to a new string where
each character in the new string is "(" if that character appears only
once in the original string, or ")" if that character appears more than
once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes

Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result,
not the input!
'''

string = input("Input string: ")
final_string = ""
string = string.lower()
for i in string:
    if string.count(i) >= 2:
        final_string += ')'
    else:
        final_string += '('
print(final_string)

'''
For building the encrypted string:
Take every 2nd char from the string, then the other chars,
that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
'''

encrypted_text = input("Input string: ")
n = int(input("Enter number: "))
final_string = ""
counter1, counter2 = 1, 1

if encrypted_text == "" or encrypted_text == "None":
    print(encrypted_text)
elif n <= 0:
    print(encrypted_text)
else:
    while n != 0:
        for i in encrypted_text:
            if not counter1 % 2:
                final_string += i
            counter1 += 1

        for i in encrypted_text:
            if counter2 % 2:
                final_string += i
            counter2 += 1

        counter1, counter2 = 1, 1

        if n != 1:
            encrypted_text = final_string
            final_string = ""

        n -= 1

    print(final_string)


text = input("Input string: ")
n = int(input("Enter number: "))
final_string = ""

if text == "" or text == "None":
    print(text)
elif n <= 0:
    print(text)
else:
    while n != 0:
        first_half = text[:int(len(text) / 2)]
        second_half = text[int(len(text) / 2):]
        counter3 = 0

        while counter3 < len(second_half):
            final_string += second_half[counter3]
            if counter3 < len(first_half):
                final_string += first_half[counter3]
            counter3 += 1

        if n != 1:
            text = final_string
            final_string = ""

        n -= 1

    print(final_string)
