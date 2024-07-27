import Options
import os

while True:
    Options.main_options.banner()

    domain = str(input("Digite o dominio: "))
    block = int(input("Digite o bloco que deseja usar: "))
    stop = int(1)

    # O código abaixo é do bloco "Information"
    if block == 1:
        while stop == 1:
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

                num = int(input("Deseja continuar?[0/1] "))
                stop += num

                if stop:
                    pass
                else:
                    break

    # O código abaixo é do bloco "Scanners"
    elif block == 2:
        while stop == 1:
            import Scanners

            os.system("clear")
            Options.main_options.banner_02()

            tool = int(input("Informe o número da ferramenta: "))
            os.system("clear")

            if tool == 1:
                Scanners.main_scann.burp_suit()
            elif tool == 2:
                Scanners.main_scann.wp_scan(domain)
            elif tool == 3:
                Scanners.main_scann.metasploit()
            elif tool == 4:
                Scanners.main_scann.dotdotpwn()
            elif tool == 5:
                Scanners.main_scann.jsql()
            else:
                print("Ferramenta não expecificada!")

            num = int(input("Deseja continuar?[0/1] "))
            stop += num

            if stop:
                pass
            else:
                break
