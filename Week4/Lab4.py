# Lab3
# Author: 

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.
print("1.")
num = input("Enter a number: ")
if int(num) > 0:
    print("Positive")
elif int(num) < 0:
    print("Negative")

# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
print("2.")
num = input("Enter a number: ")
if int(num) % 2 == 0:
    print("Even")
else:
    print("Odd")
# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
print("3.")
num = input("Enter a number: ")
i = 1
while i <= int(num):
    print(i)
    i += 1
# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.
print("4.")
sum = 0
for i in range(5):
    num = int(input("Enter a number: "))
    sum += num
    sum+=num
avg = sum / 5 
print(avg)
# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.
print("5.")
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
print("6.")
num = int(input("Enter a number: "))
count = num
while count >= 1:
    import time
    time.sleep(1)  
    print(count)
    count -= 1
print("blast off!")
# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.
print("7.")
import time
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if i % 7 == 0:
        print("Lucky")
        time.sleep(0.5)
        
        continue
    if i > 100:
        break
    print(i)
    time.sleep(0.5)
# tried something out with time lol, came out okay