#!/bin/bash
echo "Задание №33
Чтобы завершить процесс в top сначала надо прописать k
Потом надо прописать PID процесса
Далее ввести 9 для SIGKILL или 15 для SIGTERM (стоит по умолчанию)

Откройте top и завершите его процесс
!ЕСЛИ НЕ ВИДИТЕ ПРОЦЕСС - ОТКРОЙТЕ ТЕРМИНАЛ В ПОЛНОМ ОКНЕ!
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "top" ]; then
    phrase="Задание №33 решено"
    if ! grep -q "$phrase" Tasks.txt; then
      echo "$phrase" >> Tasks.txt
    fi
    top
    break
  fi

done
