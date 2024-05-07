#!/bin/bash
echo "Задание №13

Выведите все файлы txt из текущей директории и директории  dir
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "find .-maxdepth 2 -name *.txt" ]; then
      find . -maxdepth 2 -name "*.txt"
      break
    fi

done

echo -ne "\n"
echo "Дополнительно вывел text.txt из dir"

phrase="Задание №13 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10