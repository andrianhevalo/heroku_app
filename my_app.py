from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


# allow both GET and POST requests
@app.route('/classify-text', methods=['GET', 'POST'])
def classify_text():
    # this block is only entered when the form is submitted
    if request.method == 'POST':
        try:
            usertex = request.form.get('message')
            # loading trained model
            filename = 'logistic_regression.sav'
            loaded_model = pickle.load(open(filename, 'rb'))
            # classifying text
            classified_category = loaded_model.predict([usertex])
            results = {'category': classified_category[0], 'text': usertex, }
            return jsonify(results)
        except Exception:
            return "Something went wrong"

    return '''<form method="POST">
                      Message: <input type="text" name="message"><br>
                      <input type="submit" value="Submit"><br>
                  </form>'''


if __name__ == '__main__':
    app.run(debug=True)
