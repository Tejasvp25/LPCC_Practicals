#!/bin/bash
lex $1.l
gcc lex.yy.c
./a.out