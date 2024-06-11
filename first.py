#WAP relation between three numbers:
a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
c = int(input("Enter a third number : "))
if a == b and b == c and c == a:
    print('a,b,c are equal')
elif a == b or b == c or c == a:
    print('two numbers are equal')
elif a < b and a < c:
    print('a is the smallest')
elif b < a and b < c:
    print('b is the smallest')
else:
    print('c is the smallest')


#WAP to change the casing from upper → lower and lower → upper:
alpha = 'P'
if 'A'<= alpha <= 'Z': 
 print(chr(ord(alpha)+32))
 
elif  'a' <= alpha <= 'z':
  print(chr(ord(alpha)-32))
else:
  print('invalid input')


#WAP to print the grade percentage — if one sub fail all fail
c_language = 90
oops = 50
python = 70
SQl = 0
java_script = 80
HTMl = 80
sum = c_language+oops+python +SQl+ java_script + HTMl
per = sum /6
print(per)
if c_language >= 35 and oops >= 35 and python >= 35 and SQl >= 35 and java_script >= 35 and HTMl >= 35:
    if per >= 35 and per <= 49:
        print('just pass')
    elif per >= 50 and per <= 60:
        print('average')
    elif per >= 60 and per <= 70:
        print('good')
    elif per >= 70 and per <= 80:
        print('very good')
    elif per >= 80 and per <= 90:
        print('outstanding')
    elif per >=90 and per <= 100:
        print('ultra lengend')
else:
    print('you are fail')
61.6666
#o/p: you are fail