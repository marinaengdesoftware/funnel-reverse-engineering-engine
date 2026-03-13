def detect_cms(html):

    if "wp-content" in html or "wordpress" in html:
        return "WordPress"

    if "shopify" in html:
        return "Shopify"

    if "wix.com" in html:
        return "Wix"

    return "Unknown"
