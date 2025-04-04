import string
import random

def cleaner(client_list):
    """Limpia la lista de clientes eliminando espacios en blanco y duplicados"""
    client_list = delete_blank_spaces(client_list)
    client_list = remove_null_values(client_list)
    client_list = capitalize_names(client_list)
    client_list = remove_duplicates(client_list)
    return client_list

def capitalize_names(client_list):
    """Capitaliza la primera letra de cada nombre y apellido, y lo convierte a minúsculas"""
    return [client.title() for client in client_list if client and client.strip()]

def delete_blank_spaces(client_list):
    """Elimina espacios en blanco al inicio y al final de cada nombre"""
    return [client.strip() for client in client_list if client and client.strip()]

def remove_duplicates(client_list):
    """Elimina nombres duplicados"""
    return list(set(client_list))

def remove_null_values(client_list):
    """Elimina valores nulos de la lista"""
    return [client for client in client_list if client is not None or ""]

def isValidUser(user):
    """Verifico que el usuario tenga 15 o menos caracteres"""
    if len(user) <= 15:
        return True
    else:
        print("El nombre de usuario no cumple con los requisitos")
        return False
    
def isValidDate(date):
    """Verifico que la fecha tenga el formato correcto"""
    if len(date) == 10:
        return True
    else:
        print("Formato de fecha incorrecto")
        return False

def codeGenerator(user, date):
    """Genero el codigo de descuento"""
    #Calculo la cantidad de caracteres restantes para completar 30
    cant = 30 - len(user) - len(date.replace('-','')) - 2

    #Devuelvo el codigo de descuento con formato USER-DATE-RANDOM
    return f"{user.upper()}-{date.replace('-','')}-{''.join(random.choices(string.ascii_uppercase+string.digits, k=cant))}"