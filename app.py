# import the Flask class from the flask module
from flask import Flask, render_template, request, redirect
import run
import subprocess

# create the application object
app = Flask(__name__)

def run_script():
		return subprocess.check_output(["python", "run.py", "cybercorpus.txt"])

# use decorators to link the function to a url
@app.route('/')
def index():
    return render_template('welcome.html')  # render a template
    #return render_template('welcome.html')  # render a template

@app.route('/form', methods=['POST'])
def form():
	#para = request.form['paragraphs']

	x = 0
	dicty = {}

	a = run_script()
	b = run_script()
	c = run_script()
	d = run_script()

	a = a.rstrip('\n')
	b = b.rstrip('\n')
	c = c.rstrip('\n')
	d = d.rstrip('\n')

	if '(' in a:
		print(a)

	four_sent = a + ' ' + b + ' ' + c + ' ' + d
    	
    #return render_template('welcome.html', subprocess_output_a=a, subprocess_output_b=b, subprocess_output_c=c, subprocess_output_d=d)
	return render_template('welcome.html', subprocess_output_all=four_sent)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)