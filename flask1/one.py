from flask import Flask

app = Flask(__name__)


#@app.route("/")
def sayHello():
    return("<h1>Hello<h1>")

def sayBye():
    return("<h2>Bye</h2>")

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

app.add_url_rule("/", view_func=sayHello)
app.add_url_rule("/bye", view_func=sayBye)

if __name__ == '__main__':
    app.run()
