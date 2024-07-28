def options_install_tools():
    print("""
A opção que você selecionou é um manual com todos os comandos que você vai precisar
executar caso sua máquina não tenha alguma delas instalado!

[0] Golang: 
 rm -rf /usr/local/go && tar -C /usr/local -xzf go1.22.5.linux-amd64.tar.gz
 

[?] GF:
go get -u github.com/tomnomnom/gf""")
