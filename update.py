#!/usr/bin/env python3

import sys
import os
import os.path
from os import path
from os import listdir
from os.path import isfile, join
from os import walk

CRED = '\033[91m'
CEND = '\033[0m'
CGREENTXT = '\033[32m'

CGREEN = '\x1b[6;30;42m'
CGREENEND = '\x1b[0m'

def update():
    if (not (path.exists("include/")) or not(path.exists("src/"))):
        sys.stderr.write(CRED + "Error. folder include and/or src not existing\n" + CEND)
        sys.exit(84)
    if (not (path.exists("include/" + sys.argv[1]))):
        sys.stderr.write(CRED + "Error. File named '" + sys.argv[1] + "' not exist.\n" + CEND)
        sys.exit(84)
    if (sys.argv[1][len(sys.argv[1]) - 1] != 'h' or sys.argv[1][len(sys.argv[1]) - 2] != '.'):
        sys.stderr.write(CRED + "Error name. Argument should be a .h file name.\n" + CEND)
        sys.exit(84)

    onlyfiles = [j for j in listdir("src/") if isfile(join("src/", j))]
    f = open("include/" + sys.argv[1], "r")
    lines = f.readlines()
    f.close()
    f = open("include/" + sys.argv[1], "w")
    for line in lines:
        try:
            if line.strip("\n")[0:2] != "//" and line.strip("\n")[0:4] != "void" and line.strip("\n").strip("\n")[0:4] != "char" and line.strip("\n")[0:3] != "int" and line.strip("\n")[0:6] != "struct" and (line.strip("\n")[len(line.strip("\n")) - 3] != ')' and line.strip("\n")[len(line.strip("\n")) - 2] != ';') and line.strip("\n")[0:9] != "#endif /*":
                f.write(line)
        except:
            f.write(line)
    f.close()
    f = open("include/" + sys.argv[1], "a")
    for i in range(len(onlyfiles)):
        g = open("src/" + onlyfiles[i], "r")
        f.write("//" + onlyfiles[i] + "\n")
        for line in g:
            if line[0: 4] == "char" or line[0: 3] == "int" or line[0: 4] == "void" or line[0: 6] == "struct":
                f.write(line[0:-1]+";\n")
        f.write("\n")
        g.close()

    name_define = sys.argv[1]
    name_define = name_define.upper()
    name_define = list(name_define)
    name_define[len(sys.argv[1]) - 2] = '_'
    name_define.append('_')
    name_define = "".join(name_define)
    f.write("#endif /* !" + name_define + " */")
    f.close()

    f = open("include/" + sys.argv[1], "r")
    lines = f.readlines()
    f.close()

    f = open("include/" + sys.argv[1], "w")
    for i in range(len(lines)):
        if (lines[i] != '\n'):
            f.write(lines[i])
        elif (lines[i] == '\n'):
            if (lines[i + 1] != '\n'):
                f.write(lines[i])
    f.close()
