#!/usr/bin/env python3
import os
import fileinput
import re
import shutil

fortran_ext = ['.F']
#cpp_ext = ['.h', '.cpp', '.c','.hpp','.cxx','.cfg']
cpp_ext = ['.h', '.cpp', '.c','.hpp','.cxx']



def is_fortran(f):
    results = [f.endswith(ext) for ext in fortran_ext]
    return True in results

def is_cpp(f):
    results = [f.endswith(ext) for ext in cpp_ext]
    return True in results

def apply_header():
    for root, dirs, files in os.walk("../../"):
        if (not re.search("/com/",root)) and (not re.search("/extlib/",root)) and (not re.search("CMake",root)):
            for filename in files:
                if is_fortran(filename): 
                    add_header(os.path.join(root,filename))
                elif is_cpp(filename):
                    add_header(os.path.join(root,filename))

def add_header(filename):
    if is_fortran(filename):
        fic = "f_COPYRIGHT.txt"
    else:
        fic = "cpp_COPYRIGHT.txt"

#    print(filename)
# check if the header is correct
    with open(filename,encoding='latin1') as f1, open(fic,encoding='latin1') as f2:
        ok_header = True
        for i in range(22):
            if f1.readline() != f2.readline():
                ok_header = False

#if it is not, then 
        if ok_header == False:
            print("WARNING: "+filename+" has no copyright")
            shutil.copy(fic,filename+".bak")
            with open(filename,encoding='latin1') as f1, open(filename+".bak",'a',encoding='latin1') as f2:
                for line in f1:
                    if not re.search("Copyright>",line):
                        f2.write(line)
            shutil.move(filename+".bak",filename)                        

#============================================================
apply_header()

