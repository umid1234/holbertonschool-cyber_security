#!/bin/bash
find "$1" -user user2 -exec chown user3 {} \; ; ls -l "$1"
