from flask import Flask, render_template, request

app=Flask(__name__)

# Route to display the Intro page
@app.route("/")
def home():
    return "Hello World"

if __name__ == '__main__':
	app.run(debug=True)
