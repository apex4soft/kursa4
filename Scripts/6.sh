#!/bin/bash
echo "Задание №6
Чтобы скопировать файл в другую директорию используйте команду cp <название файла> <путь к директории>

Скопируйте файл copy_me.txt в директорию dir
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "cp copy_me.txt dir" ]; then
      cp copy_me.txt dir
      ls dir/
      break
    fi

done

rm dir/copy_me.txt
echo -ne "\n"
echo "Вот так копируются файлы"

phrase="Задание №6 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10