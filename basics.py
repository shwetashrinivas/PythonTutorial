import datetime 
print("  The date and time is: " , datetime.datetime.now())

# Variables
x = 10
y = "10"
z = 10.0
sum1 = x + x
sum2 = y + y
print(sum1 , sum2)
print(type(x) , type(y) , type(z))

#List (Mutable)
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0)) #Counts the items with value 10.0

mysum = sum(student_grades)
length = len(student_grades)

mean = mysum / length
print(mean)

max_value = max(student_grades)
print(max_value)

print(list(range(1, 10))) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) #[1, 3, 5, 7, 9]

username = "Shweta"
print(username.lower())

weekday = [1,2,3,4,5,6]
weekday.append(7)
print(weekday)

#Dictionary --------- dir(dict)
student_marks = {"Shweta": 99, "Smita" : 100, "Shiny": 98}
print(student_marks.values())
print(student_marks.keys())

#Tuples  (immutable)
temperatures = (30 , 35 , 40)
print(temperatures)

#To find out what Python builtin functions there are:
dir(__builtins__)

#Documentation for a Python command can be found with:
help(str)
help(str.replace)
help(dict.values)