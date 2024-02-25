from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')

words_to_promote = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                    'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '</br>'.join(
        'Человечество вырастает из детства.  Человечеству мала одна планета.  Мы сделаем обитаемыми безжизненные пока '
        'планеты.  И начнем с Марса!  Присоединяйся!'.split(
            '  '))


@app.route('/image_mars')
def image_mars():
    return render_template('index.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('index_css.html')


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    return render_template('anketa_for_astr.html')


@app.route('/choice/<username>')
def choice(username):
    return render_template('index_choice.html', username=username)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('index_results.html', nickname=nickname, level=level, rating=rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        print(1)
        file = request.files['filename']
        return render_template('index_load_photo.html', filename=f'static/img/{file.filename}')
    elif request.method == 'GET':
        return render_template('index_load_photo.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
