import shutil
import os
import PySimpleGUI as sg

oldAdress = sg.popup_get_folder('Selecione a pasta que quer organizar')  # pasta origem
newAdresspdf = sg.popup_get_folder('Selecione a pasta dos PDFs')  # pasta destino PDF
newAdresstxt = sg.popup_get_folder('Selecione a pasta dos Textos')  # pasta destino TXT
newAdressppt = sg.popup_get_folder('Selecione a pasta dos PowerPoints')  # pasta destino PowerPoint
newAdressdoc = sg.popup_get_folder('Selecione a pasta dos Words')  # pasta destino DOC
newAdressxl = sg.popup_get_folder('Selecione a pasta das Planilhas Excel')  # pasta destino Excel
newAdressimg = sg.popup_get_folder('Selecione a pasta das Imagens')  # pasta destino imagens
newAdressvid = sg.popup_get_folder('Selecione a pasta dos Vídeos')  # pasta destino videos

files = []  # crio uma lista

for i in os.listdir(oldAdress):  # leio cada arquivo do diretório 'oldAdress'
    fname = i  # fname recebe o nome de cada arquivo no diretório 'oldAdress' selecionado
    files.append(f'{oldAdress}/{fname}')  # acrescento na lista files o valor do 'oldAdress' + '/' + nome do arquivo

# Contadores
cnt_pdf = 0
cnt_txt = 0
cnt_ppt = 0
cnt_doc = 0
cnt_xl = 0
cnt_img = 0
cnt_vid = 0

# Contadores erro
err_pdf = 0
err_txt = 0
err_ppt = 0
err_doc = 0
err_xl = 0
err_img = 0
err_vid = 0

i = 0
while i < len(files):
    if files[i].endswith('.pdf') or files[i].endswith('.PDF'):
        try:
            shutil.move(files[i], newAdresspdf)
            cnt_pdf += 1
        except shutil.Error:
            err_pdf += 1
            pass
    elif files[i].endswith('.txt') or files[i].endswith('.TXT') or files[i].endswith('.log'):
        try:
            shutil.move(files[i], newAdresstxt)
            cnt_txt += 1
        except shutil.Error:
            err_txt += 1
            pass
    elif files[i].endswith('.ppt') or files[i].endswith('.pptx'):
        try:
            shutil.move(files[i], newAdressppt)
            cnt_ppt += 1
        except shutil.Error:
            err_ppt += 1
            pass
    elif files[i].endswith('.doc') or files[i].endswith('.docx') or files[i].endswith('.rtf'):
        try:
            shutil.move(files[i], newAdressdoc)
            cnt_doc += 1
        except shutil.Error:
            err_doc += 1
            pass
    elif files[i].endswith('.xls') or \
            files[i].endswith('.xlsm') or \
            files[i].endswith('.xlsx') or \
            files[i].endswith('.csv') or \
            files[i].endswith('.xlsb') or \
            files[i].endswith('.XLSX') or \
            files[i].endswith('.xltx'):
        try:
            shutil.move(files[i], newAdressxl)
            cnt_xl += 1
        except shutil.Error:
            err_xl += 1
            pass
    elif files[i].endswith('.png') or \
            files[i].endswith('.jpg') or \
            files[i].endswith('.jpeg') or \
            files[i].endswith('.bmp') or \
            files[i].endswith('.gif'):
        try:
            shutil.move(files[i], newAdressimg)
            cnt_img += 1
        except shutil.Error:
            err_img += 1
            pass
    elif files[i].endswith('.mp4') or \
            files[i].endswith('.avi') or \
            files[i].endswith('.wmv') or \
            files[i].endswith('.mkv'):
        try:
            shutil.move(files[i], newAdressvid)
            cnt_vid += 1
        except shutil.Error:
            err_vid += 1
            pass

    i += 1

layout = [[sg.Text('Processo finalizado!')],
          [sg.Text(f'PDFs movidos: {cnt_pdf}. {err_pdf} erros')],
          [sg.Text(f'Textos movidos: {cnt_txt}. {err_txt} erros')],
          [sg.Text(f'PowerPoints movidos: {cnt_ppt}. {err_ppt} erros')],
          [sg.Text(f'Words movidos: {cnt_doc}. {err_doc} erros')],
          [sg.Text(f'Planilhas movidas: {cnt_xl}. {err_xl} erros')],
          [sg.Text(f'Imagens movidas: {cnt_img}. {err_img} erros')],
          [sg.Text(f'Vídeos movidos: {cnt_vid}. {err_vid} erros')],
          [sg.Button('Ok', size=(10, 1))]]

window = sg.Window('Arquivos movidos', layout, element_justification='c')

while True:
    event, values = window.Read()
    if event is None or event == 'Ok':
        break
window.Close()
