def wp_scan(domain):
    import subprocess
    print("""
__          _______   _____
\\ \\        / /  __ \\ / ____|
 \\ \\  /\\  / /| |__) | (___   ___  __ _ _ __
  \\ \\/  \\/ / |  ___/ \\___ \\ / __|/ _` | '_ \
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
    elif command == 5:
        shell = str(input("Shell:"))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)
