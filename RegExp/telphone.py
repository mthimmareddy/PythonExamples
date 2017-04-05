import re

#pat1=r"( ((\+)?1)? ((\s)+)?  (\((\d){3}\)) ((-|\s)?)  (\((\d){3}\))  ((-|\s)?) (\d){4} )"
pat1=r"(((\+)?1)?((\s)+)?(\(?(\d){3})\)?((-|\s)?)(\(?(\d){3})\)?((-|\s)?)(\d){4})"

pat=r"\+12623665056"

match=re.match(pat1,"+12623665056")
if match:
 print (match.groups())

match=re.match(pat1,"+1 262 366 5056")
if match:
 print ("found 1")


match=re.match(pat1,"+1 (262)(366) 5056")
if match:
 print ("found 2")

match=re.match(pat1,"+1 262-366-5056")
if match:
 print ("found 3")


