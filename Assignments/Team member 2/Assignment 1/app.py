from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
@app.route('/register')
def registrationpage():
    return render_template('register.html')

@app.route("/success",methods=['POST','GET'])
def success():
      if request.method=='POST':
            l=request.form.get('username')
            m=request.form.get('email')
            n=request.form.get('phonenumber')
            return render_template('success.html',username=l,email=m,phonenumber=n)

if __name__ == "__main__":
    app.run(debug = True)