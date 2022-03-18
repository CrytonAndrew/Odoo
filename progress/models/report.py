from odoo import api, fields, models, _

class Report(models.Model):
    _name = "progress.report"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Progress Report"

    name = fields.Char(string="Report Name", required=True, tracking=True)
    reference = fields.Char(string="Report Reference", required=True, readonly=True, default=lambda self: _('New'))
    city = fields.Char(string="City", tracking=True)
    image = fields.Binary(string="Report Image")
    notes = fields.Text(string="Notes", tracking=True)
    coordinate_ids = fields.One2many('progress.coordinate', 'report_id', string="Coordinates")
    coordinate_count = fields.Integer(string='Number of Coordinates', compute='_compute_appointment_count')

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('progress.report') or ('New')
        res = super(Report, self).create(vals)
        return res
    
    def _compute_appointment_count(self):
        # Hydrate self over a for loop to solve singleton error
        for rec in self:
            appointment_count = self.env['progress.coordinate'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count