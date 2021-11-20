from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<head>\
    <title>OpenAI</title>\
</head>\
<body>\
    <h2>This is the test page</h2>\
</body>'