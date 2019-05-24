# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FiscalPosConfingInterface(models.Model):

    # _name = 'config_interface.config'
    _inherit = ['config.interface']

        
    printer_type = fields.Selection(
        string=u'Tipo de impresora',
        selection=[('bixolon', 'Bixolon/HKA'), ('custom', 'Custom'), ('epson', 'Epson'), ('star', 'Star/Citizen')],
        default="bixolon"
    )

    mode_restaurant = fields.Boolean(
        string=u'Modo restaurante',
        default=True,
        help=u"Activado: Impresora Modo FastFood, Desactivado:  Impresora Modo Retail"
    )

    use_legal_tip = fields.Boolean(
        string=u'Propina legal',
        help=u"Para que todas los documentos apliquen el 10% de propinal legal"
    )




class InterfacePosConfig(models.Model):

    _name = 'pos.config'
    _inherit = 'pos.config'

    config_interface_id = fields.Many2one(
        "config.interface", u"Parámetro")


class AccountFiscalPosition(models.Model):

    _inherit = 'account.fiscal.position'

    use_for_delivery = fields.Boolean(
        string=u'Usar para LLevar/Delivery',
        help ="Activar si desea que esta posicion fiscal,hace que no se aplique el 10%\
        de la propinal legal."
    )


