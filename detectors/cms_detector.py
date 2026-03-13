def detect_cms(html):

    html = html.lower()

    if "wp-content" in html or "wordpress" in html:
        return "WordPress"

    if "shopify" in html:
        return "Shopify"

    if "wix.com" in html:
        return "Wix"

    if "squarespace" in html:
        return "Squarespace"

    if "webflow" in html:
        return "Webflow"

    return "Unknown"
