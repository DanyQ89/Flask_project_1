from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
