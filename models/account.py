from odoo import fields,models

class AccountMove(models.Model):
    _inherit = "account.move"

    def add_saudi_in_arabic_field(self):
        if self.ar_amount_untaxed:
            modified_string = self.ar_amount_untaxed.replace('فقط', '').replace('لاغير', '').replace(' ريال سعودي','').strip()
            modified_string += ' ريال سعودي'
            modified_string =  modified_string + 'فقط'
            self.ar_amount_untaxed = modified_string
        if self.amount_in_word_ar:
            modified_string = self.ar_amount_untaxed.replace('فقط', '').replace('لاغير', '').replace(' ريال سعودي','').strip()
            modified_string += ' ريال سعودي'
            modified_string = modified_string + 'فقط'
            self.amount_in_word_ar = modified_string

    # def print_tax_values(self):
    #     for line in self.invoice_line_ids:
    #         print(line.enz_natcom_compute_tax_value())
    #         print(line.enz_natcom_compute_taxed_subtotal())

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
