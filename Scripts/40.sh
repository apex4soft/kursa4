#!/bin/bash
echo "Задание №40
Команда awk - мощный инструмент для фильтрации и обработки текста
Простейшее ее использование - выборка

Для команды echo one two three | awk {print $<номер слова после пробела>}
Выведите слова по порядку от меньшего к большему

!В ДАННОЙ ОБОЛОЧКЕ НЕ ИСПОЛЬЗУЙТЕ ЗНАК $ !
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "echo one two three | awk {print 1}" ]; then
    echo "one two three" | awk '{print $1}'
    break
  fi

done

echo -ne "\n"
echo "Теперь следующее"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "echo one two three | awk {print 2}" ]; then
    echo "one two three" | awk '{print $2}'
    break
  fi

done

echo -ne "\n"
echo "Теперь следующее"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "echo one two three | awk {print 3}" ]; then
    echo "one two three" | awk '{print $3}'
    break
  fi

done

phrase="Задание №40 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10