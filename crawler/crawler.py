import requests

def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except Exception as e:
        print("Erro ao acessar página:", e)
        return ""
