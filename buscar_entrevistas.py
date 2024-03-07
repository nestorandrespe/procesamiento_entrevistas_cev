import requests
import json
import argparse
import os
import desanonimizar_json
import armar_documentos

resultados = []

def obtener_id(identifier):
    with open('assets/listado_equivalencia.csv', 'r') as f:
        data = f.readlines()
        for d in data:
            d = d.strip()
            if d.split(',')[1] == identifier:
                return d.split(',')[0]

def buscar_entrevistas(output_folder, query, pages=1, limit=False):
    from_number = 0

    while from_number < int(pages) * 10:
        payload = {'q': query, 'from': from_number, 'size': 10, 'source': 'museo', 'user': 1, 'fondo': ["001-EV"]}
        response = requests.post('https://api.archivo.comisiondelaverdad.co/api/search', json=payload)
        data = response.json()

        for d in data['hits']:
            from_number += 1
            if limit and from_number > int(limit):
                from_number = int(pages) * 10
                break
            ident = d['_source']['document']['ident']
            id_ = obtener_id(ident)
            print(id_, ident)
            

            filename = output_folder + 'json/entrevistas_single_' + id_ + '.json'
            if not os.path.exists(filename):
                entrevista_path = 'entrevistas/entrevistas_single_' + id_ + '.json'
                desanonimizar_json.desanonimizar_json(entrevista_path, output_folder)

            armar_documentos.armar_documentos(filename, output_folder)

            resultados.append({
                'id': id_,
                'identifier': ident,
                'filename': 'entrevistas_single_' + id_
            })

        if not os.path.exists(output_folder + 'busquedas'):
            os.makedirs(output_folder + 'busquedas')

        with open(output_folder + 'busquedas/' + query + '.csv', 'w') as f:
            f.write('id,identifier,filename\n')
            for r in resultados:
                f.write(r['id'] + ',' + r['identifier'] + ',' + r['filename'] + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--limit', type=str, default=False, required=False)
    args = parser.parse_args()

    query = input('Ingrese la busqueda: ')
    pages = input('Ingrese el numero máximo de paginas (son 10 resultados por página): ')

    if pages.isdigit():
        buscar_entrevistas(args.output, query, pages, args.limit)
    else:
        print('El número de páginas debe ser un número entero')