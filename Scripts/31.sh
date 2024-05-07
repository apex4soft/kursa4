#!/bin/bash
echo "Задание №31
Чтобы посмотреть все запущенные процессы используйте команду - top
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "top" ]; then
    phrase="Задание №31 решено"
    if ! grep -q "$phrase" Tasks.txt; then
      echo "$phrase" >> Tasks.txt
    fi
    top
    break
  fi

done
