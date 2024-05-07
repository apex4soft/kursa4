#!/bin/bash
echo "Задание №8
Чтобы переименовать файл используйте команду mv <старое название файла> <новое название файла>

Переименуйте файл rename_me.txt в new.txt
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "mv rename_me.txt new.txt" ]; then
      mv rename_me.txt new.txt
      ls ./
      break
    fi

done

touch rename_me.txt
rm new.txt
echo -ne "\n"
echo "Вот так переименовываются файлы"

phrase="Задание №8 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10