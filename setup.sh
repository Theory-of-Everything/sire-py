#!/bin/bash

echo "Enter/Paste your bot Token"
read token
echo "Enter your Server Config (optional)"
read s_conf
echo "Install Dependencies? [y/n]"
read depend

if [ $depend = "y" ] ; then
    python3 -U -r requirements.txt
else
    :
fi

touch .env

echo "TOKEN=$token" > .env
echo "SERVER_CONFIG=$s_conf" >> .env
