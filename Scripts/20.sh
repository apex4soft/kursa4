#!/bin/bash
echo "Задание №20
VIM - текстовый редактор, похожий на nano, но имеющий свои особенности

Установим его с помощью команды sudo apt install vim и откроем файл vim_tutor
Если установлен vim, прописываем vim vim_tutor

!ВНИМАНИЕ! Закрывайте данный файл без сохранения(:q!)
"

while [ True ]; do

  read -p "home/Linux/~$ " command

  if [ "$command" = "sudo apt install vim" ]; then
    sudo apt install vim
    echo -ne "\n"
    echo "Пропишите vim vim_tutor"
  elif [ "$command" = "vim vim_tutor" ]; then
    sudo vim vim_tutor
    echo "А теперь откроем с его помощью файл"
    echo "Пропишите vim vim_tutor"
    break
  fi

done

echo "Вот вы и познакомились с vim"

phrase="Задание №20 решено"
if ! grep -q "$phrase" Tasks.txt; then
  echo "$phrase" >> Tasks.txt
fi

sleep 10