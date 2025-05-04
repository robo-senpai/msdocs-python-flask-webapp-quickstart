from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/workout', methods=['GET', 'POST'])
def workout():
    if request.method == 'POST':
        name = request.form.get('exercise_name')
        minutes = min(int(request.form.get('duration', 0)), 60)  # limit to 60
        return render_template('workout.html', name=name, minutes=minutes)
    return render_template('workout.html', name="", minutes=0)
