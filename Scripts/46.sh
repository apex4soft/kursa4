#!/bin/bash
echo "Задание №46"

echo "Элементы регулярных выражений можно объединять и ссылаться на них как на один элемент.
Делается это с помощью круглых скобок."

echo "Попробуй найти все слова, которые начинаются на tr pr str в файле Домашка"

while :
do
        read -p "home/Linux/~$ " s1
        if [ "$s1" == "ls ~/Домашка | grep '^(tr|pr|str)'" ]; then
                echo "trina
                traktor
                triss
                priz
                prize
                primochka
                stroka
                strela
                strax"
                break

        else :
                echo "попробуй подругому"
        fi
done

phrase="Задание №46 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10