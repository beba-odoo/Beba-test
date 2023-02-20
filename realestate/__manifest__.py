{
    'name': "Real Estate",
    'version': '14',
    'depends': ['base','crm'],
    'author': "BEBA",
    'category': 'Realestate',
    'description': """
    APP for real estate
    """,
    # data files always loaded at installation
    'data': [
        'views/realestate_view.xml',
        'Security/country state.csv',
        'Security/Security access rights real estate.csv'
    ],
}
