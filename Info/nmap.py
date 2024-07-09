def scan_net(domain):
    import subprocess

    print("""
    .-. .-..-.   .-.  .--.  .----. 
    |  `| ||  `.'  | / {} \ | {}  }
    | |\  || |\ /| |/  /\  \| .--' 
    `-' `-'`-' ` `-'`-'  `-'`-'         
    
    O nmap é uma ferramenta gratuita que faz uma varredura de rede para
    trazer uma lista de portas abertas, suas informações, e sistemas operacionais.
    
    [0] Pré-Pronto (proxychains nmap -sS -F <domain>)
    [1] -r: Verificação sequencial rápida (proxychains nmap -sS -r -F <domain>)
    [2] -sO: Verificação do IP (proxychains nmap -sO <domain>)
    [3] -sV: Investiga portas abertas para determinar informações de serviço
    [4] -p: Para o scanning de portas especificas
    [5] --script: Para o uso de scripts
    [6] -oN: Para salvar o scanning em um arquivo
    [7] Monte seu comando\n""")

    command = int(input("\tComando: "))

    if command == 0:
        print(f"\n\tComando executado: proxychains nmap -sS -F {domain}")
        subprocess.call(f"(proxychains nmap -sS -F {domain}", shell=True)

    elif command == 1:
        print(f"\n\tComando executado: proxychains nmap -sS -r -F {domain}")
        subprocess.call(f"proxychains nmap -sS -r -F {domain}", shell=True)

    elif command == 2:
        print(f"\n\tComando executado: proxychains nmap -sO")