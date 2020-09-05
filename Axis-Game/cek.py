import re

with open('3.dis') as f:
	string = re.findall(r"LOAD_CONST.*?\('(.*?)'\)",f.read())[:-1]
	print ''.join(chr(len(i)) for i in string)
