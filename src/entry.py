import sys

from flask import Flask, request
from matchMaker import MatchMaker 

app = Flask(__name__)

# app.debug = True
# 

matchMaker = MatchMaker()

@app.route('/', methods = ['POST'])
def default():
   print('post called')
   entities = request.form['entities']
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