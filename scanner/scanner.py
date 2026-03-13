import requests

def scan_site(url):
    response = requests.get(url)
    html = response.text

    results = {}

    # CMS
    if "wp-content" in html:
        results["CMS"] = "WordPress"

    # Vimeo
    if "vimeo.com" in html:
        results["Video Platform"] = "Vimeo"

    # Facebook Pixel
    if "facebook.net" in html:
        results["Facebook Pixel"] = "Detected"

    # Google Analytics
    if "google-analytics.com" in html:
        results["Google Analytics"] = "Detected"

    return results


if __name__ == "__main__":
    url = input("Digite a URL: ")
    data = scan_site(url)

    print("\nFUNNEL TECH REPORT\n")

    for key, value in data.items():
        print(f"{key}: {value}")
