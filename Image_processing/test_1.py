import numpy as np
import pandas as pd

 #A die is thrown twice and the sum of the numbers appearing is observed to be 6.
# What is the probability that the number 4 has appeared at least once?

print("A represents number of all possibles pairs came from die that makes sum 6")
A = 5
print("B represents number of all possibles moves from die that makes sum 6 and atleast one of the is 4","\n")
B = 2
print("Pr(B) = ",B/A)


#Simulation
import random


N = 1000000
count_number_of_fours = 0
for i in range(0,N):
    x = random.randint(1,5)
    y = 6-x
    #since we conditioned the sum to be 6.
    if(x == 4 or x == 2):
        count_number_of_fours = count_number_of_fours+1;
    
print("Pr(B) using simulation = ",count_number_of_fours/N)
#print("completed")
