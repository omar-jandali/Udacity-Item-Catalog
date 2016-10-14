#The following is the very basic / minial version of a flask app#

#the following two lines of code will import the framwork and create an instance
#of the framework called app
from flash import flask
app = Flask(__name__)

# the following are wrap functions that are created by the Flask Framework

# if wither of the two routes are accessed, it will activate or trigger the HellowWOrld
# function that is defined below
@app.route('/')
@app.route('/hello')

def HelloWorld():
    return "Hello World"

#the following well set the server port
#the webserver will only run of the function is directly run from this application and not imported
if __name__ == '__main__':
    app.debug = True
    #initialize the server port to run, it is inly run from the local machine and nothing else
    #the following line also will reset the server every time there is a change in code
    app.run(host = '0.0.0.0', port = 5000)
