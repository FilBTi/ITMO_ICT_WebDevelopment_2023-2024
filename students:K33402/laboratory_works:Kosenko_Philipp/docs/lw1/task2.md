# Задание №2

???+ question "Задание"

    Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
    сервера выполнение математической операции, параметры, которые вводятся с
    клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
    клиенту. Вариант - Поиск площади трапеции.

    Обязательно использовать библиотеку `socket`  
    Реализовать с помощью протокола TCP

#
    Для упрощения процесса разработки и поддержки, 
    я решил сделать сервер модульным. 
    Поэтому сервер в данной работе представляет собой совокупность
    классов Server и MathModule. При этом необходимые строковые 
    константы берутся в виде статических методов из класса Messages. 

=== "MathModule"

    ```Python title="mathModule.py"
    --8<-- "Lab1/Task2/Server/mathModule.py"
    ```
    
    Данный класс предназначен для решения квадратного уравнения, исходя из значений 
    его коэффициентов. Сущность содержит два статических метода - метод для решения ур-ия
    и метод для нахождения дискриминанта. Метод для решения ур-ия возвращает строку 
    ( либо численные решения, либо сообщения о невозможности найти решение в действ. числах )


=== "Сервер"

    ```Python title="server.py"
    --8<-- "Lab1/Task2/Server/server.py"
    ```

    - Инициализируем TCP-сервер при помощи описанного ранее конфигуратора.
    - Принимаем клиентское подключение. 
    - Отсылаем клиенту сообщение о необходимости ввести данные.
    - Получаем данные от клиента.
    - Парсим клиентские данные. 
    - Передаем информацию в математический модуль. 
    - Получаем ответ от математического модуля. 
    - Передаем ответ клиенту. 

=== "Клиент"

    ```Python title="client.py"
    --8<-- "Lab1/Task2/client.py"
    ```

    - Импортируем конфигуратор и получаем необходимую информацию о серверном сокете. 
    - Инициализируем клиенсткий TCP-сокет. 
    - Подключаемся к серверу. 
    - Получаем приветственное сообщение от сервера. 
    - Запрашиваем пользовательский ввод с клавиатуры. 
    - Передаем введенные данные на сервер. 
    - Принимаем ответ от сервера. 
    - Выводим результат в консоль. 