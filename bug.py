import Brute
import Info
import Options
import Scan
import Vuls
import os


while True:
    print("""
    +---------------------------------------+-----------------------------------------+
    |                Info                   |                  Scan                   |
    +---------------------------------------+-----------------------------------------+
    | * Domain:                             | 13 - Owasp             16 - Metasploit  |
    |     1 - Whois           2 - Host      | 14 - Burp suite        17 - Nmap        |
    | * DNS:                                | 15 - Wpscan            18 - Waf00f      |
    |     3 - Dnsenum         4 - Dnsrecon  +-----------------------------------------+
    | * Net:                                |                 Subdomain               |
    |     5 - Nmap            6 - Wafw00f   +-----------------------------------------+
    +---------------------------------------+ * Crowlers:                             |
    |             Brute Force               |   19 - Gau   20 - Wayback   21 - Chaos  |
    +---------------------------------------| * Images:                               |
    |* - Senhas:                            |       22 - Aquatone  23 - Gowitness     |
    |  7 - Hydra                8 - John    |  * Validação:                           |
    |             9 - Hashcat               |       24  - Htppx    25 - Httprobe      |
    |* - Url:                               |                                         |
    |  10 - Feroxbuster      11 - Gobuster  |               \\((-^-)))/                |
    |             12 - Wfuzz                |                                         |
    +---------------------------------------+-----------------------------------------+
    |                Vuls                   |                 Options                 |
    +---------------------------------------+-----------------------------------------+
    | * Injection:                          | 29 - Prepare folder                     |
    |  26 - Jsql              27 - Sqlmap   | 30 - Order to tools                     |
    | * LFI:                                | 31 - Main                               |
    |           28 - DotDotpwn              | 32 - Sites                              |
    |                                       | 33 - Dorks                              | 
    |             ---(0_0)---               |                                         |
    +---------------------------------------+-----------------------------------------+\n""")

    domain = str(input("Domain: "))
    decision = int(input("Tools: "))

    os.system("clear")

    if decision == 1:
        Info.domain_info(domain)
    elif decision == 2:
        Info.domain_ip(domain)
    elif decision == 3:
        Info.dns_info_1(domain)
    elif decision == 4:
        Info.dns_info_2(domain)
    elif decision == 5:
        Info.scan_net(domain)
    elif decision == 6:
        Info.firewall_scan(domain)
    else:
        pass

    cont = int(input("\nContinuar?[1/0] "))

    if cont == 1:
        os.system("clear")
        pass
    else:
        os.system("clear")
        break
