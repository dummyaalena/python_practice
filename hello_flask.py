from flask import Flask

app = Flask(__name__)

@app.route('/hello' , defaults={'name' : 'Welcome to Flask'})
@app.route('/hello/<name>')
def hello(name):
    return 'Hello, World %s' % name

@app.route('/introute/<int:mynum>')
def introute(mynum):
    return 'The number is: ' + str(mynum)

@app.route('/combineroute/<string:mystring>/<int:myint>')
def combineroute(mystring, myint):
    return 'The string value is: ' + mystring + 'the int value is ' + str(myint)

@app.route('/pathroute/<path:mypath>')
def pathroute(mypath):
    return 'The path is: ' + mypath

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    
if __name__ == "__main__":
    app.run(debug=True)
