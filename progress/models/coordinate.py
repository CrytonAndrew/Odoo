from odoo import api, fields, models, _

class Report(models.Model):
    _name = "progress.coordinate"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Progress Report"

    latitude = fields.Char(string="Latitude", required=True, tracking=True)
    longitude = fields.Char(string="Longitude", required=True, tracking=True)
    report_id = fields.Many2one('progress.report', string="Report", required=True)