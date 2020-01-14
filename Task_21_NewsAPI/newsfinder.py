from newsapi import NewsApiClient
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
YOUR_API_HERE = input("Enter your API key here: ")
newsapi = NewsApiClient(api_key=YOUR_API_HERE)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        results = newsapi.get_everything(q='linux', page_size=10)
        results_1 = newsapi.get_everything(q='open source', page_size=10)
        results_2 = newsapi.get_everything(q='android', page_size=10)
        results = results['articles'] + results_1['articles'] + results_2['articles']
        results.sort(key=lambda date: datetime.strptime(date['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'), reverse=True)
        return render_template("index.html", results=results)
    else:
        query = request.form['query']
        results = newsapi.get_everything(q=query, page_size=10)
        return render_template("index.html", results=results['articles'])


if __name__ == "__main__":
    app.run(debug=True)