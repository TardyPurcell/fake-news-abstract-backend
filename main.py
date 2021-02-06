from flask import Flask
from textrank4zh import TextRank4Sentence


app = Flask(__name__)


@app.route('/api/<text>')
def work(text):

    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source="all_filters")

    return {"content": "".join([x.sentence + '。' for x in sorted(tr4s.get_key_sentences(num=10), key=lambda x: x.index)])}


if __name__ == '__main__':
    app.run()
