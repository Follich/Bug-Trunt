def domain_ip(domain):
    import subprocess

    print("""
     ___                             ___     
    (   )                           (   )    
     | | .-.     .--.       .--.     | |_    
     | |/   \   /    \    /  _  \   (   __)  
     |  .-. .  |  .-. ;  . .' `. ;   | |     
     | |  | |  | |  | |  | '   | |   | | ___ 
     | |  | |  | |  | |  _\_`.(___)  | |(   )
     | |  | |  | |  | | (   ). '.    | | | | 
     | |  | |  | '  | |  | |  `\ |   | ' | | 
     | |  | |  '  `-' /  ; '._,' '   ' `-' ; 
    (___)(___)  `.__.'    '.___.'     `.__.  
    
    Host é um utilitário simples para realizar pesquisas de DNS. Normalmente é usado
    para converter nomes em endereços IP e vice-versa. Quando não há argumentos ou opções
    são fornecidas, o host imprime um breve resumo de seus argumentos de linha de comando
    e opções.
    
    Comandos:
    
    [0] Pré-Pronto(default)
    [1] -p Esta opção especifica a porta a ser consultada no servidor. O padrão é 53.
    [2] -d Esta opção imprime rastreamentos de depuração e é equivalente a -v (opção detalhada).
    [3] -l -a imprimem todos os registros na zona.
    [4] -4 Esta opção especifica que apenas IPv4 deve ser usado para consulta
    [5] -6 Esta opção especifica que apenas IPv6 deve ser usado para consulta
    [6] Monte seu comando\n""")

    command = str(input("\tComando: "))

    if command == 0:
        subprocess.call(f"host {domain}", shell=True)
    elif command == 1:
        port = int(input("\tPorta: "))
        subprocess.call(f"host -p {port} {domain}", shell=True)
    elif command == 2:
        subprocess.call(f"host -d {domain}", shell=True)
    elif command == 3:
        subprocess.call(f"host -l -a {domain}", shell=True)
    elif command == 4:
        subprocess.call(f"host -4 {domain}", shell=True)
    elif command == 5:
        subprocess.call(f"host -6 {domain}", shell=True)
    else:
        shell = str(input("\tShell: "))
        subprocess.call(f"{shell}", shell=True)
