from Campana import Campana
import os
from datetime import datetime

if __name__ == '__main__':
    try:
        campana = Campana('Campana', '2021-01-01', '2021-12-31')
        campana.agregar_anuncio('video', ancho=1920, alto=1080, url_archivo='video.mp4', url_click='https://www.ejemplo.com', sub_tipo='instream', duracion=10)
        campana.nombre = input('Ingrese el nombre de la campaña: ')
        campana.anuncios[0].sub_tipo = input('Ingrese el subtipo del anuncio: ')
    except Exception as e:
        with open(os.path.join(os.path.dirname(__file__), 'error.log'), 'a') as log:
            log.write(f'{datetime.now()} - {e}\n')