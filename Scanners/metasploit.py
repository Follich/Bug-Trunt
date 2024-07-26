def metasploit():
    import subprocess
    print("""
Comandos:
    
help: Menu de Ajuda
exit: Sai do console\n""")
    subprocess.call("msfconsole", shell=True)
