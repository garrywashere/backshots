#!/bin/sh

echo "\n[+] Starting server...\n"
gunicorn -w 1 -b 127.0.0.1:8080 backshots-srv:app
echo "\n[-] Server stopped.\n"