import os

def parse(file, i):
	if(file.split(".")[-1] == "doc"):
		return False
	import textract as tx 
	try:
		txt = tx.process(file).decode('utf-8')
		if (txt != ""):
			with open("corpus/op/"+str(i)+".txt", "w", encoding="utf-8") as op:
				op.write(txt)
		else:
			with open("err.txt", "a", encoding="utf-8") as op:
				op.write("Empty: " + file + "\n")		
		return True
	except:
		import traceback
		traceback.print_exc()
		with open("err.txt", "a", encoding="utf-8") as op:
			op.write("Failed: " + file + "\n")
		return False

def explore(dir = os.getcwd()):
	files = []
	formats = ["csv", "doc", "docx", "eml", "epub", "gif", "htm", "html", "jpeg", "jpg", "json", "log", "mp3", "msg", "odt", "ogg", "pdf", "pkl", "png", "pptx", "ps", "psv", "rtf", "tff", "tif", "tiff", "tsv", "txt", "wav", "xls", "xlsx"]

	for f in os.listdir(dir):
		if(os.path.isdir(os.path.join(dir, f)) and dir not in ["op", "corpus", "templates"] and dir[0] not in ["!", "_", "."]):
			files = files + explore(os.path.join(dir, f))
		elif(os.path.isfile(os.path.join(dir, f)) and f.split('.')[-1] in formats):
			files.append(os.path.join(dir, f))
	return files

def doc2x():
	import subprocess
	files = explore()
	for f in files:
		if(f.endswith(".doc")):
			subprocess.call(['soffice', '--headless', '--convert-to', 'docx', '--outdir', 'resumes/doc2', f])

if __name__ == '__main__':
 	print(explore(os.getcwd()))
