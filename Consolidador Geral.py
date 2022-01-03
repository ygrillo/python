import os
import pandas as pd
import PySimpleGUI as sg

path = sg.popup_get_folder('Selecione a pasta dos arquivos')  # usuário seleciona a pasta

x = 0
try:
    try:
        file_path = f'{path}/Consolidado.xlsx'  # digo que o caminho é o caminho que selecionei + "/Consolidado..."
        os.remove(file_path)  # removo o arquivo consolidado antigo
        sg.popup_ok('Arquivo Consolidado.xlsx antigo removido')
    except Exception:
        pass

    files = []  # crio uma lista

    for i in os.listdir(path):  # leio cada arquivo do diretório 'path'
        fname = i  # fname recebe o nome de cada arquivo no diretório 'path' selecionado
        files.append(f'{path}/{fname}')  # acrescento na lista files o valor do 'path' + '/' + nome do arquivo

    df = pd.DataFrame()  # crio um dataframe usando o pandas

    for file in files:  # para cada arquivo na lista 'files', verifico se é '.xlsx' e acrescento no dataframe
        if file.endswith('.xlsx') or file.endswith('.XLSX'):
            df = df.append(pd.read_excel(file), ignore_index=True)
        x += 1  #  contador utilizado pelo PySimpleGUI para fazer a barra de progresso
        if not sg.one_line_progress_meter('Consolidador Geral', x + 0, len(files), '-key-'):  # barra de progresso
            break
    df.to_excel(f'{path}/Consolidado.xlsx', index=False)  # exporta em Excel o dataframe inteiro
    sg.Popup('Processo finalizado')

except ValueError:
    sg.popup_ok('Programa cancelado!')
except FileNotFoundError:
    sg.popup_ok('Nenhum arquivo selecionado')