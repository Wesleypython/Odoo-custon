from odoo import fields, models

class HrWorkLoc(models.Model):
    _inherit = 'hr.work.location'
    local= fields.One2many(
        comodel_name='hr.employee',
        inverse_name='work_location_id',
        string='Funcionários do Local',
    )# mapeie o campo funcionario (os funcionarios que estão  em determinada localização de trabalho)

    # Filtrar o local.
    # O One2many serve para mapear exatamente o outro atributo.
    # Enquanto o Many2many serve para que o escritorio(local) possa referenciar O Felipe e tantos outros funcionarios,
    # e o Felipe pode referenciar que trabalha em muitos escritorios.
