# -*- coding: utf-8 -*-


"""autotype.run: provides entry point main()."""

__version__ = "0.0.1"

import sys
from .autocode import AutoCode
import argparse

def main():
	# argument parser 
	parser = argparse.ArgumentParser(description='AutoCode. Ctrl-C to exit.')
	parser.add_argument('file', metavar='file', type=str,
                   help='input file to read from.')
	parser.add_argument('--n', metavar='', type=int, default=3,
                   help='number of characters to read per key. (Default 3. Min 1 | Max 6)')
	parser.add_argument('--GODMODE', metavar='', type=bool, default=False,		
							help='Use brain waves to code. (Default False)')
	# parse the arguments 
	args = parser.parse_args()

	if args.n < 1 or args.n > 6:
		print ('Error: Invalid input for N. N should be between 1 and 6.')
		sys.exit(1)

	with open(args.file, 'r') as file:        
		file_ = file.read()
    # Engine instantiation                             
	at = AutoCode(file_, args.n, args.GODMODE)   

    # start the engine 
	if args.GODMODE == True:         
		at.gmode()
	else:
		at.start()		
