#!/bin/bash
echo "Задание №19
Чтобы узнать в какой вы директории и путь до неё используйте команду pwd

Протестируйте
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "pwd" ]; then
      pwd
      break
    fi

done

echo -ne "\n"
echo "Вот текущая директория и полный путь к ней"

phrase="Задание №19 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10