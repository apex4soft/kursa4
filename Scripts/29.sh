#!/bin/bash
echo "Задание №29
Также можно изменять владельца прав, основные которые: root, <ваше имя в системе>, minimal

Измените владельца на minimal для файла in.txt
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "chown minimal in.txt" ]; then
    echo '-r-xr-xr-x 1 root minimal    0 Apr  7 16:06 in.txt'
    break
  fi

done

echo -ne "\n"
echo "Так меняется владелец прав для файлов"

phrase="Задание №29 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10