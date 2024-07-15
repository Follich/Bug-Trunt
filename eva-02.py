import Brute
import Info
import Options
import Scan
import Vuls
import os

while True:
    print("""
   :::::::::: :::     :::     :::                            :::::::   :::::::: 
   :+:        :+:     :+:   :+: :+:                         :+:   :+: :+:    :+:
   +:+        +:+     +:+  +:+   +:+                        +:+  :+:+       +:+ 
   +#++:++#   +#+     +:+ +#++:++#++:     +#++:++#++:++     +#+ + +:+     +#+   
   +#+         +#+   +#+  +#+     +#+                       +#+#  +#+   +#+     
   #+#          #+#+#+#   #+#     #+#                       #+#   #+#  #+#      
   ##########     ###     ###     ###                        #######  ##########

+---------------------------------------+-----------------------------------------+
|                Info                   |                  Scan                   |
+---------------------------------------+-----------------------------------------+
| * Domain:                             | 9 - Owasp              12 - Metasploit  |
|     1 - Whois           2 - Host      | 10 - Burp suite                         |
| * DNS:                                | 11 - Wpscan                             |
|     3 - Dnsenum         4 - Dnsrecon  +-----------------------------------------+
| * Net:                                |                 Subdomain               |
|     5 - Nmap            6 - Wafw00f   +-----------------------------------------+
+---------------------------------------+ * Crowlers:                             |
|             Brute Force               |   13 - Gau   14 - Wayback   15 - Chaos  |
+---------------------------------------| * Images:                               |
|* - Url:                               |       16 - Aquatone  17 - Gowitness     |
| 7 - Feroxbuster           8 - Wfuzz   | * Validação:                            |
|                                       |        18 - Htppx    19 - Httprobe      |
+---------------------------------------+-----------------------------------------+
|                Vuls                   |                 Options                 |
+---------------------------------------+-----------------------------------------+
| * Injection:                          | 23 - Prepare folder                     |
|  20 - Jsql              21 - Sqlmap   | 24 - Order to tools                     |
| * LFI:                                | 25 - Main                               |
|           22 - DotDotpwn              | 26 - Sites                              |
|                                       | 27 - Dorks                              | 
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
    elif decision == 7:
        Brute.brute_url(domain)
    elif decision == 8:
        Brute.fuzz_web(domain)
    else:
        pass

    cont = int(input("\nContinuar?[1/0] "))

    if cont == 1:
        os.system("clear")
        pass
    else:
        os.system("clear")
        break
