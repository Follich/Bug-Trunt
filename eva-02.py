import Subdomain
import Information
import Options
import Scanners
import os

while True:
    Options.banner_main()

    domain = str(input("Domain: "))
    decision = int(input("Tools: "))

    os.system("clear")

    if decision == 1:
        Information.whois(domain)
    elif decision == 2:
        Information.censys(domain)
    elif decision == 3:
        Information.host(domain)
    elif decision == 4:
        Information.dnsenum(domain)
    elif decision == 5:
        Information.dnsrecon(domain)
    elif decision == 6:
        Information.nmap(domain)
    elif decision == 7:
        Information.waf(domain)
    elif decision == 8:
        Subdomain.feroxbuster(domain)
    elif decision == 9:
        Subdomain.wfuzz(domain)
    elif decision == 16:
        Scanners.burp_suit()
    elif decision == 17:
        Scanners.metasploit()
    elif decision == 18:
        Scanners.wp_scan(domain)
    else:
        pass

    cont = int(input("\nContinuar?[1/0] "))

    if cont == 1:
        os.system("clear")
        pass

    else:
        os.system("clear")
        break
