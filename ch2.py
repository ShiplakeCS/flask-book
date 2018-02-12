from flask import Flask, make_response, request
from flask_script import Manager  #p17

app = Flask(__name__)
manager = Manager(app)  #p17

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

# Example of reading dynamic content (values) from the URL path
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name.title())


# Example of setting a cookie value in the response object
@app.route('/cookie/<text>')
def cookie(text):
    response = make_response("<p>This response contains a cookie. Inspect it to find out its value!</p>")
    response.set_cookie('cookie_text', text)
    return response

# Example of reading a cookie value and using it
@app.route('/cookie/')
def cookie_base():
    cookie_val = request.cookies['cookie_text']
    return 'The cookie value is {}'.format(cookie_val)



if __name__ == '__main__':
    #app.run(debug=True)  #p17
    manager.run()
