Этот проект был задуман, как способ быстрого моделирования расклада поля для настольной игры.
Смысл довольно простой - нужно выложить 64 шестигранных тайла на стол, так чтобы хотябы одно поле на шестигранниках совпадало и шестигранники не перекрывали друг друга.
Всего 4 типа поля, на одном шестиграннике может быть 3 любых поля. Шестигранники не повторяются.

Пример стильных гексов на чёрном поле

![size_0](https://github.com/iisakov/BoardGame/assets/59264679/1f041bea-973f-44a7-a90a-a5303a6e004b) 

Рандомный выброс гексов на поле

![gex](https://github.com/iisakov/BoardGame/assets/59264679/01fafe7b-6ff8-438d-8a76-fa14973988c8)
![gex](https://github.com/iisakov/BoardGame/assets/59264679/6029482e-bafb-4ee7-bf44-6a6eae5c8ecd)


Пытливый глаз может заметить, что тайлы на поле падают центрами в одни и теже места. Да - это происходит птому что гексы изначально привязаны к сетке в зависимости от своего размера. Размер задаётся для карты, для гекса и для колоды.


Финишная прямая
![map](https://github.com/iisakov/BoardGame/assets/59264679/2fa3c4f3-529d-4004-9d29-98ed46d11cfc)
![map](https://github.com/iisakov/BoardGame/assets/59264679/1843f6bb-34c1-4cc1-b71c-b21eeb3c6660)


А теперь собирать статистику (но для этого, сначала нужно убирать лишние поля)
![map_0_1_False](https://github.com/iisakov/BoardGame/assets/59264679/af2d9095-336e-4382-816d-0d6559165149)
![map_0_1_False](https://github.com/iisakov/BoardGame/assets/59264679/caba162a-682f-4b02-b42c-367dc17e3f76)


Статистика и выкладывание гексов по правилам
![map_0_500_True](https://github.com/iisakov/BoardGame/assets/59264679/8d8dd3e4-0323-4507-b510-2119e6893865)
![image](https://github.com/iisakov/BoardGame/assets/59264679/74d93a65-d178-4ead-946c-b4ab6619c413)

Статистика на экране, по ходам и по игрокам.
![map_1500_True](https://github.com/iisakov/BoardGame/assets/59264679/74d66c7a-6bff-4859-9e50-e13f88a9c916)
