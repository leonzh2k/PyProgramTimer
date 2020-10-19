import time
from datetime import datetime
timer = time.time()
#######################################

#WRITE YOUR PROGRAM HERE

#######################################
now = datetime.now()
current_date = now.strftime("(%m/%d/%Y %I:%M:%S %p)\n")
runtime = time.time() - timer
time_secs = str(runtime) + " " + "seconds" + "\n"
time_mins = str(runtime / 60) + " " + "minutes" + "\n"
time_hrs =  str(runtime / 3600) + " " + "hours" + "\n"
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
        runtimes.write("------------------------------\n")
        runtimes.write(time_secs)
        runtimes.write("or\n")
        runtimes.write(time_mins)
        runtimes.write("or\n")
        runtimes.write(time_hrs)
        runtimes.write("\n")
        runtimes.write("==============================\n\n")
