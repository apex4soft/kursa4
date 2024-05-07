#!/bin/bash
echo "Задание №22
Чтобы заменить содержимое файла используйте команду: sed -i 's/старое/новое/g' file.txt

Замените Linux на Unix в файле rename_me.txt
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "sed -i 's/Linux/Unix/g' rename_me.txt" ]; then
    sed -i 's/Linux/Unix/g' rename_me.txt
    cat rename_me.txt
    break
  fi

done

sed -i 's/Unix/Linux/g' rename_me.txt
echo -ne "\n"
echo -ne "\n"
echo "Так заменяются значения в файлах"

phrase="Задание №22 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10