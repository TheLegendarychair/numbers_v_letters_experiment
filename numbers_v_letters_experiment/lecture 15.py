# -*- coding: utf-8 -*-
import numpy as np
import time as time
import matplotlib.pyplot as plt
import os


with open("numbers.txt","r") as file:
    letter_nums = file.readlines()

def distract():
    for i in range(20):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

for i in range(1):
    number_array = [ np.random.randint(1,100) for number in range(7)]
    for i in number_array:
        print(i)
    time.sleep(10)
    distract()
        
    num_correct = 0
    for j in range(7):
        num_input = int(input("input the number "))
        for num in number_array:
            if num == num_input:
                num_correct +=1
    print(num_correct)
    
    letter_array = [letter_nums[np.random.randint(1,100)].strip('\n') for number in range(7)]
    word_correct = 0
    for z in letter_array:
        print(z)
    time.sleep(10)
    distract()
    for k in range(7):
        word_num_input = input("input the number ")
        for num in letter_array:
            if num == word_num_input:
                word_correct +=1
    print(word_correct)
    
file_path = 'statistics_log.txt'

if not os.path.exists(file_path):
    with open(file_path,'w') as file:
        file.write("0\n0")
    
with open(file_path, 'r') as f:
    statisticts = f.readlines()
    number_statistics = int(statisticts[0].strip('\n'))
    word_statistics = int(statisticts[1])
    word_statistics += word_correct
    number_statistics += num_correct
    f.close()
    


statistics_list = [number_statistics,word_statistics]                          
types = ['number','letter']

plt.bar(types,statistics_list)
plt.xlabel("display type")
plt.ylabel("correct answers")
plt.title("remembering numbers that are written with words vs numbers")
plt.show()

with open(file_path, 'w') as f:
    f.write(str(number_statistics))
    f.write('\n')
    f.write(str(word_statistics))
    f.close()
    
    
    
    
        
        
        
            



    