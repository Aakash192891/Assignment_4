# Question 1 
def Towers_Of_Hanoi(numdisks, frm_disc, to_disc, aux_disc):
    if numdisks == 1:
        print("Move disk [1] from rod [",
              frm_disc, "] to rod {", to_disc, '}')
        return
    Towers_Of_Hanoi(numdisks-1, frm_disc, aux_disc, to_disc)
    print("Move disk ["+str(numdisks) + "] from rod [",
          str(frm_disc)+" ] to rod {", to_disc, '}')
    Towers_Of_Hanoi(numdisks-1, aux_disc, to_disc, frm_disc)
numdisks = 4
Towers_Of_Hanoi(numdisks, 'A', 'C', 'B') 

# Output 1
Move disk [1] from rod [ A ] to rod { B }
Move disk [2] from rod [ A ] to rod { C }
Move disk [1] from rod [ B ] to rod { C }
Move disk [3] from rod [ A ] to rod { B }
Move disk [1] from rod [ C ] to rod { A }
Move disk [2] from rod [ C ] to rod { B }
Move disk [1] from rod [ A ] to rod { B }
Move disk [4] from rod [ A ] to rod { C }
Move disk [1] from rod [ B ] to rod { C }
Move disk [2] from rod [ B ] to rod { A }
Move disk [1] from rod [ C ] to rod { A }
Move disk [3] from rod [ B ] to rod { C }
Move disk [1] from rod [ A ] to rod { B }
Move disk [2] from rod [ A ] to rod { C }
Move disk [1] from rod [ B ] to rod { C }



#Question 2
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6) 

# Output 2 
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]



# Question 3
val1 = int(input("Enter first integer value(dividend): "))
while True:                                                                                     
    val2 = int(input("Enter second integer value(divisor): "))
    if val2 != 0:
        break
    else:
        print("\nDivisor must not be 0\nPlease enter the divisor again")
result = divmod(val1,val2)
print("\nQuotient:",result[0],"\nRemainder:",result[1])

print("\na. Check whether the function (divmod()) is callable or not:")                           
a_part = callable(divmod)
print(a_part, end="")
if a_part == True:
    print(", which means it is callable")
else:
    print(", which means it is not callable")

print("\nb. Check whether all the values are zero or not:")                                        
if all(x != 0 for x in result):
    print("All values in result(i.e. quotient and remainder) are non-zero.")
else:
    print("All values in result(i.e. quotient and remainder) are not non-zero(i.e. one of them is 0).")

print("\nc. Add (4,5,6) to the result and filter out values greater than 4:")                     
c_part = result + (4,5,6)
c_part_output = sorted(list((x for x in c_part if x>4)))
print("Values greater than 4(in list format) are:", c_part_output)

print("\nd. Convert the above result into a set datatype:")                                          
d_part = set(c_part_output)
print("The output of previous part in set datatype would be:", d_part)

print("\ne. Make the set immutable:")                                                             
e_part = frozenset(d_part)
print("The immutable set would be:", e_part)

print("\nf. Evaluate the maximum value from the set and find out its hash value:")              
f_part = max(e_part)
print("The maximum value from the set is:", f_part)
print("The hash value of %d(considering it to be integer) is %d and its hash value is %d(if we consider %s as a string)." % (f_part,hash(f_part),hash(str(f_part)),str(f_part)))


# Output
Enter first integer value(dividend): 20
Enter second integer value(divisor): 11

Quotient: 1 
Remainder: 9

a. Check whether the function (divmod()) is callable or not:
True, which means it is callable

b. Check whether all the values are zero or not:
All values in result(i.e. quotient and remainder) are non-zero.

c. Add (4,5,6) to the result and filter out values greater than 4:
Values greater than 4(in list format) are: [5, 6, 9]

d. Convert the above result into a set datatype:
The output of previous part in set datatype would be: {9, 5, 6}

e. Make the set immutable:
The immutable set would be: frozenset({9, 5, 6})

f. Evaluate the maximum value from the set and find out its hash value:
The maximum value from the set is: 9
The hash value of 9(considering it to be integer) is 9 and its hash value is -2396473482507532415(if we consider 9 as a string).



# Question 4 
class Student:                                                                           
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        print("Object Created\n")
    def __del__(self):
        print("\nObject destroyed")
name = input("Enter name of student: ").strip()                                                      
roll_no = int(input("Enter SID of %s: " % (name)))
student1 = Student(name,roll_no)                                                              
print("The name of the student is %s and his/her roll number is %d" % (student1.name,student1.rno))  
del student1 


# Output 4
Enter name of student: Aakash
Enter SID of Aakash: 20105003
Object Created

The name of the student is Aakash and his/her roll number is 20105003

Object destroyed



# Question 5 
class Employee:                                                                                 
    def __init__(self,name,salary):        
        self.name = name
        self.salary = salary
    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))
employee1 = Employee("Mehak",40000)                                                                   
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)
print("The current database is:")                                                                
for i in [employee1,employee2,employee3]:
    i.print_data()

print("\na. Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")     
employee1.salary = 70000
print(employee1.salary)

print("\nb. Deleted the record of %s(whose salary is %d)" % (employee3.name,employee3.salary))
del employee3

print("\nThe final database is:")                                           
for i in [employee1,employee2]:
    i.print_data()

    

    
# Output 5
The current database is:
Mehak has a salary of 40000 rupees
Ashok has a salary of 50000 rupees
Viren has a salary of 60000 rupees

a. Updated the salary of Mehak from 40000 to 70000

b. Deleted the record of Viren(whose salary is 60000)

The final database is:
Mehak has a salary of 70000 rupees
Ashok has a salary of 50000 rupees



# Question 6 
utter_word = input("Frist friend please enter the uttered word: ")
print()
new_word = input("Friend 2 please enter new word to test your friendship: ")
print()

count_list_uttered_word = [0]*26
count_list_new_word = [0]*26

for letter in utter_word:
    count_list_uttered_word[ord(letter.lower()) - ord('a')] += 1

for letter in new_word:
    count_list_new_word[ord(letter.lower()) - ord('a')] += 1

if count_list_uttered_word == count_list_new_word:

    while True:

        check = input("Please enter whether the new word have meaning or not(Y or N): ")
        print()
        if check == "Y":
            print("You and your friend passed the friendship test.")
            break
        elif check == "N":
            print("Oops! You and your friend failed the friendship test")
            break
        else:
            print("Please enter a valid input.(Y or N)")

else:
    print("Oops! You and your friend failed the friendship test") 
