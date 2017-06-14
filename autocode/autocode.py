import curses
from time import sleep 
import sys

# TODO - 
# handle terminal size 
# improve UI
# Scrolling support 

HEADER = 'CODEPAD v2.3'
LOG_FILENAME = 'debug.log'

class AutoCode():    
    def __init__(self, file, n, godmode):
        """
        main is the wrapper window
        There are two nested windows, namely header and stdscr.        
        """
        self.main = curses.initscr()
        self.ROWS, self.COLS = self.main.getmaxyx()  

        self.header = self.main.subwin(2, self.COLS, 0, 0)
        # center the text 
        # cast it to int for python3 support
        center = int((self.COLS / 2) - (len(HEADER) / 2))
        self.header.addstr(center * ' ' + HEADER)        
        self.header.refresh()

        self.stdscr = self.main.subwin(self.ROWS-1, self.COLS, 1, 0)        
        self.stdscr.idlok(True) 
        self.stdscr.scrollok(True)  

        curses.cbreak()        
        curses.noecho()         

        self.stdscr.keypad(1)
        self.stdscr.refresh()
        
        self.file = file           
        # this is for handling the backspaces 
        self.virtualfile = file.split('\n') 

        self.godmode = godmode
        self.n = n   

        # handle terminal size
        if self.COLS < 100:
            curses.endwin()            
            print ('Error: Increase the width of your terminal')
            sys.exit(1)


    def get_text(self, fileptr):
        """
        Returns n characters ahead the fileptr
        """    
        return self.file[fileptr:fileptr+self.n]            

    def start(self):   
        """
        start iterates the file and paints the text on the screen.
        exits when q is pressed. 
        """
        try:      
            fileptr = 0
            key = ''
            lines = 1        
            while True:
                # get the cursor position for further manipulation 
                y, x = self.stdscr.getyx()
                key = self.stdscr.getch()
                if key == curses.KEY_BACKSPACE or key == curses.KEY_DC or \
                    key == curses.KEY_DL or key == 127 :  
                    # handle backspace                             
                    if x == 0 and y == 0: 
                        continue                     
                    # take the file pointer back one step 
                    fileptr -= 1
                    # update the screen     
                    if x == 0:   
                        lines -= 1
                        self.stdscr.addstr(y-1, len(self.virtualfile[lines-1]), ' ')
                        self.stdscr.move(y-1, len(self.virtualfile[lines-1]))                                   
                    else:
                        self.stdscr.addstr(y, x-1, ' ')
                        self.stdscr.move(y, x-1)                
                elif key == curses.KEY_UP or key == curses.KEY_DOWN or \
                    key == curses.KEY_RESIZE or key == -1:
                    # ignore 
                    continue                           
                else:   
                    text = self.get_text(fileptr)                    
                    # increase the lines if there are "\n" s 
                    lines += sum([1 if c == '\n' else 0 for c in text])
                    fileptr += self.n        
                    self.stdscr.addstr(text)
                                
                self.stdscr.refresh()                
            # graceful exit                 
            curses.endwin()
        except KeyboardInterrupt:            
            curses.endwin()
            exit()  

    def gmode(self):
        """
        Types automatically
        """
        try:
            fileptr = 0 
            while (fileptr + self.n) < len(self.file):                  
                text = self.get_text(fileptr)                    
                fileptr += self.n        
                self.stdscr.addstr(text)
                self.stdscr.refresh()
                sleep(0.1)  
            curses.endwin()                                                                                
        except KeyboardInterrupt:            
            curses.endwin()
            exit()      


        