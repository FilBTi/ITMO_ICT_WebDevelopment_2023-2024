# Задание №3

???+ question "Задание"

    Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
    клиент получает http-сообщение, содержащее html-страницу, которую сервер
    подгружает из файла `index.html`.

    Обязательно использовать библиотеку `socket`

# 
Как и в предыдущем задании сервер состоит из нескольких модулей. В данном случае - 
сущности Response и Server

=== "Response"

    ```Python title="response.py"
    --8<-- "Lab1/Task3/Server/response.py"
    ```
    
    Это простая модельная сущность, описывающая HTTP-ответ

=== "Сервер"

    ```Python title="server.html"
    --8<-- "Lab1/Task3/Server/server.py"
    ```

    - Конфигурируем серверный TCP-сокет. 
    - Принимаем клиентское соединение. 
    - Загружаем HTML-страницу из файловой системы. 
    - Отправляем ответ клиенту. 

=== "Клиент"
    ```Python title="server.html"
    --8<-- "Lab1/Task3/client.py"
    ```

    - Конфигурируем клиентский TCP-сокет. 
    - Подключаемся к серверу. 
    - Отправляем запрос на сервер. 
    - Получаем ответ от сервера. 
    - Выводим результат в консоль. 