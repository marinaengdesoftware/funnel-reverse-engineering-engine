def detect_pixels(html):

    html = html.lower()

    pixels = []

    if "facebook.net" in html or "fbq(" in html:
        pixels.append("Facebook Pixel")

    if "google-analytics.com" in html or "gtag(" in html:
        pixels.append("Google Analytics")

    if "googletagmanager.com" in html:
        pixels.append("Google Tag Manager")

    if "clarity.ms" in html:
        pixels.append("Microsoft Clarity")

    if "tiktok" in html:
        pixels.append("TikTok Pixel")

    return pixels
