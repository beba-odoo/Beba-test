from dateutil.relativedelta import relativedelta
from odoo import models, fields

class realestate(models.Model):
    _name = "real.estate"
    _description = "Real Estate"
    name = fields.Char(required=True,index=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=lambda self: fields.Date.today() + relativedelta(months=+3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default='2')
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('North', 'North'), ('South', 'South'),('East', 'East'), ('West', 'West')])
    state = fields.Selection(selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], string='State', default='new', required=True, copy=False)
    partner_id = fields.Many2one("res.partner", string="Buyer")
    user_id = fields.Many2one("res.user", string="Salesman")
    property_id= fields.Many2one("real.estate.property", string="Property Type")
 
class propertytypes(models.Model):
    _name = "real.estate.property"
    _description = "Type of property"
    name = fields.char(required=True,index=True)
