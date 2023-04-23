from flask import *
from database import*

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/home")
def index():
	return render_template("index.html")

@app.route('/signin', methods=['GET','POST'])
def signin(): 
    if request.method == 'POST':
        prn = request.form["prn"]
        print(prn)
        pwd=request.form["pwd"]
        print(pwd)
        x=loginchecker(prn,pwd)
        if x is True:
            return profile()
        else:
            return render_template("signin.html") 
    return render_template('signin.html')  


@app.route("/profile",methods=['GET','POST']) 
def profile(): 
    request.method == 'POST'
    prn = request.form["prn"]
    name(prn)
    
    return render_template("profile.html")



if __name__ == '__main__':
	app.run(debug=True,port=1000)
