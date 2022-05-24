from odoo import _, api, fields, models

import logging


_logger = logging.getLogger(__name__)


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'
    _description = 'Stock Valuation Layer'

    def get_data_stratified(self, year, month):
        year_, month_ = year + 1, 1 if month == '12' else year, month
        query = f"""
        SELECT
            svl.create_date,
            po.id as order_id,
            po.name AS order,
            svl.quantity,
            uu.name as uom,
            svl.value
        FROM
            stock_valution_layer svl
            LEFT JOIN stock_move sm ON sm.id = svl.stock_move_id
            LEFT JOIN product_product pp ON pp.id = svl.product_id
            LEFT JOIN purchase_order_line pol ON pol.id = sm.purchase_line_id
            LEFT JOIN purchase_order po ON po.id = pol.order_id
            LEFT JOIN product_template pt ON pp.product_tmpl_id = pt.id
            LEFT JOIN uom_uom uu ON uu.id = svl.uom_id
        WHERE
            create_date BETWEEN '{year}-{month}-01'
            AND '{year_}-{month_}-01'
        ORDER BY
            svl.product_id, svl.create_date;
        """
        self.env.cr.execute(query)
