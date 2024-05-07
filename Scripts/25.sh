#!/bin/bash
echo "Задание №25
Чтобы перенаправить вывод в файл используйте команнду: echo <текст> >> <название файла>

Кроме >> можно использовать >
В таком случае переход на следующую строку не произойдет.

Перенаправьте строку Hello в файл in.txt
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "echo Hello >> in.txt" ]; then
    echo 'Hello' >> in.txt
    break
  fi

done

cat in.txt
rm -rf in.txt
touch in.txt

echo -ne "\n"
echo "Так происходит перенаправление"

phrase="Задание №25 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10