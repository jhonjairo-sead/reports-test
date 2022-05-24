from odoo import _, api, fields, models

import logging
import base64
from io import BytesIO
import pandas as pd


_logger = logging.getLogger(__name__)


class StratifiedKardex(models.TransientModel):
    _name = 'stratified.kardex'
    _description = 'Stratified Kardex'

    month = fields.Selection([
        (1, 'January'),
        (2, 'January'),
        (3, 'January'),
        (4, 'January'),
        (5, 'January'),
        (6, 'January')
        (7, 'January')
        (8, 'January')
        (9, 'January')
        (10, 'January')
        (11, 'January')
        (12, 'January')
    ], string='Month')
    year = fields.Integer('Year')
    xlsx = fields.Binary('xlsx')

    def get_data_xlsx(self):
        data = base64.b64decode(self.xlsx)
        bytes = BytesIO(data)
        sheet = 'Hoja1'
        data = pd.read_excel(bytes, sheet_name=f'{sheet}', engine=None)
        for index, row in data.iterrows():
            _logger.info(f"get_data_xlsx {row['order_id']}")
            record_data = {
                'purchase_order_id': row['order_id'],
                'amount_1': row['c1'],
                'amount_2': row['c2'],
                'amount_3': row['c3'],
                'amount_4': row['c4']
            }

            self.env['product.template'].browse(row['product_tmpl_id']).history_purchase_stratified_ids = [(0, 0, record_data)]

    def print_report_stratified_kardex(self):
        self.env['stock.valuation.layer'].print_report_stratified_kardex()

    def generate_stratitifed_kardex(self):
        if self.xlsx:
            self.get_data_xlsx()
        self.print_report_stratified_kardex()
