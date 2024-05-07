#!/bin/bash
echo "Задание №48"

echo "посмотреите, что спрятано в файле phonenumber.txt"
while :
do
  read -p "home/Linux/~$ " s1
  if [ "$s1" == "cat phonenumber.txt" ]; then
    echo "(185) 136-1035
    (95) 213-1874
    (37) 207-2639
    (285) 227-1602
    (275) 298-1043
    (107) 204-2197
    (799) 240-1839
    (218) 750-7390
    (114) 776-2276
    (7012) 219-3089"

    echo "теперь найди все неисправные номера. Один из ключей, которые могут тебе помочь -E(второй вспоминай сам)"

    while :
    do
    read -p "home/Linux/~$ " s2
      if [ "$s2" == "grep -Ev '^([0-9]{3}) [0-9]{3}-[0-9]{4}$' phonenumbers.txt" ]; then
        echo "ты проделал хорошую работу, на этом курс регулярных выражений окончен"
        echo "Перезайдите в приложение)"
        break
      else :
        echo "попробуй иначе"
      fi
    done
    break
  fi
done

phrase="Задание №48 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10