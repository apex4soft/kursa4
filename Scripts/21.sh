#!/bin/bash
echo "Задание №21
Чтобы обновить все пакеты устройства используйте команду: sudo apt update && sudo apt upgrade

Обновите все пакеты.
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "sudo apt update && sudo apt upgrade" ]; then
    sudo apt update && sudo apt upgrade
    break
  fi

done

echo -ne "\n"
echo "Так обновляются пакеты"

phrase="Задание №21 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10