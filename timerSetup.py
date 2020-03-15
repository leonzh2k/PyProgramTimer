"""
Script to automatically generate a .py file with all time testing material included
as well as two text documents, one containing the runtimes, one keeping track of the
number of runs. RUN ONLY ONCE. THIS MUST BE PLACED IN THE SAME FILE AS THE PROGRAM YOU WANT TO TEST.
"""

with open('name.py', 'w') as file1:
    #file1.write(importTime)
    #file1.write(importDateTime)
    #file1.write(timer)
    #file1.write(
    file1.write(
'''import time
from datetime import datetime
timer = time.time()

#WRITE YOUR PROGRAM HERE

now = datetime.now()
current_time = now.strftime("(%d/%m/%Y %H:%M:%S)\\n")
runtime = time.time() - timer
time_secs = "finished in" + " " + str(runtime) + " " + "seconds" + "\\n"
time_mins = "or" + " " + str(runtime / 60) + " " + "minutes" + "\\n"
time_hrs =  "or" + " " + str(runtime / 3600) + " " + "hours" + "\\n"
print(time_secs, end='')
print(time_mins, end='')
print(time_hrs, end='')

        
decision = str(input("Would you like to write this time to the list of runtimes? (y/n)\\n"))
if decision == "y":
    with open("metadata.txt", "r+") as metadata:
        for line in metadata:
            num_runs = int(line[0])
            num_runs += 1
            current_time = "Run " + str(num_runs) + " " + current_time
            metadata.seek(0)
            metadata.truncate(0)
            metadata.write(str(num_runs))
            
    with open("runtimes.txt", "a") as runtimes:
        runtimes.write("\\n")
        runtimes.write(current_time)
        runtimes.write(time_secs)
        runtimes.write(time_mins)
        runtimes.write(time_hrs)
'''
)

    
    
with open('runtimes.txt', 'w') as file2:
    file2.write('')

with open('metadata.txt', 'w') as file3:
    file3.write('0') #0 runs yet



