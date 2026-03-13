import requests


def fetch_page(url):

    print("\n[LOG] Baixando página...")

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=15)

        print("[LOG] Status HTTP:", response.status_code)

        html = response.text

        print("[LOG] Tamanho do HTML:", len(html))

        if len(html) < 500:
            print("[WARNING] HTML muito pequeno. Pode ser bloqueio ou redirecionamento.")

        return html

    except Exception as e:

        print("[ERRO] Falha ao acessar página:", e)

        return ""
