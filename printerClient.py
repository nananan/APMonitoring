 #!/usr/bin/python

import curses, re, sys
import printerF

import texttable
from texttable import Texttable



class PrinterClient(printerF.Printer):
    
    HEIGHT_TABLE = 25
    CONSTANT = 189
    
    
    HEADER = [' STATION             ', ' AUTH',' DEAUTH ', ' PWR ',' HAND_SUCC ',' HAND_FAIL ',' CORRUPT ',' CORR%',' DATA  ',' RTS ',' CTS ',' ACK',' BEACON  ', ' PROBE_REQ  ', ' PROBE_RESP  ', ' TOT_PACK', ' OTHER']
    
    HEADER_CLIENT_2 = ['STATION            ', 'AUTH','DEAUTH', 'PWR','HAND_SUCC','HAND_FAIL','CORRUPT','CORR%','DATA','RTS','CTS','ACK','BEACON', 'PROBE_REQ  ', 'PROBE_RESP', 'TOT_PACK', 'OTHER']
    
    HEADER_CLIENT_TMP = [' STATION             ', ' AUTH',' DEAUTH ', ' PWR ',' HAND_SUCC ',' HAND_FAIL ',' CORRUPT ',' CORR%',' DATA  ',' RTS ',' CTS ',' ACK',' BEACON  ', ' PROBE_REQ  ', ' PROBE_RESP  ', ' TOT_PACK', ' OTHER']
    
   
    HEADER_INFO_2 = ['ESSID                ','BSSID              ','STATION            ','AUTH  ','DEAUTH  ','PWR  ','HAND_SUCC  ','HAND_FAIL  ','CORRUPT  ','CORR%  ','DATA   ','RTS  ','CTS  ','ACK  ','BEACON  ', 'PROBE_REQ  ', 'PROBE_RESP  ', 'TOT']
    
    
    def __init__(self, height):
        printerF.Printer.__init__(self, height) 
        
        self.tableInfo = texttable.Texttable()
        self.tableOrdClient = texttable.Texttable()
        self.tableOrdClient_2 = texttable.Texttable()
        self.tableOrdClientSelect = texttable.Texttable()
        
        self.dimTableInfo = 0
        self.dimTableClient = 0
        self.dimTableClient_2 = 0
        
        
    def drawTable(self):
        self.src.addstr(0,0, str(PrinterClient.HEADER).strip("[]").replace("'","").replace(",",""), self.colorHeader)
        self.src.addstr(1,0, str("="*163))
        #if not self.tupl:
            #self.src.insstr(2, 0, self.tableOrdClient.draw())
        #else:
        if self.indexCursor > 0:
            self.src.addstr(2, 0, self.tableOrdClient.draw())
            self.src.addstr(2+self.indexCursor, 0, self.tableOrdClientSelect.draw(), curses.color_pair(1))
            if not self.pressedInfo:
                #try:
                self.src.addstr(2+self.indexCursor+1, 0, " "*PrinterClient.CONSTANT)
                self.src.addstr(2+self.indexCursor+2, 0, self.tableOrdClient_2.draw())
                #except Exception, e:
                    #print str(e)
                    #sys.exit(0)
                    #self.src.insstr(2+self.indexCursor+2, 0, self.tableOrdClient_2.draw())
            else:
                #try:
                self.tableInfo.draw().decode('utf-8')
                self.src.addstr(2+self.indexCursor+1,0, " "*PrinterClient.CONSTANT)
                self.src.addstr(2+self.indexCursor+2, 0, str(PrinterClient.HEADER_INFO_2).strip("[]").replace("'","").replace(",","") , curses.color_pair(3))
                self.src.addstr(2+self.indexCursor+3,0, str("="*PrinterClient.CONSTANT))
                self.src.addstr(4+self.indexCursor+2, 0, self.tableInfo.draw())
                self.src.addstr(6+self.contInfoClient+self.indexCursor, 0, str(" "*PrinterClient.CONSTANT))
                self.src.addstr(7+self.contInfoClient+self.indexCursor, 0, self.tableOrdClient_2.draw())
                #except Exception:
                    #self.fileLog = open("log.log", "a")
                    #self.fileLog.write("ehi")
                    #self.fileLog.close()
                    #self.tableInfo.draw().decode('utf-8')
                    
                #self.src.addstr(7+self.contInfoClient+self.indexCursor,0, " "*PrinterClient.CONSTANT)
        else:
            self.src.addstr(2, 0, self.tableOrdClientSelect.draw(), curses.color_pair(1))
            if not self.pressedInfo:
                self.src.addstr(3, 0, " "*PrinterClient.CONSTANT)
                self.src.addstr(4, 0, self.tableOrdClient_2.draw())
            else:
                #try:
                self.tableInfo.draw().decode('utf-8')
                self.src.addstr(2+self.indexCursor+1,0, " "*PrinterClient.CONSTANT)
                self.src.addstr(2+self.indexCursor+2, 0, str(PrinterClient.HEADER_INFO_2).strip("[]").replace("'","").replace(",","") , curses.color_pair(3))
                self.src.addstr(2+self.indexCursor+3,0, "="*PrinterClient.CONSTANT)
                self.src.addstr(4+self.indexCursor+2, 0, self.tableInfo.draw())
                self.src.addstr(6+self.contInfoClient+self.indexCursor, 0, str(" "*PrinterClient.CONSTANT))
                self.src.addstr(7+self.contInfoClient+self.indexCursor, 0, self.tableOrdClient_2.draw())
                #except Exception:
                    #self.fileLog = open("log.log", "a")
                    #self.fileLog.write("ehi")
                    #self.fileLog.close()
                    #self.tableInfo.draw().decode('utf-8')
                #self.src.addstr(7+self.contInfoClient+self.indexCursor,0, " "*PrinterClient.CONSTANT)
                        
    
    def cleanRow(self):
        #if self.indexCursor < PrinterClient.HEIGHT_TABLE:
        start = self.dimTableClient + self.dimTableClient_2 + 1
        end = PrinterClient.HEIGHT_TABLE + start + 10
        for i in range(start, end):
            self.src.addstr(i, 0, " "*PrinterClient.CONSTANT)

    
    def resetHeaderIndex(self, index):
        PrinterClient.HEADER[index] = PrinterClient.HEADER_CLIENT_TMP[index]

    
    def refreshTable(self):
        self.src.refresh(self.mypad_pos_client, 0, 0, 0, PrinterClient.HEIGHT_TABLE, 190)
        
    
    def resizeTable(self, height):
        self.height = height
        self.src.resize(height, 300)
    
        
    def reset(self):
        self.tableInfo.reset()
        self.tableOrdClient.reset()
        self.tableOrdClient_2.reset()
        self.tableOrdClientSelect.reset()
        
        self.dimTableClient = 0
        self.dimTableClient_2 = 0
        self.dimTableInfo = 0
    
    
    def createTable(self, header, indexClient):
        
        self.tableInfo.set_deco(Texttable.HEADER)
        self.tableInfo.set_cols_align(["l", "r", "c", "c","c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
        self.tableInfo.set_cols_valign(["t", "b", "m", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
        
        self.tableInfo.add_rows([[header[0], header[1], header[2], header[3], header[4], header[5], header[6], header[7], header[8], header[9], header[10], header[11], header[12], header[13], header[14], header[15], header[16], header[17]]])
        
        
        self.init_table(self.tableOrdClient)
        self.init_table(self.tableOrdClient_2)
        self.init_table(self.tableOrdClientSelect)
        
        PrinterClient.HEADER[indexClient] = PrinterClient.HEADER_CLIENT_TMP[indexClient]
        #header_client[indexClient] = re.sub("^", ' ', header_client[indexClient])
        PrinterClient.HEADER[indexClient] = re.sub("^ ", '>', PrinterClient.HEADER[indexClient])
        #header_client[indexClient] = header_client[indexClient] + ">"
        
        self.tableOrdClient.add_rows([PrinterClient.HEADER_CLIENT_2])
        self.tableOrdClient_2.add_rows([PrinterClient.HEADER_CLIENT_2])
        self.tableOrdClientSelect.add_rows([PrinterClient.HEADER_CLIENT_2])
    
    
    
    def init_table(self, table):
        table.set_deco(Texttable.HEADER)
        table.set_cols_align(["l", "r", "c", "c","c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
        table.set_cols_valign(["t", "b", "m", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    
    
    def add_rows(self, tup, index):
        if index == 0:
            self.tableOrdClientSelect.add_rows(tup, False)
        elif index == 1:
            self.tableOrdClient.add_rows(tup,False)
            self.dimTableClient += 1
        elif index == 2:
            self.tableOrdClient_2.add_rows(tup,False)
            self.dimTableClient_2 += 1
        elif index == 3:
            self.tableInfo.add_rows(tup,False)
            self.dimTableInfo += 1
        
    
    def setMyPadPos(self, mypad_pos):
        self.mypad_pos_client = mypad_pos

    def setIndexCursor(self, indexCursor, whatDo):
        if whatDo == 0:
            self.indexCursor = indexCursor
        elif whatDo == 1:
            self.indexCursor += indexCursor
        elif whatDo == 2:
            self.indexCursor -= indexCursor