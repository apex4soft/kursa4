#!/bin/bash
echo "Задание №47"

echo "Искать слова можно эффектовнее, если они находятся в большом диапазоне.
Чтобы искать слова от A до Z нужно указать диапазон [A-Z], если нужно найти слова в том же диапазоне, но нижнего регистра, то это будет выглядеть вот так: [a-z].
точно так же работает и диапазон цифр, например: [1-5]."

echo "Для начала найдите все слова, начинающиеся на k-z в домашней дирректории"

while :
do
        read -p "home/Linux/~$ " s1
        if [ "$s1" == "ls ~ | grep '^[k-z]'" ]; then
                echo "неплохо, теперь найди все слова, начинающиеся на цифры от 3-7"
       while :
       do
       		read -p "home/Linux/~$ " s2
                if [ "$s2" == "ls ~ | grep '^[3-7]'" ]; then
                    echo "хорошо, теперь скомбинируй полученный навык и найди слова начинающиеся на g-m и 2-5"
			while :
			do
        read -p "home/Linux/~$ " s3
        if [ "$s3" == "ls ~ | grep '^[g-m2-5]'" ]; then
               echo "хорошая работа"
               break
        else :
              echo "попробуй иначе"
        fi
      done
      break
                else :
                        echo "попробуй иначе"
                fi
	done
	break
        else :
                echo "попробуй подругому"
        fi
done

phrase="Задание №47 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10