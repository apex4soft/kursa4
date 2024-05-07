#!/bin/bash
echo "Задание №44"

echo "Кроме описания совпадения с любым символом в заданной позиции (.) в регулярных выражениях имеется возможность описать символ из определенного множества.
Делается это с помощью квадратных скобок.
В следующем примере ищутся соответствия со строками bzip и gzip:

ls /bin | grep '[bg]zip'
Output:
bzip2
bzip2recover
gzip"

echo "Найди все совпадения слов krip rrip drip одной строкой"

while :
do
        read -p "home/Linux/~$ " s1
        if [ "$s1" == "ls /bin | grep '[krd]rip'" ]; then
                echo "хорош"
                break

        else :
                echo "попробуй подругому"
        fi
done

phrase="Задание №44 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10