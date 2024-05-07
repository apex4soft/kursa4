#!/bin/bash
echo "Задание №28
В побитовой записи можно изменить права сразу у все 3-х групп
Для этого надо просто прописать <+/- права>

Измените права файла in.txt всех групп на чтение и выполнение через побитовую запись
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "chmod -w in.txt" ]; then
    echo '-r-xr-xr-x 1 root root    0 Apr  7 16:06 in.txt'
    break
  fi

done

echo -ne "\n"
echo "Так меняются права через побитовую запись для всех групп сразу"

phrase="Задание №28 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10