# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:31:03 2019

@author: Sandra
"""

import nmap
import sys

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan('127.0.0.1','80',arguments='-O')
#nm_scan.scan('127.0.0.1','80')
print(nm_scanner)