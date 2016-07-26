import openerp
from openerp import pooler
from openerp.report import report_sxw
import xlwt
from openerp.addons.report_xls.report_xls import report_xls
from openerp.tools.translate import _

class openacademy_course_xls_parser(report_sxw.rml_parse):
	def __init__(self, cursor, uid, name, context):
		super(openacademy_course_xls_parser, self).__init__(cursor, uid, name, context=context)
		self.pool = pooler.get_pool(self.cr.dbname)
		self.cursor = self.cr

		self.localcontext.update({
			'cr': cursor,
			'uid': uid,
			'report_name': _('COURSE LIST'),
			})

_column_sizes = [
	('0',30),
	('1',30),
	('2',20)
]

import time

class openacademy_course_xls(report_xls):
	column_sizes = [x[1] for x in _column_sizes]

	def generate_xls_report(self, _p, _xs, data, objects, wb):
		ws = wb.add_sheet(_p.report_name[:31])
		ws.panes_frozen = True
		ws.remove_splits = True
		ws.portrait = 0
		ws.fit_width_to_pages = 1
		row_pos = 6

		ws.header_str = self.xls_headers['standard']
		ws.footer_str = self.xls_footers['standard']

		#write empty to define column
		c_sizes = self.column_sizes
		c_specs = [('empty%s' % i, 1, c_sizes[i], 'text', None) for i in range(0,len(c_sizes))]
		cell_format = _xs['bold'] + _xs['underline']
		so_style = xlwt.easyxf(cell_format)

		cell_format = _xs['bold'] + _xs['borders_all'] + _xs['center']
		table_title_style = xlwt.easyxf(cell_format)

		cell_format = _xs['right']
		right_style = xlwt.easyxf(cell_format)

		cell_format = _xs['underline'] + _xs['right']
		underline_style =  xlwt.easyxf(cell_format)

		for so in objects:
			c_specs = [('title',3,0,'text','Subject: %s' %(so.name)),]

			row_data = self.xls_row_template(c_specs, [x[0] for x in c_specs])
			row_pos = self.xls_write_row(ws, row_pos, row_data)
			ws.set_horz_split_pos(row_pos)



openacademy_course_xls('report.openacademy.course.list.xls','openacademy.course', parser=openacademy_course_xls_parser)