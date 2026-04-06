import requests 
import json
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def extract_weather_data(url: str) -> list:
    response = requests.get(url)
    #transformando a resposta em um dicionario python 
    data = response.json()

    if response.status_code != 200:
        logging.error("Erro na requisição")
        return []
    
    if not data:
        logging.warn("Nehum dado retornado")
        return[]

    #CRIANDO O PATH do data
    output_path = 'data/weather_data.json'
    # criando o diretorio
    output_dir = Path(output_path).parent
    #parents=true vai trazer todo o caminho
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
    #Diferente do json.dumps(), que transforma um objeto em uma string, o json.dump() faz a conversão e já salva o resultado no disco. 
        json.dump(data, f, indent=4)

    logging.info(f"Arquivo salvo em {output_path}")
    return data    


