from flask import Flask, render_template, request, jsonify
import extracting as ext

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
    ans = ext.check_web(search_word)
    return jsonify(ans)

if __name__ == "__main__":
    app.run(debug=True)