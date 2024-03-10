import requests
import json
URL = "https://reqres.in/api/users"

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


if __name__ == "__main__":
    users_data, r_code = api_request("GET", URL)

    if r_code != 200:
        print(f"Ocurrio un error {r_code}")
        exit()

    print("Usuarios:")
    for user in users_data['data']:
        print(f'{user["id"]}: {user["first_name"]} {user["last_name"]}')

    nuevo_usuario = {'name': 'Ignacio', 'job': 'Profesor'}

    created_user, r_code = api_request("POST", URL, nuevo_usuario)

    if r_code != 201:
        print(f"Ocurrio un error {r_code}")
        exit()

    print(f"Usuario creado:\n{created_user}")

    updated_user = {
    "name": "morpheus",
    "job": "zion resident",
    "residence": "zion"
    }

    updated_user, r_code = api_request("PUT", f"{URL}/2", updated_user)

    if r_code != 200:
        print(f"Ocurrio un error {r_code}")
        exit()

    print(f"Usuario actualizado:\n{updated_user}")

    # Asumnumos que el id ya lo sabemos
    r_code = api_request("DELETE", f"{URL}/6")

    print(f"Usuario eliminado con código {r_code}")