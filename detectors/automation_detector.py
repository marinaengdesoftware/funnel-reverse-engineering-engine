def detect_automation(html):

    tools = []

    if "sleekflow" in html:
        tools.append("Sleekflow")

    if "activecampaign" in html:
        tools.append("ActiveCampaign")

    if "mailchimp" in html:
        tools.append("Mailchimp")

    return tools
