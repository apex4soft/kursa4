#!/bin/bash
echo "Задание №32
Аналогично top для вывода всех процессов можно использовать ps aux (нет, не тот aux)
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "ps aux" ]; then
    ps aux
    break
  fi

done

phrase="Задание №32 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10