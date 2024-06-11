#WAP to find the Armstrong number or not
n = int(input('enter the number')) 
res = 0 #27/ 152
a = n #153/ 15/ 1
while a > 0: #153 < 0/ 15<0/ 1>0
  i = a%10 #153%10 =3/ 15%10 = 5
  res = res+i**3 #0+3^3=27/ 27+5^3= 152/ 152+1 = 153
  a = a//10# 153//10 = 15/ 15//10 = 1/ 1//10= 0
if res == n:
  print('it is a amstrong number')
else:
  print('it is not a armstrong num')

#----------withour tracing-------

n = int(input('enter the number')) 
res = 0 
a = n 
while a > 0: 
  i = a%10 
  res = res+i**3 
  a = a//10
if res == n:
  print('it is a amstrong number')
else:
  print('it is not a armstrong num')


#WAP to toggle the vowel if lower change to upper if upper change to lower
a = 'AeIouBu'
str = ''
for i in a:
  if i in 'AEIOU':
    str = str+chr(ord(i)+32)
  elif i in 'aeiou':
    str = str+chr(ord(i)-32)
  else:
    str = str+i
print(str)
#o/p: aEiOUBU


#WAP to print the upper case letters and lower case letter in list separately
a = 'SumANtH'
low = []
upp = []
for i in a:
  if 'A'<=i<='Z':
   upp = upp +[i]
  elif 'a'<=i<='z':
    low = low+[i]
print(upp,low)
#o/p:['S', 'A', 'N', 'H'] ['u', 'm', 't']


#WAP to change the casing from upper to lower and lower to upper
a = 'SuManTH'
s = ''
for i in a:
  if 'A'<=i<='Z':
    z = chr(ord(i)+32)
    s = s+z
  elif 'a'<=i<='z':
    z = chr(ord(i)-32)
    s = s+z
  else:
    print('invalid character')
print(s)
#o/p: sUmANth


#WAP to print the number of odd numbers present in the list
a = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in a:
  if i%2!=0:
    count= count+1
print(count)