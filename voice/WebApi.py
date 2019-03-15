from flask import Flask, request,render_template
import predict as pt
import Client as socketclient
app = Flask(__name__)


# Blank、Unkonw、“yes”、“no”、“up”、“down”、“left”、“right”、“on”、“off”、“stop”或“go”。

@app.route('/voice', methods={'POST', 'GET'})
def start():
    name = request.args.get('name')
    print(name)
    path = '/Users/wangjinhu/Downloads/' + name
    result=pt.predict(path)
    """Send message to c platform"""
    # socketclient.sendMessages(result)
    return result


@app.route('/index')
def index():
    return render_template('mavvoice.html')


if __name__ == '__main__':
    app.run()
