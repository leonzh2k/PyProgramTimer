# PyProgramTimer 
A tool that generates files to help you test and compare runtimes of your Python programs.

## Table of Contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Requirements](#Requirements)
* [Setup](#Setup)
* [Usage](#Usage)
* [Todo](#Todo)
* [Status](#Status)

## Introduction
### Background and Purpose
There was a period of time where I was really into solving  <a href="https://projecteuler.net/" target="_blank">Project Euler </a>problems. Oftentimes, the programs I wrote to solve the problems would have really long runtimes, since unless there was some mathematical trick that could be used, an obscene amount of mathematical operations would be required to derive the answer. However, it is written on the website that with an efficient implementation, answers to problems can be derived in under *one minute*. Needless to say, my programs were not meeting that standard. Thus, I became curious about seeing the runtimes of my solutions and how they got better with successive iterations. And thus the idea for this script was born.

## Technologies
* Python 3.7.3

## Requirements
This script was written in Python 3.7.3, but may work on older versions.

## Setup

1. Download `timerSetup.py`. This is similar to the conventional installer program that installs software. 
2. Create an empty directory that you wish to develop your program in. 
3. Move `timerSetup.py` into the directory, and execute it ONLY ONCE.
4. New files will be created. You may have to reload the directory to see them.
5. You will see one new file and three new folders:
    *  `name.py` is the file where you will develop your program. You can rename this whatever you like.
    * `data` is the folder that contains info about the runtimes:
        *  `runtimes.txt` keeps track of runtimes. You probably shouldn't edit this.
        *  `numruns.txt` is used to keep track of how many runs have been logged to `runtimes.txt`. You probably shouldn't edit this either.
    * `dependencies` contains modules necessary for the tool to work.
    * `versions` contains different versions of your program. The current version of your program is saved here when you choose to log a run. The filename is suffixed with the run number which corresponds to the run number in `runtimes.txt`. This way you can easily remember how fast earlier versions of your program ran. 
6. Delete or move `timerSetup.py` out of the directory (you can reuse it for other programs). If you don't do this, you may accidentally run it again and run the risk of overwriting important data; fortunately there is a safeguard against that (The program will prompt you before overwriting.)
7. Develop your program.


## Usage
The general use cycle of this tool would probably be something like this:
1. Write the first (working) iteration of your program.
2. Run it and view the runtime in `runtimes.txt`.
3. Make some changes to your program.
4. Run it and view the runtime in `runtimes.txt`.
5. Repeat steps 3-4.
6. See how much faster your program has gotten and how far you've come.....

## Todo
* Create `compareRunTimes.py` that allows you to compare runtimes
* Possible GUI interface to compare two versions of programs with tkinter?
* Update README to reflect changes in code
* <del>Figure out how to format runtime to specify less decimal places</del>
* <del>Package timer and run-logging code into modules to reduce clutter in main program<del>

## Status
Stopped but not complete. May continue development in the future.

## Bugs


