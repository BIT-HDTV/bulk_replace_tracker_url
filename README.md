# Bulk Replace Tracker Announce Url

Replaces old tracker url of torrents. Good for tracker announce url change or passkey change.


This tutorial works for qbitorrent, rtorrent, transmission

#### 1. Install

##### Windows

    1. Download python from https://www.python.org/downloads/ or Windows store (Python 3.10)

    2. Run the installer

    3. after the installed is done open command Prompt or PowerShell and write

    `python -V`

    and you should see
    example `Python 3.10.4`

##### Linux Ubuntu / Debian

(Most of you maybe have linux seedboxes that might have a sudo ssh terminal available)

    sudo apt install python3

without sudo

    version=3.10.4
    wget "https://www.python.org/ftp/python/$version/Python-$version.tgz"
    tar -zxvf "Python-$version.tgz"
    rm "Python-$version.tgz"
    cd "Python-$version"
    ./configure --prefix=$HOME/python
    make
    make altinstall
    cd ..
    rm -r "Python-$version"
    majMin="${version%.*}"
    ln -s "$HOME/python/bin/python${majMin}" ~/python/bin/python
    ln -s "$HOME/python/bin/pip${majMin}" ~/python/bin/pip

#### 2. Clone project

    open a terminal

    git clone https://github.com/BIT-HDTV/bulk_replace_tracker_url.git

    cd bulk_replace_tracker_url

#### 3. Get dependencies

    pip3 install -r requirements.txt

#### 4. Stop your client and backup the folder  !!!!! (see next point)

#### 5. Find out where your client stores the torrents

These are default paths for these clients, your might be different

qbitorrent
    usually in a folder called "BT_backup"

    Windows: C:\Users\<user>\AppData\Local\qBittorrent\BT_backup
    Ubuntu Desktop: ~/.local/share/data/qBittorrent/BT_backup
    Docker: <path_mount>/data/BT_backup

rtorrent/rutorrent

    usually in a folder called ".session"

    Windows: -
    Ubuntu: ~/.session
    docker: <path_mount>/rtorrent/session
    seedbox: ~/rtorrent/.session or ~/.session

transmission

    usually in a folder called "torrents"

    Windows: C:\Users\<user>\AppData\Local\transmission\Torrents
    Ubuntu Desktop: ~/.config/transmission/torrents
    Ubuntu server as daemon:  /var/lib/transmission-daemon/.config/transmission-daemon/torrents
    docker: <path_mount>/torrents
    seedbox:
    Qnap: ?
    Synology: ?

#### 6. Run


    python3 bulk_replace_tracker_url.py

answer the prompts

I advice to not run this script directly on the live client torrent's folder
This scripts makes a .bak file of the modified file already but just to be on the safe side.

#### 7. Start your client
