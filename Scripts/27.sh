#!/bin/bash
echo "Задание №27
В побитовой записи для изменения прав используются +/- (добавить/убрать)
Изменения для разных групп прописываются так: <название группы><команда><нужные права>, (другая группа по такому же принципу)

Измените права файла in.txt только на чтение на пользователе(user) и на запись с выполнением на группе(group) через побитовую запись
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "chmod u-wx,o-r in.txt" ]; then
    echo '-r---wxrwx 1 root root    0 Apr  7 16:06 in.txt'
    break
  fi

done

echo -ne "\n"
echo "Так меняются права через побитовую запись"

phrase="Задание №27 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10