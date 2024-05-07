#!/bin/bash
echo "Задание №4
Чтобы удалить файл используйте команду rm <название файла>

Удалите файл deleteme.txt
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "rm deleteme.txt" ]; then
      rm ./deleteme.txt
      ls ./
      echo -ne "\n"
      echo "Чтобы удалить директорию пропишите rmdir <название директории>"
      echo "Удалиет директорию deleteme_dir"
      echo -ne "\n"
      break
    fi

done

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "rmdir deleteme_dir" ]; then
      rmdir ./deleteme_dir
      ls ./
      echo -ne "\n"
      break
    fi

done

touch ./deleteme.txt
mkdir ./deleteme_dir
echo "Вот так удаляются файлы или директории"

phrase="Задание №4 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10