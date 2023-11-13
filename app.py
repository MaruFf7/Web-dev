from flask import Flask, jsonify, render_template

app=Flask(__name__)
ITEMS=[
  {
  'id':1,
  'name':'Iphone 15 pro',
  'price':89000
  },
  {
  'id':2,
  'name':'Poco c55',
  'price':7760
  },
  {
    'id':3,
    'name':'Samsung s22'
  }
]
@app.route('/')
def hello_world():
    return render_template("home.html",items=ITEMS)


@app.route('/items')
def list_items() :
    return jsonify(ITEMS)
  
if __name__== '__main__':
   app.run(host='0.0.0.0',debug=True)