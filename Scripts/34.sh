#!/bin/bash
echo "Задание №34
Также можно посмотреть процессы в более закономерном виде
Для этого пропишите pstree
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "pstree" ]; then
    pstree
    break
  fi

done

phrase="Задание №34 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 100