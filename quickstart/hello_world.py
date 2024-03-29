from flask import Flask, escape
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return 'Hello, World!\n こんにちは世界！'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    '''
    /projects -> converted as /projects/
    '''
    return 'The project page'


@app.route('/about')
def about():
    '''
    /about/ -> Not Found!
    '''
    return 'The about page'
