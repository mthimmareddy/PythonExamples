import re

pattren=r"manju"

pat2=r"(([\w]+)@([\w]+)\.([\w]+))"

match=re.match(pat2,"manju@gmail.com")
if match:
	print (match.group(0))
else:
	print ("Gmail not found")

if re.match(pattren,"manju"):
  print ("matched")
else:
  print ("No match Found") 

pat1=r"^m...u$"

if re.match(pat1,"manju"):
  print ("Manju found")
if re.match(pat1,"mghtu"):
  print("Pattern found")   

