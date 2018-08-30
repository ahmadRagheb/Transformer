# -*- coding: utf-8 -*-
# Copyright (c) 2018, ahmedragheb75@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def call_me():
	frappe.msgprint("call me")
