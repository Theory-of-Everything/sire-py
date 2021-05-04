#!/bin/bash

env_F=".env"

echo "Enter/Paste your bot Token"
read token
echo "Enter your Server Config (optional)"
read s_conf
echo "Enter your reddit dev app ID"
read r_id
echo "Enter your reddit dev app Secret"
read r_secret
echo "Install Dependencies? [y/n]: "
read depend

if [ $depend = "y" ] ; then
    python3 -U -r requirements.txt
else
    :
fi

touch .env

echo "TOKEN=$token" > .env
echo "SERVER_CONFIG=$s_conf" >> .env
echo "APP_ID=$r_id" >> .env
echo "APP_SECRET=$r_secret" >> .env
