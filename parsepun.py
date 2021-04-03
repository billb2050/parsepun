#!/usr/bin/env python3
"""
This Python 3 CLI program reads the local Hercules punch file 
from MVS, and extracts the output from the IBM utility IEBPTPCH
This output is placed in a subdirectory of the Hercules pch 
subdirectory so as to not clutter it up!

IEBPTPCH provides a way to punch data from an MVS PDS to the Hercules
punch subdirectory.

If the punch data starts with MEMBER NAME assume, there are 
multiple members from a PDS, otherwise assume it’s a single member

You may want to do a “devinit 00d” before running punch jobs!

The following are the local punch files I saw created on the day 
I wrote this:
pch00d.txt
pch10d.txt

  By: Bill Blasingim
  On: 03/31/2021

"""
import os, string, time
cr=chr(13)	# Carriage return
lf=chr(10)	# Line Feed
crlf=cr+lf
nl="\n"	# New line
start=True
end=False
endCnt=0
lastLine=0
firstLine=1
jobs = {}
#tmpFil=subdir+"tmp"+str(int(time.time()))+".txt"
tmpFil="tmp"+str(int(time.time()))+".txt" #create temp workfile
fo = open(tmpFil, "w")
CUUs=['00d','10d']

for cuu in CUUs:
  start=True
  end=False      
  FILEIN = "pch"+cuu+".txt"
  print("\nReading "+FILEIN)
  alpha='A'
  if FILEIN[5:6]=='f':
    alpha='Z'

  try:
    fi = open(FILEIN, "r", encoding = "ISO-8859-1")
  except IOError:
    print("File "+FILEIN+" does not exist!")
    continue    
  # Create "jobs" subdirectory if it doesn't exist
  subdir="pch"+"-"+cuu+"/"
  if not os.path.exists(subdir):
      os.makedirs(subdir)
  else:
      # Delete existing files!
      directory_path = os.getcwd()
      files = os.listdir(subdir)
      for fil in files:
            delMe=directory_path+"/"+subdir+fil
            os.remove(delMe)

  ln=0
  filCnt=0
  memberName=""
  while 1:
    line = fi.readline()
    if not line: break
    ln=ln+1
    LineOut=line[:]

    if LineOut[:12]=="MEMBER NAME ":
      memberName=LineOut[13:-1]
      fo.close()
      if os.path.exists(subdir+memberName):
        print(memberName+" exists!")
      fo = open(subdir+memberName, "w")
      filCnt+=1
      continue

    if memberName=="":
      if LineOut[:2]=="//":
          memberName=LineOut[2:10]
          fo = open(subdir+"SingleMember.TXT", "w")          

    fo.write(LineOut)

  print(str(ln) + " lines read.")
  print(str(filCnt) + " Jobs written.")

os.remove(tmpFil)      # Remove last temp file
fi.close()
fo.close()
