# PyProgramTimer
A simple script that when executed generates files to help you test and compare runtimes of your Python programs.

## Introduction
### Background and Purpose
There was a period of time where I was really into solving Euler Project problems. Oftentimes, the programs I wrote to solve the problems would have really long runtimes, since unless there was some mathematical trick that could be used, an obscene amount of mathematical operations would be required to derive the answer. However, it is written on the website that with an efficient implementation, answers to problems can be derived in under *one minute*. Needless to say, my programs were not meeting that standard. Thus, I became curious about seeing the runtimes of my solutions and how they got better with successive iterations. And thus the idea for this script was born.

## Requirements
This script was written in Python 3.7.3, but may work on older versions.

## Setup

1. Download `timerSetup.py`. 
2. Create an empty directory that you wish to develop your program in. 
3. Move `timerSetup.py` into the directory, and execute it ONLY ONCE. 
4. You will see two new files, `numruns.txt` and `runtimes.txt`. `runtimes.txt` keeps track of runtimes, and `numruns.txt` is used to keep track of how many runs have been logged to `runtimes.txt`.
4. Delete or move `timerSetup.py` out of the directory (you can do this anytime). 


## Usage
The general use cycle of this script would probably be something like this:
1. Write the first (working) iteration of your program.
2. Record the runtime on `runtimes.txt`.
3. Make some changes to your program and run.
4. Record the runtime on `runtimes.txt`.
5. Repeat steps 3-4.
6. See how much faster your program has gotten and how far you've come.....