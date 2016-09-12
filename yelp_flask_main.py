# b1u3c1ph3r's Final Project for One Month Python

from flask import Flask, render_template, request
import os
import yelp_api_script

app = Flask(__name__)

@app.route("/")
def index():
    location = request.values.get('location')
    search_term = request.values.get('search_term')
    suggestions = []
    if location and search_term:
        suggestions = yelp_api_script.get_business_list(search_term, location)
    return render_template('index.html', location=location, search_term=search_term, suggestions=suggestions)

@app.route("/about.html")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

