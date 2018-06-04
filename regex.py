import re
key = r"<html><body><h1>hello world<h1></body></html>"
p1 = r"(?<=<h1>).+?(?=<h1>)"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,key)
print(matcher1.group(0))
