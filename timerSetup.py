import os.path
import shutil

"""
Script to automatically generate a .py file with all time testing material included
as well as two text documents, one containing the runtime data, one keeping track of the
number of runs. RUN ONLY ONCE. THIS MUST BE PLACED IN THE SAME DIRECTORY AS THE PROGRAM YOU WANT TO TEST.
"""

def createRunTimes():
    with open('./runtimes.txt', 'w') as file2:
        file2.write('')
    
def createNumRuns():
    with open('./numruns.txt', 'w') as file3:
        file3.write('0') #0 runs at init

def createVersions():
    os.mkdir('./versions')

def createNamePy():
    with open('./name.py', 'w') as file1:
        """
        The indentation of the write string may look weird, 
        but it's intended. Don't change it unless you know 
        what you're doing or it may mess up the indentation 
        in name.py and you'll have to manually fix it.
        """
        file1.write(
'''import os
import shutil
import time
from datetime import datetime
timer = time.time()
"""
create a "pending run" version of this program. This is created 
before everything else because the user may modify the file during 
the program is running, and if they decide to log the run, the 
version that will be copied will be the one that they modified 
during the run, not the version that was actually used to run.
"""
program_name = os.path.basename(__file__) #https://stackoverflow.com/questions/4152963/get-name-of-current-script-in-python
split_program_name = program_name.split('.')
pending_program_name = split_program_name[0] + "_" + "pending" + "_" + "run" + ".py"
shutil.copyfile(program_name, "./versions/" + pending_program_name)
#check if program's name changed. If so, update all file names in versions to reflect the change
#more specifically, checks the first file in versions and compares its name to tested program
#first_name_in_versions = os.scandir("./versions")
#split_first_name_in_versions = first_name_in_versions.split("_")
try:
    #DO NOT SPLIT BY _. USERS COULD HAVE A PROGRAM NAME WITH _ IN IT AND WILL MESS UP STUFF
    for file in os.scandir("./versions"):
        dir_entry = str(file)
        #print(dir_entry)
        #first, split the dir_entry to get the full file name
        full_file_name = (dir_entry.split("'"))[1] #nam3e_run7.py
        #print(full_file_name)
        #then, split the full file name to get the name after the underscore
        name_after_underscore = (full_file_name.split("_"))[1]
        #print(name_after_underscore)
        name_before_underscore = (full_file_name.split("_"))[0]
        #print(name_before_underscore)

        
        # file_name = (((dir_entry.split("'"))[1]).split("_"))[0]
        if name_before_underscore != split_program_name[0]:
            os.rename("./versions/" + full_file_name, "./versions/" + split_program_name[0] + "_" + name_after_underscore)
except:
    print("Uh oh, an error occured while checking file names. Please check that the files in your versions folder are in correct naming format (name_run#.py)")
    os.remove("./versions/" + pending_program_name)
    exit()
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
    #increment runs in numruns by 1
    with open("numruns.txt", "r+") as numruns:
        for line in numruns:
            num_runs = int(line[0])
            num_runs += 1
            current_date = "Run " + str(num_runs) + " " + current_date
            numruns.seek(0)
            numruns.truncate(0)
            numruns.write(str(num_runs))
    #log new run to runtimes        
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

    #add current version of tested program to versions folder
    program_name = os.path.basename(__file__) #https://stackoverflow.com/questions/4152963/get-name-of-current-script-in-python
    split_program_name = program_name.split('.')
    program_version = "run" + str(num_runs)
    #final_name is in format name_run#.py
    final_program_name = split_program_name[0] + "_" + program_version + '.py'

    #rename pending_name file to final_program_name in versions
    os.rename("./versions/" + pending_program_name, "./versions/" + final_program_name)

else:
    os.remove("./versions/" + pending_program_name)
'''
)

def main():
    #os.path.isfile checks whether the name.py file already exists in the current directory
    if os.path.isfile('./name.py'):
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

    if os.path.isfile('./runtimes.txt'):
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

    if os.path.isfile('./numruns.txt'):
        overwriteNumRuns = str(input("A file called 'numruns.txt' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        while (overwriteNumRuns != "y" and overwriteNumRuns != "n"):
            overwriteNumRuns = str(input("A file called 'numruns.txt' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        if overwriteNumRuns == "y":
            createNumRuns()
            print("numruns.txt successfully overwritten.\n")
        else:
            pass
    else:
        createNumRuns()
        print("Successfully created numruns.txt.")


    if os.path.isdir('./versions'):
        overwriteVersions = str(input("A folder called 'versions' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        while (overwriteVersions != "y" and overwriteVersions != "n"):
            overwriteVersions = str(input("A folder called 'versions' already exists in this directory. Are you sure you want to overwrite it? (y/n): "))
        if overwriteVersions == "y":
            #can just remove versions if empty
            if len(os.listdir('./versions') ) == 0:
                os.rmdir('./versions')
                createVersions()
                print("'versions' successfully overwritten.")
            #case is not empty, will need to prompt for final confirmation
            else:    
                reallyOverwriteVersions = str(input("'versions' is not an empty directory. Do you REALLY want to overwrite it? (y/n): "))
                while (reallyOverwriteVersions != "y" and reallyOverwriteVersions != "n"):
                    reallyOverwriteVersions = str(input("'versions' is not an empty directory. Do you REALLY want to overwrite it? (y/n): "))
                if reallyOverwriteVersions == 'y':
                    try:
                        shutil.rmtree('./versions')
                        createVersions()
                        print("'versions' successfully overwritten.")
                    except OSError as e:
                        print("Error: %s : %s" % ('./versions', e.strerror))
                else:
                    pass
        else:
            pass
    else:
        createVersions()
        print("Successfully created 'versions'.")







if __name__ == "__main__":
    main()












