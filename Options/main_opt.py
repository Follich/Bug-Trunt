import subprocess

order = """
Aqui vai uma recomendação de qual ordem seguir de execução das ferramentas:

0 - Prepare Folder 
1 - Sites 
2 - Step by Step
3 - Burpsuite
4 - Whois
5 - Host
6 - Censys (redes / url) 
7 - Dnsrecon
8 - Gauplus (url / javascript )
9 - Wayback 
10 - Amass (url / asn)
11 - ParamSpider
12 - Apit git
13 - Gir Dorker
14 - Xargs (juntar todas as listas)
15 - Nuclei
16 - Httpx / Httprobe
17 - Aquatone 
18 - Subjs
19 - Anti-burl
20 - Jsscanner
22 - GF
23 - Wpscan
25 - Report"""
dorks = """
Dorks:
    
    inurl:responsible disclosure program
    inurl:vulnerability disclosure program
    inurl:vulnerability program rewards
    inurl:security@ report vulnerability
    inurl:bugbounty reward program"""
report = """
Elementos Essenciais de um Relatório:

Título Conciso e Descritivo: 
   * O título deve resumir a vulnerabilidade de forma clara e objetiva.
   Exemplo: "SQL Injection na página de login do sistema de e-commerce".
   
Descrição Detalhada:
    * Passo a passo para reproduzir o problema: Descreva cada etapa de forma clara e concisa, 
    utilizando uma linguagem técnica quando necessário.
    
    * Impacto da vulnerabilidade: Explique as consequências da exploração da vulnerabilidade, 
    como por exemplo, acesso não autorizado a dados sensíveis, execução de código arbitrário
    ou negação de serviço.
    
    Evidências: Inclua screenshots, vídeos, logs de rede ou outros tipos de evidências que comprovem
    a existência da vulnerabilidade.
    
Informações Técnicas:
    * Tipo de vulnerabilidade: Especifique o tipo de vulnerabilidade (SQL Injection, XSS, CSRF, etc.)
    e as referências a padrões de segurança relevantes (OWASP Top 10, CWE).
    
    * Versões de software e hardware: Indique as versões dos softwares e hardware envolvidos, pois isso
     pode ajudar a identificar se a vulnerabilidade já foi corrigida em versões mais recentes.
     
    * Gravidade: Avalie a gravidade da vulnerabilidade com base no impacto potencial e na facilidade
     de exploração. Utilize uma escala de severidade padrão (crítica, alta, média, baixa).
     
    * Recomendações: Sugira soluções para corrigir a vulnerabilidade, como patches, atualizações de software
     ou mudanças no código.

Dicas Adicionais:

    Seja claro e objetivo: Evite jargões técnicos excessivos e utilize uma linguagem clara e concisa.
    Organize as informações: Utilize uma estrutura lógica para o seu relatório, facilitando a compreensão do leitor.
    Priorize as informações mais importantes: Destaque as informações mais relevantes para a equipe de desenvolvimento.
    Seja profissional: Mantenha um tom profissional e respeitoso em todo o relatório.
    Utilize ferramentas de relatório: Existem diversas ferramentas que podem auxiliar na criação de relatórios de bug bounty, como plataformas de bug bounty e ferramentas de gerenciamento de vulnerabilidades."""
sites = """
Sites:

https://www.croxyproxy.com/ - spys.one = Proxy
crt.sh = certificado de dominios
https://nmap.org/nsedoc/scripts/ = para diferentes scripts
registro.br = consulta de infos de dominios br
https://en.fofa.info/result?qbase64=QmFuY29jbi5jb20%3D219.73.114.130:8000 = Api

Extensões:

Wappalyzer
Js beautify
Mate Translate"""
step_by_step = """
Coleta de informações:
* Logs:


* Emails:


* Números:


* Servidores dns:


* Portas abertas, IP'S:


* Infos Dominios / Subdominios:


* Url e arquivos ocultos:

* Javascript:

* Asn:


* Fluxo lógico da aplicação:

Scanning:

* Informações tiradas:

* Quais sistemas o site usa:

* Quais são os parametros do site:


Mapeamento:

* Acessível sem estar logado?
* Interage com a base de dados?
* Acessa alguma aplicação de terceiros?
* É possível fazer upload ou download de arquivos?
* Tem alguma interação? Formulários, pesquisa e etc?
* Exibe alguma mensagem de erro?"""
install_tools = """
apt install gccgo-go 
apt install golang-go
go install -v github.com/tomnomnom/anew@latest
mv /root/go/bin/anew /usr/bin
go install github.com/tomnomnom/gf@latest && mv /root/go/bin/gf /usr/bin/
mkdir /root/.gf 
cd /root/.gf
git clone https://github.com/1ndianl33t/Gf-Patterns
mv /root/.gf/Gf-Patterns/* /root/.gf
rm -rf Gf-Patterns
echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf
go install github.com/tomnomnom/unfurl@latest
mv /root/go/bin/unfurl /usr/bin
git clone https://github.com/devanshbatham/paramspider
cd paramspider
pip install .
cd .. 
rm -rf paramspider
pip3 install arjun
GO111MODULE=on go install -v github.com/lc/subjs@latest
mv /root/go/bin/subjs /usr/bin 
go install github.com/bp0lr/gauplus@latest
mv /root/go/bin/gauplus /usr/bin
go install github.com/tomnomnom/waybackurls@latest
mv /root/go/bin/waybackurls /usr/bin
wget https://raw.githubusercontent.com/tomnomnom/hacks/master/anti-burl/main.go
go build main.go 
rm main.go
mv main anti-burl
mv anti-burl /usr/bin
git clone https://github.com/j3ssie/metabigor.git
cd metabigor
go install
mv /root/go/bin/metabigor /usr/bin
cd ..
rm -rf metabigor
wget https://github.com/assetnote/kiterunner/releases/download/v1.0.2/kiterunner_1.0.2_linux_amd64.tar.gz
tar -xvf kiterunner_1.0.2_linux_amd64.tar.gz
mv kr /usr/bin
rm kiterunner_1.0.2_linux_amd64.tar.gz
wget https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-small.json.tar.gz
tar -xvf routes-small.json.tar.gz
rm routes-small.json.tar.gz
wget https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz
tar -xvf routes-large.kite.tar.gz 
rm routes-large.kite.tar.gz 
mv routes-large.kite /usr/bin
mv routes-small.json /usr/bin
git clone https://github.com/gwen001/github-search
cd github-search
pip3 install -r requirements.txt
cd ..
mv github-search /usr/bin
git clone https://github.com/obheda12/GitDorker
cd GitDorker 
pip3 install -r requirements.txt
cd ..
mv GitDorker /usr/bin
apt install ffuf
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
mv /root/go/bin/httpx /usr/bin
go install github.com/tomnomnom/httprobe@latest
mv /root/go/bin/httprobe /usr/bin
wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
unzip aquatone_linux_amd64_1.7.0.zip
mv aquatone /usr/bin
rm aquatone_linux_amd64_1.7.0.zip 
rm LICENSE.txt
rm README.md
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
mv /root/go/bin/nuclei /usr/bin
nuclei update-templates
go install github.com/hahwul/dalfox/v2@latest+
mv /root/go/bin/dalfox /usr/bin
go install github.com/projectdiscovery/katana/cmd/katana@latest
mv /root/go/bin/katana /usr/bin
git clone https://github.com/0x240x23elu/JSScanner.git
cd JSScanner
pip3 install -r  requirements.txt
cd ..
mv JSScanner /usr/bin
apt install leafpad
apt install jsql -y
apt update -y
apt upgrade -y"""


def man():
    man_choosen = str(input("Digite o nome da ferramenta (tudo minúsculo): "))
    subprocess.call(f"leafpad Man/{man_choosen}")


def options_install_tools():
    print("""
A opção que você selecionou é um manual com todos os comandos que você vai precisar
executar caso sua máquina não tenha alguma delas instalado!

[0] Golang: 
 apt install gccgo-go 
 apt install golang-go

[1] Anew:

go install -v github.com/tomnomnom/anew@latest
mv /root/go/bin/anew /usr/bin

[2] GF:

go install github.com/tomnomnom/gf@latest && mv /root/go/bin/gf /usr/bin/
mkdir /root/.gf 
cd /root/.gf
git clone https://github.com/1ndianl33t/Gf-Patterns
mv /root/.gf/Gf-Patterns/* /root/.gf
rm -rf Gf-Patterns
echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf

[3] Unfurl:

go install github.com/tomnomnom/unfurl@latest
mv /root/go/bin/unfurl /usr/bin 

[4] ParamSpider:

git clone https://github.com/devanshbatham/paramspider
cd paramspider
pip install .
cd .. 
rm -rf paramspider

[5] Arjun:

pip3 install arjun

[6] Subjs:

GO111MODULE=on go install -v github.com/lc/subjs@latest
mv /root/go/bin/subjs /usr/bin 

[7] Gauplus:

go install github.com/bp0lr/gauplus@latest
mv /root/go/bin/gauplus /usr/bin

[8] Waybackurls:

go install github.com/tomnomnom/waybackurls@latest
mv /root/go/bin/waybackurls /usr/bin

[9] Anti-Burl:

wget https://raw.githubusercontent.com/tomnomnom/hacks/master/anti-burl/main.go
go build main.go 
rm main.go
mv main anti-burl
mv anti-burl /usr/bin 

[10] Metabigor:

git clone https://github.com/j3ssie/metabigor.git
cd metabigor
go install
mv /root/go/bin/metabigor /usr/bin
cd ..
rm -rf metabigor 

[11] Kiterunner:

wget https://github.com/assetnote/kiterunner/releases/download/v1.0.2/kiterunner_1.0.2_linux_amd64.tar.gz
tar -xvf kiterunner_1.0.2_linux_amd64.tar.gz
mv kr /usr/bin
rm kiterunner_1.0.2_linux_amd64.tar.gz
wget https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-small.json.tar.gz
tar -xvf routes-small.json.tar.gz
rm routes-small.json.tar.gz
wget https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz
tar -xvf routes-large.kite.tar.gz 
rm routes-large.kite.tar.gz 
mv routes-large.kite /usr/bin
mv routes-small.json /usr/bin

[12] Api git:

git clone https://github.com/gwen001/github-search
cd github-search
pip3 install -r requirements.txt
cd ..
mv github-search /usr/bin

[13] Git-Dorker:

git clone https://github.com/obheda12/GitDorker
cd GitDorker 
pip3 install -r requirements.txt
cd ..
mv GitDorker /usr/bin

[14] Ffuf:

apt install ffuf

[15] Htppx:

go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
mv /root/go/bin/httpx /usr/bin

[16] Httprobe:

go install github.com/tomnomnom/httprobe@latest
mv /root/go/bin/httprobe /usr/bin

[17] Aquatone:

wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
unzip aquatone_linux_amd64_1.7.0.zip
mv aquatone /usr/bin
rm aquatone_linux_amd64_1.7.0.zip 
rm LICENSE.txt
rm README.md 

[18] Nuclei:

go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
mv /root/go/bin/nuclei /usr/bin
nuclei update-templates 

[19] Dalfox:

go install github.com/hahwul/dalfox/v2@latest+
mv /root/go/bin/dalfox /usr/bin

[20] Katana:

go install github.com/projectdiscovery/katana/cmd/katana@latest
mv /root/go/bin/katana /usr/bin

[21] JSscanner:

git clone https://github.com/0x240x23elu/JSScanner.git
cd JSScanner
pip3 install -r  requirements.txt
cd ..
mv JSScanner /usr/bin""")
    install = int(input("Deseja instalar todas as ferramentas? [0/1]"))
    if install == 0:
        subprocess.call(f"{install_tools}", shell=True)
    else:
        pass


def prepare_folder(domain):
    try:
        subprocess.call(f"mkdir {domain} | cd {domain} | mkdir lists | mkdir images | mkdir js | mkdir infos | mkdir vuls", shell=True)
        subprocess.call(f"cd infos | leafpad infos.txt", shell=True)
        print("Tudo pronto!")
    except:
        print("Algo deu errado!")
