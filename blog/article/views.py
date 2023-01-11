from flask import Blueprint, render_template

article = Blueprint('article', __name__, url_prefix='/article', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'article_1',
        'text': 'article_1 text',
        'author': {
            'name': 'Alice',
            'id': 1,
        }
    },
    2: {
        'title': 'article_2',
        'text': 'article_2 text',
        'author': {
            'name': 'Jon',
            'id': 2
        }
    },
    3: {
        'title': 'article_3',
        'text': 'article_3 text',
        'author': {
            'name': 'Mike',
            'id': 3,
        }
    },
}


@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)
