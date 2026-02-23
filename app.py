from flask import Flask, render_template

app = Flask(__name__)

# Наши статьи (пока 3 для теста)
articles = [
    {
        'id': 1,
        'title': 'Нейропластичность: как менять мозг',
        'category': 'Нейробиология',
        'content': 'Нейропластичность — это способность мозга менять свою структуру... Полный текст статьи про нейропластичность здесь.'
    },
    {
        'id': 2,
        'title': 'Дофаминовое голодание',
        'category': 'Привычки',
        'content': 'Дофамин — это нейромедиатор мотивации... Полный текст про дофамин.'
    },
    {
        'id': 3,
        'title': '5 минут медитации в день',
        'category': 'Менталка',
        'content': 'Медитация меняет структуру мозга за 8 недель... Полный текст про медитацию.'
    }
]

@app.route('/')
def index():
    """Главная страница с разделами"""
    return render_template('index.html')

@app.route('/library')
def library():
    """Страница со списком статей"""
    return render_template('library.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    """Страница отдельной статьи"""
    # Ищем статью по id
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return render_template('article.html', article=article)
    return "Статья не найдена", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
