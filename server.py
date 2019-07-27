from flask import Flask, render_template
from forms import UploadJD
import parsers as pr
from run import run

def gg(dic):
	return {'abc':[1,2,3], 'xyz':2}

app = Flask("my app")
app.config['SECRET_KEY'] = 'ce3cbf5309689c6e3487c49e59a9addb'

@app.route('/', methods=['GET','POST'])
def upload():
	form = UploadJD()
	results = {}
	if form.validate_on_submit():
		results = run(form.jd.data, pr.explore('corpus/tokenized/'))
	return render_template("jd.html", form=form, results=results)

if __name__ == '__main__':
	app.run(debug=True)