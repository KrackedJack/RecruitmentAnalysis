import json 
import pandas as pd
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
def python_dict_to_json_file(file_path):
            try:
                # Get a file object with append permission.
                file_object = open(file_path, 'a')
                # Save dict data into the JSON file.
                json.dump(data, file_object)
                print(file_path + " created. ")    
            except FileNotFoundError:
                print(file_path + " not found. ")  
stop_words = set(stopwords.words('english')) 
file1 = open("C:/Users/Abhinav/Desktop/Project/JD/sampleJD.txt",'r') 
line = file1.read()# Use this to read file content as a stream: 
words = line.split() 
for r in words: 
    if not r in stop_words:
            data=dict(check = r)
            print(data)          
            if __name__ == '__main__':
                python_dict_to_json_file("C:/Users/Abhinav/Desktop/Project/JD/data.json")
        
