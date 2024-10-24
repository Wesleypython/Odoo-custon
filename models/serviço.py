from odoo import models, fields, api

class Servico(models.Model):
    _name = 'servico'
    employee_id = fields.Many2one(comodel_name='hr.employee',
                                  string='Nome do Responsável',
                                  domain="[('id','in',campo_managers)]",
                                  required=True )

    campo_managers = fields.Many2many(comodel_name='hr.employee',
                                      compute='domain')

    name = fields.Char(string='Nome/Ordem',
                       readonly=True)

    numero_da_ordem = fields.Integer(string='Número da Ordem de Serviço')

    data_de_emissao = fields.Date(string='Data de Emissão')

    difficulty_ids = fields.Many2many(comodel_name='dificuldade',
                                      string='Nível de dificuldade',
                                      required=True)

    descricao = fields.Char(string='Descrição detalhada do serviço a ser realizado')

    equipamentos = fields.Char(string='Equipamentos ou produtos envolvidos')

    equipe = fields.Many2many(comodel_name='hr.employee',
                              string='Equipe de execução',
                              compute='compute_equipe',
                              store=True,
                              readonly=False,
                              domain="[('id','in',only_son)]"
                                       )

    @api.depends('employee_id')
    def compute_equipe(self):
        for rec in self:
            equipe_ids= self.env['hr.employee'].search([('parent_id','=',rec.employee_id.id)])
            self.write({
                    "equipe": [[
                        6, False, equipe_ids.ids
                    ]]
                })
                                         # hr.employee é o modelo, Store Define se o valor calculado deve ser armazenado no banco de dados.
                                        # domain= dominio, limitando apenas os IDs que estiverem no only_son
    #descrição: a equipe recebe apenas os IDs que estiverem no only_son, sendo calculado pelo compute

    only_son = fields.Many2many(comodel_name='hr.employee',
                                compute='domain_equipe',
                                relation='servico_domain_equipe_rel'
                                )
# O campo recebe varios registros do modelo employee, e calcula pelo compute, assim reescreve o campo equipe

    # equipe = fields.One2many(comodel_name='hr.job', inverse_name='many',string='Equipe')

     #@api.model   # Isso indica que o método é um método de modelo,   é redundante Felipe?

    def name_get(self):
        result = [] # lista
        for record in self: # Para cada registro em self, esperando os registros do úsuario, parametro do python utilizado,
            # para registrar em instancias que contem obejetos aptos para receber atributos.
            if record.employee_id and record.id:
                employee_name = record.employee_id.name
                first_name = employee_name.split()[0][:10]
                name = f'{first_name} - Ordem: {record.id}'
                # name = f"{record.employee_id.name or 'Sem Nome'} - Ordem: {record.id or 'N/A'}"# objeto da instancia que espera receber
                # peguei o nome do employee_id e coloquei dentro do meu registro
                # um registro em seus atributos, nome, e no numero_da_ordem
                result.append((record.id, name)) # Adicionando na lista record cada nova registro e su id.
                self.name = name
            else:
                name = f' Ordem: {record.id}'
                result.append((record.id, name))  # Adicionando na lista record cada nova registro e su id.
                self.name = name
        return result



    @api.depends('equipe')
    def domain_equipe(self):
        # Permite add os funcionários especificos existentes do gerente
        for record in self:
            filter_two = self.env['hr.employee'].search([('parent_id', '=', record.employee_id.id)])
            if filter_two:
          #Quero criar self.write que vai escrever somente os funcionarios que fazem parte daquele gerente
        # Duas ideias: ou remove o ids que não estão no filter_two ou add apenas os que estão
                record.write({
                    "only_son": [[
                        6, False, filter_two.ids
                    ]]
                })
            else:
                record.write({
                    "only_son": [[
                        5, False, False
                    ]]
                })

    @api.depends('employee_id')
    def domain(self):
        # Verifica quem são os gerentes
        for rec in self:
            # whole = rec.employee_id.parent_id != False
            managers = self.env['hr.employee'].search([('parent_id', '!=', False)])
            some = managers.mapped('parent_id').ids
            self.write({
                "campo_managers": [[
                    6, False, some
                ]]
            })


