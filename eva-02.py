import Options
import os

while True:
    Options.main_options.banner()

    domain = str(input("Digite o dominio: "))
    block = int(input("Digite o bloco que deseja usar: "))
    stop = bool

    # O código abaixo é do bloco "Information"
    while stop:
        if block == 1:
            import Information

            os.system("clear")
            Options.main_options.banner_01()

            tool = int(input("Informe o número da ferramenta: "))

            if tool == 1:
                Information.main_information.whois(domain)
            elif tool == 2:
                Information.main_information.host(domain)
            elif tool == 3:
                Information.main_information.censys(domain)
            elif tool == 4:
                Information.main_information.dnsenum(domain)
            elif tool == 5:
                Information.main_information.dnsrecon(domain)
            elif tool == 5:
                Information.main_information.nmap(domain)
            elif tool == 6:
                Information.main_information.waf(domain)
            else:
                print("Ferramenta não expecificada!")

            conclusion = bool(input("Deseja continuar?[1/0] "))
            stop = stop == conclusion

            if not stop:
                break
            else:
                pass
