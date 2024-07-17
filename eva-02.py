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
|     1 - Whois           2 - Host      |  16 - Owasp             19 - Burp suite |
|               3 - Censys              |  17 - Metasploit        20 - Wpscan     |
| * DNS:                                |  18 - W3af                              |
|     4 - Dnsenum         5 - Dnsrecon  +-----------------------------------------+
| * Net:                                |                 Subdomain               |
|     6 - Nmap            7 - Wafw00f   +-----------------------------------------+
+---------------------------------------+ * Crowlers:                             |
|             Brute Force               |   21 - Gau                24 - Wayback  |
+---------------------------------------|   22 - Reflector          25 - Chaos    |
| * - Url:                              |   23 - Amass              26 - Api git  |
|     8 - Feroxbuster      9 - Wfuzz    | * Images:                               |
| * - Pass:                             |       27 - Aquatone  28 - Gowitness     |
|     10 - Hydra         11 - John      | * Validação:                            |
|              12 - HashCat             |        29 - Htppx    30 - Httprobe      |
+---------------------------------------+-----------------------------------------+
|                Vuls                   |                 Options                 |
+---------------------------------------+-----------------------------------------+
| * Injection:                          | 31 - Prepare folder                     |
|      13 - Jsql          14 - Sqlmap   | 32 - Order to tools                     |
| * LFI:                                | 33 - Main                               |
|           15 - DotDotpwn              | 34 - Sites                              |
|                                       | 35 - Dorks                              | 
|             ---(0_0)---               | 36 - Config Setup - tools               |
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
    else:
        pass

    cont = int(input("\nContinuar?[1/0] "))

    if cont == 1:
        os.system("clear")
        pass

    else:
        os.system("clear")
        break
