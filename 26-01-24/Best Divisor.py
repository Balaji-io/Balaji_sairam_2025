#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    l=[]
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
    d={}
    for i in l:
        s1=0
        if(i<10):
            d[i]=i

        else:
            j=i
            while(i>0):
                s1+=i%10 
                i//=10 
            if s1 not in d:
                d[s1]=j
            else:
                if j<d[s1]:
                    d[s1]=j
          
    k=max(d.keys())
    print(d[k])
