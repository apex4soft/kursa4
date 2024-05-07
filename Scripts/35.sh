#!/bin/bash
echo "Задание №35
Также можно остановить процесс командой kill <PID процесса>

Для удобства поиска и просмотра пропишите top в данной оболочке и откройте вторую вкладку
В ней используйте ps aux и остановите процесс top (Вкладка с top закроется через 10с)
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "top" ]; then
    phrase="Задание №35 решено"
    if ! grep -q "$phrase" Tasks.txt; then
      echo "$phrase" >> Tasks.txt
    fi
    top
    break
  fi

done

sleep 10