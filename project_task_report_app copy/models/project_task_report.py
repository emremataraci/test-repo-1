from odoo import models, fields

class Task(models.Model):
    _name = 'task.task'
    name = fields.Char(string='Task Name', required=True)
    user_id = fields.Many2one(comodel_name='res.users', string='Assigned To', required=True)
    date_start = fields.Date(string='Start Date', required=True)
    date_end = fields.Date(string='End Date', required=True)
    description = fields.Text(string='Description')
