#!/bin/bash
echo "Задание №9
Чтобы переименовать и переместить файла в директорию используйте команду mv <старое название> <путь к директории/новое название>

Переместите файл rename_me.txt в директорию dir и переименуйте в new.txt в одну команду
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "mv rename_me.txt dir/new.txt" ]; then
      mv rename_me.txt dir/new.txt
      ls dir/
      break
    fi

done

touch rename_me.txt
rm dir/new.txt
echo -ne "\n"
echo "Вот так перемещаются и переименовываются файлы в одну команду"

phrase="Задание №9 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10