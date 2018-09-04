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
	frappe.msgprint(source)
	frappe.msgprint(items)

	ifile  = open(os.path.abspath(source), "rb")
	reader = csv.reader(ifile)
	try:
	    os.remove(os.path.abspath("/files/dummp2.csv"))
	except OSError:
	    pass


	ofile  = open(os.path.abspath("/files/dummp2.csv"), "wb")
	writer = csv.writer(ofile)

	found = {}
	for idx, row in enumerate(reader):
		if idx != 0 :
			if row[3] not in found:
				found[row[3]] = int(row[16])
			else:
				found[row[3]] = int(found[row[3]]) + int(row[16])
	ifile.close()

	ifile  = open(os.path.abspath(source), "rb")
	reader = csv.reader(ifile)
	exist=[]
	for idx, row in enumerate(reader):
		if idx != 0 :
			if row[3] not in exist:
				row[16] = found[row[3]]
				exist.append(row[3])
				writer.writerow(row)
		else:
			writer.writerow(row)

	ifile.close()
	ofile.close()


	ifile  = open(os.path.abspath("/files/dummp2.csv"), "rb")
	reader = csv.reader(ifile)


	try:
	    os.remove(os.path.abspath("/files/to_upload.csv"))
	except OSError:
	    pass

	ofile  = open(os.path.abspath("/files/to_upload.csv"), "wb")
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
			temp_row.insert(2,row[3])
			temp_row.insert(3,str("مجموعات جميع الاصناف"))
			temp_row.insert(4, "Nos")
			temp_row.insert(5, 0 )
			temp_row.insert(6, 1)
			temp_row.insert(7, row[16])
			temp_row.insert(8, "")
			temp_row.insert(9, row[3])
			temp_row.insert(10, row[11])
			temp_row.insert(11, row[0])
			temp_row.insert(12, row[1])
			temp_row.insert(13, row[2])
			temp_row.insert(14, row[4])
			temp_row.insert(15, row[5])
			temp_row.insert(16, row[6])
			temp_row.insert(17, row[7])
			temp_row.insert(18, row[8])
			temp_row.insert(19, row[9])
			#color
			temp_row.insert(20, row[12])
			#modelo
			temp_row.insert(21, row[10])
			#temp
			temp_row.insert(22, row[13])
			temp_row.insert(23, row[14])
			temp_row.insert(24, row[15])
			temp_row.insert(25, row[16])

			#valuation rate
			temp_row.insert(26,1)		

			writer.writerow(temp_row)

	ifile.close()
	ofile.close()

	return "/files/to_upload.csv"