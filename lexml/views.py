from django.utils.translation import ugettext_lazy as _

from crud import Crud

from .models import LexmlProvedor, LexmlPublicador

lexml_provedor_crud = Crud(
    LexmlProvedor, 'lexml_provedor', [

        [_('Provedor Lexml'),
         [('id_provedor', 2),
            ('nome', 10)],
            [('id_responsavel', 2), ('nome_responsavel', 5),
             ('email_responsavel', 5)],
            [('xml', 12)]],

    ])

lexml_publicador_crud = Crud(
    LexmlPublicador, 'lexml_publicador', [

        [_('Publicador Lexml'),
         [('id_publicador', 2),
            ('nome', 5), ('sigla', 5)],
            [('id_responsavel', 2), ('nome_responsavel', 5),
             ('email_responsavel', 5)]],
    ])
