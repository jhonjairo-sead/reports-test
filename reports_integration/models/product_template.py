from odoo import _, api, fields, models

import logging


_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    history_purchase_stratified_ids = fields.One2many('purchase.stratified', 'product_tmpl_id', string='History purchase stratified')


class PurchaseStratified(models.Model):
    _name = 'purchase.stratified'
    _description = 'Purchase Stratified'

    product_tmpl_id = fields.Many2one('product.template', string='Product Template')
    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order')
    amount_total = fields.Float('Amount total', compute='get_amount_total')
    amount_1 = fields.Float('Amount 1')
    amount_2 = fields.Float('Amount 2')
    amount_3 = fields.Float('Amount 3')
    amount_4 = fields.Float('Amount 4')

    def get_amount_total(self):
        self.amount_total = self.amount_1 + self.amount_2 + self.amount_3 + self.amount_4
