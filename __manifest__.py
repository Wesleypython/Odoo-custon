{
    'name': "FABRICA",
    'summary': "gerenciando a industria/ subtitulo",
    'description': """
    """,
    'author': "Wesley",
    'website': "Uma_url, para saber mais sobre o módulo",
    'category': 'Usado para organizar módulos por áreas de interesse. O que o Vini comentou de colocar o principal em cima',
    'version': '16.0.1',
    'depends': ['base','hr'],
    'data':[
        'views/views_hr_department.xml',
        'views/views_ferramentas.xml',
        'views/servico.xml',
        'views/hr_job.xml',
        'views/dificuldade.xml',
        'views/hrwork_location.xml',
        'security/ir.model.access.csv'
    ],
}
#    'demo': " ",
#lista de caminhos relativos para os arquivos de dados a serem carregados durante a instalação