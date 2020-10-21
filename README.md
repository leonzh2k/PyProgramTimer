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

1. Download `timerSetup.py`. 
2. Create an empty directory that you wish to develop your program in. 
3. Move `timerSetup.py` into the directory, and execute it ONLY ONCE.
4. You will see three new files:
    *  `name.py` is the file where you will develop your program. You can rename this whatever you like.
    *  `runtimes.txt` keeps track of runtimes. You probably shouldn't edit this.
    *  `numruns.txt` is used to keep track of how many runs have been logged to `runtimes.txt`. You probably shouldn't edit this either.
4. Delete or move `timerSetup.py` out of the directory (you can reuse it for other programs). If you don't do this, you may accidentally run it again and run the risk of overwriting important data; fortunately there is a safeguard against that. 
5. Develop your program.


## Usage
The general use cycle of this script would probably be something like this:
1. Write the first (working) iteration of your program.
2. Record the runtime on `runtimes.txt`.
3. Make some changes to your program and run.
4. Record the runtime on `runtimes.txt`.
5. Repeat steps 3-4.
6. See how much faster your program has gotten and how far you've come.....

## Todo
* Figure out how to format runtime to specify less decimal places
* Create `compareRunTimes.py` that allows you to compare runtimes
* 

## Status
Ongoing?

## Bugs


