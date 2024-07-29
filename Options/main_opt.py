def options_install_tools():
    print("""
A opção que você selecionou é um manual com todos os comandos que você vai precisar
executar caso sua máquina não tenha alguma delas instalado!

[0] Golang: 
 1 - apt install gccgo-go 
 2 - apt install golang-go
 3 - rm -rf /usr/local/go && tar -C /usr/local -xzf go1.22.5.linux-amd64.tar.gz
 4 - Coloque o comando = "export PATH=$PATH:/usr/local/go/bin" dentro de /root/.bashrc

[?] GF:

go install github.com/tomnomnom/gf@latest && mv /root/go/bin/gf /usr/bin/
mkdir /root/.gf 
cd /root/.gf
git clone https://github.com/1ndianl33t/Gf-Patterns
mv /root/.gf/Gf-Patterns/* /root/.gf
rm -rf Gf-Patterns
echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf

[?] Unfurl:

go install github.com/tomnomnom/unfurl@latest
mv /root/go/bin/unfurl /usr/bin 

[?] ParamSpider:

git clone https://github.com/devanshbatham/paramspider
cd paramspider
pip install .
cd .. 
rm -rf paramspider

[?] Arjun:

pip3 install arjun

[?] Subjs:

GO111MODULE=on go install -v github.com/lc/subjs@latest
mv /root/go/bin/subjs /usr/bin 

[?] Gauplus:

go install github.com/bp0lr/gauplus@latest
mv /root/go/bin/gauplus /usr/bin

[?] Waybackurls:

go install github.com/tomnomnom/waybackurls@latest
mv /root/go/bin/waybackurls /usr/bin

[?] Anti-Burl:

wget https://raw.githubusercontent.com/tomnomnom/hacks/master/anti-burl/main.go
go build main.go 
rm main.go
mv main anti-burl
mv anti-burl /usr/bin 

[?] Metabigor:

git clone https://github.com/j3ssie/metabigor.git
cd metabigor
go install
mv /root/go/bin/metabigor /usr/bin
cd ..
rm -rf metabigor 

[?] Kiterunner:

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

[?] Api git:

git clone https://github.com/gwen001/github-search
cd github-search
pip3 install -r requirements.txt
cd ..
mv github-search /usr/bin""")
