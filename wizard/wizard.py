from scanner.scanner import scan_site
from report.report_generator import generate_report


def start_wizard():

    print("\n===================================")
    print(" FUNNEL REVERSE ENGINEERING ENGINE ")
    print("===================================\n")

    print("1 - Analisar página de vendas")
    print("2 - Sair\n")

    option = input("Escolha uma opção: ")

    if option == "1":

        url = input("\nDigite a URL do site: ")

        print("\nExecutando análise...\n")

        results = scan_site(url)

        generate_report(results)

    else:
        print("\nEncerrando.\n")


if __name__ == "__main__":
    start_wizard()
