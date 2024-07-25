import Brute
import Info
import Options
import Scan
import Vuls
import os

while True:
    print("""
     :::::::::: :::     :::     :::                        :::::::   :::::::: 
     :+:        :+:     :+:   :+: :+:                     :+:   :+: :+:    :+:
     +:+        +:+     +:+  +:+   +:+                    +:+  :+:+       +:+ 
     +#++:++#   +#+     +:+ +#++:++#++:     +#++:++#+     +#+ + +:+     +#+   
     +#+         +#+   +#+  +#+     +#+                   +#+#  +#+   +#+     
     #+#          #+#+#+#   #+#     #+#                   #+#   #+#  #+#      
     ##########     ###     ###     ###                    #######  ##########
     
+---------------------------------------+-----------------------------------------+
|                Info                   |                  Scan                   |
+---------------------------------------+-----------------------------------------+
| * Domain:                             | * Scan-Others                           |
|     1 - Whois           2 - Host      |  8 - Burp suite            10 - Wpscan  |
|               3 - Censys              |  9 - Metasploit            11 - W3af    |
| * DNS:                                | * Vuls                                  |
|     4 - Dnsenum         5 - Dnsrecon  |       12 - Jsql       13 - DotDotpwn    |
| * Net:                                |                                         |
|     6 - Nmap            7 - Wafw00f   |              --( ~ _ ~ ) --             |
+---------------------------------------+-----------------------------------------+
|              Subdomain                |                Enumeration              |
+---------------------------------------+-----------------------------------------+
| * Crowlers:                           | * Asn:                                  |
|   14 - Gau       17 - Reflector       |   * Metabigor                           |
|   15 - Amass     18 - Wayback         | * Javascript:                           |
| * Validação:                          |                                         |
|   19 - Htppx     20- Httprobe         | * Endpoints:                            |
| * Api:                                |                                         |
|   * - Api git   * - Git dorker        | * Subdirectories:                       |
|                                       |    8 - Feroxbuster         9 - Wfuzz    |
+---------------------------------------+-----------------------------------------+
|                                    Options                                      |
+---------------------------------------+-----------------------------------------+
| 30 - Prepare folder                           31 - Order to tools               |
| 32 - Main                                     33 - Sites                        |
| 34 - Dorks                                    35 - Config Setup - tools         |
+---------------------------------------+-----------------------------------------+\n""")

    domain = str(input("Domain: "))
    decision = int(input("Tools: "))

    os.system("clear")

    if decision == 1:
        Info.whois(domain)
    elif decision == 2:
        Info.host(domain)
    elif decision == 3:
        Info.censys(domain)
    elif decision == 4:
        Info.dnsenum(domain)
    elif decision == 5:
        Info.dnsrecon(domain)
    elif decision == 6:
        Info.nmap(domain)
    elif decision == 7:
        Info.waf(domain)
    elif decision == 8:
        Brute.feroxbuster(domain)
    elif decision == 9:
        Brute.wfuzz(domain)
    elif decision == 16:
        Scan.burp_suit()
    elif decision == 17:
        Scan.metasploit()
    elif decision == 18:
        Scan.wp_scan(domain)
    else:
        pass

    cont = int(input("\nContinuar?[1/0] "))

    if cont == 1:
        os.system("clear")
        pass

    else:
        os.system("clear")
        break
