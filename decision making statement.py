
'''1. Write a python program to check whether a number is even or odd.'''

print("\n1.check even and odd.")
n=int(input("enter no: "))

if n%2==0:

    print(n,"is even number.")
else:

    print(n,"is odd number.") 


'''2. Write a python program to check whether a number is positive, negative, or zero. '''

print("\n2.check number is positive,negative or zero.")
num=int(input("enter num: ")) 

if num > 0 :

    print(num,"is a positive number.")

elif num < 0:

    print(num,"is a negative number.")
else:

    print(num,"is a zero.")


'''3. Write a python program to find the largest of two numbers using if-else. '''

print("\n3.find the largest of two numbers using if-else.")

num1=int(input("enter 1st number: "))

num2=int(input("enter 2nd number: "))

print("user entered number are: ",num1,num2)

if num1 > num2:

    print(num1," is greater than a ",num2)
else:

    print(num2," is greater than a ",num1)


'''4. Write a python program to find the largest of three numbers. '''

print("\n4.find the largest of three number.")

n1=int(input("enter 1st number: "))

n2=int(input("enter 2nd number: "))

n3=int(input("enter 3rd numbrer: "))

print("user enter 3 numbers are: ",n1,n2,n3)

if n1 > n2 and n1 > n3:

    print(n1,"is a greater than a ",n2,n3 )

elif n2 > n1 and n2 > n3:

    print(n2," is a greater than a ",n1,n3 )
else:

    print(n3," is a greater than a ",n1,n2)
    

'''5. Write a python program to check whether a given year is a leap year or not. '''

print("\n5.check whether a given year is a leap year or not.")

year=int(input("enter year: "))

if year % 400 == 0 or (year % 4==0 and year % 100 !=0):

    print(year," is a leap year.")
else :

    print(year," is not a leap year.")
 

'''6. Write a python program to check whether a person is eligible to vote (age ≥ 18). '''

print("\n6.whether a person is eligible to vote.")
age=int(input("enter age: "))

if age >= 18 :

    print("eligible for vote,age is ",age)
else:

    print("not eligible for vote,age is ",age)


'''7. Write a python program to assign a grade based on marks using else-if ladder.'''

print("\n7.assign a grade based on mark using else-if leader.")

mark=int(input("enter mark: "))

if mark >= 90:

    print("Grade A.")

elif mark >=75:

    print("grade B.")

elif mark >= 50:

    print("Grade C.")

elif mark >=  35:

    print("Grade D.")
else:

    print("fail.")



'''8. Write a python program to check whether a character is a vowel or consonant.'''

print("\n8.check whether a character is a vowel or consonant.")
char=input("enter character: ")

if char.lower()=='a' or char.lower()=='e' or char.lower()=='i' or char.lower()=='o' or char.lower()=='u':

    print(char," is a vowel.")
else:

    print(char," is a consonant.")


'''9. Write a python program to check whether a character is uppercase or lowercase.''' 

print("\n9.check whether a character is uppercase or lowercase.")
character=input("enter character: ")

if  character.isupper():

    print(character ," is a uppercase.")

elif character.islower():

    print(character," is lowercase.")
else:

    print(character," not an alphabet.")


'''10. Write a python program to check whether a character is an alphabet, digit, or special character. '''

print("\n10.check whether a character is an alphabet, digit, or special character.")
c=input("enter character: ")

if c.isalpha():

    print(c," is a alphabet.")

elif c.isdigit():

    print(c," is a digit.")
else:

    print(c," is a special symbol.")
   




'''11. Write a python program to check whether a number is divisible by 5 and 11. '''

print("\n11.check whether a number is divisible by 5 and 11.")

num=int(input("enter number: "))

if num % 5 == 0 and num % 11 == 0:

    print(num," is divisible by both 5 & 11.")
else:

    print(num," is not divisible by both 5 & 11.") 


'''12. Write a python program to calculate discount based on purchase amount. '''

print("\n12.calculate discount based on purchase amount.")
amount=int(input("enter amount: "))

if amount>=2500:

    discount=amount*0.20

    print(amount," is and discount is ",discount)

elif amount >=1500:

    discount=amount*0.10

    print(amount," is and discount is ",discount)
else:

    discount=amount * 0.05

    print(amount,"is and discount is ",discount)


'''13. Write a python program to check whether three sides form a valid triangle. '''

print("\n13.check whether three sides form a valid triangle.")
s1=int(input('enter 1st side: '))

s2=int(input("enter 2nd side: "))

s3=int(input("enter 3rd side: "))

if s1+s2 > s3 and s3+s1>s2 and s3+s2 >s1:

    print("valid triangle.")
else:

    print("invalid triangle.")
    
'''14. Write a python program to determine the type of triangle (equilateral, isosceles, or scalene). '''

print("\n14.determine the type of triangle (equilateral, isosceles, or scalene). ")
s1=int(input("enter 1 side: "))

s2=int(input("enter 2 side: "))

s3=int(input("enter 3 side: "))
if s1== s2 and s2== s3 and s3==s1:
    print("equilateral triangle.")
elif s1==s2 or s2==s3 or s3==s1:
    print("isosceles triangle.")
else:
    print("scalene triangle.")

'''15. Write a python program to create a simple calculator using match-case. '''

print("\n15.simple calculator using match-case.")

print("operation list.\n1.addition\n2.subtraction\n3.multiplication\n4.division")

n1=int(input("enter 1 value: "))

n2=int(input("enter 2 value: "))
match int(input("enter operation: ")):
    case 1:

        print(f"addition of {n1} and {n2} is {n1+n2}.")

    case 2:

        print(f"subtraction of {n1} and {n2} is {n1-n2}.")

    case 3:

        print(f"multiplication of {n1} and {n2} is {n1*n2}.")

    case 4:

        print(f"division of {n1} and {n2} is {n1/n2}.")
    
    case _:
        print("invalid operation.")

'''16. Write a python program to print the day of the week based on day number using switch. '''
print("\n16.print the day of the week based on day number using switch. ")
day=int(input("enter day: "))
match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")
    
    case 6:
        print("Saturday")
    
    case 7:
        print("Sunday")
    
    case _:
        print("invalid day.")

'''17. Write a python program to print number of days in a month using switch-case. '''
print("\n17.print number of days in a month using switch-case.")
month=int(input("enter month: "))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12: 
        print("30 days.")

    case 4 | 6 | 9 | 11:
        print("31 days.")

    case 2:
        print("28 / 29 days.")

    case _:
        print("invalid month.")

'''18. Write a python program to find the absolute value of a number. '''
print("\n18.find the absolute value of a number.")
num=int(input("enter number: "))
if num < 0:
    abs_value=- num
else:
    abs_value=num
print(abs_value," is absolute number of ",num)

'''19. Write a python program to check whether a number is a multiple of 3 or 7. '''
print("\n19.check whether a number is a multiple of 3 or 7.")
num=int(input("enter number: "))
if num % 3 == 0 or num % 7 ==0:
    print(num," is a multiple of 3 or 7.")  
else:
    print(num," is a not multiple of 3 or 7.")
    
'''20. Write a python program to compare two strings (equal or not). '''
print("\n20.compare two strings (equal or not).")
str1=input("enter 1 string: ")
str2=input("enter 2 string: ")
if str1==str2:
    print(str1," & ",str2,"both are equals.")
else:
    print(str1," & ",str2," both are not equals.")

'''21. Write a python program for login validation using username and password.''' 
print("\n21.for login validation using username and password.")
username="nisha"
password=123456
u=input("enter username: ")
p=int(input("enter password: "))
if username==u and password==p:
    print("valid for login.")
else:
    print("no valid for login.")

'''22. Write a python program to check even or odd using the ternary operator. '''
print("\n22.check even or odd using the ternary operator.")
n=int(input("enter number: "))
result="even" if n % 2 == 0 else "odd"
print(result)

'''23. Write a python program to find the largest of three numbers using nested if. '''
print("\n23.find the largest of three numbers using nested if.")
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
n3=int(input("enter 3rd number: "))
print("user enterd numbers are ",n1,n2,n3)
if n1 >= n2: 
    if n1 >= n3:
        print(n1," is a largest number.")
    else:
        print(n3,"is a largest number.")
else:
    if n2 >= n3:
        print(n2," is a largest number.")
    else:
        print(n3," is a largest number.")

'''24. Write a python program to check leap year using the ternary operator. '''
print("\n24.check leap year using the ternary operator.")
year=int(input("enter year: "))
result = "leap" if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else "not leap"
print(result)


'''25. Write a python program using nested if to verify if a person can enter a club (age + ID proof). '''
print("\n25.nested if to verify if a person can enter a club (age + ID proof).")
age=int(input("enter age: "))
ID_Proof=input("enter ID_Proof: ")

ID_P="NI123"
if age >= 18 and ID_Proof == ID_P :
    print("yes you can be enter in club.")
else:
    print("no you can not be enter in club.")

'''26. Write a python program to check whether a student passed or failed based on marks. '''
print("\n26.check whether a student passed or failed based on marks.")
mark=int(input("enter mark: "))
if mark >= 35 :
    print("pass.")
else:
    print("fail.")

'''27. Write a python program to determine income tax based on salary slabs using else-if. '''
print("\n27.determine income tax based on salary slabs using else-if.")
salary=int(input("enter salary: "))
if salary >= 50000 :
    income_tax=5000
    purchase_salary=salary-income_tax
    print("salary is ",salary," and income_tax is ",income_tax," and employee purchase salary is ",purchase_salary)
elif salary >= 25000 :
    income_tax= 2500
    purchase_salary=salary-income_tax
    print("salary is ",salary," and income tax is ",income_tax," and employee purchase salary is ",purchase_salary)
else:
    income_tax=1000
    purchase_salary=salary-income_tax
    print("salary is ",salary," and income tax is ",income_tax," and employee purchase salary is ",purchase_salary)
    
'''28. Write a python program to check if a number lies within a specific range (10 to 20). '''
print("\n28.check if a number lies within a specific range (10 to 20).")
num=int(input("enter number: "))
if num >= 10 and num <= 20:
    print("yes.")
else:
    print("no.") 

'''29. Write a python program to find the maximum of four numbers using if statements. '''
print("\n29.find the maximum of four numbers using if statements.")
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
n3=int(input("enter 3rd number: "))
n4=int(input("enter 4th number: "))
print("user entered numbers: ",n1,n2,n3,n4)
if n1 > n2 and n1 > n3 and n1 > n4 :
    print(n1,"is maximum.")
elif n2 > n1 and n2 > n3 and n2 > n4 :
    print(n2,"is a maximum number.")
elif n3 > n1 and n3 > n2 and n3 > n4 :
    print(n3 ," is a maximum number.")
else:
    print(n4," is a maximum number.")

'''30. Write a python program to categorize temperature (Cold, Warm, Hot) based on value. '''
print("\n30.categorize temperature (Cold, Warm, Hot) based on value.")
value=int(input("enter value: "))
if value < 0 :
    print("cold temperature.")
elif value < 30 :
    print("warm temperature.")
else:
    print("hot temperature.")
