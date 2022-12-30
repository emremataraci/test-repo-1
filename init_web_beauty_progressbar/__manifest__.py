{
    'name': 'matar ProgressBar',
    'version': '15.0.1.0.2',
    'category': 'Extra Tools',
    'summary': 'Beauty Progressbar',
    'author': 'Init Co. Ltd',
    'support': 'contact@init.vn',
    'website': 'https://init.vn/?utm_source=odoo-store&utm_medium=15&utm_campaign=beauty-progress-bar',
    'license': 'LGPL-3',
    'description': """
Show percent value in Progress Bar
======================================================================
Make progressbar more beautiful and show percent number in Progressbar 
    """,
    'depends': ['web'],
    'data': [],
    'qweb': [
        # 'static/src/xml/percent_progressbar_template.xml'
    ],
    'demo': [],
    'test': [],
    'images': ['static/description/banner.png'],
    'bootstrap': True,
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'init_web_beauty_progressbar/static/src/scss/progress_bar.scss'
        ],
        'web.assets_qweb': [
            'init_web_beauty_progressbar/static/src/xml/percent_progressbar_template.xml',
        ],
    }
}
