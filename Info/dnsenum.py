def dns_info_1(domain):
    import subprocess

    print("""
            ,,                                                                      
          `7MM                                                                      
            MM                                                                      
        ,M""bMM  `7MMpMMMb.  ,pP"Ybd  .gP"Ya `7MMpMMMb.`7MM  `7MM  `7MMpMMMb.pMMMb.  
      ,AP    MM    MM    MM  8I   `" ,M'   Yb  MM    MM  MM    MM    MM    MM    MM  
      8MI    MM    MM    MM  `YMMMa. 8M""""""  MM    MM  MM    MM    MM    MM    MM  
      `Mb    MM    MM    MM  L.   I8 YM.    ,  MM    MM  MM    MM    MM    MM    MM  
       `Wbmd"MML..JMML  JMML.M9mmmP'  `Mbmmd'.JMML  JMML.`Mbod"YML..JMML  JMML  JMML.
     
     O dnsenum é script multithread para enumerar informações em um domínio e para
     descobrir blocos IP não contíguos
     
     Comandos:
     
     [0] Pré-Pronto (dnsenum <domínio> -f /usr/share/dnsenum/dns.txt)
     [1] --private: Mostra e salva ips privados no final de o arquivo domínio_ips.txt.
     [2] --threads <num>: Número de threads que irão executar em consultas diferentes.
     [3] -f: Lê subdomínios de um arquivo para fazer brute force.
     [4] -v: Para que o processo seja detalhado (mostra todo o progresso e todas as mensagens de erro)
     [5] -www site:domínio: Eliminará subdomínios da pesquisa do Google.
     [6] -s: número máximo de subdomínios que será extraído do Google.
     [7] Monte seu comando\n""")

    command = int(input("\tComando: "))

    if command == 0:
        print(f"\n\tComando executado: dnsenum {domain} -f /usr/share/dnsenum/dns.txt")
        subprocess.call(f"dnsenum {domain} -f /usr/share/dnsenum/dns.txt", shell=True)

    elif command == 1:
        print(f"\n\tComando executado: dnsenum --private {domain}")
        subprocess.call(f"dnsenum --private {domain}", shell=True)

    elif command == 2:
        tr = int(input("\tNúmero de threads: "))
        print(f"\n\tComando executado: dnsenum --threads {tr} {domain}")
        subprocess.call(f"dnsenum --threads {tr} {domain}", shell=True)

    elif command == 3:
        file = str(input("\tLocal do arquivo: "))
        print(f"\n\tComando executado: dnsenum {domain} -f {file}")
        subprocess.call(f"dnsenum {domain} -f {file}", shell=True)

    elif command == 4:
        print(f"\n\tComando executado: dnsenum -v {domain}")
        subprocess.call(f"dnsenum -v {domain}", shell=True)

    elif command == 5:
        print(f"\n\tComando executado: dnsenum -www site:{domain}")
        subprocess.call(f"dnsenum -www site:{domain}", shell=True)

    elif command == 6:
        num = int(input("\tNúmero: "))
        print(f"\n\tComando executado: dnsenum -s {num} {domain}")
        subprocess.call(f"dnsenum -s {num} {domain}", shell=True)

    else:
        shell = str(input("\tShell: "))
        subprocess.call(f"{shell}", shell=True)
