#Declare your age as integer variable
Age=37
#Declare your height as a float variable
Height=180.5
#Declare a variable that store a complex number
complexNumber=1+1j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

print('Welcome to basic geometry!')
baseTriangle=input('What is the value for base of your triangle: ')
heightTriangle=input('What is the value for height of your triangle: ')
areaTriangle=0.5*int(baseTriangle)*int(heightTriangle)
print('Your triangle area is: ',areaTriangle)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle 

print('Welcome to basic geometry 2!')
sideA=int(input('What is the value for side A: '))
sideB=int(input('What is the value for side B: '))
sideC=int(input('What is the value for side C: '))
print('Your triangle perimeter is: ',sideA+sideB+sideC)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print('Welcome to basic geometry 3!')
Lenght=int(input('What is the lenght: '))
Width=int(input('What is the width: '))
print('Your perimeter is: ',2*(Lenght+Width), ' and you area is ', Lenght*Width )

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
print('Welcome to basic geometry 4!')
radius=int(input('What is radius of your circle: '))
pi=3.14
print('Your circle area is: ',pi*radius**2, ' and you circle circumference is ', 2*pi*radius )

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

m=2
b=-2
xIntercept=(b/m,0)
yIntercept=(0,b)

print('Slope is ',m, 'Intercept X ', xIntercept, 'Intercept Y',yIntercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

y1=2
y2=2
x1=6
x2=10
m2 = y2-y1/x2-x1
print('Slope is ',m2)

#Compare the slopes

print(m==m2)


#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x=-3
y=x**2 + 6*x + 9
print(y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement

python=len('python')
dragon=len('dragon')

print('Python lenght is ', python, 'and dragon lenght is ',dragon)
print (not(python==dragon))

#Use and operator to check if 'on' is found in both 'python' and 'dragon

print('on' in 'dragon' and 'on' in 'python')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence='I hope this course is not full of jargon'
word='jargon'
print(word in sentence)

#There is no 'on' in both dragon and python

word='on'
dragon='dragon'
python='python'

print(word not in (dragon) and word not in python)


#Find the length of the text python and convert the value to float and convert it to string

lenght=len('python')
lenght=float(lenght)
print(type(lenght))
lenght=str(lenght)
print(type(lenght))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python

number=int(input('What is your number: '))
modulus=number%2
conditionEven=modulus!=0
print('Is your number even? Answer: ', not(conditionEven))

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

a=7
b=3
c=int(2.7)
floor=7//3
print(c==floor)

#Check if type of '10' is equal to type of 10

d='10'
e=10
print(type(d)==type(e))

#Check if int('9.8') is equal to 10

print(int(9.8)==10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours=float(input('How many hours was the project? '))
rate=float(input('What is your rate? '))
print('Your weekly earnings are: ', hours*rate)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. 

years=int(input('Input the number of years: '))
print('You lived ', years*365*24*3600, ' seconds')

#Write a Python script that displays the following table

from tabulate import tabulate

table=tabulate([[1,2,3,4,5],[1,1,1,1,1],[1,2,3,4,5],[1,4,9,16,25],[1,8,27,64,125]])

print(table)


