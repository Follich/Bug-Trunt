import subprocess


def owasp_commum():
    subprocess.call("")


def owasp_install():
    subprocess.call("cd ~/Downloads", shell=True)

    subprocess.call("wget https://www.zaproxy.org/download/2/zap-2.15.0-linux.tar.gz | sha256sum zap-2.15.0-linux.tar.gz| sudo tar -xvf zap-2.15.0-linux.tar.gz | sudo mv zap-2.15.0 /opt/owasp-zap | sudo ln -s /opt/owasp-zap/zap.sh /usr/local/bin/zap", shell=True)
