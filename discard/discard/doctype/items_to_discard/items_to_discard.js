frappe.ui.form.on('items to discard',{
	refresh: function(frm){
		console.log("some0");
	}
	// item: function(frm){
	// 		frappe.call({
	// 	method: "discard.discard.doctype.discard_items.discard_items.get_valuation",
	// 	args: {
	// 		item_code: frm.item
	// 	},
	// 	callback: function(r) {		
	// 		if(r.message) {
	// 			console.log(r.message);
	// 			valuation_rate =r.message;
	// 			frappe.refresh_fields("valuation_rate");
	// 		} 
	// 	}
	// });
	// }

});