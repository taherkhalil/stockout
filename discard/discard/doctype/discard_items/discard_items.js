// Copyright (c) 2017, taher and contributors
// For license information, please see license.txt

frappe.ui.form.on('Discard items', {
	refresh: function(frm) {

	}

});


frappe.ui.form.on	('items to discard',{
	item: function(frm,cdt,cdn){
		var d = locals[cdt][cdn];
		frappe.call({
		method: "discard.discard.doctype.discard_items.discard_items.get_valuation",
		args: {
			item_code: d.item
		},
		callback: function(r) {		
			if(r.message) {
				console.log(r.message);
				d.valuation_rate =r.message;
				cur_frm.refresh_field(d.valuation_rate);
			} 
		}
	});
	},

	quantity:function(frm,cdt,cdn){
		var d = locals[cdt][cdn];
		quantity = d.quantity;
		console.log(quantity);
		amount = flt(quantity)*flt(d.valuation_rate);
		console.log(amount);
		d.amount = amount;
		frm.refresh_field(d.amount);
	}

});
