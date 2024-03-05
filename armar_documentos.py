import json
import argparse
import os
from docx import Document

# funcion para armar documentos
def armar_documentos(json_file, output_folder):
    with open(json_file, 'r') as f:
        data = json.load(f)

    documento = []

    # se iteran sobre los elementos del json
    for i, d in enumerate(data):
        respuesta = d['respuesta']

        documento.append(respuesta)

    texto = '\n'.join(documento)
    
    # se crea el documento
    doc = Document()
    doc.add_paragraph(texto)
    
    # si la carpeta documentos no existe, se crea
    if not os.path.exists(output_folder + '/documentos'):
        os.makedirs(output_folder + '/documentos')

    # se guarda el documento con el mismo nombre que el json
    doc.save(output_folder + '/documentos/' + json_file.split('/')[-1].split('.')[0] + '.docx')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_file', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    armar_documentos(args.json_file, args.output)