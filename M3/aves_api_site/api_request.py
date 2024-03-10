import requests
import json
#Me sirvio la funcion del ejercicio anterior jeje

def api_request(method: str, url: str, payload=None, headers=None):
    """Función para realizar peticiones a una API

    Args:
        method (string): String con la url
        url (string): Metodo GET, PUT, POST, DELETE
        payload (dict, optional): Datos para enviar. Defaults to None.
        headers (dict, optional): Cabeceras especiales para la solicitud. Defaults to None.

    Returns:
        Dict: Respuesta de la API y el código de estado
    """    
    try:
        response = requests.request(method, url, data=payload, headers=headers)
        if response.status_code == 204:
            return response.status_code
        response_dict = json.loads(response.text)
        return response_dict, response.status_code
    except requests.exceptions.RequestException as e:
        print("Ocurrio un error de conexión")
        return None, 404