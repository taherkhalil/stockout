# -*- coding: utf-8 -*-
# Copyright (c) 2017, taher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, flt, cstr, now
from frappe.model.document import Document

class Discarditems(Document):
	def on_submit(self):
		se = frappe.new_doc("Stock Entry")
		se.purpose = "Material Receipt" 
		for items in self.get('items'):
			row = se.append("items",{})
			row.t_warehouse =items.warehouse
			row.item_code = items .item
			row.qty= -items.quantity
			row.expense_account =self.expense_account		
		se.insert(ignore_permissions=True)
		se.save()
		se.submit()


@frappe.whitelist()
def get_valuation(item_code):
	last_valuation_rate = frappe.db.sql("""select valuation_rate
	from `tabStock Ledger Entry`
	where item_code = %s and valuation_rate > 0
	order by posting_date desc, posting_time desc, name desc limit 1""", item_code)
	# frappe.errprint(last_valuation_rate)
	if not last_valuation_rate:
		frappe.throw("no valuation_rate for item,check item ")
	valuation_rate = flt(last_valuation_rate[0][0])
	# frappe.errprint(valuation_rate)

	return valuation_rate





