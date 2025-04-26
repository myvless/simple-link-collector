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
        # 添加链接格式验证：必须以 http:// 或 https:// 开头
        if link and (link.startswith('http://') or link.startswith('https://')):
            save_link(link)
        # 可选：如果格式错误，可以记录或忽略（当前仅忽略）
    links = read_links()
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)