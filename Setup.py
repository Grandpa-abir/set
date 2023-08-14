import os

def setup_termux():
    os.system("pkg update -y")
    os.system("pkg install git python python-dev clang -y")
    os.system("pkg install nano wget curl -y")
    os.system("pkg install libxml2 libxslt libjpeg-turbo -y")
    os.system("pkg install mercurial subversion -y")
    os.system("termux-setup-storage")
    os.system("pkg install neovim -y")
    os.system("pkg install openssh -y")
    os.system("sshd")
    os.system("pip install numpy matplotlib")
    os.system("pkg install apache2 -y")
    os.system("apachectl start")
    os.system("pkg install php -y")
    os.system("pkg install mariadb -y")
    os.system("mysqld_safe")
    os.system("pkg install nodejs -y")
    os.system("pkg install openjdk-17-jdk -y")
    os.system("pkg install ruby -y")
    os.system("pkg install make cmake autoconf -y")
    os.system("pkg install nginx -y")
    os.system("pkg install python-lxml libxml2-dev libxslt-dev -y")
    os.system("pkg install sed awk grep -y")
    os.system("pkg install git subversion -y")
    os.system("pkg install ufw -y")
    os.system("ufw enable")
    os.system("pkg install docker -y")
    os.system("pkg install rust -y")
    os.system("pkg install golang -y")
    os.system("pkg install zsh -y")
    os.system("sh -c '$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'")
    os.system("pkg install espeak -y")
    os.system("pip install jupyter")

    # Additional setup commands
    os.system("pkg install htop -y")
    os.system("pkg install tmux -y")
    os.system("pkg install ffmpeg -y")
    os.system("pkg install tree -y")
    os.system("pkg install vim -y")
    os.system("pkg install wget -y")
    os.system("pkg install curl -y")
    os.system("pkg install lynx -y")
    os.system("pkg install gimp -y")
    os.system("pkg install wireshark -y")
    os.system("pkg install nmap -y")
    os.system("pkg install netcat -y")
    os.system("pkg install telnet -y")
    os.system("pkg install whois -y")
    os.system("pkg install traceroute -y")
    os.system("pkg install dnsutils -y")
    os.system("pkg install tor -y")
    os.system("pkg install proxychains-ng -y")
    os.system("pkg install libreoffice -y")
    os.system("pkg install vlc -y")
    os.system("pkg install youtube-dl -y")
    os.system("pkg install newsboat -y")
    os.system("pkg install ranger -y")
    os.system("pkg install ncdu -y")
    os.system("pkg install hexedit -y")
    os.system("pkg install sqlite -y")
    os.system("pkg install transmission-cli -y")
    os.system("pkg install sshpass -y")
    os.system("pkg install irssi -y")
    
    # More setup commands
    os.system("pkg install figlet -y")
    os.system("pkg install toilet -y")
    os.system("pkg install cmatrix -y")
    os.system("pkg install cowsay -y")
    os.system("pkg install fortune -y")
    os.system("pkg install sl -y")
    os.system("pkg install screenfetch -y")
    os.system("pkg install ranger -y")
    os.system("pkg install fish -y")
    os.system("pkg install lynx -y")
    os.system("pkg install w3m -y")
    os.system("pkg install tmux -y")
    os.system("pkg install mpv -y")
    os.system("pkg install nmap -y")
    os.system("pkg install figlet -y")
    os.system("pkg install toilet -y")
    os.system("pkg install cmatrix -y")
    os.system("pkg install cowsay -y")
    os.system("pkg install fortune -y")
    os.system("pkg install sl -y")
    os.system("pkg install screenfetch -y")
    os.system("pkg install ranger -y")
    os.system("pkg install fish -y")
    os.system("pkg install lynx -y")
    os.system("pkg install w3m -y")
    os.system("pkg install tmux -y")
    os.system("pkg install mpv -y")
    os.system("pkg install nmap -y")
    os.system("pkg install wget -y")
    os.system("pkg install curl -y")
    os.system("pkg install zip -y")
    os.system("pkg install unzip -y")
    os.system("pkg install tar -y")
    os.system("pkg install gzip -y")
    os.system("pkg install bzip2 -y")
    os.system("pkg install xz-utils -y")
    os.system("pkg install ssh -y")
    os.system("pkg install telnet -y")
    os.system("pkg install rsync -y")
    os.system("pkg install wget -y")
    os.system("pkg install curl -y")
    os.system("pkg install zip -y")
    os.system("pkg install unzip -y")
    os.system("pkg install tar -y")
    os.system("pkg install gzip -y")
    os.system("pkg install bzip2 -y")
    os.system("pkg install xz-utils -y")
    os.system("pkg install ssh -y")
    os.system("pkg install telnet -y")
    os.system("pkg install rsync -y")
    
    # Even more setup commands
    os.system("pkg install mc -y")
    os.system("pkg install midnight-commander -y")
    os.system("pkg install lynx -y")
    os.system("pkg install w3m -y")
    os.system("pkg install tmux -y")
    os.system("pkg install mpv -y")
    os.system("pkg install nmap -y")
    os.system("pkg install figlet -y")
    os.system("pkg install toilet -y")
    os.system("pkg install cmatrix -y")
    os.system("pkg install cowsay -y")
    os.system("pkg install fortune -y")
    os.system("pkg install sl -y")
    os.system("pkg install screenfetch -y")
    os.system("pkg install ranger -y")
    os.system("pkg install fish -y")
    os.system("pkg install lynx -y")
    os.system("pkg install w3m -y")
    os.system("pkg install tmux -y")
    os.system("pkg install mpv -y")
    os.system("pkg install nmap -y")
    os.system("pkg install wget -y")
    os.system("pkg install curl -y")
    os.system("pkg install zip -y")
    os.system("pkg install unzip -y")
    os.system("pkg install tar -y")
    os.system("pkg install gzip -y")
    os.system("pkg install bzip2 -y")
    os.system("pkg install xz-utils -y")
    os.system("pkg install ssh -y")
    os.system("pkg install telnet -y")
    os.system("pkg install rsync -y")
    os.system("pkg install wget -y")
    os.system("pkg install curl -y")
    os.system("pkg install zip -y")
    os.system("pkg install unzip -y")
    os.system("pkg install tar -y")
    os.system("pkg install gzip -y")
    os.system("pkg install bzip2 -y")
    os.system("pkg install xz-utils -y")
    os.system("pkg install ssh -y")
    os.system("pkg install telnet -y")
    os.system("pkg install rsync -y")
    
if __name__ == "__main__":
    setup_termux()
