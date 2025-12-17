#!/bin/bash
rm -f "$1" "$1.pub"
ssh-keygen -t rsa -b 4096 -f "$1" -N ""

