from odoo import models, fields


class FerramentasFuncionario(models.Model):
    _inherit = 'hr.job'
    ferramentas_ids = fields.One2many(comodel_name='ferramenta', inverse_name='id_job', string='Ferramentas de Utilização')
    # job_id = fields.Many2one(comodel_name='hr.job', string='Cargo')


