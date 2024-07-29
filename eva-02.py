import Banners
import os

stop = int(1)
while stop == 1:
    try:
        print(Banners.main_ban.banner_main)

        domain = str(input("Digite o dominio: "))
        block = int(input("Digite o bloco que deseja usar: "))

        # O código abaixo é do bloco "Information"
        if block == 1:
            while stop == 1:
                import Information

                os.system("clear")
                print(Banners.main_ban.banner_info)

                # Aqui é onde ele irá chamar as ferramentas.
                tool = int(input("Informe o número da ferramenta: "))
                os.system("clear")

                if tool == 1:
                    Information.main_info.whois(domain)
                elif tool == 2:
                    Information.main_info.host(domain)
                elif tool == 3:
                    Information.main_info.censys(domain)
                elif tool == 4:
                    Information.main_info.dnsenum(domain)
                elif tool == 5:
                    Information.main_info.dnsrecon(domain)
                elif tool == 5:
                    Information.main_info.nmap(domain)
                elif tool == 6:
                    Information.main_info.waf(domain)

                num = int(input("Deseja continuar?[0/1] "))
                os.system("clear")
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
                print(Banners.main_ban.banner_scan)

                # Aqui é onde ele irá chamar as ferramentas.
                tool = int(input("Informe o número da ferramenta: "))
                os.system("clear")

                if tool == 1:
                    Scanners.main_scan.burp_suit()
                elif tool == 2:
                    Scanners.main_scan.wp_scan(domain)
                elif tool == 3:
                    Scanners.main_scan.metasploit()
                elif tool == 4:
                    Scanners.main_scan.dotdotpwn()
                elif tool == 5:
                    Scanners.main_scan.jsql()

                num = int(input("Deseja continuar?[0/1] "))
                os.system("clear")
                stop += num

                if stop:
                    pass
                else:
                    break

        # O código abaixo é do bloco "Enumeration"
        elif block == 3:
            while stop:
                import Enumeration

                os.system("clear")
                print(Banners.main_ban.banner_enum)

                # Aqui é onde ele irá chamar as ferramentas.

                tool = int(input("Informe o número da ferramenta: "))
                os.system("clear")

                if tool == 1:
                    Enumeration.main_enum.gf(domain)
                elif tool == 2:
                    Enumeration.main_enum.unfurl(domain)
                elif tool == 3:
                    Enumeration.main_enum.paramspider(domain)
                elif tool == 4:
                    Enumeration.main_enum.arjun(domain)
                elif tool == 5:
                    Enumeration.main_enum.subjs(domain)
                elif tool == 6:
                    Enumeration.main_enum.anti_burl()
                elif tool == 7:
                    Enumeration.main_enum.amass(domain)
                elif tool == 8:
                    Enumeration.main_enum.metabigor(domain)

                num = int(input("Deseja continuar?[0/1] "))
                os.system("clear")
                stop += num

                if stop:
                    pass
                else:
                    break

        # O código abaixo é do bloco "Subdomain"
        elif block == 4:
            while stop == 1:
                import Subdomain

                os.system("clear")
                Banners.main_ban.banner_sub()

                tool = int(input("Informe o número da ferramenta: "))
                os.system("clear")

                if tool == 1:
                    Subdomain.main_sub.kitterunner(domain)
                elif tool == 2:
                    Subdomain.main_sub.git_api(domain)

    except:
        print("\nErro de internet: 500 Network Error\nTente novamente mais tarde. (kk brinqs :3)")
        num = int(input("Deseja continuar?[0/1] "))
        stop += num

        if stop:
            os.system("clear")
            pass
        else:
            break
