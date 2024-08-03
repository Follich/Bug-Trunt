import subprocess


def burp_suit():
    print("""
_____  __ __ _____ _____ 
| () )|  |  || () )| ()_)
|_()_) \\___/ |_|\\_\\|_|

O Burp Suite é uma plataforma integrada para a realização de testes de segurança em aplicações web.
Ele possui diversas ferramentas que funcionam em conjunto para apoiar todo o processo de testes,
desde o mapeamento e análise da superfície de ataque até a descoberta e exploração de vulnerabilidades.\n""")

    subprocess.call("burpsuite", shell=True)
    print("Pressione CTRL + C para fechar.")


def wp_scan(domain):
    print("""
__          _______   _____
\\ \\        / /  __ \\ / ____|
 \\ \\  /\\  / /| |__) | (___   ___  __ _ _ __
  \\ \\/  \\/ / |  ___/ \\___ \\ / __|/ _` | '_ \\
   \\  /\\  /  | |     ____) | (__| (_| | | | | 
    \\/  \\/   |_|    |_____/ \\___|\\__,_|_| |_|

O WPScan é um scanner de vulnerabilidades de código aberto e multiplataforma, escrito na linguagem Ruby.

Comandos:

[0] Pré-Pronto: ()
[1] -e: Enumeração
[2] -t: Threads
[3] --proxy: Proxy
[4] -f: Formato
[5] Monte seu comando.\n""")
    command = int(input("Comando: "))

    if command == 0:
        print(f"Comando executado: wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -t 1 -f json -o wp.txt")
        subprocess.call(f"wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -t 1 -f json -o wp.txt", shell=True)

    elif command == 1:
        plugins = str(input("""
        Que tipo de enumeração você gostaria de fazer?

        * vp = Plugins vulneráveis
        * ap = Todos os plugins
        * vt = Temas vulneráveis
        * tt = ThimThumbs
        * cb = Backups de recuperação
        * dbe = Exportações de banco de dados
        * u = Intervalo de IDs de usuário. por exemplo: u1-5
        * m = Intervalo de IDs de mídia. por exemplo, m1-15 Nota

        (Separe por ',' se usar mais de um)R: \n"""))

        print(f"Comando executado: wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -e {plugins} -t 1 -o wp.txt")

        subprocess.call(f"wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -e {plugins} -t 1 -o wp.txt", shell=True)

    elif command == 2:
        threads = int(input("Defina o número de threads: "))

        print(f"Comando executado: wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -t {threads} -o wp.txt")
        subprocess.call(f"wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -t {threads} -o wp.txt", shell=True)

    elif command == 3:
        proxy_definido = str(input("Defina seu proxy [Protocolo://Ip:Porta]"))

        print("""
        Que tipo de modo você gostaria de usar? 

        * --user-agent: modo padrão
        * --random-user-agent: usuário aleatório para cada scan
        * --stealthy: Definido como --random-user-agent / --detection-mode passivo / --plugins-version-detection passivo""")
        modo_definido = str(input("Modo: "))

        print(f"Comando executado: wpscan {proxy_definido} {modo_definido} --url {domain} --force -t 1 -o wp.txt")
        subprocess.call(f"wpscan {proxy_definido} {modo_definido} --url {domain} --force -t 1 -o wp.txt", shell=True)

    elif command == 4:
        print("Tipos de formato: cli-no-color, cli-no-color, json, cli")
        formato = str(input("Formato: "))

        print(f"comando executado: wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -t 1 -f {formato} -o wp.txt")
        subprocess.call(f"wpscan --proxy SOCKS5://127.0.0.1:9050 --stealthy --url {domain} --force -t 1 -f {formato} -o wp.txt", shell=True)

    else:
        shell = str(input("Shell:"))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def metasploit():
    print("""
Comandos:

msfdb init: inicia o banco de dados
help: Menu de Ajuda
exit: Sai do console\n""")
    print("Depois de: service postgresql stop")
    subprocess.call("service postgresql start | msfdb init | msfconsole", shell=True)


def dotdotpwn():
    print("""
#################################################################################
#                                                                               #
#  CubilFelino                                                       Chatsubo   #
#  Security Research Lab              and            [(in)Security Dark] Labs   #
#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #
#                                                                               #
#                               pr0udly present:                                #
#                                                                               #
#  ________            __  ________            __  __________                   #
#  \\______ \\    ____ _/  |_\\______ \\    ____ _/  |_\\______   \\__  _  __ ____    #
#   |    |  \\  /  _ \\   __\\|    |  \\  /  _ \\   __\\|     ___/\\ \\/ \\/ //    \\   #
#   |    `   \\(  <_> )|  |  |    `   \\(  <_> )|  |  |    |     \\     /|   |  \\  #
#  /_______  / \\____/ |__| /_______  / \\____/ |__|  |____|      \\/\\_/ |___|  /  #
#          \\/                      \\/                                      \\/   #
#                              - DotDotPwn v3.0.2 -                             #
#                         The Directory Traversal Fuzzer                        #
#                         http://dotdotpwn.sectester.net                        #
#                            dotdotpwn@sectester.net                            #
#                                                                               #
#                               by chr1x & nitr0us                              #
#################################################################################

Dodotpwn é ferramenta de fuzz para LFI! E usar ela é simples basta apenas colocar a url
e o parametro para ser testado.

Sinopse: 

dotdotpwn -k root -m <módulo> -u <url=TRAVERSAL> -t <threads> -b | tee dotdot

Comandos:

[0] Padrão = Sinopse
[1] Monte seu comando

-m: Módulo [http | http-url | ftp | tftp | payload | stdout]
-O: Detecção do sistema operacional para fuzzing inteligente (nmap)
-s: Detecção da versão do serviço (banner grabber)
-d: Profundidade das travessias (por exemplo, profundidade 3 é igual a ../../../; padrão: 6)
-u: URL com a parte a ser fuzzed marcada como TRAVERSAL (por exemplo, http://foo:8080/id.php?x=TRAVERSAL&y=31337)
-p: Nome do arquivo com o payload a ser enviado e a parte a ser fuzzed marcada com a palavra-chave TRAVERSAL
-t: Tempo em milissegundos entre cada teste (padrão: 300 (.3 segundos))
-X: Use o Algoritmo de Bissecção para detectar a profundidade exata assim que uma vulnerabilidade for encontrada
-e: Extensão do arquivo anexada no final de cada string fuzz (por exemplo, ".php", ".jpg", ".inc")
-M: Método HTTP a ser usado ao usar o módulo 'http' [GET | POST | HEAD | COPY | MOVE] (padrão: GET)
-r: Nome do arquivo do relatório (padrão: 'HOST_MM-DD-YYYY_HOUR-MIN.txt')
-b: Interromper após a primeira vulnerabilidade ser encontrada

Como é bem simples é preferível que você monte seu comando ou use o padrão.\n""")
    command = int(input("Comando: "))

    if command == 0:
        threads = int(input("Threads: "))
        url = str(input("Digite a url completa faltando o valor do parametro:"))
        print(f"Comando executado: dotdotpwn -k root -m http-url -u {url}TRAVERSAL -t {threads} -b")
        subprocess.call(f"dotdotpwn -k root -m http-url -u {url}TRAVERSAL -t {threads} -b", shell=True)
    else:
        shell = str(input("Digite seu comando: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def jsql():
    print("""
 ,  ,-.   ,-.   ,   
 | (   ` /   \\  |   
 |  `-.  |   |  |   
 | .   ) \\   X  |   
-'  `-'   `-' ` `--'

O jsql é uma ferramenta que tem diversas funções de scan mas é que é focada
príncipalmente no sql injection.Tendo também outras funções e sendo bem útil!\n

Decidi também adicionar o sqlmap por que ele é bem útil.

[0] Pré-pronto: sqlmap -u "<url>" --current-db --tor --check-tor --random-agent --threads=<threads> -v <verbose> --risk=<risk> --level=<lvl>
[1] Jsql.
[2] Monte seu comando.

--random-agent Use o valor de cabeçalho HTTP User-Agent selecionado aleatoriamente
--proxy=PROXY Use um proxy para conectar-se à URL de destino
--tor Use a rede de anonimato Tor
--check-tor Verifique se o Tor está sendo usado corretamente

-a, --all Recupera tudo
-b, --banner Recupera banner DBMS
--current-user Recupera usuário atual DBMS
--current-db Recupera banco de dados atual DBMS
--passwords Enumera hashes de senha de usuários DBMS
--dbs Enumera bancos de dados DBMS
--tables Enumera tabelas de banco de dados DBMS
--columns Enumera colunas de tabela de banco de dados DBMS
--schema Enumera esquema DBMS
--dump Esvazia entradas de tabela de banco de dados DBMS
--dump-all Esvazia todas as entradas de tabela de banco de dados DBMS
-D Banco de dados DBMS a ser enumerado
-T TBL Tabela(s) de banco de dados DBMS a ser enumerada
-C COL Coluna(s) de tabela de banco de dados DBMS a ser enumerada
--level=LEVEL  Level of tests to perform (1-5, default 1)
--risk=RISK  Risk of tests to perform (1-3, default 1)\n""")
    command = int(input("Comando:"))

    if command == 0:
        url = str(input("Url contaminada: "))
        threads = int(input("Número de threads: "))
        verbose = int(input("Nivel de verbose 1-6: "))
        risk = int(input("Risk (1-3) = "))
        level = int(input("Level (1-5) = "))
        print(f"Comando executado: sqlmap -u {url} --current-db --tor --check-tor  --random-agent --threads={threads} -v {verbose} --risk={risk} --level={level}")
        subprocess.call(f"sqlmap -u {url} --current-db --tor --check-tor  --random-agent --threads={threads} -v {verbose} --risk={risk} --level={level}", shell=True)
    elif command == 1:
        subprocess.call("jsql", shell=True)

    else:
        shell = str(input("Digite seu comando: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)
