def burp_suit():
    import subprocess
    print("""
_____  __ __ _____ _____ 
| () )|  |  || () )| ()_)
|_()_) \\___/ |_|\\_\\|_|

O Burp Suite é uma plataforma integrada para a realização de testes de segurança em aplicações web.
Ele possui diversas ferramentas que funcionam em conjunto para apoiar todo o processo de testes,
desde o mapeamento e análise da superfície de ataque até a descoberta e exploração de vulnerabilidades.\n""")

    subprocess.call("burpsuite", shell=True)
