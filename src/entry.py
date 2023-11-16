import sys

from flask import Flask, request
from matchMaker import MatchMaker 
from entityExtractor import EntityExtractor 

app = Flask(__name__)

matchMaker = MatchMaker()
entityExtractor = EntityExtractor()

@app.route('/', methods = ['POST'])
def default():
   print('post called')
   text = request.form['entities']
   entities = entityExtractor.extract(text)

   clean_entities = set([entity.strip() for entity in entities.split(',')])
   # print(clean_entities)

   return matchMaker.match(clean_entities)

@app.route('/shutdown')
def shutdown():
    sys.exit()
    os.exit(0)
    return


if __name__ == '__main__':
   app.run(debug = True, port = 8080)