# Question 1

print("Question 1")
def TowerOfHanoi(n,source,dest,auxi):
    if n==1:
        print("Move the disk 1 from source",source,"to destination",dest)
        return
    else:
        TowerOfHanoi(n-1,source,auxi,dest)
        print("Move the disk",n,"from source",source,"to destination",dest)
        TowerOfHanoi(n-1,auxi,dest,source)


TowerOfHanoi(3,'A','C','B')
print("\n")

#Question 2

print("Question 2")
from math import factorial
from tracemalloc import start
#input the n
n=int(input("Enter the number of rows of pascal triangle you want to be printed\n"))
print("USING LOOPS")
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")#for left spacing
    for j in range(i+1):
        print(factorial(i)//(factorial(i-j)*factorial(j)), end=" ")
    print()
print("\n")

print("USING RECURSION")
def pascal_triangle(n,original_length=n):
    if n == 0:
        return
    pascal_triangle(n-1,original_length)
    print('  '*(original_length-n), end='')
    start=1
    for i in range(1,n+1):
        print(start,end='  ')
        start=start*(n-i)//i
    print()
pascal_triangle(n)
print("\n")

#Question 3

print("Question 3")

int_1=int(input("Enter the first integer\n"))
int_2=int(input("Enter the second integer\n"))

Quotient=int_1//int_2
remainder=int_1 % int_2

print("Quotient is :",Quotient)
print("remainder is :",remainder)

#part a
print("part (A)")
print(callable(Quotient))
print(callable(remainder))
print("")

#part b
print("part (B)")
if Quotient == 0:
    print("the value of quotient is zero(0)")
elif remainder == 0:
    print("the value of remainder is zero(0)")
else:
    print("ALL THE VALUES ARE NON-ZERO")
print("")

#part c
print("Part (C)")
list = [Quotient + 4, remainder + 4, remainder + 5, Quotient + 5, remainder + 5, Quotient + 6, remainder + 6]

result = []
for i in range(len(list)):
    if list[i] > 4:
        result.append(list[i])
print(f" Filtered out numbers that are greater than 4 are : {result}")
print("")

#part d
print("part (D)")
set_datatype_result = set(result)
print(" Set:",set_datatype_result)
print("")
#part e
print("part (E)")
immutable_Set = frozenset(set_datatype_result) 
print( "Immutable set:",immutable_Set)
print("")

#part F
print("part (F)")
print("Maximun value of the immutable set:",max(immutable_Set))
print("Hash value of the above maximum value is :", hash(max(immutable_Set)))
print("\n")


# Question 4
print("Question 4")

class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object that was created is now destroyed")

#creating object
student_1 = Student("Rithik", 21103054)
print("Object is created...")
#printing the assigned values
print("")
print(f"The name of the student is '{student_1.name}' and SID is '{student_1.roll_no}'.")
print("")
#deleting object
del student_1
print("\n")

# Question 5
print("Question 5")
class employees:
    def __init__(self,employee,salary):
        self.name = employee
        self.salary = salary

employee_1=employees("Mehak",40000)
employee_2 =employees("Ashok", 50000)
employee_3 =employees("Viren", 60000)

#part <a> updating salary
print("Part (A)")
employee_1.salary = 70000
print(f" The updated salary of {employee_1.name} is {employee_1.salary} ")
print("")

#part <b> deleting a record
print("Part (B)")
print("Record of Viren is deleted", end='')
del employee_3
print("\n")

#Question 6
print("Question 6")
#inputting a word from the first friend
word =input("Enter the word: ")
word=word.lower()

#inputting a meaningful word with the exact same letters
testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword=testword.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()