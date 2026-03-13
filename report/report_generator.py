import json
import os


def generate_report(data):

    print("\n==========================")
    print(" FUNNEL TECH REPORT ")
    print("==========================\n")

    for key, value in data.items():

        if not value:
            value = "Not detected"

        print(f"{key}: {value}")

    print("\n==========================\n")

    save_json(data)
    save_markdown(data)


def save_json(data):

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/funnel_report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("[LOG] Relatório JSON salvo em outputs/funnel_report.json")


def save_markdown(data):

    os.makedirs("outputs", exist_ok=True)

    md = "# Funnel Architecture Report\n\n"

    for key, value in data.items():
        md += f"**{key}:** {value}\n\n"

    with open("outputs/funnel_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("[LOG] Relatório Markdown salvo em outputs/funnel_report.md")
