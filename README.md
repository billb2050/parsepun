  This Python 3 CLI program reads the local Hercules punch file 
  from MVS, and extracts the output from the IBM utility IEBPTPCH
  This output is placed in a subdirectory of the Hercules pch subdirectory so as to not clutter it up!

  IEBPTPCH provides a way to punch data from an MVS PDS to the Hercules punch subdirectory.

  If the punch data starts with MEMBER NAME assume, there are 
  multiple members from a PDS, otherwise assume it's a single member

  You may want to do a "devinit 00d" before running punch jobs!

  The following are the local punch files I saw created on the day 
  I wrote this:
  pch00d.txt
  pch10d.txt

