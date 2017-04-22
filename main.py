from flask import Flask, request, session, render_template

app = Flask(__name__)
app.config.from_object(__name__)

#When page is visited with just / route this
#code is executed
#Example localhost:5000/, 127.0.0.1/5000
@app.route('/', methods = ['GET', 'POST'])
def serve_page():
    print("someone visted / route")
    return render_template('index.html')

# When page is visited with /page2 route thus
#code is executed
#Example localhost:5000/page2, 127.0.0.1/5000/page2
@app.route('/page2', methods = ['GET', 'POST'])
def servepage2():
    print("someone visited /page2 route")
    return("someone visited /page2 route")


#Running on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)



