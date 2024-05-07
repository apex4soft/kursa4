#!/bin/bash
echo "Задание №11
Жесткие ссылки создаются с помощью команды ln <путь/название файла> <название ссылки>
Жесткие ссылки ссылаются в частности только на другие файлы, поэтому при перемещении в другие директории они становятся битыми

Сделайте жесткую ссылку на readme.txt link
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "ln readme.txt link" ]; then
      ln -s readme.txt link
      ls ./
      cat link
      echo -ne "\n"
      echo "Переместите в директорию dir и посмотрите что будет"
      break
    fi

done

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "mv link dir/link" ]; then
      mv link dir/link
      cat dir/link
      echo "Ссылка не открывается"
      break
    fi

done

rm dir/link
echo -ne "\n"
echo "Вот так создаются жесткие ссылки"

phrase="Задание №11 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10