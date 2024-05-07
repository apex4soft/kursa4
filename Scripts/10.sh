#!/bin/bash
echo "Задание №10
Символьные ссылки создаются с помощью команды ln -s <путь/название файла> <название ссылки>
Символьные ссылки ссылаются на другие файлы по имени, поэтому при перемещении в другие директории или удалении ссылаемого файла они становятся битыми

Сделайте символьную ссылку на readme.txt link_s
"

ls ./

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "ln -s readme.txt link_s" ]; then
      ln -s readme.txt link_s
      ls ./
      cat link_s
      echo -ne "\n"
      echo "Переместите в директорию dir и посмотрите что будет"
      break
    fi

done

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "mv link_s dir/link_s" ]; then
      mv link_s dir/link_s
      ls dir/
      cat dir/link_s
      echo "Ссылка не открывается"
      break
    fi

done

rm dir/link_s
echo -ne "\n"
echo "Вот так создаются символьные ссылки"

phrase="Задание №10 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10