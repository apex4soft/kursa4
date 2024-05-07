#!/bin/bash
echo "Задание №24
Чтобы выводить в терминал строки(пригодиться в следующих заданиях) используйте команнду: echo <текст(в кавычках)>

!В приложении не используйте кавычки, в отличие от терминала!

Выведите фразу Linux
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "echo Linux" ]; then
    echo "Linux"
    break
  fi

done

echo -ne "\n"
echo "Так выводяться строки"

phrase="Задание №24 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10