# -*- coding: utf-8 -*-
# Copyright (c) 2018, ahmedragheb75@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import csv
import os

class Transformer(Document):
	pass
	
@frappe.whitelist()
def call_me(source,items):
	save_path = 'site2.local/public/files'
	# file_name = os.path.join(save_path, "dummp2.csv")
	to_upload = os.path.join(save_path, "to_upload.csv")
	source 	  = os.path.join(save_path, source.split('/')[-1])
	items 	  = os.path.join(save_path, items.split('/')[-1])
	
	ifile  = open(source, "rb")
	reader = csv.reader(ifile)

	try:
	    os.remove(to_upload)
	except OSError:
	    pass

	ofile  = open(to_upload, "wb")
	writer = csv.writer(ofile)

	ifile_template  = open(items, "rb")
	reader2 = csv.reader(ifile_template)

	for idx, row in enumerate(reader2):
		if idx  < 20:
			writer.writerow(row)

	ifile_template.close()

	for idx, row in enumerate(reader):
		if idx != 0 :
			temp_row = []
			#item name = articelo
			temp_row.insert(0,"")
			temp_row.insert(1,"")
			temp_row.insert(2,"Journal Entry")
			temp_row.insert(3,"JV-")
			temp_row.insert(4, row[2].replace('/','-'))
			temp_row.insert(5, "MITWALLI" ) #company
			temp_row.insert(6, "")
			temp_row.insert(7,"" )
			temp_row.insert(8, row[9]) #txt / user remarks
			temp_row.insert(9, row[7]) #debit
			temp_row.insert(10, row[8]) #total credit
			temp_row.insert(11, "") #difference
			temp_row.insert(12, "1") #multi_currency
			temp_row.insert(13, "") #clearance_date
			temp_row.insert(14, row[9])#txt / user remarks
			temp_row.insert(15, row[1]) #bill no
			temp_row.insert(16, "")
			temp_row.insert(17, "")
			temp_row.insert(18, "")
			temp_row.insert(19, "")
			temp_row.insert(20, "")
			temp_row.insert(21, "")
			temp_row.insert(22, "")
			temp_row.insert(23, "")
			temp_row.insert(24, "")
			temp_row.insert(25, "")
			temp_row.insert(26,"")		
			temp_row.insert(27,"")		
			temp_row.insert(28,u"{} - MSP".format(row[6]))		
			temp_row.insert(29,"")		
			temp_row.insert(30,u"{} - MSP".format(row[11]))
			writer.writerow([unicode(s).encode("utf-8") for s in temp_row])
	ifile.close()
	ofile.close()


	return "/files/to_upload.csv"
