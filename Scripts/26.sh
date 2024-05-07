#!/bin/bash
echo "Задание №26
У файлом есть три вида разрешения:
r(4) - read(чтение)
w(2) - write(запись)
x(1) - execute(выполнение)
-(0) - отсутствие прав

Полная запись rwx(побитовая запись) это 4+2+1=7(числовая запись)

Они есть у трех групп:
u - user(пользователь)
g - group(группа)
o - others(другие)

Чтобы получить эту информацию используйте команду ls -l

Измените права файла in.txt только на выполнение через числовую запись
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "chmod 111 in.txt" ]; then
    echo '---x--x--x 1 root root    0 Apr  7 16:06 in.txt'
    break
  fi

done

echo -ne "\n"
echo "Так меняются права через числовую запись"

phrase="Задание №26 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10