from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("survey.html")

@app.route("/result", methods = ['POST'])
def processForm():
    print(request.form)
    nameFromForm = request.form['name']
    locationFromForm = request.form['location']
    languageFromForm = request.form['language']
    commentFromForm = request.form['message']
    return render_template("surveyResults.html", nameTemplate = nameFromForm, locationTemplate = locationFromForm, languageTemplate = languageFromForm, commentTemplate = commentFromForm)

if __name__=="__main__":
    app.run(debug=True)