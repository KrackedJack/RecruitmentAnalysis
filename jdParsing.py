import json 
from nltk.corpus import stopwords  
def python_dict_to_json_file(file_path):
            try:
                # Get a file object with write permission.
                file_object = open(file_path, 'a')
                # Save dict data into the JSON file.
                json.dump(data, file_object)
                print(file_path + " created. ")    
            except FileNotFoundError:
                print(file_path + " not found. ")       
#word_tokenize accepts a string as an input, not a file. 
stop_words = stopwords.words('english')
newstopwords=['ah','alas','dear','eh','er','God','hello', 'hullo','hey','hi','hmm','oh', 'o','ouch','uh',
'uh-huh','um','umm','well','wow','&','and/or','of','with','at','from','into','during','including','until','against','among',
'throughout','despite','towards','upon','concerning','to','in','for','on','by','about','like','through','over','before','between','after','since',
'without','under','within','along','following','across','behind','beyond','etc','etcetra','^[0-9]','gathering','identifying','analyzing','large','Services','Collaborate','create','solutions',
'areas','test','knowledge','MUST','hands-on','etc.);','must','ability','track','environment','Familiarity','one','popular','Candidate','self-motivated','detail-oriented','willing','learn',
'understanding','willing','Products','Applications','etc.']
stop_words.extend(newstopwords)
file1 = open("C:/Users/Abhinav/Desktop/Project/JD/sampleJD2.txt",'r') 
line = file1.read()# Use this to read file content as a stream: 
words = line.split() 
for r in words: 
    if not r in stop_words:
            data=dict(check = r)
            print(data)          
            if __name__ == '__main__':
                python_dict_to_json_file("C:/Users/Abhinav/Desktop/Project/JD/data2.json")
        
