# Cinnamon
Application for real time monitoring of a wireless network, by capturing and analysing the flow of 802.11 frames on a given environment. In order to achieve this, one can base its application on tools like Scapy, a Python program written to manipulate network packages. We used Scapy to sniff packets and to pass them to Python code purposely implemented in order to analyse and save collected data. The analysis was carried out by studying the structure of 802.11 frames in order to extract pivotal fields such as the type and the subtype. Then it is important to precisely define the type of a frame, and then to differentiate it. After that, we implemented a module able to read the analysis and insert them in some tables that are be displayed on the console screen with the use of Curses, a library that allows to manage textual terminals regardless of the terminal screen and keyboard. The tables are of two types: the first collects information relating to the stations, while the second contain the APs's information. The first table is, in turn, comprising another table containing more detailed information relating to the selected station and the AP with which it has exchanged a few packs. You can also save sniffing packets in a pcap file, or you can also do offline analysis, such as the analysis of the packages contained in pcap files.  You can also get, at the end of the analysis, a file containing some statistics of the tables's fields.

## Installation & Running

If it's the first time you use the Cinnamon tool, you must first install external software used in implementation. So, you need to ensure to have installed:
  - _Python_ (in this work we use 2.7 version)
  - _Scapy_
  - _Curses_



Steps to run include:
  - Grab the code:
    - `git clone https://github.com/nananan/Cinnamon`
    
  - Run the script called _install.sh_ to run the installation of Python's external component used:
    - `cd Cinnamon/Script`
    - `chmod +x install.sh`
    - `./install.sh`
    
  - Set wireless card into monitor mode: (this is possible in two modes)
    - You can set your interface in monitor mode:
      - `ifconfig NAME_OF_WIRELESS_CARD down`
      - `iwconfig NAME_OF_WIRELESS_CARD mode monitor`
      - `ifconfig NAME_OF_WIRELESS_CARD up`
    - **Or** you can add an interface in monitor mode
      - `iw dev NAME_OF_WIRELESS_CARD interface add NAME_OF_NEW_WIRELESS_CARD type monitor`
    
  - Once the card is in monitor mode:
    - `sudo python monitoringAP.py -i NAME_OF_WIRELESS_CARD_IN_MONITOR_MODE`
  
  - To exit:
    - `q`
    
Useful options include:
  - `-h, --help` - Show the help message and exit.
  - `-i INTERFACE, --interface INTERFACE` - Used to insert the interface to use for sniffing.
  - `-f FILE, --file FILE` - Used to insert the file to read for offline sniffing
  - `-b BSSID, --bssid BSSID` - Set a bssid
  - `-c CHANNEL, --channel CHANNEL` - Set a channel
  - `-s, --save` - To save the capture
  - `-a, --analyze` - To print the analysis in two file (_DATA_AP.txt_ and _DATA_STATION.txt_) at the end of execution
    
