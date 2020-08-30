#!/bin/bash
#
# BRANDIN BULICKI
# 4.20.18
#
#
# PLATFORM:
#
# EDITOR: tabstop=3, Cols=80
#

# Take in the filenames of each of the regular files in the working directory
# Prints the Filename, # of Lines, # of words to stdout

for file in *
 do
  if [ -f "$file" ] #if the file is a regular file
   then
    echo -n "$file"  #output the filename 
     wc -lw < "$file" #output the wc
  fi
done

exit 0
#EOP

#Referenced "Linux in a nutshell"
