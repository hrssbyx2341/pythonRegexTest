import re
key = r"<html><body><h1>hello world<h1></body></html>"
p1 = r"(?<=<h1>).+?(?=<h1>)"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,key)
if matcher1 == None:
    print("None");
else:
    for string in (pattern1.findall(key)):
        print(string)

key = "saas saaas saaaaas saaaas "
p1 = "sa{1,4}s" ''' "sa{1,1}s" "sa{1,2}s" "sa{1,3}s" "sa{1,4}s"  "sa{1,5}s"'''
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,key)
if matcher1 == None:
    print("None");
else:
    for string in (pattern1.findall(key)):
        print(string)
