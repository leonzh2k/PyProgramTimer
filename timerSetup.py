import os.path

"""
Script to automatically generate a .py file with all time testing material included
as well as two text documents, one containing the runtime data, one keeping track of the
number of runs. RUN ONLY ONCE. THIS MUST BE PLACED IN THE SAME DIRECTORY AS THE PROGRAM YOU WANT TO TEST.
"""

def createRunTimes():
    with open('runtimes.txt', 'w') as file2:
        file2.write('')
    
def createNumRuns():
    with open('numruns.txt', 'w') as file3:
        file3.write('0') #0 runs yet

def createNamePy():
    with open('name.py', 'w') as file1:
        """
        The indentation of the write string may look weird, 
        but it's intended. Don't change it unless you know 
        what you're doing or it may mess up the indentation 
        in name.py and you'll have to manually fix it.
        """
        file1.write(
'''import time
from datetime import datetime
timer = time.time()
#######################################

#WRITE YOUR PROGRAM HERE

#######################################
now = datetime.now()
current_date = now.strftime("(%m/%d/%Y %I:%M:%S %p)\\n")
runtime = time.time() - timer
time_secs = str(runtime) + " " + "seconds" + "\\n"
time_mins = str(runtime / 60) + " " + "minutes" + "\\n"
time_hrs =  str(runtime / 3600) + " " + "hours" + "\\n"
print("Finished in:")
print("====================")
print(time_secs, end='')
print("or")
print(time_mins, end='')
print("or")
print(time_hrs, end='')

        
decision = str(input("Would you like to write this time to the list of runtimes? (y/n): "))
while (decision != "y" and decision != "n"):
    decision = str(input("Would you like to write this time to the list of runtimes? (y/n): "))
if decision == "y":
    with open("numruns.txt", "r+") as numruns:
        for line in numruns:
            num_runs = int(line[0])
            num_runs += 1
            current_date = "Run " + str(num_runs) + " " + current_date
            numruns.seek(0)
            numruns.truncate(0)
            numruns.write(str(num_runs))
            
    with open("runtimes.txt", "a") as runtimes:
        runtimes.write(current_date)
        runtimes.write("------------------------------\\n")
        runtimes.write(time_secs)
        runtimes.write("or\\n")
        runtimes.write(time_mins)
        runtimes.write("or\\n")
        runtimes.write(time_hrs)
        runtimes.write("\\n")
        runtimes.write("==============================\\n\\n")
'''
)

def main():
    #os.path.isfile checks whether the name.py file already exists
    if os.path.isfile('name.py'):
        overwriteName = str(input("A file called 'name.py' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        while (overwriteName != "y" and overwriteName != "n"):
            overwriteName = str(input("A file called 'name.py' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        if overwriteName == "y":
            createNamePy()
            print("name.py successfully overwritten.\n")
        else:
            pass
    else:
        createNamePy()
        print("Successfully created name.py.\n")

    if os.path.isfile('runtimes.txt'):
        overwriteRunTimes = str(input("A file called 'runtimes.txt' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        while (overwriteRunTimes != "y" and overwriteRunTimes != "n"):
            overwriteRunTimes = str(input("A file called 'runtimes' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        if overwriteRunTimes == "y":
            createRunTimes()
            print("runtimes.txt successfully overwritten.\n")
        else:
            pass
    else:
        createRunTimes()
        print("Successfully created runtimes.txt.\n")

    if os.path.isfile('numruns.txt'):
        overwriteNumRuns = str(input("A file called 'numruns.txt' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        while (overwriteNumRuns != "y" and overwriteNumRuns != "n"):
            overwriteNumRuns = str(input("A file called 'numruns.txt' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        if overwriteNumRuns == "y":
            createNumRuns()
            print("numruns.txt successfully overwritten.")
        else:
            pass
    else:
        createNumRuns()
        print("Successfully created numruns.txt.")

if __name__ == "__main__":
    main()












