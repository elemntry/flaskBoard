from flask import Flask, render_template, request, url_for, flash, redirect
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'


@app.route('/')
def index():
    if 'ads' in session:
        print('ads in session')
    else:
        print('ads not in session')
        session['ads'] = [{'title': 'ssss1'},
                          {'title': 'ssss2'}]
    print(session.get('ads'))
    return render_template('index.html', ads=session.get('ads'))


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        ad = request.form['addad']
        if not ad:
            flash('Заполните поле ввода!')
        else:

            session['ads'].append({'title': ad})
            session.modified = True
            print('session append')
            print(session.get('ads'))
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/remove/<num>')
def remove(num):
    session['ads'].pop(int(num) - 1)
    session.modified = True
    print(session.get('ads'))
    return redirect(url_for('index'))
