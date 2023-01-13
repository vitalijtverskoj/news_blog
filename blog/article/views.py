from flask import Blueprint, render_template, redirect

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


@article.route('/', endpoint='list')
def article_list():

    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('/<int:pk>', endpoint="details")
def get_article(pk: int):
    try:
        art_name = ARTICLES[pk]['title']
        art_text = ARTICLES[pk]['text']
        art_author = ARTICLES[pk]['author']['name']
    except KeyError:
        # raise NotFound(f'User id {pk} not found')
        return redirect('/articles/')
    return render_template(
        'articles/details.html',
        art_name=art_name,
        art_text=art_text,
        art_author=art_author,
        pk=pk,
    )
