from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

@app.route('/')
def root():
    '''u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=NBx9UYnutMTyDhg7i4hc8V6S2yU0wcDaLVwUZZBo")
    dic = json.loads(u.read())
    title = dic['title']
    image = dic['url']
    explanation = dic['explanation']'''

    ch = urllib2.urlopen("https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.labs.whatWouldMicahSay&access_token=&format=json")
    dic = json.loads(ch.read())
    micah = dic['micah']
    stat = dic['stat']
    
    #return render_template('base.html', title = title, image = image, explanation=explanation)
    return render_template('base.html', micah = micah, stat = stat)



if __name__ == '__main__':
    app.debug = True
    app.run()
