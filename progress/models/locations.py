from odoo import api, fields, models, _

class ProgressLocations(models.Model):
    _name = "progress.locations"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Progress Locations"

    user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
    latitude = fields.Char(string="Latitude", required=True, tracking=True)
    longitude = fields.Char(string="Longitude", required=True, tracking=True)
    update_date = fields.Datetime(string="Updated Date Time", tracking=True)