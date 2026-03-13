def detect_checkout(html):

    checkouts = []

    if "hotmart" in html:
        checkouts.append("Hotmart")

    if "kiwify" in html:
        checkouts.append("Kiwify")

    if "stripe" in html:
        checkouts.append("Stripe")

    return checkouts
