from flask import Flask, render_template, url_for
app=Flask(__name__) # Intantiate Flask Object
# app.debug=True
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',info='Welcome to My Blog Page')

@app.route('/about')
def about():
    return '<h1>Welcome to My About Us Page!</h1>'

if __name__=='__main__':
    app.run(debug=True,port=80)