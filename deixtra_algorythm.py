#cамый популярный алгоритм для поиска кратчайшего пути
# если вес ядра не равен 1, то записываем его вес в матрицу
import sys

def vertexWithMinWeight(grath, visited):
    index = ""
    dist_min = INF
    for vertex in grath:
        if dist[vertex] < dist_min and not visited[vertex]

def dijkstra(grath, start):
    INF = MAX_INT
    visited ={}
    dist = {}
    for vertex in range(grath):
        dist[vertex] = INF

    dist[start] = 0
    while False in visited:
        u = vertexWithMinWeight(grath,)

        for v in grath[u]:
            if grath[u][v] != 0 and not visited[v]:
                dist[v]= min(dist[u + grath[u][v]])
    visited[u] = True

    return dist
# голанг
# стажка скуэль в какой форме хранятся данные на уровне представления? - связанные почему она релиационная. знать инеры, селекты, короче базовые вещи в эскуэль
# почитать про нормальные формы \ избыточные формы
# кликхауз - (где бы вы хранили аналитику)база данных от яндекса, которая используется для аналитики. данные хранятся в виде столбцов. это значит, что если мы обычно получаем данные в виде строк, в
# мы храним в виде столбца, значит можем записывать данные огромной пачкой сырые данные. кликхаус с этим отлично справляется.
# кафка - (брокер сообщений)любой брокер сообщение плотно не надо. просто понимание что это такое и для чего это нужно. идет безумная нагрузка, не хочу ничего потерять, чтобы не вернуло 500. отправить сообщение в кафку на день,
# чтобы потом через день лежания сервера не потерять это сообщение
# докер - команд пять выучить базово : что такое докер
# кубернетс
# понимание принципов солид - проектирование моих интерфейсов. буква Д
#гит лаб
# главное это язык программирования
# есть еще ноу эскуэль решение


#php
#скуэль(постгре, mysql) - стандарт бэкэндера (голанг джава плюсы)
# nosql(mongodb)
#nginx - один из самых популярных серверов, делает чпу, настраивает статику
#гит
#солид, ооп
#

#java
#спринг самый популярный фреймворк
#редиса будет достаточно, хотя касандру тоже посмотреть
# mongodb
#кликхаус
#солид
#ооп
#гит
#постгрескл

#плюсы
#с++ 17
#boost
#понимание солид, ооп
#linux
#git
#cmake

#питон
#знание основных сетевых веб протоколов как минимум https стэк
#dgango, gs, css, html
#понимание пригципов solid, ооп
#docker
#git

#ml
#phython( numpy, scikit-learn, opneCV, Pandas)
#deep learning фреймворки pytorch/jax
#git
#фреймворки на уровне того, что они есть, установить их и потыкаться, чтобы козырнуть
#


#дата саентист
#sql по полной программе на уровне сложных
#docker
#
#
#


