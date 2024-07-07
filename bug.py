import Brute
import Info
import Options
import Scan
import Vuls

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
    |     5 - Nmap            6 - Waf00f    +-----------------------------------------+
    +---------------------------------------+ * Crowlers:                             |
    |             Brute Force               |   19 - Gau   20 - Wayback   21 - Chaos  |
    +---------------------------------------| * Images:                               |
    |* - Senhas:                            |       22 - Aquatone  23 - Gowitness     |
    |  7 - Hydra                8 - John    |  * Validação:                           |
    |             9 - Hashcat               |       24  - Htppx    25 - Httprobe      |
    |* - Url:                               |                                         |
    |  10 - Feroxbuster      11 - Gobuster  |         ＼(((￣(￣(￣▽￣)￣)￣)))／        |
    |             12 - Wfuzz                |                                         |
    +---------------------------------------+-----------------------------------------+
    |                Vuls                   |                 Options                 |
    +---------------------------------------+-----------------------------------------+
    | * Injection:                          | 29 - Prepare folder                     |
    |  26 - Jsql              27 - Sqlmap   | 30 - Order to tools                     |
    | * LFI:                                | 31 - Main                               |
    |           28 - DotDotpwn              | 32 - List                               |
    |                                       | 33 - Wtf who is this                    | 
    |               ( •̀ ω •́ )y              | 34 - Sites                              |
    +---------------------------------------+-----------------------------------------+
    
    """)
    domain = str(input("Domain: "))
    protocol = str(input("Http or Https: "))
    decision = int(input("Tools: "))

        
