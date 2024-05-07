#!/bin/bash
echo "Задание №7
Чтобы переместить файл в другую директорию используйте команду mv <название файла> <путь к директории>

Переместите файл rename_me.txt в директорию dir
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "mv rename_me.txt dir" ]; then
      mv rename_me.txt dir
      ls dir/
      break
    fi

done

touch rename_me.txt
rm dir/rename_me.txt
echo -ne "\n"
echo "Вот так перемещаются файлы"

phrase="Задание №7 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10