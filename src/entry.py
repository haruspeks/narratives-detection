import sys

from flask import Flask, request
from matchMaker import MatchMaker 
from entityExtractor import EntityExtractor 
from data import Data 
from chatGPT import ChatGPT 

app = Flask(__name__)

data = Data()
matchMaker = MatchMaker()
entityExtractor = EntityExtractor()
chatGPT = ChatGPT()

@app.route('/', methods = ['POST'])
def default():
   print('post called')
   data.get('id')

   # text = request.form['entities']
   result = chatGPT.analyse('text')
   # result = chatGPT.create_embeddings()
   # clean_entities = entityExtractor.extract_entity_ids(text)

   # clean_entities = set([entity.strip() for entity in entities.split(',')])
   # print(clean_entities)

   return result

@app.route('/shutdown')
def shutdown():
    sys.exit()
    os.exit(0)
    return


if __name__ == '__main__':
   app.run(debug = True, port = 8080)