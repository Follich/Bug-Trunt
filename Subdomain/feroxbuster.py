def feroxbuster(domain):
    import subprocess
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
