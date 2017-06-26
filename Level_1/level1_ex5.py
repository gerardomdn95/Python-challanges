"""
Write a program that asks the user how many Fibonnaci numbers to generate and 
then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.

Hint 
The Fibonnaci seqence is a sequence of numbers where the next number 
in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, 


"""
x = int(input("How many Fibonnaci numbers do you want to generate? "))

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fiboList=[fibo(n) for n in range(1,x+1)]

print(fiboList)