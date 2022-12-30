from odoo import http
from odoo.http import request

class TaskReportController(http.Controller):
    @http.route('/task/report', type='http', auth='user')
    def task_report(self):
        task_obj = request.env['task.task']
        tasks = task_obj.search([])
        return request.render('task_reporting.task_report_template', {'tasks': tasks})
