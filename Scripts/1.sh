#!/bin/bash
echo "Задание №1
Приветствую в изучении Linux!
Первым делом ознакомимся с простейшими командами:

ls - Показывает все нескрытые файлы и директории в текущей;
ls -l - Аналогично с ls, показывает доп параметры;
ls -la (ls -all) - Показывает все файлы и директории в текущей.

Начните с ls
"

while [ True  ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "ls" ]; then
    ls ./
    echo -ne "\n"
    echo "Посмотрите как работает ls -l."
    echo -ne "\n"
    break
  fi

done

while [ True  ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "ls -l" ]; then
    ls -l ./
    echo -ne "\n"
    echo "А теперь попробуйте остальные команды."
    echo -ne "\n"
    break
  fi

done

while [ True  ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "ls -la" ] || [ "$command" = "ls -all" ]; then
    ls -la
    echo -ne "\n"
    echo "Появились  файлы, которые не показывались ранее."
    echo -ne "\n"
    break
  fi

done

echo -ne "\n"
echo "Вот вы и познакомились с командой ls"
echo -ne "\n"

phrase="Задание №1 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10