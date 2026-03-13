def start_wizard():

    print("\n==============================")
    print(" FUNNEL ANALYSIS WIZARD ")
    print("==============================\n")

    print("1 - Analisar página de vendas")
    print("2 - Sair\n")

    option = input("Escolha uma opção: ")

    if option == "1":

        url = input("\nDigite a URL: ")

        print("\nExecutando análise...\n")

        results = scan_site(url)

        generate_report(results)

    else:
        print("\nEncerrando sistema.\n")
