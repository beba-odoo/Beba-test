from odoo import models, fields

class realestate(models.Model):
    _name = "real.estate"
    _description = "Real Estate"
 name = fields.Char()