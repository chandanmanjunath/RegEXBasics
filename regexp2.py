#search function is imported from re module
import re

line='Cats are smarter than dogs'

matchObj=re.search(r'(.*) are (.*?) (.*?) .*',line,re.I|re.M)

if matchObj:
     print "group()",matchObj.group()
     print "group(1)",matchObj.group(1)
     print "group(2)",matchObj.group(2)
     print "group(3)",matchObj.group(3)
     print "groups",matchObj.groups()

else:
    print "no match found"
