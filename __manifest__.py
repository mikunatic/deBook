{
    'name': 'deBook',
    'category': 'Library',
    'summary': 'Library CRM',
    'version': '1.0',
    'author': 'Mila Martins',
    'contributors': [
        'Ágatha Jamille'
        'Eric Gonçalves'
        'Júlia Morais'
    ],
    'description': """Management model for Library""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/publisher_view.xml',
        'wizard/book_registry_view.xml',
        'views/author_view.xml',
        'views/genre_view.xml',
        'views/book_view.xml',
        'views/customer_view.xml',
        'views/rent_view.xml',
        'data/genres.xml',
        'data/authors.xml',
        'data/publishers.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}