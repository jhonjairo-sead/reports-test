# -*- coding: utf-8 -*-


from odoo import fields, models


class StockvaluationLayer(models.Model):
    _inherit = 'stock.valuation.layer'
    _description = 'Report of stratified kardex'

    def print_report_stratified_kardex(self):
        return {
            'type': 'ir.actions.report',
            'model': "stock.valuation.layer",
            'report_type': "xlsx",
            'report_name': "report_integration.stock_valuation_layer_report",
            'file': "Report of stratified kardex",
            'attachment_use': "False"
        }
