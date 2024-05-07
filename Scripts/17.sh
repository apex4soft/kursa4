#!/bin/bash
echo "Задание №17
Архивирование:
tar -czf <название архива>.tar.gz <файл/папка>

Заархивируйте файл archive_me.txt в archive_me.tar.gz
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "tar -czf archive_me.tar.gz archive_me.txt" ]; then
      tar -czf archive_me.tar.gz archive_me.txt
      ls ./
      break
    fi

done

rm archive.tar.gz
echo -ne "\n"
echo "Появился архив archive_me.tar.gz"

phrase="Задание №17 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10