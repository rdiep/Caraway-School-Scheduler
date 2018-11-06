from flask import Flask, render_template, request, redirect, url_for

# import DB_Script.py

# app = Flask(__name__)
# @app.route("/")

# TO INSTALL FLASK:
# $ pip install Flask

# Flask example call to run on localhost:
# $ FLASK_APP=hello.py flask run
# * Running on http://localhost:5000/

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route('/main', methods=['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('adminpage.html', username=username, password=password)  # edited


@app.route('/admin-createaccount', methods=['GET', 'POST'])
def admincreateaccount():
    return render_template('admin-createaccount.html')


@app.route('/admin-editaccount', methods=['GET', 'POST'])
def admineditaccount():
    return render_template('admin-editaccount.html')


@app.route('/admin-statistics', methods=['GET', 'POST'])
def adminstatistics():
    return render_template('admin-statistics.html')


@app.route('/admin-schedule', methods=['GET', 'POST'])
def adminschedule():
    return render_template('admin-schedule.html')


# Teacher Home
@app.route('/teacherpage', methods=['GET', 'POST'])
def teacherhome():
    return render_template('teacherpage.html')


# Teacher Blue Room
@app.route('/teacher-blueroom', methods=['GET', 'POST'])
def teacherblueroom():
    return render_template('teacher-blueroom.html')


# Teacher Purple Room
@app.route('/teacher-purpleroom', methods=['GET', 'POST'])
def teacherpurpleroom():
    return render_template('teacher-purpleroom.html')


# Teacher Green Room
@app.route('/teacher-greenroom', methods=['GET', 'POST'])
def teachergreenroom():
    return render_template('teacher-greenroom.html')


# Teacher Red Room
@app.route('/teacher-redroom', methods=['GET', 'POST'])
def teacherredroom():
    return render_template('teacher-redroom.html')


# Teacher Grey Room
@app.route('/teacher-greyroom', methods=['GET', 'POST'])
def teachergreyroom():
    return render_template('teacher-greyroom.html')


# Family Home
@app.route('/familypage', methods=['GET', 'POST'])
def familyhome():
    return render_template('familypage.html')


# Family Account Info
@app.route('/family-accountinfo', methods=['GET', 'POST'])
def familyaccountinfo():
    return render_template('family-accountinfo.html')


# Family Schedule
@app.route('/family-schedule', methods=['GET', 'POST'])
def familyschedule():
    return render_template('family-schedule.html')


if __name__ == "__main__":
    app.run()
