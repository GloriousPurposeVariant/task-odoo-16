{
    'name': 'Sale Automation',
    'version': '1.0',
    'depends': ['sale_management', 'base_automation'],
    'data': [
        'data/sale_order_server_action.xml',
        'data/sale_email_template.xml',
        'views/sale_order_view.xml',
        'report/report_sale_order_document.xml'
    ],
    'installable': True,
    'application': False,
}
