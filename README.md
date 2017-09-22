# Cinnamon
Application for real time monitoring of a wireless network, by capturing and analysing the flow of 802.11 frames on a given environment. In order to achieve this, one can base its application on tools like Scapy, a Python program written to manipulate network packages. We used Scapy to sniff packets and to pass them to Python code purposely implemented in order to analyse and save collected data. The analysis was carried out by studying the structure of 802.11 frames in order to extract pivotal fields such as the type and the subtype. Then it is important to precisely define the type of a frame, and then to differentiate it. After that, we implemented a module able to read the analysis and insert them in some tables that are be displayed on the console screen with the use of Curses, a library that allows to manage textual terminals regardless of the terminal screen and keyboard. The tables are of two types: the first collects information relating to the stations, while the second contain the APs's information. The first table is, in turn, comprising another table containing more detailed information relating to the selected station and the AP with which it has exchanged a few packs. You can also save sniffing packets in a pcap file, or you can also do offline analysis, such as the analysis of the packages contained in pcap files.  You can also get, at the end of the analysis, a file containing some statistics of the tables's fields.

## Installation & Running

Steps to run include:
  - Grab the code:
    - `git clone https://github.com/nananan/Cinnamon`
    - `cd Cinnamon`
    
  - Set wireless card into monitor mode: (this is possible in two modes)
    1. You can set your interface in monitor mode:
      - `ifconfig NAME_OF_WIRELESS_CARD down`
      - `iwconfig NAME_OF_WIRELESS_CARD mode monitor`
      - `ifconfig NAME_OF_WIRELESS_CARD up`
    2. You can also add an interface in monitor mode
      - `iw dev NAME_OF_WIRELESS_CARD interface add NAME_OF_NEW_WIRELESS_CARD type monitor`
    
  - Once the card is in monitor mode:
