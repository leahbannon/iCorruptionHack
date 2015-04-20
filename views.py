from app import app
from models import File, Contribution

@app.route('/')
def summary():
    text = '<h1>Database Summary</h1>\n'
    file1 = File.get(id=1)
    file2 = File.get(id=2)
    file3 = File.get(id=3)

    text += '<h2>' + file1.name + '</h2>\n'
    text += '<h2>' + file2.name + '</h2>\n'
    text += '<h2>' + file3.name + '</h2>\n'

    return text
