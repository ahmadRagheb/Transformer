// Copyright (c) 2018, ahmedragheb75@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transformer', {
	refresh: function(frm) {

	}
});


frappe.ui.form.on("Transformer", "download_result", function(frm) {
  frappe.call({
    method: "transformer.transformer.doctype.transformer.transformer.call_me",
    callback: function(r) { 
    	console.log("successz")
    }
  })
});
