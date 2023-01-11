from odoo import http
from odoo.http import request

class TaskReportController(http.Controller):
    @http.route('/task/report/update', type='json', auth='user')
    def update_task_report(self, employee_id):
        # Search for tasks belonging to the selected employee
        task_obj = request.env['task.task']
        tasks = task_obj.search([('user_id', '=', employee_id)])
        # Return the task names and descriptions as a list of dictionaries
        task_data = []
        for task in tasks:
            task_data.append({
                'name': task.name,
                'description': task.description,
            })
        return task_data
