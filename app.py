from flask import Flask, request, render_template

app = Flask(__name__)

def read_links():
    try:
        with open('links.txt', 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_link(link):
    with open('links.txt', 'a') as file:
        file.write(link + '\n')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        if link:
            save_link(link)
    links = read_links()
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)