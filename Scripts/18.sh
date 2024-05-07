#!/bin/bash
echo "Задание №18
Разархивирование
tar -xvf archive.tar.gz

Разархивируйте архив archive_dir.tar.gz
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "tar -xvf archive_dir.tar.gz" ]; then
      tar -xvf archive_dir.tar.gz
      break
    fi

done

rm -rf archive_dir
echo -ne "\n"
echo "Появилась дирекотория archive_dir из архива"

phrase="Задание №18 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10