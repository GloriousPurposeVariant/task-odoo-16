from odoo import api, fields, models


class Book(models.Model):
    _name = 'book.book'
    _description = 'Book'

    name = fields.Char(string='Name')
    author = fields.Char(string='Author')
    publication_date = fields.Date(string='Publication Date')
