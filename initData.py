import os
import docx as dx
import parsers as pr

i = 0
files = pr.explore(os.getcwd())
print(files)
for f in files:
	if (f.split(".")[-1] in ["docx","doc"]):
		if(pr.parse_docx(f, i) == 1):
			i += 1