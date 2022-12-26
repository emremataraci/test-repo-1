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
