# -*- coding: utf-8 -*-
# Copyright (c) 2017, taher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StockOUT(Document):
	def on_submit(self):
		frappe.errprint("in on on_submit")
		# it = self.get('items')
		# frappe.errprint(it)
		se = frappe.new_doc("Stock Entry")
		se.purpose = "Material Receipt" 
		for items in self.get('items'):
			row = se.append("items",{})
			row.t_warehouse =items.warehouse
			row.item_code = items .item
			row.qty= -items.quantity
			expense_account =self.expense_account
		se.insert(ignore_permissions=True)
		se.submit()
	