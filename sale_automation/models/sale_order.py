from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_send_sale_mail(self):
        """
          Sends the Sale Order Confirmation Email to the customer.

          Uses the `email_template_sale_order_confirmation` template and sends it to the
          customer (partner) associated with the sale order. The email is sent immediately
          with the light email layout applied.

          Example:
              sale_order.action_send_sale_mail()
        """
        mail_template = self.env.ref('sale_automation.email_template_sale_order_confirmation')
        for record in self:
            email_values = {
                'email_to': record.partner_id.email
            }
            mail_template.send_mail(record.id, force_send=True, email_values=email_values,
                                    email_layout_xmlid='mail.mail_notification_light')
