#Declare a first name variable and assign a value to it
first_name='John'
#Declare a last name variable and assign a value to it
last_name='Smith'
#Declare a full name variable and assign a value to it
full_name=first_name+ ' ' +last_name
#Declare a country variable and assign a value to it
country='Italy'
#Declare a city variable and assign a value to it
city='Spezia'
#Declare an age variable and assign a value to it
age=33
#Declare a year variable and assign a value to it
year=1988
#Declare a variable is_married and assign a value to it
is_married=False
#Declare a variable is_true and assign a value to it
is_true=True
#Declare a variable is_light_on and assign a value to it
is_light=False
#Declare multiple variable on one line
car,color,manufacturer=True,'red','Fiat'

print(full_name,country,city,age,year,is_light,is_married,car,color,manufacturer)



#Check the data type of all your variables using type() built-in function
print(type(car))
print(type(color))
print(type(year))
print(type(full_name))
#Using the len() built-in function, find the length of your first name
print(len(first_name))
#Compare the length of your first name and your last name
print(len(first_name)==len(last_name))
#Declare 5 as num_one and 4 as num_two
num_one=5
num_two=4
#Add num_one and num_two and assign the value to a variable total
total=num_one+num_two
print(total)
#Subtract num_two from num_one and assign the value to a variable diff
diff=num_two-num_one
print(diff)
#Multiply num_two and num_one and assign the value to a variable product
product=num_two*num_one
print(product)
#Divide num_one by num_two and assign the value to a variable division
division=num_one/num_two
print(division)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder=num_two%num_one
print(remainder)
#Calculate num_one to the power of num_two and assign the value to a variable ex
ex=num_one**num_two
print(ex)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division=num_one//num_two
print(floor_division)
#The radius of a circle is 30 meters.
radius=30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
pi=3.14
area_of_circle=pi*(radius**2)
print (area_of_circle)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle=2*pi*radius
print(circum_of_circle)
#Take radius as user input and calculate the area.
user_radius=input('What is circle radius?')
area_of_user_circle=pi*(int(user_radius)**2)
print(area_of_user_circle)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_first_name=input('First Name:')
user_last_name=input('Last Name:')
user_country=input('Country:')
user_age=input('Age:')
user_details=user_first_name,user_last_name,user_country,user_age
print(user_details)
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords') 