#!/bin/bash
echo "Задание №30
Чтобы посмотреть действующие процессы используйте команду - ps
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "ps" ]; then
    ps
    break
  fi

done

echo -ne "\n"
echo "Так можно получить действующие процессы"

phrase="Задание №30 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10