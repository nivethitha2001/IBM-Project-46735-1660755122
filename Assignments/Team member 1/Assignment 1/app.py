from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/register')
def registrationpage():
    return render_template('register.html')

@app.route("/success",methods=['POST'])
def success():
       return render_template('success.html')

if __name__ == "__main__":
    app.run(debug = True)