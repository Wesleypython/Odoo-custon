from odoo import models, fields
class Classe(models.Model):
    def __init__(self, nome, cor):
        self.cor = cor
        self.nome = nome

    def mostra_info(self):
        return f"{self.__class__.__name__} - nome: {self.modelo}, cor: {self.cor}"

# Criando uma instância
carro= Classe('fusca','red')


info = carro.mostrar_info()
print(info)  # Saída: "Carro - Modelo: Fusca, Cor: azul"






class Student(models.Model):
    _name = "student"

    name = fields.Char()

    school_id = fields.Many2one(
        comodel_name="school",
        string="Escola"
    )

class School(models.Model):
    _name = "school"

    name = fields.Char()

    student_ids = fields.One2many(
        comodel_name="student",
        inverse_name="school_id"


    )

    class School(models.Model):
        _name = "school"

        name = fields.Char()

        student_ids = fields.One2many(
            comodel_name="student",
            inverse_name="school_id"
        )

        member_ids = fields.One2many(
            comodel_name='hr.employee',
            inverse_name='department_id'
        )
        # select from hr.employee where department_id = self.id



