import os
import json
from graphviz import Digraph

os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"


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
    generate_diagram(data)


def save_json(data):

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/funnel_report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("[LOG] Relatório JSON salvo em outputs/funnel_report.json")


def save_markdown(data):

    os.makedirs("outputs", exist_ok=True)

    md = "# Funnel Architecture Report\n\n"

    for key, value in data.items():

        if not value:
            value = "Not detected"

        md += f"**{key}:** {value}\n\n"

    with open("outputs/funnel_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("[LOG] Relatório Markdown salvo em outputs/funnel_report.md")


def generate_diagram(data):

    os.makedirs("outputs", exist_ok=True)

    diagram = Digraph(comment="Funnel Architecture")

    diagram.attr(rankdir="TB")

    cms = data.get("CMS", "Landing Page")
    video = data.get("Video Platform", "Video")
    automation = data.get("Automation Tools", "Automation")
    checkout = data.get("Checkout Platforms", "Checkout")

    diagram.node("A", f"Landing Page\n{cms}")
    diagram.node("B", f"VSL\n{video}")
    diagram.node("C", f"Automation\n{automation}")
    diagram.node("D", f"Checkout\n{checkout}")

    diagram.edge("A", "B")
    diagram.edge("B", "C")
    diagram.edge("C", "D")

    output_path = "outputs/funnel_architecture"

    diagram.render(output_path, format="png", cleanup=True)

    print("[LOG] Diagrama salvo em outputs/funnel_architecture.png")
