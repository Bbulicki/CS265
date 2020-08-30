#!/usr/bin/python3
#
#      id2.py  -  Convert list in file to sorted dictionary
#
# Brandin Bulicki
#
# Last Update: 4/6/18
#

import sys


#Make sure that there is a commandline arguement

if len(sys.argv) == 1 :
 
 for line in sys.stdin:
  print (line) 
  
else :
 
 filename = sys.argv
 idList = open( filename[1] , "r")
 ID={}
 for line in idList :
  data = line.strip().split()

#Make the name one object
  
  i = 1
  name = ""
  while i < len(data) :
   if name == "" :
    name = data[i]
   else :
    name = name + " "  + data[i]
   i += 1

#Puts the IDs and Name into a Dictionary  
  ID[ int( data[0] ) ] = name

#Sort the Dictionary
for key in sorted(ID.keys()) :
 print (key, ID[key])
 
   
#EOF 


