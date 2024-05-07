from flask import Flask, render_template, request, redirect
import os
from flask import send_from_directory 

app = Flask(__name__, static_url_path='')
def root():
    return app.send_static_file('index.html')
# Define a list of user objects (for demonstration purposes only)
users = [
  {'id': 1, 'username': 'John'},
  {'id': 2, 'username': 'Bob'},
  {'id': 3, 'username': 'Charlie'}
]
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/users/create', methods=['POST'])
def create_user():
    username = request.form['username']
    # Assign the next available user ID
    user_id = max(user['id'] for user in users) + 1 if users else 1
    new_user = {'id': user_id, 'username': username}
    users.append(new_user)
    # Redirect the user back to the index page
    return redirect('/')

@app.route('/users/delete', methods=['POST'])
def delete_user():
    user_id = int(request.form['user_id'])
    # Find the user with the given ID and remove it from the list of users
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            break
    # Redirect the user back to the index page
    return redirect('/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5010)