# Question 1
print("question 1")
ri=str(input("ENTER ANY STRING :"))
list=ri.split() #to split all the elements of the string
dict={} # initializing an empty dictionary
if list.__len__()==1 :
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)

print("   \n")


#question 2
print("Question 2")
while(True):#while loop is used so that if any wrong value is entered then will be entered again
    day=int(input("ENTER THE DAY:"))
    if(1<=day<=31):
        break
    else:
        print("Enter a valid date")

while(True):
    month=int(input("Enter the month:"))
    if(1<=month<=12):
        break
    else:
        print("Enter a valid month")

while(True):
    year=int(input("Enter a year between 1800 and 2025:"))
    if(1800<=year<=2025):
        break
    else:
        print("Enter the year between 1800 and 2025 only")
if(month==1 or 3 or 5 or 7 or 8 or 10):
    if(day==31):
        day=1
        month=month+1
        print(day,"/",month,"/",year)
    elif(day<31):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("please enter correct date")

elif(month==4 or 6 or 9 or 11):
    if(day==30):
        day=1
        month=month+1
        print(day,"/",month,"/",year)
    elif(day<30):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("please enter correct date")

elif(month==2):
    if((year%400==0) or
    (year%100 !=0) and
    (year%4 == 0) ):
      if(day==29):
          day=1
          month=month+1
          print(day,"/",month,"/",year)
      elif(day<29):
          day+=1
          print(day,"/",month,"/",year)
      else:
          print("please enter correct date")

    else:
        if(day==28):
            day=1
            month+=1
            print(day,"/",month,"/",year)
        elif(day<28):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("please enter correct date")

elif(month==12):
    if(day==31):
        day=1
        month=1
        year+=1
        print(day,"/",month,"/",year)
    elif(day<31):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("please enter correct date")
else:
    print("9please enter correct date")
print("   \n")    
    

#question 3
print("Question 3")
input_list=input("enter the elements with a space: \n")
user_list=input_list.split()
#print this list
print('list:', input_list )

#converting each string input into int
for i in range(len(user_list)):
    user_list[i]=float(user_list[i])

square_list=[(user_list[i],user_list[i]**2) for i in range(len(user_list))]
print("the required result is :",square_list)
print("   \n")


#question 4
print("Question 4")
point=int(input("Enter the grade point: \n"))
if point <4 or point>10:
    print("Invalid grade point! Try again.")
elif(point==4):
    print("Your grade is 'D' and poor performance")
elif(point==5):
    print("Your grade is 'C' and below average performance")
elif(point==6):
    print("Your grade is 'C+' and average performance")
elif(point==7):
    print("Your grade is 'B' and Good performance")
elif(point==8):
    print("Your grade is 'B+' and very goood performance")
elif(point==9):
    print("Your grade is 'A' and Excellent performance")
else:
    print("Your grade is 'A+' and outstanding performance")
print("   \n")

#question 5
print("Question 5")
x=6
for i in range(x):#printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65+j),end='') #ASCII value of A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72
    print()
print("  \n")

#question 6
print("Question 6")
sid=int(input("Enter your sid: \n"))
name=input("Enter name: \n")
students={sid:name}

while True:
    option=input("Do you want to enter another student entry(Y or N):").upper()
    if option=='Y':
        sid=int(input("Enter sid: "))
        name=input("Enter name: ")
        students[sid]=name
    elif option=='N':
        break
    else:
        print("Invalid input!")

# part(a)-print the dictionary
print("<a>\n",students)

#part (b)-sort according to the names
print("<b>\n",{k:v for k,v in sorted(students.items(), key=lambda x:x[1])})

#part (c)-sort according to the sids 
print("<c>\n",{k:v for k,v in sorted(students.items())})

#part (d)-search for a student by their sid 
sid=int(input("Search Name with SID: \n"))
print("<d>\n",students[sid])


#question 7
print("Question 7")
# Function to display the Fibonacci sequence
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES:  \n"))
if no_of_terms <=0:
    print("Please enter positive integer")
else:
    print("Fibonacci sequenceL: ")
    sum=0
    for i in range(no_of_terms):
        print(recur_fibo(i))
        sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("AAVERAGE OF THE RESULTANT FIBONACCI SERIES IS: ",avg)

#Question 8
print("Question 8")
Set_1 ={1,2,3,4,5}
Set_2 ={2,4,6,8}
Set_3 ={1,5,9,13,17}

#part (a)
Set_union=Set_1.union(Set_2)
Set_intersection=Set_1.intersection(Set_2)
Part_A_Set=Set_union - Set_intersection
print("<a>\n",Part_A_Set)

#part (b)-subtracting intersection of sets taken two at a time from the union of all three sets 
Part_B_set= Set_1.union(Set_2.union(Set_3))- Set_1.intersection(Set_2) -Set_2.intersection(Set_3) - Set_3.intersection(Set_1)
print("<b>\n",Part_B_set)

# part (c)-subtracting intersection of three from two taken at one time
Part_C_Set=((Set_1.intersection(Set_2)).union((Set_1.intersection(Set_3)).union(Set_2.intersection(Set_3))))-(Set_1.intersection(Set_2.intersection(Set_3)))
print("<c>\n",Part_C_Set)

#part (d)-excluding the numbers from 1 to 10 that are occuring in set1
Part_D_Set=set()
for i in range(1,11):
    if i not in Set_1:
        Part_D_Set.add(i)
print("<d> \n",Part_D_Set)

#part e
Part_E_Set=set()
if i in range(1,11):
    if i not in Set_1 and i not in Set_2 and i not in Set_3:
        Part_E_Set.add(i)
print("<e>\n",Part_E_Set)
