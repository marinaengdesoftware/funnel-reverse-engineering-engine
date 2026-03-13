def detect_pixels(html):

    pixels = []

    if "connect.facebook.net" in html:
        pixels.append("Facebook Pixel")

    if "google-analytics.com" in html:
        pixels.append("Google Analytics")

    if "googletagmanager.com" in html:
        pixels.append("Google Tag Manager")

    return pixels
