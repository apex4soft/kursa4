#!/bin/bash
echo "Задание №43"

echo "Мы уже столкнулись с простыми регулярными выражениями.
К примеру,  выражение «zip» обозначает строку, соответствующую следующим критериям:
  1) в строке не меньше трех символов;
  2) в строке присутствуют символы «z», «i», «p», причем именно в таком порядке;
  3) между ними нет других символов. Символы, соответствующие сами себе (как «z», «i», «p») называются литералами.

Кроме того, существуют другая категория символов, называемая метасимволами.
Они применяются для составления различных критериев поиска.
К метасимволам в BRE относятся:
  ^ $ . [ ] * \ -"

echo "\b Граница слова
\B Не граница слова
\G Предыдущий успешный поиск

Квантификатор после символа, символьного класса или группы определяет, сколько раз предшествующее выражение может встречаться.

? - Ноль или одно повторение {0,1}
* - Ноль или более повторение {0,}
+ - Одно или более повторение {1,}
.* - любое число символов"

echo "Символ «карет» (^) и «доллар» ($) в регулярных выражениях играют роль якорей.
Это означает, что в их присутствии совпадение с шаблоном возможно, только если оно будет найдено в начале строки (^) или в ее конце ($)."

echo "Попробуйте найти слово sus в начале строки"

echo "!НЕ ЗАБЫВАЙТЕ ПРО ОДИНАРНЫЕ КАВЫЧКИ!"

while :
do
	read -p "home/Linux/~$ " s1
	if [ "$s1" == "ls /bin | grep '^sus'" ]; then
		echo "а теперь найди совпадения слова keks в конце строки"
		read -p "home/Linux/~$ " s2
		if [ "$s2" == "ls /bin | grep 'keks$'" ]; then
                      echo "неплохо, малыш"
                      break
	      else :
		      echo "заново"
		fi
	else :
		echo "попробуй сначала"
	fi
done

phrase="Задание №43 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10