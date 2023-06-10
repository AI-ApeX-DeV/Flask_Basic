from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = request.form['science']
        maths = request.form['maths']
        english = request.form['english']
        total_score = int(science) + int(maths) + int(english)
        res = ""
        if (total_score < 50):
            res = "fail"
        else:
            res = "success"
        dict = {'science': science, 'maths': maths, 'english': english,
                'total_score': total_score, 'result': res}
    return render_template('result.html', dicct=dict)


@app.route('/success/<int:score>')
def success(score):
    return render_template('success.html', marks=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('fail.html', marks=score)


@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result, score=marks))


@app.route('/result/<int:marks>')
def result(marks):
    return render_template('result.html', marks=marks)


if __name__ == '__main__':
    app.run(debug=True)
