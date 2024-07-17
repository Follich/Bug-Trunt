def censys(domain):
    import subprocess
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
