def firewall_scan(domain):
    import subprocess

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
