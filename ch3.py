from flask import Flask, make_response, request, render_template
from flask_script import Manager  #p17
from flask_bootstrap import Bootstrap #p26

app = Flask(__name__)
manager = Manager(app)  #p17
bootstrap = Bootstrap(app) #p26

@app.route('/')
def index():
    return render_template('index.html')

# Example of reading dynamic content (values) from the URL path
@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', user=name)


# Example of using a Jinja2 filter to show the provided numerical value as 'human readable' sizes
# See more filters here: http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters
@app.route('/file/<int:size>')
def file(size):
    return render_template('file_info.html', size=size)

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

# Example of setting up a custom 404 route
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    #app.run(debug=True)  #p17
    manager.run()
