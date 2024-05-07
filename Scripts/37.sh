#!/bin/bash
echo "Задание №37
Чтобы сделать задержку используется команда sleep <количестов времени>
По умолчанию в секундах

Сделайте задержку в 3 секунды
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "sleep 3" ]; then
    sleep 3
    break
  fi

done

echo -ne "\n"
echo "Вывело строку с задержкой в 3с"

phrase="Задание №37 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10