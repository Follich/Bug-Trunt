def dns_info_2(domain):
    import subprocess

    print("""
          _                                    
       __| |_ __  ___ _ __ ___  ___ ___  _ __  
      / _` | '_ \\/ __| '__/ _ \\/ __/ _ \\| '_ \\ 
     | (_| | | | \\__ \\ | |  __/ (_| (_) | | | |
      \\__,_|_| |_|___/_|  \\___|\\___\\___/|_| |_|
     
     Dsnrecon é um script python simples que permite coletar informações
     orientadas a DNS em um determinado alvo.
     
     Comandos:
     
     [0] Pré-Pronto (dnsrecon -d <domain>)
     [1] -j JSON: Salva as informações em um arquivo JSON
     [2] -t <tipo>: Tipo de enumeração a ser executada. Existem vários tipos possíveis
     [3] -r <faixa>: Faixa de IP para brute force de pesquisa reversa.
     [4] --tcp: Usa o protocolo TCP para fazer consultas.
     [5] --threads <num>: Número de threads a ser usados
     [6] -n <ns_server>: Servidor de domínio a ser usado. Se nada for passado, o SOA do destino será usado.
     [7] Monte seu comando.\n""")

    command = int(input("Comando: "))

    if command == 0:
        print(f"\nComando executado: dnsrecon -d {domain}")
        subprocess.call(f"dnsrecon -d {domain}", shell=True)

    elif command == 1:
        print(f"\nComando executado: dnsrecon -j JSON -d {domain}")
        subprocess.call(f"dnsrecon -j JSON -d {domain}", shell=True)

    elif command == 2:
        print("""
        • padrão: SOA, NS, A, AAAA, MX e SRV.

        • rvl: Pesquisa reversa de um determinado intervalo CIDR ou IP.

        • brt: Domínios e hosts de força bruta usando um determinado dicionário.

        • srv: registros SRV.

        • axfr: Teste todos os servidores NS para uma transferência de zona.

        • bing: Execute a pesquisa do Bing para subdomínios e hosts.

        • yand: Realiza busca Yandex por subdomínios e hosts.

        • crt: Execute a pesquisa crt.sh de subdomínios e hosts.

        • snoop: Execute a espionagem de cache em todos os servidores NS de um determinado domínio,
         testando todos com o arquivo contendo os domínios, arquivo fornecido com a opção -D.

        • tld: Remova o TLD de determinado domínio e teste todos os TLDs registrados na IANA.

        • zonewalk: Execute uma caminhada na zona DNSSEC usando registros NSEC.\n""")

        enum = str(input("Qual tipo de enumeração você quer fazer? "))
        print(f"\nComando executado: dnsrecon -t {enum} -d {domain}")
        subprocess.call(f"dnsrecon -t {enum} -d {domain}", shell=True)

    elif command == 3:
        ip_info = float(input("Ip: "))
        print(f"\nComando executado: dnsrecon -r {ip_info} -d {domain}")
        subprocess.call(f"dnsrecon -r {ip_info} -d {domain}", shell=True)

    elif command == 4:
        print(f"\nComando executado: dnsrecon --tcp -d {domain}")
        subprocess.call(f"dnsrecon --tcp -d {domain}", shell=True)

    elif command == 5:
        num_tr = int(input(f"Número de threads: "))
        print(f"\nComando executado: dnsrecon --threads {num_tr} -d {domain}")
        subprocess.call(f"dnsrecon --threads {num_tr} -d {domain}", shell=True)

    elif command == 6:
        server = str(input("Server: "))
        print(f"\nComando executado: dnsrecon -n {server} -d {domain}")
        subprocess.call(f"dnsrecon -n {server} -d {domain}", shell=True)

    else:
        shell = str(input("Shell: "))
        subprocess.call(f"{shell}", shell=True)
