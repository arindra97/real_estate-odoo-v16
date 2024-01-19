{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Maks",
    'category': 'test',
    'license': 'LGPL-3',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'application':True,
}