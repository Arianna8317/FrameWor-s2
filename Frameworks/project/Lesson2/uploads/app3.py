from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.get('/news/')
def news():
    news = [
        {
            'title': 'Новый 2023 Год!',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'published_at': '01.01.2023'
        },
        {
            'title': 'C 8 Марта!',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'published_at': '08.03.2023'
        },
        {
            'title': 'C Днем Программиста!',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'published_at': '13.09.2023'
        },
    ]

    return render_template('news.html', news=news)

if __name__ == '__main__':
    app.run()