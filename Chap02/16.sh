# あとでやる
split -l $(expr $(wc -l hightemp.txt | cut -d " " -f 1) / $1 + 1) hightemp.txt Ex16
