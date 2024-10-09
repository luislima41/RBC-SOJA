import PySimpleGUI as sg
fonte = ("Helvetica", 12)
def janelaInicial():
    sg.theme('DarkGrey')
    coluna1 = [
        [sg.Text('Área Danificada', font=fonte)],
        [sg.Combo(['Baixas Áreas', 'Espalhado', 'Áreas Superiores', 'Campo Inteiro'], key='areaDamaged',
                  enable_events=True, readonly=True)],

        [sg.Text('Lesão de Cancro', font=fonte)],
        [sg.Combo(['Sem Resposta', 'Marrom', 'dk-marrom-blk', 'Bronzeado'], key='canker-lesion',
                  enable_events=True, readonly=True)],

        [sg.Text('Histórico de Cultura', font=fonte)],
        [sg.Combo(
            ['Diferente do primeiro ano', 'Mesmo do primeiro ano', 'Mesmo do ultimo ano', 'Mesmo do ultimo dois anos'],
            key='crop-hist', enable_events=True, readonly=True)],

        [sg.Text('Data', font=fonte)],
        [sg.Combo(
            ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro'], key='date', enable_events=True, readonly=True)],

        [sg.Text('Decadência Externa', font=fonte)],
        [sg.Combo(['Ausente', 'Firme e Seco'], key='external decay', enable_events=True, readonly=True)],

        [sg.Text('Manchas de Frutas', font=fonte)],
        [sg.Combo(['Não tem resposta', 'Ausente', 'Marrom com manchas pretas', 'Colorido'], key='manchasdeFrutas',
                  enable_events=True, readonly=True)],

        [sg.Text('Corpos de Frutificação', font=fonte)],
        [sg.Combo(['Ausente', 'Presente'], key='corposdeFrutificacao', enable_events=True, readonly=True)],

        [sg.Text('Vagens de Frutas', font=fonte)],
        [sg.Combo(['Não tem resposta', 'pouco presente', 'Normal', 'Doente'], key='vagensdeFrutas', enable_events=True,
                  readonly=True)],

        [sg.Text('Germinação', font=fonte)],
        [sg.Combo(['abaixo de 80%', '80-89 %', '90-100%'], key='germinacao', enable_events=True, readonly=True)]

    ]
    coluna2 = [
        [sg.Text('Saudação', font=fonte)],
        [sg.Combo(['Não', 'Sim'], key='saudacao', enable_events=True, readonly=True)],

        [sg.Text('Descoloração', font=fonte)],
        [sg.Combo(['Nenhum', 'Preto'], key='descoloracao', enable_events=True, readonly=True)],

        [sg.Text('Folha-Malf', font=fonte)],
        [sg.Combo(['Ausente', 'Presente'], key='folhaMalf', enable_events=True, readonly=True)],

        [sg.Text('Folha-Suave', font=fonte)],
        [sg.Combo(['Ausente', 'Baixo surf', 'Alto surf'], key='folhaSuave', enable_events=True, readonly=True)],

        [sg.Text('Folhagem', font=fonte)],
        [sg.Combo(['Ausente', 'Presente'], key='folhagem', enable_events=True, readonly=True)],

        [sg.Text('Manchas-Halo', font=fonte)],
        [sg.Combo(['Ausente', 'Sem halo amarelo', 'halo amarelo'], key='manchasHalo', enable_events=True,
                  readonly=True)],

        [sg.Text('Tamanho da Mancha', font=fonte)],
        [sg.Combo(['Nenhuma das alternativas', 'Abaixo de 1/8', 'Acima de 1/8'], key='tamanhodaMancha',
                  enable_events=True, readonly=True)],

        [sg.Text('Manchas de Folhas-Marg', font=fonte)],
        [sg.Combo(['Nenhuma das alternativas', 'no-w-s-marg', 'w-s-marg'], key='manchasdeFolhasMarg',
                  enable_events=True, readonly=True)],

        [sg.Text('Folhas', font=fonte)],
        [sg.Combo(['Anormal', 'Normal'], key='folhas', enable_events=True, readonly=True)]

    ]
    coluna3 = [
        [sg.Text('Alojamento', font=fonte)],
        [sg.Combo(['Não', 'Sim'], key='alojamento', enable_events=True, readonly=True)],

        [sg.Text('Crescimento de Mofo', font=fonte)],
        [sg.Combo(['Ausente', 'Presente'], key='crescimentodeMofo', enable_events=True, readonly=True)],

        [sg.Text('Micélio', font=fonte)],
        [sg.Combo(['Ausente', 'Presente'], key='micelio', enable_events=True, readonly=True)],

        [sg.Text('Crescimento da Planta', font=fonte)],
        [sg.Combo(['Anormal', 'Normal'], key='crescimentodaPlanta', enable_events=True, readonly=True)],

        [sg.Text('Estande de Plantas', font=fonte)],
        [sg.Combo(['Abaixo do normal', 'Normal'], key='estandedePlantas', enable_events=True, readonly=True)],

        [sg.Text('Precipício', font=fonte)],
        [sg.Combo(['Abaixo do normal', 'Normal', 'Acima do Normal'], key='precipício', enable_events=True,
                  readonly=True)],

        [sg.Text('Raízes', font=fonte)],
        [sg.Combo(['Cistos de Vesícula', 'Normal', 'Apodrecido'], key='raiz', enable_events=True, readonly=True)],

        [sg.Text('Sclerotia', font=fonte)],
        [sg.Combo(['Ausente', 'Presente'], key='sclerotia', enable_events=True, readonly=True)],

        [sg.Text('Semente', font=fonte)],
        [sg.Combo(['Anormal', 'Normal'], key='semente', enable_events=True, readonly=True)]

    ]
    coluna4 = [
        [sg.Text('Descoloração da Semente', font=fonte)],
        [sg.Combo(['Ausente ', 'Presente'], key='descoloracaodaSemente', enable_events=True, readonly=True)],

        [sg.Text('Tamanho da Semente', font=fonte)],
        [sg.Combo(['Abaixo do normal', 'Normal'], key='tamanhodaSemente', enable_events=True, readonly=True)],

        [sg.Text('Semente-Tmt', font=fonte)],
        [sg.Combo(['Nenhum', 'Fungicida', 'Outros'], key='sementeTmt', enable_events=True, readonly=True)],

        [sg.Text('Gravidade', font=fonte)],
        [sg.Combo(['Menor', 'Grave', 'Severo'], key='gravidade', enable_events=True, readonly=True)],

        [sg.Text('Murchando', font=fonte)],
        [sg.Combo(['Ausente', 'Presente'], key='murchando', enable_events=True, readonly=True)],

        [sg.Text('Tronco', font=fonte)],
        [sg.Combo(['Anormal', 'Normal'], key='tronco', enable_events=True, readonly=True)],

        [sg.Text('Cancros do Caule', font=fonte)],
        [sg.Combo(['Ausente', 'Abaixo do Solo', 'Acima do Solo', 'Acima do Segundo'], key='cancrosdoCaule',
                  enable_events=True, readonly=True)],

        [sg.Text('Temperatura', font=fonte)],
        [sg.Combo(['Abaixo do normal', 'Normal', 'Acima do Normal'], key='temperatura',
                  enable_events=True, readonly=True)]
    ]
    layout = [
        [sg.Column(coluna1), sg.Column(coluna2), sg.Column(coluna3), sg.Column(coluna4)],
        [sg.Text('', expand_x=True),
         sg.Button('Continuar', key='botao'),
         sg.Text('', expand_x=True),
         sg.Text('Limite CNF'),
         sg.Input('0', key='porcentagem', size=(3, 1)),
         sg.Text('%')
         ]
    ]
    return sg.Window('RBC-SOJA', layout=layout, finalize=True)

def janelaSecundaria(lista, lista2, lista3, cursor):
    listadoencas = []
    listaP1 = []
    listaP = []
    listaPP = []
    listaP1.append('area-damaged')
    listaP1.append('canker-lesion')
    listaP1.append('crop-hist')
    listaP1.append('date')
    listaP1.append('external decay')
    listaP1.append('fruit spots')
    listaP1.append('fruiting-bodies')
    listaP1.append('fruit-pods')
    listaP1.append('germination')
    listaP1.append('hail')
    listaP1.append('int-discolor')
    listaP1.append('leaf-malf')
    listaP1.append('leaf-mild')
    listaP1.append('leaf-shread')
    listaP1.append('leafspots-halo')
    listaP1.append('leafspot-size')
    listaP1.append('leafspots-marg')
    listaP1.append('leaves')
    listaP1.append('lodging')
    listaP1.append('mold-growth')
    listaP1.append('mycelium')
    listaP1.append('plant-growth')
    listaP1.append('plant-stand')
    listaP1.append('precip')
    listaP1.append('roots')
    listaP1.append('sclerotia')
    listaP1.append('seed')
    listaP1.append('seed-discolor')
    listaP1.append('seed-size')
    listaP1.append('seed-tmt')
    listaP1.append('severity')
    listaP1.append('shriveling')
    listaP1.append('stem')
    listaP1.append('stem-cankers')
    listaP1.append('temp')
    for n in range(len(listaP1)):
        listaP2 = [listaP1[n], lista[n]]
        listaP.append(listaP2)
    coluna1 = [
        [sg.Table(values=listaP, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'], auto_size_columns=False, expand_x=True, key='-TB-')]
    ]

    for casos in lista2: # ListaDoencas
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE Caso = ?", (casos[0],))
        resultado = cursor.fetchall()
        listadoencas.append(resultado[0])
    for n in range(len(lista2)):
        listaP3 = [lista2[n][0], listadoencas[n], str(lista3[n])+'%']
        listaPP.append(listaP3)
    coluna3 = [
        [sg.Table(values=listaPP, select_mode=sg.SELECT_MODE_BROWSE, headings=[' Caso ', 'Doenca', 'Porcentagem'], auto_size_columns=False, expand_x=True, key='-TB2-', enable_events=True)]
    ]
    layout = [
        [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna3)]
    ]
    return sg.Window('RBC-SOJA', layout=layout, finalize=True), listaPP, listaP

def janelaFinal(listaP, casoSel, cursor):
    lista = []
    coluna1 = [
        [sg.Table(values=listaP, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'],
                  auto_size_columns=False, expand_x=True, key='-TB3-')]
    ]
    cursor.execute("SELECT * FROM bancoprincipal WHERE Caso = ?", (casoSel,))
    resultado = cursor.fetchall()
    for n in range(len(listaP)):
        listaprov = [listaP[n][0], resultado[0][3+n]]
        lista.append(listaprov)
    coluna2 = [
        [sg.Table(values=lista, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'],
                  auto_size_columns=False, expand_x=True, key='-TB4-')]
    ]
    layout = [
        [sg.Text('Solução:' + resultado[0][2])],
        [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna2)]
    ]
    return sg.Window('RBC-SOJA', layout=layout, finalize=True)