#!/bin/bash
echo "Задание №14

Выведите все файлы, не содержащие txt, из текущей директории
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "find . -not -name *.txt" ]; then
      find . -not -name "*.txt"
      break
    fi

done

echo -ne "\n"
echo "Вывел не содержащие txt файлы и директории"

phrase="Задание №14 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10