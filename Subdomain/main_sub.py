import subprocess


def gauplus(domain):
    print("""

 .oOOOo.                       o             
.O     o                      O              
o                             o              
O                             O              
O   .oOOo .oOoO' O   o  .oOo. o  O   o  .oOo 
o.      O O   o  o   O  O   o O  o   O  `Ooo.
 O.    oO o   O  O   o  o   O o  O   o      O
  `OooO'  `OoO'o `OoO'o oOoO' Oo `OoO'o `OoO'
                        O                    
                        o' 

Comandos: 

[1] Pré-pronto: echo \"domain\" | gauplus -b png,jpg,gif -p 127.0.0.1:9050 -random-agent -subs | anew 
[2] Monte seu comando:

-b string: extensões para pular, ex: ttf,woff,svg,png,jpg
-json: escreve a saída como json
-o string: nome do arquivo para escrever os resultados
-p string: proxy HTTP para usar
-providers string:  provedores para buscar URLs (padrão "wayback,otx,commoncrawl")
-random-agent: usa user-agent aleatório
-subs: inclui subdomínios do domínio de destino
-t int: quantidade de workers paralelos (padrão 5)
-v habilita o modo verbose\n""")

    command = int(input("Comando: "))
    if command == 1:
        print(
            f"Comando executado: echo \"{domain}\" | gauplus -b png,jpg,gif -p 127.0.0.1:9050 -random-agent -subs | anew")
        subprocess.call(f"echo \"{domain}\" | gauplus -b png,jpg,gif -p 127.0.0.1:9050 -random-agent -subs | anew",
                        shell=True)
    elif command == 2:
        shell = str(input("Shell: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def waybackurl(domain):
    print("""
.::        .::                   .::                       .::     
.::        .::                   .::                       .::     
.::   .:   .::   .::    .::   .::.::         .::       .:::.::  .::
.::  .::   .:: .::  .::  .:: .:: .:: .::   .::  .::  .::   .:: .:: 
.:: .: .:: .::.::   .::    .:::  .::   .::.::   .:: .::    .:.::   
.: .:    .::::.::   .::     .::  .::   .::.::   .::  .::   .:: .:: 
.::        .::  .:: .:::   .::   .:: .::    .:: .:::   .:::.::  .::
                         .::

O waybackurl é uma ferramenta que busca por subdiretórios dentro do web archive.

[0] Pré-pronto: echo \"domain\" | waybackurls -dates | anew
[1]-dates: mostra a data da busca na primeira coluna
[2]-get-versions: lista URLs para versões rastreadas de URL(s) de entrada
[3]-no-subs: não inclui subdomínios do domínio de destino
[4] Monte seu comando\n""")
    command = int(input("Comando: "))
    if command == 1 or command == 2:
        print(f"Comando executado: echo \"{domain}\" | waybackurls -dates | anew")
        subprocess.call(f"echo \"{domain}\" | waybackurls -dates | anew", shell=True)
    elif command == 3:
        print(f"Comando executado: echo \"{domain}\" | waybackurls -get-versions | anew")
        subprocess.call(f"echo \"{domain}\" | waybackurls -get-versions | anew", shell=True)
    elif command == 4:
        print(f"Comando executado: echo \"{domain}\" | waybackurls -no-subs | anew")
        subprocess.call(f"echo \"{domain}\" | waybackurls -no-subs | anew", shell=True)
    elif command == 5:
        shell = str(input("Shell: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def feroxbuster(domain):
    print("""
 _____                    ____            _            
|  ___|__ _ __ _____  __ | __ ) _   _ ___| |_ ___ _ __ 
| |_ / _ \\ '__/ _ \\ \\/ / |  _ \\| | | / __| __/ _ \\ '__|
|  _|  __/ | | (_) >  <  | |_) | |_| \\__ \\ ||  __/ |   
|_|  \\___|_|  \\___/_/\\_\\ |____/ \\__,_|___/\\__\\___|_|

Feroxbuster é uma das ferramentas mais rápidas de brute force de url
para ser usada! 

Comandos:

[0] Pré-Pronto
[1] -a: Para definir um usuário (padrão: feroxbuster/2.10.2).
[2] -f: Anexa / ao URL de cada solicitação.
[3] --dont-scan <URL>: Para excluir varreduras
[4] Monte seu código.\n""")

    command = int(input("Comando: "))

    if command == 0:
        print(f"Comando executado: feroxbuster --burp -u {domain}")
        subprocess.call(f"feroxbuster --burp -u {domain}", shell=True)

    elif command == 1:
        version = str(input("User: "))
        print(f"Comando executado: feroxbuster -a {version} -u {domain}")
        subprocess.call(f"feroxbuster -a {version} -u {domain}", shell=True)

    elif command == 4:
        print(f"Comando executado: feroxbuster -f -u {domain}")
        subprocess.call(f"feroxbuster -f -u {domain}", shell=True)

    elif command == 3:
        url = str(input("Url: "))
        print(f"Comando executado: feroxbuster --dont-scan {url} -u {domain}")
        subprocess.call(f"feroxbuster --dont-scan {url} -u {domain}", shell=True)

    elif command == 4:
        shell = str(input("Shell: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def wfuzz(domain):
    print("""
\\ \\        /  _|                 
 \\ \\  \\   /  |    |   | _  / _  /
  \\ \\  \\ /   __|  |   |   /    / 
   \\_/\\_/   _|   \\__,_| ___| ___|

O Wfuzz é uma ferramenta de fuzzing para testar aplicações web de forma simples e eficiente.

Comandos:

[0] Pré-Pronto.
[1] -p ip:port:type : Para uso de proxy. (SOCKS4, SOCKS5, HTTP)
[2] --script= : para uso de scripts
[3] -t <num> : Especifique o número de conexões simultâneas (10 padrão)
[4] -L : Siga redirecionamentos HTTP
[5] Método -X: Especifique um método HTTP para a solicitação, ou seja. HEAD ou FUZZ
[6] -d pós-dados: Use dados de postagem (ex: "id=FUZZ&catalogue=1")
[7] Monte seu comando.\n""")

    print("Arquivos a serem usados: ")
    subprocess.call("ls /usr/share/wfuzz/wordlist/general/", shell=True)

    command = int(input("\nComando: "))
    protocol = str(input("http ou https: "))
    sub_director = str(input("Sub diretórios para fuzz (tire o primeiro /): "))
    file = str(input("Digite o arquivo para fuzzing: "))

    if command == 0:
        print(
            f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -p 127.0.0.1:9050:SOCKS5 --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")
        subprocess.call(f"wfuzz -p 127.0.0.1:9050:SOCKS5 --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ",
                        shell=True)

    elif command == 1:
        proxy_config = str(input("IP:PORT:TYPE = "))
        print(
            f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -p {proxy_config} --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")
        subprocess.call(
            f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -p {proxy_config} --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")

    elif command == 2:
        scripts_list = str(input("\nListar scripts?[y/n]")).lower()
        if scripts_list == "y":
            subprocess.call("wfuzz -e scripts", shell=True)
        elif not scripts_list:
            pass

        script = str(input("\nDigite o 'name' do script: "))
        print(
            f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} --script={script} --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")
        subprocess.call(
            f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} --script={script} --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ",
            shell=True)

    elif command == 3:
        threads = int(input("Número de threads: "))
        print(
            f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -t {threads} --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")
        subprocess.call(
            f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -t {threads} --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ",
            shell=True)

    elif command == 4:
        print(
            f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -L --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")
        subprocess.call(
            f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -L --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ",
            shell=True)

    elif command == 5:
        m_tod = str(input("HEAD or FUZZ: "))

        print(
            f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} {m_tod} -X --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")
        subprocess.call(
            f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} {m_tod} -X --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ",
            shell=True)

    elif command == 6:
        dates = str(input("Dates: "))

        print(
            f"Comando executado: wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -d '{dates}' --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ")
        subprocess.call(
            f"wfuzz -w /usr/share/wfuzz/wordlist/general/{file} -d '{dates}' --hc 404 -u {protocol}://{domain}/{sub_director}FUZZ",
            shell=True)

    elif command == 7:
        shell = str(input("Shell: "))
        subprocess.call(f"{shell}", shell=True)

