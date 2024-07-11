def domain_ip(domain):
    import subprocess

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

    command = int(input("\tComando: "))

    if command == 0:
        print(f"\n\tComando executado: host {domain}")
        subprocess.call(f"host {domain}", shell=True)

    elif command == 1:
        port = int(input("\tPorta: "))
        print(f"\n\tComando executado: host -p {port} {domain}")
        subprocess.call(f"host -p {port} {domain}", shell=True)

    elif command == 2:
        print(f"\n\tComando executado: host -d {domain}")
        subprocess.call(f"host -d {domain}", shell=True)

    elif command == 3:
        print(f"\n\tComando executado: host -l -a {domain}")
        subprocess.call(f"host -l -a {domain}", shell=True)

    elif command == 4:
        print(f"\n\tComando executado: host -4 {domain}")
        subprocess.call(f"host -4 {domain}", shell=True)

    elif command == 5:
        print(f"\n\tComando executado: host -6 {domain}")
        subprocess.call(f"host -6 {domain}", shell=True)

    else:
        shell = str(input("\tShell: "))
        subprocess.call(f"{shell}", shell=True)
