from odoo import fields, models

class Ferramenta(models.Model):
    _name = 'ferramenta'
    id_job = fields.Many2one(comodel_name='hr.job', string='Cargo')
    name = fields.Char(string='Nome de equipamentos de utilização',
                       readonly=True,
                       required=True)
    # ferramentas_id = fields.One2many(comodel_name='ferramentas_dos_funcionarios', inverse_name='job_id')
    # parent_id = fields.Many2one('hr.job', string='Parent Job', ondelete='cascade')

   # job_id = fields.Many2one(comodel_name='ferramentas_dos_funcionarios', inverse_name='job_id')
    # parent_id= fields.Many2one('hr.job', string='Parent Job', ondelete='cascade')



   # parent_id= fields.Many2one('hr.job', tring='Parent Job', ondelete='cascade')
#ondelete = 'cascade     Ao excluir o pai os filhos também serão excluidos
    # Trabalho A       (pai)
    #       Trabalho B   (filho)
    #       Trabalho C   (filho)