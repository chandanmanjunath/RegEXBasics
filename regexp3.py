#search function is imported from re module
import re

line='Cats are smarter than dogs'

matchObj1=re.search(r'dogs',line,re.I|re.M)
matchObj2=re.match(r'dogs',line,re.I|re.M)

if matchObj1:
     print "group()",matchObj1.group()
else:
    print "no match found for matchObj1"

if matchObj2:   
     print "group()",matchObj2.group()
else:
    print "no match found for matchObj2"
