echo $1
echo $2
cd $2
for f in *.MP4; do 
    # echo mv "$f" "$(stat -f '%Sm' -t '%Y-%m-%d %H.%M.%S' "$f").${f##*.}"

    # echo $f
    IFS='-' read -r -a name <<< "$f"
    # echo "${name[1]}"
    IFS='.' read -r -a ext <<< "${name[1]}"
    # echo "${ext[0]}"
    # echo "${ext[1]}"
    if [ "$1" == "run" ];then
    	echo mv "$f" "${ext[0]}-${name[0]}.${ext[1]}"
    	mv "$f" "${ext[0]}-${name[0]}.${ext[1]}"
	else	
		echo mv "$f" "${ext[0]}-${name[0]}.${ext[1]}"
	fi
done