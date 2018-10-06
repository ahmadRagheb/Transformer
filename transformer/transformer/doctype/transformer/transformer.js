// Copyright (c) 2018, ahmedragheb75@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transformer', {
	refresh: function(frm) {

	}
});


frappe.ui.form.on("Transformer", "download_result", function(frm) {
  frappe.call({
  	args: {
        source:cur_frm.doc.source,
  			items:cur_frm.doc.items
      },
    method: "transformer.transformer.doctype.transformer.transformer.call_me",
    callback: function(r) { 
	if(r.message == "/files/to_upload.csv"){
    		cur_frm.set_value("result",r.message)
                frappe.msgprint("Successfully created");
		window.location = cur_frm.doc.result;

	}else{
		frappe.msgprint("Error please contact your IT Department")
	}
    }
  })
});
