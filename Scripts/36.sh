#!/bin/bash
echo "Задание №36
Раз уж речь зашла про дерево
Пропишите команду tree
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "tree" ]; then
    tree
    break
  fi

done

echo -ne "\n"
echo "Похоже на ls и на pstree"

phrase="Задание №36 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 100