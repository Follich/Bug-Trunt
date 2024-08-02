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
                elif tool == 6:
                    Information.main_info.nmap(domain)
                elif tool == 7:
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
                elif tool == 6:
                    Scanners.main_scan.hacker_help()

                num = int(input("Deseja continuar?[0/1] "))
                os.system("clear")
                stop += num

                if stop:
                    pass
                else:
                    break

        # O código abaixo é do bloco "Enumeration"
        elif block == 3:
            while stop == 1:
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
                print(Banners.main_ban.banner_sub)

                # Aqui é onde ele irá chamar as ferramentas.

                tool = int(input("Informe o número da ferramenta: "))
                os.system("clear")

                if tool == 1:
                    Subdomain.main_sub.kitterunner(domain)
                elif tool == 2:
                    Subdomain.main_sub.git_api(domain)
                elif tool == 3:
                    Subdomain.main_sub.git_dorker(domain)
                elif tool == 4:
                    Subdomain.main_sub.ffuf(domain)
                elif tool == 5:
                    Subdomain.main_sub.gauplus(domain)
                elif tool == 6:
                    Subdomain.main_sub.waymore(domain)
                elif tool == 7:
                    Subdomain.main_sub.feroxbuster(domain)
                elif tool == 8:
                    Subdomain.main_sub.wfuzz(domain)
                elif tool == 9:
                    Subdomain.main_sub.httpx(domain)
                elif tool == 10:
                    Subdomain.main_sub.httprobe()
                elif tool == 11:
                    Subdomain.main_sub.aquatone()

                num = int(input("Deseja continuar?[0/1] "))
                os.system("clear")
                stop += num

                if stop:
                    pass
                else:
                    break

        # O código abaixo é do bloco "Structure"
        elif block == 5:
            while stop == 1:
                import Structure

                os.system("clear")
                print(Banners.main_ban.banner_str)

                # Aqui é onde ele irá chamar as ferramentas.

                tool = int(input("Informe o número da ferramenta: "))
                os.system("clear")

                if tool == 1:
                    Structure.main_struct.xargs()
                elif tool == 2:
                    Structure.main_struct.nuclei()
                elif tool == 3:
                    Structure.main_struct.dalfox()
                elif tool == 4:
                    Structure.main_struct.katana(domain)
                elif tool == 5:
                    Structure.main_struct.jsscanner()

                num = int(input("Deseja continuar?[0/1] "))
                os.system("cear")
                stop += num

                if stop:
                    pass
                else:
                    break

        # O código abaixo é do bloco "Options"
        elif block == 6:
            while stop == 1:
                import Options

                os.system("clear")
                print(Banners.main_ban.banner_opt)

                # Aqui é onde ele irá chamar as ferramentas.

                tool = int(input("Número da opção: "))
                os.system("clear")

                if tool == 1:
                    print(Options.main_opt.man)
                elif tool == 2:
                    print(Options.main_opt.order)
                elif tool == 3:
                    print(Options.main_opt.dorks)
                elif tool == 4:
                    print(Options.main_opt.sites)
                elif tool == 5:
                    Options.main_opt.other(domain)
                elif tool == 6:
                    print(Options.main_opt.report)
                elif tool == 7:
                    print(Options.main_opt.step_by_step)
                elif tool == 8:
                    Options.main_opt.options_install_tools()
                elif tool == 9:
                    Options.main_opt.prepare_folder(domain)

                num = int(input("Deseja continuar?[0/1] "))
                os.system("clear")
                stop += num

                if stop:
                    pass
                else:
                    break
    except:
        print("\nErro de internet: 500 Network Error\nTente novamente mais tarde. (kk brinqs :3)")
        num = int(input("Deseja continuar?[0/1] "))
        stop += num

        if stop:
            os.system("clear")
            pass
        else:
            break
