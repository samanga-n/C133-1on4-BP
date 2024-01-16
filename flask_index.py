from flask import Flask, render_template
app = Flask(__name__)
#in the function return render_template(‘index.html’)
@app.route("/")
def first_flask():
    #Create a variable
    name = ''
    # Pass the variable in the template
    return render_template('index.html', )
app.run(debug=True)



