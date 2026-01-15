from odoo import models, fields

class MiModelo(models.Model):
    _name = "mi_primer_modulo.item"
    _description = "Item de ejemplo"

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    activo = fields.Boolean(string="Activo", default=True)
