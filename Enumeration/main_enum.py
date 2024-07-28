import subprocess


def gf(domain):
    print("""
   ,___        _   ______                 
  /   /o      //  (  /     o             /
 /  __.  _   //    -/--_  ,  _  _ _   __/ 
(___/ (_/ (_(/_   _/  / (_(_(/_/ / /_(_/_ 

Gf é uma ferramenta de enumeração de vulnerabilidades por parametros em diversas
urls psssadas.

Sinopse:

echo "domain" | <ferramenta de enumeração de url | gf <patterns>

Patterns disponiveis:

1 - debug_logic     5 - interestingparams  9 - sqli  13 - ssrf
2 - idor            6 - interestingsubs    10 - rce       
3 - img-traversal   7 - jsvar              11 - ssti
4 - interestingEXT  8 - lfi                12 - xss

Comandos:

[1] Pré-pronto = Sinopse
[2] Monte seu comando\n""")

    try:
        command = int(input("Digite seu comando: "))

        if command == 1:
            tool_enum = str(input("Qual ferramenta de enumeração de url deseja usar? "))
            pattern = str(input("Qual pattern listado a cima deseja usar? "))

            print(f"Comando executado: echo \"{domain}\" | {tool_enum} | gf {pattern}")
            subprocess.call(f"echo \"{domain}\" | {tool_enum} | gf {pattern}", shell=True)
        elif command == 2:
            shell = str(input("Digite seu comando: "))
            print(f"Comando executado: {shell}")
            subprocess.call(f"{shell}", shell=True)
    except:
        pass
