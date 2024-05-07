#!/bin/bash
echo "Задание №23
Чтобы подсчитать количество строк в файле используйте команду: wc -l file.txt

Подсчитайте количество строк в файле Tasks.txt
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "wc -l Tasks.txt" ]; then
    wc -l Tasks.txt
    break
  fi

done

echo -ne "\n"
echo "Так подсчитывается количество строк в файлах"

phrase="Задание №23 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10