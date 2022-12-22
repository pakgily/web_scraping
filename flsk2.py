from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('flsk2.html',user="반원",data={'level':60,'point':360,'exp':45000})
if __name__ == '__main__':
    app.run(debug=True)