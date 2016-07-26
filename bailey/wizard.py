from openerp import models, fields, api

from openerp.osv import fields, osv

class wizard(osv.osv_memory):
	_name = 'wizard'

	_columns = {
        'start_date': fields.date('hehe')
    }

	def download(self, cr, uid, ids, context=None):
		datas = {'ids': context.get('active_ids', [])}
		res = self.read(cr, uid, ids,['start_date'], context=context)
		res = res and res[0] or {}

		datas['form'] = res
		if res.get('id',False):
			datas['ids']=[res['id']]
		# get report_format
		if res.get('report_format', 'pdf') == 'xls':
			context['xls_export'] = 1

		context['data'] = datas
		result = self.pool['report'].get_action(cr, uid, [], 
			'openacademy_course_list_xls', data=datas, context=context)
		return result