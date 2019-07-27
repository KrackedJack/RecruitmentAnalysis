import nltk
import pickle
import parsers as pr 
from gensim.models import Word2Vec

def train_model(corpus, model_name):
	model = Word2Vec(corpus, size=300, window=5, sg=1)
	model.save(model_name)
	return True

if __name__ == '__main__':
	files = pr.explore('corpus/tokenized/')
	tkns = [] 
	for file in files:
		with open(file, 'rb') as f:
			tkns.append(pickle.load(f))
	
	if(train_model(tkns, 'w2v_model')):	print("Model trained")



