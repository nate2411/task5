from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def shopping():
    return render_template('shopping.html')

@app.route('/showiterms', methods=['POST', 'GET'])
def showiterms():
    if request.method == 'POST':
        result = request.form
        return render_template('showitems.html', result=result)

    if __name__ == '__main__':
        app.debug = True
        app.run()

