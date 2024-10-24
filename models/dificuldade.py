from odoo import api, fields, models
from datetime import timedelta



class Dificuldade(models.Model):
    _name = 'dificuldade'
    data = fields.Many2one(comodel_name='data_de_previsao',
                           string='Data prevista')
    nome = fields.Char(string='Nome da Atividade') #fazer um M2o com o tipo de serviço
    # action = fields.Char(string='Qual é a a atividade')
    time = fields.Integer(string='Quantos dias demora a atividade')
    week = fields.Integer(string='Quantas semanas demora a atividade')
    forecast = fields.Integer(string='Acrescimo de tempo')
    difficulty = fields.Date(string='Data de previsão de conclusão',
                                  readonly=True,
                                  compute='conclusao',
                                  store=True,
                                  )

    @api.depends('time', 'week', 'forecast')
    def conclusao(self):
        for rec in self:
            total_days=rec.time+(rec.week*7)+rec.forecast
            today = fields.Date.context_today(self)
            # Calcula a nova data de previsão de conclusão
            rec.difficulty = today + timedelta(days=total_days)
            # self.write({
            #     "difficulty": [[
            #         6, False, total_days.ids
            #     ]]
            # })



#repair_management