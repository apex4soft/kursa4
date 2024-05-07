#!/bin/bash
echo "Задание №2
Чтобы перемещаться по директориям используется команда cd <путь к директории>
Если надо вернуться к прошлой директории - cd ..

Перейдите в директорию dir
"

ls ./

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "cd dir" ]; then
    cd ./dir
    ls ./
    echo "А вот и содержимое)"
    echo -ne "\n"
    echo "Теперь вернитесь в прошлую директорию"
    echo -ne "\n"
    break
  fi

done

while [ True ]; do

  read -p "home/Linux/dir/~$ " command

  if [ "$command" = "cd .." ]; then
    cd ..
    ls ./
    echo -ne "\n"
    echo "Вуаля. Вы снова в изначачльной директории"
    echo -ne "\n"
    break
  fi

done

echo "Вот так осуществляется переход между директориями"

phrase="Задание №2 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10