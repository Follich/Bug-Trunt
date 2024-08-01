import subprocess


def xargs(domain):
    print("""
_ _ ____ ____ ____ ____
_X_ |--| |--< |__, ====

O xargs é O xargs é um comando usado para construir e executar linhas de comando.

Comandos: 

[0] Pré-Pronto: xargs -a <list> -I@ sh -c '<ferramenta> @ | anew <list_2>' = chama o bash para concatenar uma lista a outra.
[1] Monte seu comando.

-a, --arg-file=FILE: Lê argumentos de FILE, não da entrada padrão
-d, --delimiter=CHARACTER: Os itens no fluxo de entrada são separados por CHARACTER, não por espaço em branco;
-E END: Define a sequência EOF lógica se END ocorrer como uma linha de entrada, o restante da entrada será ignorado (ignorado se -0 ou -d for especificado)
-e, --eof[=END]: Equivalente a -E END se END for especificado; caso contrário, não há string de fim de arquivo
-I R: Igual a --replace=R -i
--replace[=R]: Substitua R em INITIAL-ARGS por nomes lidos da entrada padrão. divididos em novas linhas;
-L, --max-lines=MAX-LINES: Use no máximo MAX-LINES linhas de entrada não vazias por linha de comando 
-l[MAX-LINES]: Semelhante a -L, mas o padrão é no máximo uma linha de entrada não em branco se MAX-LINES não for especificado 
-n, --max-args=MAX-ARGS: Usa no máximo argumentos MAX-ARGS por linha de comando 
-o, --open-tty: Reabrir stdin como /dev/tty no processo filho antes de executar o comando; útil para executar um aplicativo interativo. 
-P, --max-procs=MAX-PROCS: Executa no máximo processos MAX-PROCS por vez
-p, --interactive: Avisa antes de executar comandos
--process-slot-var=VAR: Define a variável de ambiente VAR em processos filhos 
-r , --no-run-if-empty: Se não houver argumentos, então não execute COMMAND; se esta opção não for fornecida, COMMAND será executado pelo menos uma vez 
-s, --max-chars=MAX-CHARS: Limita o comprimento da linha de comando para MAX-CHARS 
--show-limits: Mostra limites no comprimento da linha de comando 
-t, --verbose: Imprime comandos antes de executá-los 
-x, --exit: Sai se o tamanho (veja -s) for excedido\n""")
    command = int(input("Comando: "))

    if command == 0:
        subprocess.call("ls", shell=True)
        lista_01 = str(input("Nome ou caminho da primeira lista: "))
        lista_02 = str(input("Nome ou caminho da segunda lista: "))
        ferramenta = str(input("Nome da ferramenta a ser usada: "))
        print(f"\nComando executado: xargs -a {lista_01} -I@ sh -c \'{ferramenta} @ | anew {lista_02}")
        subprocess.call(f"xargs -a {lista_01} -I@ sh -c \'{ferramenta} @ | anew {lista_02}", shell=True)
    else:
        subprocess.call("ls", shell=True)
        shell = str(input("Shell: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def nuclei(domain):
    print("""
                     __     _
   ____  __  _______/ /__  (_)
  / __ \\/ / / / ___/ / _ \\/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\\__,_/\\___/_/\\___/_/ 

O nuclei é usado para enviar solicitações entre destinos com base em um modelo, 
levando a zero falsos positivos e fornecendo varredura rápida em um grande número de hosts. 
O Nuclei oferece digitalização para uma variedade de protocolos, incluindo TCP, DNS, HTTP, SSL, Arquivo, Whois, 
Websocket, Headless, Código, etc. Com modelos flexíveis,
o Nuclei pode ser usado para modelar todos os tipos de verificações de segurança.

Comandos:

[0] Pré-Pronto: cat <list_01> | nuclei -t /root/nuclei-templates -o nuclei_results
[1] Monte seu comando.

-u, -target string[] URLs/hosts de destino para escanear
-l, -list string caminho para o arquivo contendo uma lista de URLs/hosts de destino para escanear (um por linha)
-eh, -exclude-hosts string[] hosts para excluir para escanear da lista de entrada (ip, cidr, nome do host)
-resume string retomar escaneamento usando resume.cfg (o clustering será desabilitado)
-sa, -scan-all-ips escanear todos os IPs associados ao registro dns
-o, -output string arquivo de saída para gravar problemas/vulnerabilidades encontrados
-t, -templates string[] lista de modelos ou diretório de modelos para executar (separados por vírgula, arquivo)
-w, -workflows string[] lista de fluxos de trabalho ou diretório de fluxos de trabalho para executar\n""")
    command = int(input("Comando: "))

    if command == 0:
        subprocess.call("ls", shell=True)
        lista_01 = str(input("Caminho ou nome do arquivo: "))
        print(f"Comando executado: cat {lista_01} | nuclei -t /root/nuclei-templates -o nuclei_results")
        subprocess.call(f"cat {lista_01} | nuclei -t /root/nuclei-templates -o nuclei_results", shell=True)
    else:
        subprocess.call("ls", shell=True)
        shell = str(input("Shell:"))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def dalfox():
    print(f"""
    _..._
  .' .::::.   __   _   _    ___ _ __ __
 :  :::::::: |  \\ / \\ | |  | __/ \\ V /
 :  :::::::: | o ) o || |_ | _( o )) (
 '. '::::::' |__/|_n_||___||_| \\_//_n_\
   '-.::''    

DalFox é uma poderosa ferramenta de código aberto que se concentra na automação
tornando-a ideal para verificar rapidamente falhas de XSS e analisar parâmetros. 
Seu mecanismo de teste avançado e recursos de nicho são projetados para agilizar o processo de detecção
e verificação de vulnerabilidades.

Comandos:

[0] Pré-pronto: cat <list> | dalfox --delay <int> (1000= 1s) | tee dalfox_results
[1] Monte seu comando.

conclusion: Gerar o script de autocompletar para o shell especificado
file: Usar modo de arquivo (lista de alvos ou rawdata)
help: Ajuda sobre qualquer comando
payload: Modo de carga útil, criar e enum cargas úteis
pipe: Usar modo de pipeline
server: Iniciar servidor de API
sxss : Usar modo XSS armazenado
url: Usar modo de alvo único
version: Mostrar versão

-b, --blind string: Adicione seu xss
-o, --output string: Grava no arquivo de saída (por padrão, apenas o código PoC é salvo)
--proxy string: Envia todas as solicitações ao servidor proxy.
-F, --follow-redirects: Segue o redirecionamento\n""")
    command = int(input("Comando: "))

    if command == 0:
        subprocess.call("ls", shell=True)
        lista_01 = str(input("Caminho ou nome da lista: "))
        print(f"Comando executado: cat {lista_01} | dalfox | tee dalfox_results")
        delay = int("Delay: ")
        subprocess.call(f"cat {lista_01}| dalfox --delay {delay} | tee dalfox_results", shell=True)
    else:
        subprocess.call("ls", shell=True)
        shell = str(input("Shell:"))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def katana(domain):
    print("""
   __        __                
  / /_____ _/ /____ ____  ___ _
 /  '_/ _  / __/ _  / _ \\/ _  /
/_/\\_\\\\_,_/\\__/\\_,_/_//_/\\_,_/\\  

Essa ferramenta serve para:
* Rastreamento da web rápido e totalmente configurável
* Modo padrão e sem cabeça Modo ativo e passivo 
* Análise / rastreamento de JavaScript 
* Preenchimento automático de formulário personalizável 
* ...

Comandos:

[0] Pré-pronto: katana -u <domain> | anew | tee katana_results
[1] Monte seu comando.

-u, -list string[]: Url de destino / lista para rastrear
-resume String: retomar varredura usando resume.cfg
-e, -exclude string[]: Excluir host que corresponde ao filtro especificado ('cdn', 'private-ips', cidr, ip, regex)
-r, -resolvers string[]: lista de resolvedores personalizados (arquivo ou separado por vírgula) 
-d, -profundidade int: profundidade máxima para rastrear (padrão 3) 
-jc, -js-crawl: habilitar análise/rastreamento de endpoint em arquivo javascript 
-jsl, -jsluice: habilitar a análise do jsluice no arquivo javascript (memória intensiva) 
-ct, -crawl-duration: valor duração máxima para rastrear o alvo para (s, m, h, d) (padrão s)
-proxy string: http/socks5 proxy a ser usado\n""")
    command = int(input("Comando: "))

    if command == 0:
        print(f"Comando executado: katana -u {domain}| anew | tee katana_results")
        subprocess.call(f"katana -u {domain}| anew | tee katana_results", shell=True)
    else:
        shell = str(input("Shell: "))
        print(f"Comando executado: {shell}")
        subprocess.call(f"{shell}", shell=True)


def jsscanner():
    print("""
/**
* ;_][ ((5 ((5 << //-\\ ][\\][ ][\\][ ]E ][2
*/

O jsscanner é uma ferramenta para testar urls .js para ver
se existe alguma informação sensivel lá dentro.

usr/bin/JSScanner/regex.txt\n""")
    subprocess.call("python3 usr/bin/JSScanner", shell=True)
