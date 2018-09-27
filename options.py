#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:18:10 2018

@author: kmsnyder2
"""

import socket

def port_services(low, high):
    
    for i in range(low, high + 1):
        print('port: ', i, '    service: ', socket.getservbyport(i))

    
if __name__ == '__main__':
    low = 80
    high = 85
    port_services(low, high)
        