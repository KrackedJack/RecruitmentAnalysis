import os
import textract as tx
import parsers as pr

i = 0
files = pr.explore(os.getcwd())
for f in files:
	if(pr.parse(f, i) == 1): i += 1
