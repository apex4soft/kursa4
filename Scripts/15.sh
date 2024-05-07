#!/bin/bash
echo "Задание №15
Чтобы найти строку с искомым словом в файле используйте команду grep <искомое слово(в кавычках)> <название файла>

Найдите строку, содержащую значение 14 из файла Tasks.txt
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "grep 14 Tasks.txt" ]; then
      grep "14" Tasks.txt
      break
    fi

done

echo -ne "\n"
echo "Вывелась строка с заданным значением"

phrase="Задание №15 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10