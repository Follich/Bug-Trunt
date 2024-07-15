def domain_info(domain):
    import subprocess

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
