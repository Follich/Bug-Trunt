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
""")
