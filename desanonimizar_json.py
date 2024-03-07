import json
import argparse
import openai
import os

from templates import departamentos, instrucciones

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

respuestas = []

# funcion para obtener una respuesta de openai
def getResponse(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content":"Eres un asistente de redación de contenido para desanonimizar textos."
            },
            {
            "role": "user",
            "content": text
            }
        ],
        temperature=1,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

# funcion para desanonimizar un texto
def desanonimizar_json(json_file, output_folder):
    with open(json_file, 'r') as f:
        data = json.load(f)

    text = data['text']

    for i in range(1, 8):
        text = text.replace(f'ENT {i}', 'ENT')
        text = text.replace(f'ENT{i}', 'ENT')

    for i in range(1, 8):
        text = text.replace(f'TEST {i}', 'TEST')
        text = text.replace(f'TEST{i}', 'TEST')

    # separar el texto por párrafos, un párrafo por ejemplo es una pregunta que empieza por ENT
    paragraphs = text.split('ENT:')
    # se vuelve a añadir el prefijo ENT a cada párrafo
    paragraphs = ['ENT:' + p for p in paragraphs]

    

    # se itera sobre cada párrafo y se desanonimiza
    for i, p in enumerate(paragraphs):
        resp = {
            'original': p,
            'respuesta': p
        }

        # si el parrafo no tiene --- no se desanonimiza
        if '---' not in p:
            respuestas.append(resp)
            continue
        
        # eliminar saltos de línea a p
        p = p.replace('\n', ' ')

        # se obtiene la respuesta de openai
        response = getResponse(instrucciones.format(p))

        resp['respuesta'] = response
        # se añade la respuesta a la lista de respuestas
        respuestas.append(resp)

    # se guarda la lista de respuestas en un archivo json en la carpeta /json dentro de output_folder con el mismo nombre que el archivo de entrada. si la carpeta no existe se crea
    if not os.path.exists(output_folder + '/json'):
        os.makedirs(output_folder + '/json')
    
    with open(output_folder + '/json/' + os.path.basename(json_file), 'w') as f:
        json.dump(respuestas, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_file', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    desanonimizar_json(args.json_file, args.output)