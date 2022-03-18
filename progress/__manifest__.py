{
    'name': 'Progress Report',
    'version': '1.0',
    'summary': 'Progress Report',
    'sequence': -9,
    'description': """
        This is a practise addon where i will apply as many skills as possible
    """,
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/report_view.xml',
        'views/coordinate_view.xml',
        'views/locations_view.xml'
,    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}