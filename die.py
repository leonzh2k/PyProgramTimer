import os
import shutil
from dependencies import progtimer
from dependencies import proglogger
program_name = os.path.basename(__file__)
pending_program_name = proglogger.createPendingProgram(program_name)
proglogger.checkProgramName(program_name, pending_program_name)

startTime = progtimer.startProgramTimer() # start timer here so it starts just before the program starts
#######################################

#WRITE YOUR PROGRAM HERE

#######################################
endTime = progtimer.stopProgramTimer(startTime)
current_date = progtimer.getCurrentDate()
(time_secs, time_mins, time_hrs) = progtimer.formatRunTime(endTime)
progtimer.printFormattedRunTime(time_secs, time_mins, time_hrs)
proglogger.askToLog(time_secs, time_mins, time_hrs, current_date, program_name, pending_program_name)
