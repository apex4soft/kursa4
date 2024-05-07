#!/bin/bash
echo "Задание №5
Чтобы создать файл используйте команду touch <название файла>
Чтобы создать директорию используйте команду mkdir <название директории>

Создайте директорию my_dir, потом создайте файл my_file.txt
"

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "mkdir my_dir" ]; then
      mkdir ./my_dir
      ls ./
      break
    fi

done

while [ True ]; do

    read -p "home/Linux/~$ " command

    if [ "$command" == "touch my_file.txt" ]; then
      touch ./my_file.txt
      ls ./
      break
    fi

done

echo -ne "\n"
echo "Таким образмо можно создавать директории и файлы"

rm ./my_file.txt
rmdir ./my_dir

phrase="Задание №5 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10