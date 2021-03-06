with open('ohvat1421.txt', 'r', encoding="utf-8") as oh:
    d=dict()
    for line in oh:
        a=0
        line=line.strip().lower().split()
        for i in line:
            if line[a] in d:
                d[line[a]]+=1
            else:
                d[line[a]]=1
            a+=1

stopwords = (
    'илья', 'в', 'агент', 'сен', 'окт','поддержки','ответ', 'есть', 'для','вопроса', 'у','годности','срок','истек','поддержка','бизнеса',
    'вопрос','ожидает', 'обработки', 'поддержкиответил', 'охват', 'по','12', 'не','сегодня', '#11350ответил', '13',
    'новый', 'вчера', 'рассмотрен', '11', '8', '10', '7', '#11289ответил','охваты', '#11352ответил', 'к','охвата', 'обжалование', 'страйка', 'сообществе', '1', '9',
    'с', '#11205ответил', '#11074ответил','группы', 'как', '#11313ответил',  'мария', '4', '#10971ответил', '#586ответил', 'почему',
     'badsupport', 'группе', 'сообщества', '21:50', 'и', '9:00', 'от', '#10234ответил', 'на', '19:32', '5','аудиозапись',
    '14:43', 'кирилл', 'сообщество', 'александр', '17:41', '#1315ответил', '9:22', '20:45', 'добрый', 'когда', 'никита', 'рома', 'сахапов13', '9:34', 'сильно', '36', 'уведомления7', 'предыдущая', 'воспроизвести', 'следующая', 'kovacs',
    '—', 'the', 'devil', 'you', 'know', 'настройки', '47', '20', 'mobile', 'alerts', '2743', '1076', '64', 'блог', 'разработчикам', 'действияещё', 'отмена', 'все', 'вопросы', 'новые', 'открытые', 'агентов', 'ответами', 'долго', 'ждущие', 'закрытые', 'временно', 'найдено', '28', '063', '2', '3', '»', 'то', 'а', '#11198ответил', '21:21', 'сети', 'владельца', '#10455ответил', '1:38', 'чтобы', 'дмитрий',
    '17','18', '16','18:34','16:29','#10398ответил', '#11130ответил', 'иван','находится', 'рассмотрении','максим', '22:21', 'человек','#11202ответил',

)

keywords = (
    'порнография', 'ненужных', 'попадают', 'попадает', 'скам'
)

fuuuu = (
    'ненужных', 'отключение', 'отключите', 'мешают', 'убрать', 'очистить', 'нерелевантного', 'клипов', 'клипы'
)

# словарь, свободный от стоп-слов
d1={}
for c in d:
    if c not in stopwords:
        d1[c]=d[c]
#         print(c, d1[c])

# #самые популярные понятия (без стоп-слов)
maximum=max(d1.values())
# print(maximum)

# #вычисление ключевых слов 2х недель (в т.ч. для стоп-слов)
# for c in d:
#     if c not in stopwords:
#         if d[c]==maximum:
#             print("'"+c+"'", end=', ')

# сортировка словаря из ключевых слов
for c in d1:
    if c in keywords:
        list_d1 = list(d1.items())
        list_d1.sort(key=lambda i: -i[1])
        for i in list_d1:
            print(i[0], ':', i[1])
