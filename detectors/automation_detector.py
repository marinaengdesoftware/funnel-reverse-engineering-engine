def detect_automation(html):

    html = html.lower()

    tools = []

    if "sleekflow" in html:
        tools.append("Sleekflow")

    if "activecampaign" in html:
        tools.append("ActiveCampaign")

    if "mailchimp" in html:
        tools.append("Mailchimp")

    if "hubspot" in html:
        tools.append("HubSpot")

    if "rdstation" in html:
        tools.append("RD Station")

    return tools
