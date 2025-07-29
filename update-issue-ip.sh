#!/bin/sh
IP=$(hostname -I | awk '{print $1}')
echo "\nBenvingut al servidor LanAccessWithZeroTier!\n" > /etc/issue
echo "🌐 Accedeix a: http://$IP\n" >> /etc/issue
