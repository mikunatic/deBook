from odoo import fields, models


class Author(models.Model):
    _name = 'author'

    name = fields.Char("Author Name")
    book_ids = fields.Many2many('book', compute="populate_books")

    def populate_books(self):
        for rec in self:
            book_ids = self.env['book'].search([('author_id','=',rec.id)])
            rec.book_ids = book_ids.ids