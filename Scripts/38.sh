#!/bin/bash
echo "Задание №38
Команда head читает первые 10 строк любого переданного текста и выводит их по стандартному каналу. Число выводимых строк можно изменить:

head -<число строк> test.txt

Прочитайте первые 3 строчки в файле readme.txt
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "head -3 readme.txt" ]; then
    head -3 readme.txt
    break
  fi

done

phrase="Задание №38 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10