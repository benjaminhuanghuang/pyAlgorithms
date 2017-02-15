# http://icejoywoo.github.io/2015/09/12/python-regex.html#greedylazypossessive
import re


test_string = ('A regular expression is a pattern which specifies a set of strings of characters; '
               'it is said to match certain strings.')

print re.findall(r'regular', test_string)  # ['regular']
# metachar
print re.findall(r'strings\.', test_string)  # ['strings.']

test_string = '''! " # $ % & ' ( ) * + , - . /
0 1 2 3 4 5 6 7 8 9
: ; < = > ? @
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
[ \ ] ^ _ `
a b c d e f g h i j k l m n o p q r s t u v w x y z
{ | } ~
'''

print re.findall(r'[0-9]', test_string)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print re.findall(r'\d', test_string)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print re.findall(r'[0-3]', test_string)  # ['0', '1', '2', '3']

#
# ---  Boundaries
#
test_string = 're great'

print re.findall(r're', test_string)  # ['re', 're']
# \b the border of word
print re.findall(r'\bre\b', test_string)  # ['re']
# \B Non-word boundary
print re.findall(r'\Bre\B', test_string)  # ['re']



#
# ---  Greedy, Lazy and Possessive）
#

print re.match(r'\d{3}', '123456').group()  # 123
print re.match(r'\d{3,6}', '123456').group()  # 123456
print re.match(r'\d{3,6}678', '12345678').group()  # 12345678

# Lazy, as less as possible
print re.match(r'\d{3,6}?', '123456').group()  # 123
print re.match(r'\d{3,6}?678', '12345678').group()  # 12345678

# 占用量词，python不支持，可以在regex101使用pcre(php)来测试
# print re.match(r'\d{3,6}+678', '12345678')  # None
# 无法匹配成功，因为\d{3,6}+会直接匹配123456，后面只剩下78，并且不回溯，无法匹配剩下的678

