from flask import Flask, request

app = Flask(__name__)

app.debug = True

@app.route('/')
def default():
   return 'Nothing to see here.'

@app.route('/match', methods = ['POST'])
def match():
   user = request.form['entity']
   print(user)
   return 'true'


if __name__ == '__main__':
   app.run()