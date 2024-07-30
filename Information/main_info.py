import subprocess


def whois(domain):
    print("""
oooo     oooo oooo                  o88              
 88   88  88   888ooooo    ooooooo  oooo   oooooooo8 
  88 888 88    888   888 888     888 888  888ooooooo 
   888 888     888   888 888     888 888          888
    8   8     o888o o888o  88ooo88  o888o 88oooooo88 

O whois é uma ferramenta que traz uma consulta de informações
que nos ajuda a saber alguns emails, números e quem hospedou aquele determinado 
site.

Comandos:
[0] Pré-Proto (default).
[1] -a: Pesquise também todos os bancos de dados espelhados.
[2] -b: Retorna breves intervalos de endereços IP com contato de abuso.
[3] -B: Desativa a filtragem de objetos. (Mostre os endereços de e-mail.)
[4] -c: Retorna o menor intervalo de endereços IP com uma referência a um objeto irt.
[5] -d: Retorna também o objeto de delegação de DNS reverso.
[6] Monte seu comando.\n""")

    command = int(input("Comando: "))

    if command == 0:
        print(f"\nComando executado: whois {domain}")
        subprocess.call(f"whois {domain}", shell=True)

    elif command == 1:
        print(f"\nComando executado: whois -a {domain}")
        subprocess.call(f"whois -a {domain}", shell=True)

    elif command == 2:
        print(f"\nComando executado: whois -b {domain}")
        subprocess.call(f"whois -b {domain}", shell=True)

    elif command == 3:
        print(f"\nComando executado: whois -B {domain}")
        subprocess.call(f"whois -B {domain}", shell=True)

    elif command == 4:
        print(f"\nComando executado: whois -c {domain}")
        subprocess.call(f"whois -c {domain}", shell=True)

    elif command == 5:
        print(f"\nComando executado: whois -d {domain}")
        subprocess.call(f"whois -d {domain}", shell=True)

    else:
        shell = str(input("Shell: "))
        subprocess.call(f"{shell}", shell=True)


def host(domain):
    print("""
 ___                             ___     
(   )                           (   )    
 | | .-.     .--.       .--.     | |_    
 | |/   \\   /    \\    /  _  \\   (   __)  
 |  .-. .  |  .-. ;  . .' `. ;   | |     
 | |  | |  | |  | |  | '   | |   | | ___ 
 | |  | |  | |  | |  _\\_`.(___)  | |(   )
 | |  | |  | |  | | (   ). '.    | | | | 
 | |  | |  | '  | |  | |  `\\ |   | ' | | 
 | |  | |  '  `-' '  ; '._,' '   ' `-' ; 
(___)(___)  `.__.'    '.___.'     `.__.  

Host é um utilitário simples para realizar pesquisas de DNS. Normalmente é usado
para converter nomes em endereços IP e vice-versa. Quando não há argumentos ou opções
são fornecidas, o host imprime um breve resumo de seus argumentos de linha de comando
e opções.

Comandos:

[0] Pré-Pronto(default)
[1] -p: Esta opção especifica a porta a ser consultada no servidor. O padrão é 53.
[2] -d: Esta opção imprime rastreamentos de depuração e é equivalente a -v (opção detalhada).
[3] -l -a: Imprimem todos os registros na zona.
[4] -4: Esta opção especifica que apenas IPv4 deve ser usado para consulta
[5] -6: Esta opção especifica que apenas IPv6 deve ser usado para consulta
[6] Monte seu comando\n""")

    command = int(input("Comando: "))

    if command == 0:
        print(f"\nComando executado: host {domain}")
        subprocess.call(f"host {domain}", shell=True)

    elif command == 1:
        port = int(input("Porta: "))
        print(f"\nComando executado: host -p {port} {domain}")
        subprocess.call(f"host -p {port} {domain}", shell=True)

    elif command == 2:
        print(f"\nComando executado: host -d {domain}")
        subprocess.call(f"host -d {domain}", shell=True)

    elif command == 3:
        print(f"\nComando executado: host -l -a {domain}")
        subprocess.call(f"host -l -a {domain}", shell=True)

    elif command == 4:
        print(f"\nComando executado: host -4 {domain}")
        subprocess.call(f"host -4 {domain}", shell=True)

    elif command == 5:
        print(f"\nComando executado: host -6 {domain}")
        subprocess.call(f"host -6 {domain}", shell=True)

    else:
        shell = str(input("Shell: "))
        subprocess.call(f"{shell}", shell=True)


def censys(domain):
    print("""
  ______  _______ .__   __.      _______.____    ____  _______.
 /      ||   ____||  \\ |  |     /       |\\   \\  /   / /       |
|  ,----'|  |__   |   \\|  |    |   (----` \\   \\/   / |   (----`
|  |     |   __|  |  . `  |     \\   \\      \\_    _/   \\   \\    
|  `----.|  |____ |  |\\   | .----)   |       |  | .----)   |   
 \\______||_______||__| \\_| |_______/        |__| |_______/    

O Censys é um mecanismo de busca que permite identificar e analisar dispositivos, serviços web, servidores,
e host.

Comandos:

[0] Search: Procura.
[1] Subdomains: Subdominios.
[2] View: Visualizar conteúdo html.
[3] Portas abertas
[4] Monte seu comando\n""")

    command = int(input("Comando: "))
    if command == 0:
        print(f"Comando executado: censys search {domain}")
        subprocess.call(f"censys search {domain}", shell=True)

    elif command == 1:
        print(f"Comando executado: censys subdomains {domain}")
        subprocess.call(f"censys subdomains {domain}", shell=True)

    elif command == 2:
        print(f"Comando executado: censys subdomains {domain}")
        subprocess.call(f"censys search {domain}", shell=True)

    elif command == 3:
        ip = str(input("Ipv4/Ipv6: "))
        print(f"Comando executado: censys search {ip}")
        subprocess.call(f"censys search {ip}", shell=True)

    else:
        shell = str(input("Comando: "))
        subprocess.call(f"{shell}", shell=True)


def dnsenum(domain):
    print("""
       ,,                                                                      
     `7MM                                                                      
       MM                                                                      
   ,M""bMM  `7MMpMMMb.  ,pP"Ybd  .gP"Ya `7MMpMMMb.`7MM  `7MM  `7MMpMMMb.pMMMb.  
 ,AP    MM    MM    MM  8I   `" ,M'   Yb  MM    MM  MM    MM    MM    MM    MM  
 8MI    MM    MM    MM  `YMMMa. 8M""""""  MM    MM  MM    MM    MM    MM    MM  
 `Mb    MM    MM    MM  L.   I8 YM.    ,  MM    MM  MM    MM    MM    MM    MM  
  `Wbmd"MML..JMML  JMML.M9mmmP'  `Mbmmd'.JMML  JMML.`Mbod"YML..JMML  JMML  JMML.

O dnsenum é script multithread para enumerar informações em um domínio e para
descobrir blocos IP não contíguos

Comandos:

[0] Pré-Pronto (dnsenum <domínio> -f /usr/share/dnsenum/dns.txt)
[1] --private: Mostra e salva ips privados no final de o arquivo domínio_ips.txt.
[2] --threads <num>: Número de threads que irão executar em consultas diferentes.
[3] -f: Lê subdomínios de um arquivo para fazer brute force.
[4] -v: Para que o processo seja detalhado (mostra todo o progresso e todas as mensagens de erro)
[5] -www site:domínio: Eliminará subdomínios da pesquisa do Google.
[6] -s: número máximo de subdomínios que será extraído do Google.
[7] Monte seu comando\n""")

    command = int(input("Comando: "))

    if command == 0:
        print(f"\nComando executado: dnsenum {domain} -f /usr/share/dnsenum/dns.txt")
        subprocess.call(f"dnsenum {domain} -f /usr/share/dnsenum/dns.txt", shell=True)

    elif command == 1:
        print(f"\nComando executado: dnsenum --private {domain}")
        subprocess.call(f"dnsenum --private {domain}", shell=True)

    elif command == 2:
        tr = int(input("Número de threads: "))
        print(f"\nComando executado: dnsenum --threads {tr} {domain}")
        subprocess.call(f"dnsenum --threads {tr} {domain}", shell=True)

    elif command == 3:
        file = str(input("Local do arquivo: "))
        print(f"\nComando executado: dnsenum {domain} -f {file}")
        subprocess.call(f"dnsenum {domain} -f {file}", shell=True)

    elif command == 4:
        print(f"\nComando executado: dnsenum -v {domain}")
        subprocess.call(f"dnsenum -v {domain}", shell=True)

    elif command == 5:
        print(f"\nComando executado: dnsenum -www site:{domain}")
        subprocess.call(f"dnsenum -www site:{domain}", shell=True)

    elif command == 6:
        num = int(input("Número: "))
        print(f"\nComando executado: dnsenum -s {num} {domain}")
        subprocess.call(f"dnsenum -s {num} {domain}", shell=True)

    else:
        shell = str(input("Shell: "))
        subprocess.call(f"{shell}", shell=True)


def dnsrecon(domain):
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


def nmap(domain):
    print("""
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \\ | {}  }
| |\\  || |\\ /| |/  /\\  \\| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'         

O nmap é uma ferramenta gratuita que faz uma varredura de rede para
trazer uma lista de portas abertas, suas informações, e sistemas operacionais.

Dê o comando: "service tor start", Para que os comandos funcionem.

[0] Pré-Pronto (nmap -v -sS -sV -F <domain> --script=vuln -oN nmap.txt)
[1] -r: Verificação sequencial rápida.
[2] -sO: Verificação do IP.
[3] -sV: Investiga portas abertas para determinar informações de serviço.
[4] -p: Para o scanning de portas especificas.
[5] --script: Para o uso de scripts.
[6] -oN: Para salvar o scanning em um arquivo.
[7] Monte seu comando.\n""")

    command = int(input("Comando: "))

    if command == 0:
        print(f"\nComando executado: nmap -v -sS -sV -F {domain} --script=vuln -oN nmap.txt")
        subprocess.call(f"proxychains nmap -v -sS -sV -F {domain} --script=vuln -oN nmap.txt ", shell=True)

    elif command == 1:
        print(f"\nComando executado:  nmap -sS -Pn -r -F {domain}")
        subprocess.call(f"proxychains nmap -sS -Pn -r -F {domain}", shell=True)

    elif command == 2:
        print(f"\nComando executado: nmap -sO {domain}")
        subprocess.call(f"proxychains nmap -sO {domain}", shell=True)

    elif command == 3:
        print(f"\nComando executado: nmap -sS -Pn -sV {domain}")
        subprocess.call(f"nmap -sS -Pn -sV {domain}", shell=True)

    elif command == 4:
        ports = str(input("Portas (21,21,80,8080): "))
        print(f"\nComando executado: nmap -sS -Pn -p{ports} {domain}")
        subprocess.call(f"nmap -sS -Pn -p{ports} {domain}")

    elif command == 5:
        print("Site: https://nmap.org/nsedoc/scripts/")
        script = str(input("Script a ser usado: "))
        print(f"\nComando executado:nmap -sS -Pn --script={script} {domain}")
        subprocess.call(f"nmap -sS -Pn --script={script} {domain}", shell=True)

    elif command == 6:
        print(f"\nComando executado: nmap -sS -Pn -oN scan_info.txt {domain}")
        subprocess.call(f"nmap -sS -Pn -oN scan_info.txt {domain}", shell=True)

    else:
        shell = str(input("\nShell: "))
        subprocess.call(f"{shell}", shell=True)


def waf(domain):
    print("""
___       __      __________       _______________________
__ |     / /_____ ___  __/_ |     / /_  __ \\_  __ \\__  __/
__ | /| / /_  __ `/_  /_ __ | /| / /_  / / /  / / /_  /_  
__ |/ |/ / / /_/ /_  __/ __ |/ |/ / / /_/ // /_/ /_  __/  
____/|__/  \\__,_/ /_/    ____/|__/  \\____/ \\____/ /_/        

É uma ferramenta de identificação e impressão digital do firewall de aplicativos da Web.

Comandos:

[0] Pré-Pronto (waf00f http://<dominio>)
[1] -a: Para investigar todos os wafs
[2] -p PROXY: Para usar o waf com um proxy
[3] -r: Comando para não seguir redirecionamentos de respostas
[4] Monte seu comando.\n""")

    command = int(input("Comando: "))

    if command == 0:
        print(f"\nComando executado: wafw00f {domain}")
        subprocess.call(f"wafw00f {domain}", shell=True)
    elif command == 1:
        print(f"\nComando executado: wafw00f -a {domain}")
        subprocess.call(f"wafw00f -a {domain}", shell=True)
    elif command == 2:
        print(f"\nwafw00f -p Socks5://hostname:1080 {domain}")
        subprocess.call(f"wafw00f -p Socks5://hostname:1080 {domain}", shell=True)
    elif command == 3:
        print(f"\nComando executado: wafw00f -r {domain}")
        subprocess.call(f"wafw00f -r {domain}", shell=True)
    else:
        shell = str(input("Shell: "))
        subprocess.call(f"{shell}", shell=True)
