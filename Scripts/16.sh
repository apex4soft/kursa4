#!/bin/bash
echo "Задание №16
Чтобы найти файлы или директории в текущей директории используйте команду ls | grep <искомое значение>

Найдите все файлы .sh
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "ls | grep .sh" ]; then
      ls | grep .sh
      break
    fi

done

echo -ne "\n"
echo "Вывелись все файлы .sh"

phrase="Задание №15 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10