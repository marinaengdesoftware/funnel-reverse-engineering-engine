def detect_checkout(html):

    html = html.lower()

    checkouts = []

    if "hotmart" in html:
        checkouts.append("Hotmart")

    if "kiwify" in html:
        checkouts.append("Kiwify")

    if "monetizze" in html:
        checkouts.append("Monetizze")

    if "eduzz" in html:
        checkouts.append("Eduzz")

    if "stripe" in html:
        checkouts.append("Stripe")

    return checkouts
