#!/bin/bash
# mod by lululla 24/06/2023
clear
atr_183e='3F FF 95 00 FF 91 81 71 FE 47 00 54 49 47 45 52 36 30 31 20 52 65 76 4D 38 37 14'
oscam_version=$(find /tmp/ -name oscam.version | sed -n 1p)
oscam_config_dir=$(grep -ir "ConfigDir" $oscam_version | awk -F ":      " '{ print $2 }')
oscam_user=$(grep -ir "httpuser" $oscam_config_dir"oscam.conf" | awk -F "=" '{ print ($2) }' | sed 's/^[ \t]*//')
oscam_passwd=$(grep -ir "httppwd" $oscam_config_dir"oscam.conf" | awk -F "=" '{ print ($2) }' | sed 's/^[ \t]*//')
oscam_httpport=$(grep -ir "httpport" $oscam_config_dir"oscam.conf" | awk -F "=" '{ print ($2) }' | sed 's/^[ \t]*//')
oscam_port=$(echo $oscam_httpport | sed -e 's|+||g')
# protocol=$(if echo $oscam_httpport | grep + >/dev/null; then echo "https"; else echo "http"; fi)
curl -s --user "${oscam_user}":"${oscam_passwd}" --anyauth -k http://127.0.0.1:$oscam_port/status.html | grep "Restart Reader" | sed -e 's|<TD CLASS="statuscol1"><A HREF="status.html?action=restart&amp;label=||g' | sed 's/^[ \t]*//' | awk -F "\"" '{ print ($1) }' >/tmp/active_readers.tmp
while IFS= read -r label; do
curl -s --user "${oscam_user}":"${oscam_passwd}" --anyauth -k http://127.0.0.1:$oscam_port/entitlements.html?label=$label >/tmp/"$label"_entitlements.html
atr=$(cat /tmp/"$label"_entitlements.html | grep "\<TD COLSPAN=\"4\">" | awk -F "[<>]" '{ print ($7) }' | sed 's/.$//g')
reader=$label
atr_string='aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1U0ZU02RGpW'
emm_file=$(echo $atr_string | base64 -d)
# if wget --spider ${emm_file} 2>/dev/null; then  # check the existence of an online file
emmm=$(curl -s $emm_file)
local_emm_file='/tmp/emm.txt'
# echo -e "$emmm" >$local_emm_file
echo -e "$emmm" > '/tmp/emm.txt'
if [ "$atr_183e" == "$atr" ]; then
    echo "Send new emms to $label card"
    curl -s -k --user $oscam_user:$oscam_passwd --anyauth "http://127.0.0.1:$oscam_port/emm_running.html?label=$reader&emmcaid=183E&ep=$emmm&action=Launch" >/dev/null
fi
done < /tmp/active_readers.tmp

rm -rf /tmp/*.tmp /tmp/*.html
exit 0
