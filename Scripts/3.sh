#!/bin/bash
echo "Задание №3
Чтобы считать файл находящийся в данной директории нужно написать cat <название файла>
Также можно считывать файлы находящиеся в другой директории - cat <путь к файлу>/<название файла>

Считайте readme.txt текущей директории
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "cat readme.txt" ]; then
      cat readme.txt
      echo -ne "\n"
      echo "А теперь считайте файл text.txt из директории dir, не переходя в неё"
      echo -ne "\n"
      break
    fi

done

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "cat dir/text.txt" ]; then
      cat dir/text.txt
      echo -ne "\n"
      break
    fi

done

echo "Вот так можно считывать файлы из консоли"

phrase="Задание №3 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10