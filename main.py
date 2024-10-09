import sqlite3
import pandas as pd
import PySimpleGUI as sg
from collections import Counter
from Interface import *


df = pd.read_excel("C:/Users/Luís/Documents/Faculdade/IA/RBC-SOJA/Base_Dados.xlsx")
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
df.to_sql("bancoprincipal", banco, if_exists="replace")
mult = 0
doencasList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
selecionado = ['Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido']
selecionado2 = []
selecionado3 = []
ids = []
valor = ''
num = 0
janelaP, janelaS, janelaF = janelaInicial(), None, None


while True:
    janela, eventos, valores = sg.read_all_windows()
    if eventos == 'areaDamaged':
        mult = 3
        if valores['areaDamaged'] == 'Baixas Áreas':
            valor = 'low-areas'
        if valores['areaDamaged'] == 'Espalhado':
            valor = 'scattered'
        if valores['areaDamaged'] == 'Áreas Superiores':
            valor = 'upper-areas'
        if valores['areaDamaged'] == 'Campo Inteiro':
            valor = 'whole-field'
        num = 0
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE areaDamaged = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE areaDamaged = ?", (valor,))
    if eventos == 'canker-lesion':
        mult = 7
        if valores['canker-lesion'] == 'Sem Resposta':
            valor = 'dna'
        if valores['canker-lesion'] == 'Marrom':
            valor = 'Brown'
        if valores['canker-lesion'] == 'dk-marrom-blk':
            valor = 'dk-brown-blk'
        if valores['canker-lesion'] == 'Bronzeado':
            valor = 'tan'
        num = 1
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE cankerLesion = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE cankerLesion = ?", (valor,))
    if eventos == 'crop-hist':
        mult = 1
        if valores['crop-hist'] == 'Diferente do primeiro ano':
            valor = 'diff-1st-year'
        if valores['crop-hist'] == 'Mesmo do primeiro ano':
            valor = 'same-1st-yr'
        if valores['crop-hist'] == 'Mesmo do ultimo ano':
            valor = 'same-lst-sev-yrs'
        if valores['crop-hist'] == 'Mesmo do ultimo dois anos':
            valor = 'same-lst-two-yrs'
        num = 2
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE cropHist = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE cropHist = ?", (valor,))
    if eventos == 'date':
        mult = 2
        num = 3
        valor = valores['date']
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE date = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE date = ?", (valor,))
    if eventos == 'external decay':
        mult = 7
        if valores['external decay'] == 'Ausente':
            valor = 'Absent'
        if valores['external decay'] == 'Firme e Seco':
            valor = 'firm-and-dry'
        num = 4
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE externalDecay = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE externalDecay = ?", (valor,))
    if eventos == 'manchasdeFrutas':
        mult = 7
        if valores['manchasdeFrutas'] == 'Não tem resposta':
            valor = 'dna'
        if valores['manchasdeFrutas'] == 'Ausente':
            valor = 'Absent'
        if valores['manchasdeFrutas'] == 'Marrom com manchas pretas':
            valor = 'Brown-w/blk-specks'
        if valores['manchasdeFrutas'] == 'Colorido':
            valor = 'Colored'
        num = 5
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE fruitSpots = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE fruitSpots = ?", (valor,))
    if eventos == 'corposdeFrutificacao':
        mult = 7
        if valores['corposdeFrutificacao'] == 'Ausente':
            valor = 'Absent'
        if valores['corposdeFrutificacao'] == 'Presente':
            valor = 'Present'
        num = 6
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE fruitingBodies = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE fruitingBodies = ?", (valor,))
    if eventos == 'vagensdeFrutas':
        mult = 8
        if valores['vagensdeFrutas'] == 'Não tem resposta':
            valor = 'dna'
        if valores['vagensdeFrutas'] == 'pouco presente':
            valor = 'few-present'
        if valores['vagensdeFrutas'] == 'Normal':
            valor = 'Norm'
        if valores['vagensdeFrutas'] == 'Doente':
            valor = 'Diseased'
        num = 7
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE fruitPods = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE fruitPods = ?", (valor,))
    if eventos == 'germinacao':
        mult = 1
        if valores['germinacao'] == '80-89 %':
            valor = '80-89 %'
        if valores['germinacao'] == 'abaixo de 80%':
            valor = 'lt-80%'
        if valores['germinacao'] == '90-100%':
            valor = '90-100%'
        num = 8
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE germination = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE germination = ?", (valor,))
    if eventos == 'saudacao':
        mult = 3
        if valores['saudacao'] == 'Não':
            valor = 'No'
        if valores['saudacao'] == 'Sim':
            valor = 'Yes'
        num = 9
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE hail = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE hail = ?", (valor,))
    if eventos == 'descoloracao':
        mult = 8
        if valores['descoloracao'] == 'Nenhum':
            valor = 'None'
        if valores['descoloracao'] == 'Preto':
            valor = 'Black'
        num = 10
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE intDiscolor = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE intDiscolor = ?", (valor,))
    if eventos == 'folhaMalf':
        mult = 7
        if valores['folhaMalf'] == 'Ausente':
            valor = 'Absent'
        if valores['folhaMalf'] == 'Presente':
            valor = 'Present'
        num = 11
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE leafMalf = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE leafMalf = ?", (valor,))
    if eventos == 'folhaSuave':
        mult = 8
        if valores['folhaSuave'] == 'Ausente':
            valor = 'Absent'
        if valores['folhaSuave'] == 'Baixo surf':
            valor = 'Lower-surf'
        if valores['folhaSuave'] == 'Alto surf':
            valor = 'Upper-surf'
        num = 12
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE leafMild = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE leafMild = ?", (valor,))
    if eventos == 'folhagem':
        mult = 7
        if valores['folhagem'] == 'Ausente':
            valor = 'absent'
        if valores['folhagem'] == 'Presente':
            valor = 'Present'
        num = 13
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE leafShread = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE leafShread = ?", (valor,))
    if eventos == 'manchasHalo':
        mult = 6
        if valores['manchasHalo'] == 'Ausente':
            valor = 'absent'
        if valores['manchasHalo'] == 'Sem halo amarelo':
            valor = 'no-yellow-halos'
        if valores['manchasHalo'] == 'halo amarelo':
            valor = 'yellow-halos'
        num = 14
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE leafspotsHalo = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE leafspotsHalo = ?", (valor,))
    if eventos == 'tamanhodaMancha':
        mult = 7
        if valores['tamanhodaMancha'] == 'Nenhuma das alternativas':
            valor = 'dna'
        if valores['tamanhodaMancha'] == 'Acima de 1/8':
            valor = 'gt-1/8'
        if valores['tamanhodaMancha'] == 'Abaixo de 1/8':
            valor = 'lt-1/8'
        num = 15
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE leafspotSize = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE leafspotSize = ?", (valor,))
    if eventos == 'manchasdeFolhasMarg':
        mult = 7
        if valores['manchasdeFolhasMarg'] == 'Nenhuma das alternativas':
            valor = 'dna'
        if valores['manchasdeFolhasMarg'] == 'no-w-s-marg':
            valor = 'no-w-s-marg'
        if valores['manchasdeFolhasMarg'] == 'w-s-marg':
            valor = 'w-s-marg'
        num = 16
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE leafspotsMarg = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE leafspotsMarg = ?", (valor,))
    if eventos == 'folhas':
        mult = 8
        if valores['folhas'] == 'Anormal':
            valor = 'Abnorm'
        if valores['folhas'] == 'Normal':
            valor = 'Norm'
        num = 17
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE leaves = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE leaves = ?", (valor,))
    if eventos == 'alojamento':
        mult = 6
        if valores['alojamento'] == 'Não':
            valor = 'No'
        if valores['alojamento'] == 'Sim':
            valor = 'Yes'
        num = 18
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE lodging = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE lodging = ?", (valor,))
    if eventos == 'crescimentodeMofo':
        mult = 8
        if valores['crescimentodeMofo'] == 'Ausente':
            valor = 'Absent'
        if valores['crescimentodeMofo'] == 'Presente':
            valor = 'Present'
        num = 19
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE moldGrowth = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE moldGrowth = ?", (valor,))
    if eventos == 'micelio':
        mult = 8
        if valores['micelio'] == 'Ausente':
            valor = 'Absent'
        if valores['micelio'] == 'Presente':
            valor = 'Present'
        num = 20
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE mycelium = ?", (valor,))
        results = cursor.fetchall()
        ids.append(results[0])
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE mycelium = ?", (valor,))
    if eventos == 'crescimentodaPlanta':
        mult = 8
        if valores['crescimentodaPlanta'] == 'Anormal':
            valor = 'Abnorm'
        if valores['crescimentodaPlanta'] == 'Normal':
            valor = 'Norm'
        num = 21
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE plantGrowth = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE plantGrowth = ?", (valor,))
    if eventos == 'estandedePlantas':
        mult = 5
        if valores['estandedePlantas'] == 'Abaixo do normal':
            valor = 'lt-normal'
        if valores['estandedePlantas'] == 'Normal':
            valor = 'Normal'
        num = 22
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE plantStand = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE plantStand = ?", (valor,))
    if eventos == 'precipício':
        mult = 6
        if valores['precipício'] == 'Abaixo do normal':
            valor = 'lt-normal'
        if valores['precipício'] == 'Normal':
            valor = 'gt-normal'
        if valores['precipício'] == 'Acima do Normal':
            valor = 'Normal'
        num = 23
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE precip = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE precip = ?", (valor,))
    if eventos == 'raiz':
        mult = 8
        if valores['raiz'] == 'Cistos de Vesícula':
            valor = 'galls-cysts'
        if valores['raiz'] == 'Normal':
            valor = 'Norm'
        if valores['raiz'] == 'Apodrecido':
            valor = 'Rotted'
        num = 24
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE roots = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE roots = ?", (valor,))
    if eventos == 'sclerotia':
        mult = 8
        if valores['sclerotia'] == 'Ausente':
            valor = 'Absent'
        if valores['sclerotia'] == 'Presente':
            valor = 'Present'
        num = 25
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE sclerotia = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE sclerotia = ?", (valor,))
    if eventos == 'semente':
        mult = 7
        if valores['semente'] == 'Anormal':
            valor = 'Abnorm'
        if valores['semente'] == 'Normal':
            valor = 'Norm'
        num = 26
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE seed = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE seed = ?", (valor,))
    if eventos == 'descoloracaodaSemente':
        mult = 7
        if valores['descoloracaodaSemente'] == 'Ausente ':
            valor = 'Absent'
        if valores['descoloracaodaSemente'] == 'Presente':
            valor = 'Present'
        num = 27
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE seedDiscolor = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE seedDiscolor = ?", (valor,))
    if eventos == 'tamanhodaSemente':
        mult = 8
        if valores['tamanhodaSemente'] == 'Abaixo do normal':
            valor = 'lt-norm'
        if valores['tamanhodaSemente'] == 'Normal':
            valor = 'Norm'
        num = 28
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE seedSize = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE seedSize = ?", (valor,))
    if eventos == 'sementeTmt':
        mult = 1
        if valores['sementeTmt'] == 'Nenhum':
            valor = 'none'
        if valores['sementeTmt'] == 'Fungicida':
            valor = 'fungicida'
        if valores['sementeTmt'] == 'Outros':
            valor = 'Outros'
        num = 29
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE seedTmt = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE seedTmt = ?", (valor,))
    if eventos == 'gravidade':
        mult = 3
        if valores['gravidade'] == 'Menor':
            valor = 'Minor'
        if valores['gravidade'] == 'Grave':
            valor = 'pot-severe'
        if valores['gravidade'] == 'Severo':
            valor = 'severe'
        num = 30
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE severity = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE severity = ?", (valor,))
    if eventos == 'murchando':
        mult = 8
        if valores['murchando'] == 'Ausente':
            valor = 'Absent'
        if valores['murchando'] == 'Presente':
            valor = 'Present'
        num = 31
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE shriveling = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE shriveling = ?", (valor,))
    if eventos == 'tronco':
        mult = 8
        if valores['tronco'] == 'Anormal':
            valor = 'Abnorm'
        if valores['tronco'] == 'Normal':
            valor = 'Norm'
        num = 32
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE stem = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE stem = ?", (valor,))
    if eventos == 'cancrosdoCaule':
        mult = 7
        if valores['cancrosdoCaule'] == 'Ausente':
            valor = 'Absent'
        if valores['cancrosdoCaule'] == 'Abaixo do Solo':
            valor = 'below-soil'
        if valores['cancrosdoCaule'] == 'Acima do Solo':
            valor = 'Above-soil'
        if valores['cancrosdoCaule'] == 'Acima do Segundo':
            valor = 'Above-sec-nde'
        num = 33
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE stemCankers = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE stemCankers = ?", (valor,))
    if eventos == 'temperatura':
        mult = 4
        if valores['temperatura'] == 'Abaixo do normal':
            valor = 'lt-norm'
        if valores['temperatura'] == 'Normal':
            valor = 'norm'
        if valores['temperatura'] == 'Acima do Normal':
            valor = 'gt-norm'
        num = 34
        cursor.execute("SELECT Caso FROM bancoprincipal WHERE temp = ?", (valor,))
        results = cursor.fetchall()
        ids.extend(results)
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE temp = ?", (valor,))
    if eventos == sg.WINDOW_CLOSED:
        break
        #Fechar
    if eventos == 'botao':
        contador = Counter(ids)
        moda = contador.most_common(1)[0][0]
        quantMinima = (float(valores['porcentagem']) / 100) * 35
        while moda:
            if contador[moda] >= quantMinima:
                selecionado2.append(moda)
                quantAtual = (contador[moda]*100)/35
                selecionado3.append(round(quantAtual, 1))
            ids = [item for item in ids if item != moda]
            contador = Counter(ids)
            try:
                moda = contador.most_common(1)[0][0]
            except IndexError as ie:
                moda = False
        janelaS, listaPP, listaP = janelaSecundaria(selecionado, selecionado2, selecionado3, cursor)
    if janela == janelaP and eventos != 'botao':
        selecionado[num] = valor
        results = cursor.fetchall()
        for row in results:
            if row[0] == 'diaporthe-stem-canker':
                doencasList[0] += mult
            if row[0] == 'charcoal-rot':
                doencasList[1] += mult
            if row[0] == 'rhizoctonia-root-rot':
                doencasList[2] += mult
            if row[0] == 'phytophthora-rot':
                doencasList[3] += mult
            if row[0] == 'brown-stem-rot':
                doencasList[4] += mult
            if row[0] == 'powdery-mildew':
                doencasList[5] += mult
            if row[0] == 'downy-mildew':
                doencasList[6] += mult
            if row[0] == 'brown-spot':
                doencasList[7] += mult
            if row[0] == 'bacterial-blight':
                doencasList[8] += mult
            if row[0] == 'bacterial-pustule':
                doencasList[9] += mult
            if row[0] == 'purple-seed-stain':
                doencasList[10] += mult
            if row[0] == 'anthracnose':
                doencasList[11] += mult
            if row[0] == 'phyllosticta-leaf-spot':
                doencasList[12] += mult
            if row[0] == 'alternarialeaf-spot':
                doencasList[13] += mult
            if row[0] == 'frog-eye-leaf-spot':
                doencasList[14] += mult
            if row[0] == 'diaporthe-pod-&-stem-blight':
                doencasList[15] += mult
            if row[0] == 'cyst-nematode':
                doencasList[16] += mult
            if row[0] == '2-4-d-injury':
                doencasList[17] += mult
            if row[0] == 'herbicide-injury':
                doencasList[18] += mult
    if eventos == '-TB2-':
        casoSelecionado = listaPP[valores['-TB2-'][0]][0]
        janelaF = janelaFinal(listaP, casoSelecionado, cursor)
