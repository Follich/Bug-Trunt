def scan_net(domain):
    import subprocess

    print("""
    .-. .-..-.   .-.  .--.  .----. 
    |  `| ||  `.'  | / {} \\ | {}  }
    | |\\  || |\\ /| |/  /\\  \\| .--' 
    `-' `-'`-' ` `-'`-'  `-'`-'         
    
    O nmap é uma ferramenta gratuita que faz uma varredura de rede para
    trazer uma lista de portas abertas, suas informações, e sistemas operacionais.
    
    [0] Pré-Pronto (proxychains nmap -sS -F -Pn <domain>)
    [1] -r: Verificação sequencial rápida.
    [2] -sO: Verificação do IP.
    [3] -sV: Investiga portas abertas para determinar informações de serviço.
    [4] -p: Para o scanning de portas especificas.
    [5] --script: Para o uso de scripts.
    [6] -oN: Para salvar o scanning em um arquivo.
    [7] Monte seu comando.\n""")

    command = int(input("\tComando: "))

    if command == 0:
        print(f"\n\tComando executado: proxychains nmap -sS -F -Pn {domain}")
        subprocess.call(f"(proxychains nmap -sS -Pn -F {domain}", shell=True)

    elif command == 1:
        print(f"\n\tComando executado: proxychains nmap -sS -Pn -r -F {domain}")
        subprocess.call(f"proxychains nmap -sS -Pn -r -F {domain}", shell=True)

    elif command == 2:
        print(f"\n\tComando executado: proxychains nmap -sO {domain}")
        subprocess.call(f"proxychains nmap -sO {domain}", shell=True)

    elif command == 3:
        print(f"\n\tComando executado: proxychains -sS -Pn -sV {domain}")
        subprocess.call(f"proxychains -sS -Pn -sV {domain}", shell=True)

    elif command == 4:
        ports = str(input("\tPortas (21,21,80,8080): "))
        print(f"\n\tComando executado: proxychains nmap -sS -Pn -p{ports} {domain}")
        subprocess.call(f"proxychains nmap -sS -Pn -p{ports} {domain}")

    elif command == 5:
        print("\tSite: https://nmap.org/nsedoc/scripts/")
        script = str(input("\tScript a ser usado: "))
        print(f"\n\tComando executado: proxychains nmap -sS -Pn --script={script} {domain}")
        subprocess.call(f"proxychains nmap -sS -Pn --script={script} {domain}", shell=True)

    elif command == 6:
        print(f"\n\tComando executado: proxychains nmap -sS -Pn -oN scan_info.txt {domain}")
        subprocess.call(f"proxychains nmap -sS -Pn -oN scan_info.txt {domain}", shell=True)

    else:
        shell = str(input("\n\tShell: "))
        subprocess.call(f"{shell}", shell=True)
