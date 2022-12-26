# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo import models, fields, api

def download_attachment(self, cr, uid, ids, context=None):
    attachment = self.browse(cr, uid, ids[0], context=context)
    file = attachment.datas
    file_name = attachment.name
    file_ext = file_name.split(".")[-1]
    if file:
        file = base64.b64decode(file)
        response = request.make_response(file, [('Content-Type', 'application/octet-stream'), ('Content-Disposition', 'attachment; filename=%s' % file_name)])
        return response
    else:
        raise osv.except_osv(_('Error!'), _('There is no file to download.'))

class SelectProducts(models.TransientModel):

    _name = 'select.products'
    _description = 'Select Products'

    product_ids = fields.Many2many('product.product', string='Products')
    flag_order = fields.Char('Flag Order')

    def select_products(self):
        if self.flag_order == 'so':
            order_id = self.env['sale.order'].browse(self._context.get('active_id', False))
            for product in self.product_ids:
                self.env['sale.order.line'].create({
                    'product_id': product.id,
                    'product_uom': product.uom_id.id,
                    'price_unit': product.lst_price,
                    'order_id': order_id.id
                })
        elif self.flag_order == 'po':
            order_id = self.env['purchase.order'].browse(self._context.get('active_id', False))
            for product in self.product_ids:
                self.env['purchase.order.line'].create({
                    'product_id': product.id,
                    'name': product.name,
                    'date_planned': order_id.date_planned or datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                    'product_uom': product.uom_id.id,
                    'price_unit': product.lst_price,
                    'product_qty': 1.0,
                    'display_type': False,
                    'order_id': order_id.id
                })

        