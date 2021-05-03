from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, static_folder='../static', url_prefix='/article')

ARTICLES = [
    {
        'id': 1,
        'title': 'Lorem ipsum dolor sit amet.',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aliquid doloremque doloribus dolorum '
                'expedita facere harum id ipsam nam nihil non perferendis possimus repellendus saepe sed tempora ut, '
                'vel velit. Alias architecto culpa, cum ducimus eveniet iste maiores modi? Accusamus aperiam aut '
                'autem earum fugit, illo, laborum nesciunt optio pariatur quisquam quo rerum totam? Consectetur '
                'corporis deleniti dignissimos ea eveniet expedita incidunt libero maxime minima, nesciunt, '
                'nulla provident quaerat quisquam recusandae saepe veniam voluptatem. Architecto commodi eaque '
                'eligendi minus ullam. Accusamus blanditiis dicta dignissimos dolores eligendi eos eveniet facilis '
                'impedit, iste nostrum, nulla placeat qui quo suscipit tempora? Dolores, ea.',
        'author': {
            'name': 'Alice',
            'id': 1,
        },
    },
    {
        'id': 2,
        'title': 'Lorem ipsum dolor sit amet, consectetur.',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium ad at autem beatae consequatur '
                'corporis cumque dicta, dolore eaque earum excepturi exercitationem hic id magnam molestiae nobis '
                'nostrum nulla numquam officiis, omnis pariatur quae, quasi quisquam quos sapiente sed similique '
                'temporibus veniam voluptatem voluptatum. Eum, quos soluta. Accusamus aliquid esse ex harum hic, '
                'itaque modi odit, omnis quam quo recusandae repellat similique, ullam veniam voluptatibus. Atque '
                'consectetur consequatur, eaque facilis illum incidunt inventore ipsa molestias nihil nostrum, '
                'officia quo repudiandae rerum sapiente tenetur vitae voluptatem. Aperiam aut eaque et eveniet '
                'exercitationem harum id in quae, quasi, quis repudiandae ut velit veritatis. Accusantium aliquam cum '
                'dicta, dolore ducimus eaque earum eligendi enim ex expedita facilis laboriosam laborum laudantium '
                'mollitia placeat porro possimus quasi sint temporibus tenetur voluptas, voluptate voluptatem. Animi, '
                'aperiam consectetur enim fugit molestiae rerum veniam! Adipisci alias amet commodi corporis culpa '
                'cupiditate doloribus dolorum eius facilis, fuga laboriosam magnam minima, nemo nobis officiis '
                'pariatur possimus quibusdam quidem reprehenderit sapiente sequi unde velit. Aliquam aspernatur autem '
                'commodi dolore ducimus, illo in, ipsa iusto magnam natus obcaecati perferendis sed sequi! Accusamus, '
                'consectetur consequuntur earum enim fugit inventore maxime necessitatibus nihil perspiciatis rem sed '
                'similique sunt velit veritatis vero vitae voluptatem, voluptatibus.',
        'author': {
            'name': 'John',
            'id': 2,
        },
    },
    {
        'id': 3,
        'title': 'Lorem ipsum dolor sit.',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum, magni, qui! Accusantium asperiores '
                'assumenda corporis dolorem doloribus molestias, necessitatibus obcaecati possimus quo sit. '
                'Accusantium culpa distinctio dolorem enim laborum nam, nostrum, pariatur qui repellendus '
                'reprehenderit, repudiandae velit. Accusantium ad adipisci aliquam aliquid amet aspernatur atque '
                'commodi consequuntur distinctio earum esse, et eum eveniet facere id impedit in ipsum iusto, '
                'labore natus numquam omnis optio pariatur placeat, quaerat quasi quia ratione recusandae reiciendis '
                'sequi soluta suscipit unde ut veniam voluptates voluptatibus voluptatum? Aliquid cupiditate dolorum '
                'magni veniam! Accusantium alias animi commodi culpa dolor dolore ducimus error, esse exercitationem '
                'facilis iure iusto nam necessitatibus nemo nihil nobis officiis praesentium quibusdam quis quisquam '
                'quo quos similique sint tempore vero vitae voluptas voluptate? Aliquid corporis deleniti laboriosam '
                'reiciendis voluptates! Animi aperiam cupiditate dignissimos doloribus eaque est harum id, '
                'iste maiores molestiae neque nihil non officiis praesentium qui quibusdam quisquam rerum sequi sunt '
                'ullam! Quasi.',
        'author': {
            'name': 'Mike',
            'id': 3,
        },
    }
]


@article.route('/')
def article_list():
    return render_template(
        'articles/articles_list.html',
        articles_list=ARTICLES,
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        for item in ARTICLES:
            if item['id'] == pk:
                article_item = item
        return render_template(
            'articles/details.html',
            article=article_item)
    except UnboundLocalError:
        raise NotFound(f'Article with id {pk} not found.')
