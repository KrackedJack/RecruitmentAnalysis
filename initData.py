import os
import textract as tx
import parsers as pr
import pandas as pd

def to_txt():
	i = 0
	files = pr.explore('resumes/')
	cv = []
	cv_txt = []
	cv_id = []
	for f in files:
		if(pr.parse(f, i) == 1): 
			i += 1
			cv_id.append(i)
			cv.append(f)
			cv_txt.append('corpus/op/' + str(i) + '.txt')

	d = {'cid':cv_id, 'cv':cv, 'txt':cv_txt}
	df = pd.DataFrame(d)
	df.set_index('cid')
	print(df)
	df.to_csv('db.csv')

if __name__ == '__main__':
	import parsers as pr
	pr.doc2x()
	to_txt()
