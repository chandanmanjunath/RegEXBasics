import re

#sub(regexp,replace_string,target_string,number of occurences)
line1="34372395252952965739 # phone numbers"

line1=re.sub(r'#.*$',"",line1)

print "string with  number %s" % (line1)

line1="34372395252952965739 # phone numbers"

line1=re.sub(r'[0-9]*',"",line1)
print "string with no number %s" % (line1)
