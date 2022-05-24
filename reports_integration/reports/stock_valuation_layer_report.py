# -*- coding: utf-8 -*-

from odoo import models

import logging

_logger = logging.getLogger(__name__)


class PurchaseReport(models.AbstractModel):
    _name = 'report.reports_integration._report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, obj):

        sheet = workbook.add_worksheet("Report of stratified kardex")
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'Date', bold)
        sheet.write(0, 1, 'Purchase order', bold)
        sheet.write(0, 2, 'Quantity', bold)
        sheet.write(0, 3, 'Unit of measure', bold)
        sheet.write(0, 4, 'Ammount total', bold)
        sheet.write(0, 5, 'Amount 1', bold)
        sheet.write(0, 6, 'Amount 2', bold)
        sheet.write(0, 7, 'Amount 3', bold)
        sheet.write(0, 8, 'Amount 4', bold)
        # sheet.write(0, 9, 'RUC o DNI', bold)

        row = 1

        stock_valuation_layer = self.env['account.move'].get_data_stratified()

        for record in stock_valuation_layer:

            sheet.write(row, 0, str(record.get("create_date")))
            sheet.write(row, 1, record.get("order"))
            sheet.write(row, 2, record.get("quantity"))
            sheet.write(row, 3, record.get("uom"))
            sheet.write(row, 4, record.get("value"))
            # sheet.write(row, 5, record.get("discount"))
            # sheet.write(row, 6, record.get("price_total"))
            # sheet.write(row, 7, record.get("move"))
            # sheet.write(row, 8, record.get("partner"))
            # sheet.write(row, 9, record.get("vat"))

            row += 1
