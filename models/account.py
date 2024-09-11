from odoo import fields,models

class AccountMove(models.Model):
    _inherit = "account.move"

    def add_saudi_in_arabic_field(self):
        if self.ar_amount_untaxed:
            modified_string = self.ar_amount_untaxed.replace('سعودي','')
            modified_string = modified_string.replace('ريال', 'سعودي ريال')
            self.ar_amount_untaxed = modified_string
        if self.amount_in_word_ar:
            modified_string = self.ar_amount_untaxed.replace('سعودي','')
            modified_string = modified_string.replace('ريال', 'سعودي ريال')
            self.amount_in_word_ar = modified_string


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def enz_natcom_compute_tax_value(self):
        tax_amount = 0.00
        if self.tax_ids:
            amount = sum(self.tax_ids.mapped('amount'))
            tax_amount = (self.price_subtotal/100) * amount
        return tax_amount

    def enz_natcom_compute_taxed_subtotal(self):
        return self.price_subtotal + self.enz_natcom_compute_tax_value()
