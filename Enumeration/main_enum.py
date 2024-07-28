import subprocess


def gf(domain):
    print("""
   ,___        _   ______                 
  /   /o      //  (  /     o             /
 /  __.  _   //    -/--_  ,  _  _ _   __/ 
(___/ (_/ (_(/_   _/  / (_(_(/_/ / /_(_/_ 

Gf é uma ferramenta de enumeração de vulnerabilidades por parametros em diversas
urls psssadas.

Sinopse:

echo "domain" | <crawler> | gf <patterns>

Patterns disponiveis:

1 - debug_logic     5 - interestingparams  9 - sqli  13 - ssrf
2 - idor            6 - interestingsubs    10 - rce       
3 - img-traversal   7 - jsvar              11 - ssti
4 - interestingEXT  8 - lfi                12 - xss

Comandos:

[1] Pré-pronto = Sinopse
[2] Monte seu comando\n""")

    command = int(input("Comando: "))

    if command == 1:
        crawler = str(input("Digite o crowler a ser usado: "))
        pattern = str(input("Qual pattern listado a cima deseja usar? "))

        print(f"Comando executado: echo \"{domain}\" | {crawler} | gf {pattern}")
        subprocess.call(f"echo \"{domain}\" | {crawler} | gf {pattern}", shell=True)
    elif command == 2:
        shell = str(input("Digite seu comando: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def unfurl(domain):
    print("""
╔══════════════════════════════════════════╗
║,--. ,--.         ,---.               ,--.║
║|  | |  |,--,--, /  .-',--.,--.,--.--.|  |║
║|  | |  ||      \\|  `-,|  ||  ||  .--'|  |║
║'  '-'  '|  ||  ||  .-''  ''  '|  |   |  |║
║ `-----' `--''--'`--'   `----' `--'   `--'║
╚══════════════════════════════════════════╝
O conceito do unfurl é simples, ele apenas enumera endpoints normalmente.

Sinopse:

echo "domain" | <crawler> | unfurl <key> | anew

Comandos:

[0]Pré-pronto = Sinopse.
[1]keys: Chaves da string de consulta (uma por linha)
[2]values: Valores da string de consulta (um por linha)
[3]keypairs: chaves Pares chave=valor da string de consulta (um por linha)
[4]domains: O nome do host (por exemplo, sub.example.com)
[5]paths: O caminho da solicitação (por exemplo, /users)
[6]apexes: O domínio apex (por exemplo, example.com de sub.example.com)
[7]json: Objetos de URL/formato codificados em JSON
[8]format: Especifique um formato personalizado (veja abaixo)
[9]Monte seu comando\n""")

    command = int(input("Comando: "))
    crawler = str(input("Digite o crowler a ser usado: "))

    if command == 0 or command == 5:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl path | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl path | anew ", shell=True)
    elif command == 1:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl keys | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl keys | anew ", shell=True)
    elif command == 2:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl values | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl values | anew ", shell=True)
    elif command == 3:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl keypairs | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl keypairs | anew ", shell=True)
    elif command == 4:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl domains | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl domains | anew ", shell=True)
    elif command == 6:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl apexes | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl apexes | anew ", shell=True)
    elif command == 7:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl json | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl json | anew ", shell=True)
    elif command == 8:
        print(f"Comando executado: echo \"{domain}\" | {crawler} | unfurl format | anew ")
        subprocess.call(f"echo \"{domain}\" | {crawler} | unfurl format | anew ", shell=True)
    elif command == 9:
        shell = str(input("Shell: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def paramspider(domain):
    print("""
                                      _    __       
   ___  ___ ________ ___ _  ___ ___  (_)__/ /__ ____
  / _ \\/ _ `/ __/ _ `/  ' \\(_-</ _ \\/ / _  / -_) __/
 / .__/\\_,_/_/  \\_,_/_/_/_/___/ .__/_/\\_,_/\\__/_/   
/_/                          /_/                    

O paramspider é uma ferramenta de enumeração de url/vuls feita em python.

Comandos:

[0] Pré-Pronto: paramspider -d {domain} -s --proxy SOCKS5://127.0.0.1:9050
[1]-d <domain>: Nome de domínio para buscar URLs relacionados.
[2]-l <list>: Arquivo contendo uma lista de nomes de domínio.
[3]-s: Transmita URLs no terminal.
[4]--proxy PROXY: Define o endereço de proxy para solicitações da web.
[5] Monte seu comando\n""")
    command = int(input("Comando: "))

    if command == 0:
        print(f"Comando execultado: paramspider -d {domain} -s --proxy SOCKS5://127.0.0.1:9050")
        subprocess.call(f"paramspider -d {domain} -s --proxy SOCKS5://127.0.0.1:9050", shell=True)
    elif command == 1:
        print(f"Comando executado: paramspider -d {domain}")
        subprocess.call(f"paramspider -d {domain}", shell=True)
    elif command == 2:
        archive_list = str(input("Caminho da lista: "))
        print(f"Comando executado: paramspider -d {domain} -l {archive_list}")
        subprocess.call(f"paramspider -d {domain} -l {archive_list}", shell=True)
    elif command == 3:
        print(f"Comando executado: paramspider -s -d {domain}")
        subprocess.call(f"paramspider -s -d {domain}", shell=True)
    elif command == 4:
        prox = str(input("Digite o proxy a ser usado: "))
        print(f"Comando executado: paramspider -d {domain} --proxy {prox}")
        subprocess.call(f"paramspider -d {domain} --proxy {prox}", shell=True)
    elif command == 5:
        shell = str(input("Digite seu comando: "))
        print(f"Comando executado: ")
        subprocess.call(f"{shell}", shell=True)


def arjun(domain):
    print("""
    _
   /_| _ '                                                                                                                                       
  (  |/ /(//) v2.2.6                                                                                                                             
      _/                                                                                                                                         
Arjun serve para encontra parâmetros de endpoints de URL.

Comandos:

[0] Pré-Pronto: arjun -u {domain} -oB 127.0.0.1:9050 -o arjun.txt -t 2 -d 1
[1] Monte seu comando.
 
-u: Url de desinto
-o JSON_FILE: Salva o resultado em um arquivo json (-oT para texto)
-oB [BURP_PROXY]: Saída para o Burp Suite Proxy. O padrão é 127.0.0.1:8080.
-d DELAY Atraso: entre solicitações em segundos. (padrão: 0)
-t THREADS: Número de threads simultâneas. (padrão: 5)
-w WORDLIST: Caminho do arquivo da lista de palavras. (padrão: {arjundir}/db/large.txt).
-stable: Prefira estabilidade à velocidade.
--disable-redirects: desabilita redirecionamento\n""")

    command = int(input("Monte seu comando: "))
    if command == 1:
        print(f"Comando executado: arjun -u {domain} -oB 127.0.0.1:9050 -o arjun.txt -t 2 -d 1")
        subprocess.call(f"arjun -u {domain} -oB 127.0.0.1:9050 -o arjun.txt -t 2 -d 1", shell=True)
    else:
        shell = str(input("Monte seu comando: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)