from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

@app.route('/')
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=NBx9UYnutMTyDhg7i4hc8V6S2yU0wcDaLVwUZZBo")
    d = json.loads(u.read())
    return render_template('base.html', title = d['title'], image = d['url'], explanation = d['explanation'])

if __name__ == '__main__':
    app.debug = True
    app.run()
