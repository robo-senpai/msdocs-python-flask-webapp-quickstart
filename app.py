import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        if not name or not message:
            flash("All fields are required!", "danger")
            return redirect(url_for('contact'))
        flash(f"Thanks {name}, we received your message!", "success")
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
   app.run()
