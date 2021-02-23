from flask import Flask, request
from textrank4zh import TextRank4Sentence
import json


app = Flask(__name__)


@app.route('/api/abstract', methods=['GET', 'POST'])
def abstract():
    if request.method == 'POST':
        text = json.loads(request.data)['content']
        num = json.loads(request.data)['num']

        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source="all_filters")

        return {"content": "".join([x.sentence + '。' for x in sorted(tr4s.get_key_sentences(num=int(num)), key=lambda x: x.index)])}
    elif request.method == 'GET':
        pass


if __name__ == '__main__':
    app.run()
