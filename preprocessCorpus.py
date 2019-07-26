import os 
import nltk
import pandas as pd
import parsers as pr
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pickle as pkl

corpus_dir = 'corpus/'
txt_dir = 'op/'
tkn_dir = 'tokenized/'

def prepare_corpus():
	df = pd.read_csv('db.csv')
	df.set_index('cid')
	files = pr.explore(corpus_dir + txt_dir)
	print("Files: {}".format(len(files)))

	i = 0
	tkns = []
	cid = []

	for file in files:
		with open(file, 'r') as f:
			content = f.read()
			content = nltk.word_tokenize(content)
			content = [PorterStemmer().stem(word) for word in content if word not in stopwords.words('english') and word.isalnum()]
			with open(corpus_dir + tkn_dir + file.split('/')[-1].split('.')[0] + '.pkl', 'wb') as pfile:
				pkl.dump(content, pfile)
			
			tkns.append(corpus_dir + tkn_dir + file.split('/')[-1].split('.')[0] + '.pkl')
			cid.append(file.split('/')[-1].split('.')[0])

			print("{}. {} - {}".format(i, cid[-1], tkns[-1]))
			i = i + 1
	df2 = pd.DataFrame({'cid':cid, 'tokens':tkns})
	df2.set_index('cid')
	df.join(df2, on='cid')
	df.to_csv('db2.csv')

if __name__ == '__main__':
	prepare_corpus()