from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    return 'hi'

@app.route('/change')
def change():
    return 'hello change'

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

@app.route('/html_file')
def html_file():
    return render_template('index.html')

@app.route('/variable')
def varialbe():
    name = '지밍'
    return render_template('variable.html', html_name=name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/cube/<int:num>/')
def cube(num):
    num = num
    sol = num*num*num
    return render_template('cube.html', html_sol = sol, num = num)
    
@app.route('/lunch')
def lunch():
    menu = {
        '20층A' : 'data:image/png;base64,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 \
        wd3wQgc0IcAAAAASUVORK5CYII=',
        '20층B': 'https://pbs.twimg.com/profile_images/2169981275/428292_350725884968137_332889450085114_1039389_179130573_n_400x400.jpg'
    }
    choiced_menu = random.choice(list(menu.keys()))
    return render_template('lunch.html', choice = choiced_menu, img = menu[choiced_menu])

@app.route('/movies')
def movies():
    movies = ['겨울왕국2', '쥬만지', '포드v페라리']
    return render_template('movies.html', movies = movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong', methods=['GET', 'POST'])
def pong():
    #keyword = request.args.get('keyword') #get방식
    keyword = request.form.get('keyword')
    # keyword
    return render_template('pong.html', keyword = keyword)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

if __name__ == '__main__':
    app.run(debug=True)