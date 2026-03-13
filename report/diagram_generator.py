from graphviz import Digraph
import os


def generate_diagram(data):

    os.makedirs("outputs", exist_ok=True)

    diagram = Digraph(comment="Funnel Architecture")

    diagram.attr(rankdir="TB")

    # nodes
    cms = data.get("CMS", "Landing Page")
    video = data.get("Video Platform", "Video")
    automation = data.get("Automation Tools", "Automation")
    checkout = data.get("Checkout Platforms", "Checkout")

    diagram.node("A", f"Landing Page\n{cms}")
    diagram.node("B", f"VSL\n{video}")
    diagram.node("C", f"Automation\n{automation}")
    diagram.node("D", f"Checkout\n{checkout}")

    # edges
    diagram.edge("A", "B")
    diagram.edge("B", "C")
    diagram.edge("C", "D")

    output_path = "outputs/funnel_architecture"

    diagram.render(output_path, format="png", cleanup=True)

    print("[LOG] Diagrama salvo em outputs/funnel_architecture.png")
