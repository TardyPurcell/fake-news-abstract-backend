from flask import Flask
from flask_cors import CORS
from textrank4zh import TextRank4Sentence


app = Flask(__name__)
CORS(app, resources=r'/api/*')


@app.route('/api/<text>')
def work(text):

    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source="all_filters")

    return {"content": "".join([x.sentence + '。' for x in sorted(tr4s.get_key_sentences(num=10), key=lambda x: x.index)])}


if __name__ == '__main__':
    app.run(debug=True)
