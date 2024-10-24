from odoo import models, fields

class HrDepartment(models.Model):
    _name ='hr.department'
    _inherit = _name
    assinatura = fields.Char(str='Assinatura')
    # _order = 'name ASC, turno ASC'
    turno = fields.Selection(selection=[
        ('1', 'Manhã'),
        ('2', 'Tarde'),
        ('3', 'Noite')
    ], required=True)


    #fields.Many2one(comodel_name='funcao.fabrica', inverse_name='turno',)# readonly=True




# class ContractTypeExtension(models.Model):
#     _name = 'hr.department'
#     _inherit = _name
#     _order = 'sequence'
#
#     ... extensão
#
# class ContractTypePrototype(models.Model):
#     _name = 'sector'
#     _inherit = "hr.department"
#
#     ... ter, prototipo que herda tanto atributos quanto funções
#
# class ContractTypeDelegation(models.Model):
#     _name = 'sector'
#
#     department_id = fields.Many2one(
#         comodel_name="hr.department",
#         delegate=True
#     )
#
#     ... Ser, delegação que passa a ser apenas os atributos da classe delegada