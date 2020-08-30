#!/usr/bin/python3
#
#      s1.py  -  Average Student test Grades
#
# Brandin Bulicki
#
# Last update: 4/6/18
#

import sys

#Make sure that there is a commandline argument

if len(sys.argv) == 1 :
 print( "Please enter an argument" )
else :
 
 filename = sys.argv
 students = open( "students" , "r")
 f = open( filename[1], "w") 

 for line in students :
  data = line.strip().split()

#compute average of all scored for student
  i = 1
  average = 0
  score = 0

  while i < len(data) :
   score = score + int(data[i])
   i += 1
  
  
  average = score / (i - 1 )
  average = "%.2f" % round(average, 2)

#Prints 2 columns (The name and The average)
#Puts outpu into file named from commandline arg.

  print(data[0] + " " + str(average), file=f)

#EOF


