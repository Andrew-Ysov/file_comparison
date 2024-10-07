# Скрипт по сравнению файлов на флешке и на диске

## Цель проекта:

Цель в том, чтобы на флешке были такие же файлы, как и на диске

Данный проект создан для работы с моим backup-ом (у меня есть флешка, на которой лежит мой backup в виде разных файлов, которые я хочу хранить), 
также на моём диске лежат точно такие же файлы, но я иногда изменяю содержание диска, и вместо того, чтобы повторять свои действия на флешке
я сделаю скрипт, который это будет делать вместо меня

Файлы, которых нет на диске, но есть на флешке будут удаляться с флешки


И наоборот, файлы, которые есть на диске, но нет на флешке, будут добавляться на флешку


## Причина создания проекта

Причина создания в том, чтобы увеличить эффективность копирования. Вместо того, чтобы полностью всё копировать (brute force подход) 
я хочу копировать только те файлы, которые нужно


## Как пользоваться прокетом

В файле paths.py нужно указать пути до главного диска (в переменной main_disk), до бэкапа (в переменной backup),

В будущем возможно будет реализовано добавление путей, которые можно будет игнорировать скрипту, то есть пропускать их
