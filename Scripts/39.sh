#!/bin/bash
echo "Задание №38
Команда tail работает аналогично команде head, но читает строки с конца:

tail -<число строк> test.txt

Прочитайте последние 2 строчки в файле readme.txt
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "tail -2 readme.txt" ]; then
    tail -2 readme.txt
    break
  fi

done

phrase="Задание №39 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10