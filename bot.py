import telebot
from telebot import types # для указание типов

bot= telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    nav = types.KeyboardButton("Навигатор по рофессиям")
    markup.add(btn1, btn2,nav)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])


def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет... Тебя приветствует навигатор по кеативным профессиям")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        creative_industr = types.KeyboardButton("Что такое креативная индустия?")
        what_kind = types.KeyboardButton("Какие креативные индустии есть в России?")
        benefits = types.KeyboardButton("Какие преимущества есть у Digital сферы?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(creative_industr, what_kind,benefits, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Что такое креативная индустия?"):
        bot.send_message(message.chat.id, "Креативная индустрия (creative industry, креативная экономика, экономика знаний) — сектор экономики, развивающийся преимущественно на идеях и технологиях. Речь идет о человеческой деятельности, основанной на приоритете интеллекта, оригинальных идей, инновационных технологий.")
    
    elif message.text == "Какие креативные индустии есть в России?":
        photo = open('Creative_rus.jpg','rb')
        bot.send_photo(message.chat.id, photo)

    elif message.text == "Какие преимущества есть у Digital сферы?":
        mess="""
        •	Срок освоения таких профессий краток. (3-6 месяцев)
•	Повышенный спрос на специалистов в сфере информационных технологий.
•	Здесь людей оценивают по результатам;
•	Совершенно неважен возраст и предыдущие дипломы;
•	Возможность создания личного бренда, своего кейса.
•	Постоянное совершенствование своих знаний, повышение квалификации с учетом новых требований заказчиков;
•	Более чем достойная оплата труда, назначаемая непосредственно вами;
•	Возможность работать дистанционно, ведь ваша аудитория – практически весь мир;
•	Свободная и регулируемая занятость, удобный график работы."""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
    
    elif (message.text == "Навигатор по рофессиям"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        gr_dis = types.KeyboardButton("Графический дизайнер")
        testir = types.KeyboardButton("Тестировщик")
        develop = types.KeyboardButton("Разработчик ПО")
        targetolog = types.KeyboardButton("Таргетолог")
        seo = types.KeyboardButton("SEO-специалист")
        copywrite = types.KeyboardButton("Копитрайтер")
        illustraitor = types.KeyboardButton("Иллюстратор")
        interface_d = types.KeyboardButton("Дизайнер интерфейсов")
        smm = types.KeyboardButton("SMM-менеджер")
        
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(gr_dis, testir,develop,targetolog,seo,copywrite,illustraitor,interface_d,smm, back)
        bot.send_message(message.chat.id, text="Выберите специальность", reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,nav)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "Графический дизайнер"):
        photo = open('Graf_dis.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """Работа графического дизайнера связана с созданием визуального контента посредствам графики. Профессия родилась на пересечении высоких технологий и рисования.
Графический дизайнер владеет искусством проектирования объектов с помощью графических изображений.
Одним из направлений графического дизайна является веб-дизайн – деятельность по оформлению сайтов в интернете.
Графический дизайнер – профессия творческая, близкая по смыслу и философии к работе художника, создающего живописные произведения."""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает графический дизайнер?")
        button2 = types.KeyboardButton("Soft-skills графического дизайнера")
        button3 = types.KeyboardButton("Где получить профессию графический дизайнер?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у графического дизайнера?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает графический дизайнер?"):
        text = """Приобретаемые навыки:
•	Креативное мышление и визуализация
•	Типографика.
•	Освоение профессионального ПО.
•	Освоение мультимедийного ПО.
•	Знания теории цвета.
•	Основы HTML и CSS.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills графического дизайнера"):
        text = "Эмпатия, самостоятельность, критическое мышление, настойчивость, упорство, саморазвитие"
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию графический дизайнер?"):
        text = "Вузы, ссузы"
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у графического дизайнера?"):
        text = """Перспектива трудоустройства:
•	Графический дизайнер универсал.
•	Продуктовый дизайнер.
•	Дизайнер.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif (message.text == "Разработчик ПО"):
        photo = open('develop.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """Программист – это специалист, создающий исходный код для программы.
Такой программой может быть операционная система компьютера, видеоигра, web или мобильное приложение и даже алгоритм работы микроволновки.
Программный код пишется на специальном языке программирования. Он состоит из обычных слов и некоторых специальных символов.
Сегодня насчитывается несколько сотен языков программирования, но самые распространенные из них – Java, Python, PHP, C#, JavaScript, C, С++, Objective-C, Swift.
Какой язык программирования выбрать, программист решает сам в зависимости от конкретной задачи (сделать игру, приложение для web или программу для сервера) и собственных знаний.
Квалифицированный программист уверенно использует 2-4 языка."""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает разработчик ПО?")
        button2 = types.KeyboardButton("Soft-skills разработчика ПО")
        button3 = types.KeyboardButton("Где получить профессию разработчик ПО?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у разработчика ПО?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает разработчик ПО?"):
        text = """Приобретаемые навыки:
•	Креативное мышление и визуализация
•	Типографика.
•	Освоение профессионального ПО.
•	Освоение мультимедийного ПО.
•	Знания теории цвета.
•	Основы HTML и CSS.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills разработчика ПО"):
        text = "Аккуратность, внимательность, целеустремленность, умение самостоятельно принимать решения, ответственность, терпеливость, настойчивость, склонность к интеллектуальным видам деятельности, логическое мышление; гибкость и динамичность мышления; аналитические способности; хорошая память; математические и технические способности."
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию разработчик ПО?"):
        text = "Если есть возможность поступить в вуз, то лучше выбрать один из ведущих: МГУ, МИФИ, ВШЭ, СПБГУ, МФТИ, МГТУ им. Баумана, МАИ, ИТМО и т.д. "
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у разработчика ПО?"):
        text = """Перспектива трудоустройства:
•	Графический дизайнер универсал.
•	Продуктовый дизайнер.
•	Дизайнер.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')


    elif (message.text == "Тестировщик"):
        photo = open('test.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """Тестировщик программного обеспечения планирует и выполняет тестирование приложений, отлаживает код, улучшает юзабилити программ.
Часто к названию профессии добавляют латинские буквы q и a: qa тестировщик. Также употребляют название qa-инженер. В латинских буквах спрятана суть деятельности тестировщика.
В широком смысле тестировщики участвуют в создании полезного для пользователей программного обеспечения.
Если конкретизировать, тестировщики контролируют качество приложений, над которыми работает организация.
"""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает тестировщик?")
        button2 = types.KeyboardButton("Soft-skills тестировщика")
        button3 = types.KeyboardButton("Где получить профессию тестировщик?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у тестировщика?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает тестировщик?"):
        text = """- знание основ тестирования, классификацию тестирования, методы и инструменты, создание сценариев тестирования
- знание основ программирования, протокола HTTP, умение работать с базами данных и системами контроля версий
- понимание клиент-серверной архитектуры, умение тестировать API и пользоваться снифферами (анализаторами) трафика. 
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills тестировщика"):
        text = "Внимательность к мелочам, критическое мышление, умение анализировать информацию"
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию тестировщик?"):
        text = "Если есть возможность поступить в вуз, то лучше выбрать один из ведущих: МГУ, МИФИ, ВШЭ, СПБГУ, МФТИ, МГТУ им. Баумана, МАИ, ИТМО и т.д. "
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у тестировщика?"):
        text = """- Компании, которые занимаются разработкой и поставкой программного обеспечения.
- Компании по разработке приложений и игр.
- Финансовые учреждения, брокеры, банки.
- Компании по системной интеграции для корпоративного бизнеса.
- Все чаще тестировщиков приглашают на работу в автомобильные компании, электронные ритейлеры, онлайновые образовательные учреждения и СМИ.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')
    
    elif (message.text == "Таргетолог"):
        photo = open('targetolog.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """Таргетолог — это человек, который настраивает и запускает рекламу в социальных сетях.
Название профессии происходит от английского слова target, «цель». В данном случае цель — это аудитория, заинтересованная в бренде, продукте или услуге.
Ведь эффективная реклама не та, которую увидело как можно больше людей, а та, что привела лидов — потенциальных покупателей и клиентов.
Задача таргетолога в данном случае — используя такие параметры, как возраст, профессия, интересы интернет-пользователя и его геолокацию, качественно настроить рекламу.
В итоге бизнес при минимальных бюджетных затратах получает максимальный результат.
Таргетолог — это многопрофильный специалист. Он должен разбираться в маркетинге, веб-аналитике, владеть базовыми навыками работы в графических и видео- онлайн-редакторах.
"""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает таргетолог?")
        button2 = types.KeyboardButton("Soft-skills таргетолога")
        button3 = types.KeyboardButton("Где получить профессию таргетолог?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает таргетолог?"):
        text = """Приобретаемые навыки:
- маркетинговый анализ
- умение писать короткие продающие тексты
- работа в графических и видеоредакторах
- работа в системах веб-аналитики
- медиапланирование 
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills таргетолога"):
        text = "Умение работать в режиме многозадачности, креативность, самооразование, смелость в принятии решений, внимательность, не бояться экспериментировать, высокая концентрация внимания и профессиональная педантичность, неконфликтность, склонность к аналитике и планированию."
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию таргетолог?"):
        text = "Таргетологи получают необходимые профессиональные знания на курсах. Диплом ссуза или вуза для работы в рассматриваемой сфере не требуется, средний срок обучения составляет от 2 до 6 месяцев."
        bot.send_message(message.chat.id, text, parse_mode= 'html')
        
    elif (message.text == "SEO-специалист"):
        photo = open('seo.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """SEO-специалист (специалист по продвижению сайтов) — это человек, который продвигает сайты в поисковых системах.
Результатом продвижения может быть: попадание в топ поисковых систем «Яндекс» и Google (продвижение по позициям) и увеличение трафика на сайт (продвижение по трафику).
Хороший SEO-специалист должен разбираться и в интернет-маркетинге.
"""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает SEO-специалист?")
        button2 = types.KeyboardButton("Soft-skills SEO-специалиста")
        button3 = types.KeyboardButton("Где получить профессию SEO?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у SEO-специалист?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает SEO-специалист?"):
        text = """-	правила внутренней оптимизации сайта, подбора ключевых фраз, написания и оптимизации текстов;
-	способы организации структуры сайта;
-	оптимальные технические характеристики сайта;
-	инструменты продвижения сайта;
-	основы программирования;
-	методы продвижения сайта в социальных сетях;
-	работа с контекстной рекламой;
-	HTML и CSS.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills SEO-специалиста"):
        text = "Усидчивость, умение планировать работу, широкий кругозор, ответственность, организованность, целеустремленность, хорошее логическое мышление, умение находить подход к разной аудитории, понимание психологии разных слоев населения."
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию SEO?"):
        text = """Чтобы стать SEO-оптимизатором, совсем необязательно заканчивать вуз. Для входа в профессию достаточно краткосрочных курсов. Многие самостоятельно учатся по статьям, видеокурсам в интернете.
        Необходимый минимум для начала работы – знание основ HTML-верстки, основных CMS (систем управления контентом), программ аналитики и инструментов оптимизации."""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у SEO-специалист?"):
        text = """SEO-специалисты могут работать в штате SEO-агентства, веб-студии или другой компании, а могут искать заказы самостоятельно, работая на фрилансе."""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif (message.text == "Копитрайтер"):
        photo = open('copy.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """Копирайтер (англ. сopy – рукопись, текст, write – писать) – это автор рекламных текстов, будь то название бренда, слоган,
сам рекламный текст и его составляющие, статья, пресс-релиз, сценарий рекламного ролика на телевидении, в интернете или на радио и так далее
"""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает копирайтер?")
        button2 = types.KeyboardButton("Soft-skills копирайтера")
        button3 = types.KeyboardButton("Где получить копирайтер?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у копирайтера?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает копирайтер?"):
        text = """- Слепой десятипальцевый метод печати
- Базовые знания английского языка
- Способность быстро и глубоко вникать в новую тему
- Владение разными стилями
- Знание принципов SEO
- Понимание целей текста
- Основы сайтостроения
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills копирайтера"):
        text = "Креативное мышлениее, широта интеллекта, неиссякаемая любознательность и наблюдательность, грамотная речь, уверенность, настойчивость и упорство"
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить копирайтер?"):
        text = """Специальность копирайтера можно приобрести в вузе, имеющем факультет рекламы. Подходят также филологический и факультет журналистики. Возможно обучение на курсах."""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у копирайтера?"):
        text = """Копирайтер работает в рекламных, брендинговых и PR-агентствах, а также в маркетинговых или рекламных отделах различных фирм."""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif (message.text == "Иллюстратор"):
        photo = open('illustraitor.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """Суть работы иллюстратора – создание эскизов и готовых работ для заказчиков.
Иллюстраторы должны владеть огромным количеством различных техник рисования: Графическая иллюстрация. Выполнение рисунка в технике графики.
Это может быть простой либо черный карандаш. Рисунок наносится в виде штрихов и пятен. Основным требованием графики является присутствие только одного цвета линий.
Ботаническая иллюстрация. Это картинка, являющаяся изображением описываемого объекта. Такие обычно применяют в школьных или университетских учебниках. Техническая иллюстрация.
Это всевозможные чертежи, которые являются обязательным сопровождением всей инженерной документации. Иллюстрация особыми техниками.
К ним относятся оригами, вышивка, лепка, аппликация, икебана и т.д.
Любой иллюстратор должен владеть каждой из данных техник, ведь разные заказчики предъявляют абсолютно разносторонние требования к выполняемой работе.
"""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает иллюстратор?")
        button2 = types.KeyboardButton("Soft-skills иллюстратора")
        button3 = types.KeyboardButton("Где получить профессию иллюстратор?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у иллюстратора?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает иллюстратор?"):
        text = """- создание иллюстраций;
- обработка и ретушь изображений или фотографий;
- разработка шрифтов;
- работа с векторными изображениями. 
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills иллюстратора"):
        text = "Усидчивость, дисциплинированность, умение делать контент и отчёты вовремя, самоорганизация"
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию иллюстратор?"):
        text = """МГУП (Московский Государственный Университет Печати). ВАШГД (Высшая Академическая Школа Графического Дизайна). Британская Высшая Школа Дизайна."""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у иллюстратора?"):
        text = """Перспектива трудоустройства:
- рекламные агентства
- журналы
- издательства.
 Также найти работу можно, зарегистрировавшись на сайтах фриланса.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif (message.text == "Дизайнер интерфейсов"):
        photo = open('interface_dis.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """UX/UI дизайн — это проектирование любых пользовательских интерфейсов в которых удобство использования так же важно как и внешний вид.
        Что такое UX и UI дизайн, другими словами.
        Прямая обязанность UX/UI дизайнера — это, например, «продать» товар или услугу через интерфейс.
        Именно на основе работы UX/UI дизайнера пользователь принимает решение: «Быть или не быть?». Нравится или не нравится.
        Купить или не купить.
"""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает дизайнер интерфейсов?")
        button2 = types.KeyboardButton("Soft-skills дизайнера интерфейсов")
        button3 = types.KeyboardButton("Где получить профессию жизайнер интерфейсов?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у дизайнера интерфейсов?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает дизайнер интерфейсов?"):
        text = """Приобретаемые навыки:
•	продумывать пути пользователя и рассчитывать алгоритм его действий;
•	заниматься написанием пользовательских сценариев;
•	рисовать промо-материалы и страницы (для этого надо иметь хотя бы минимальные художественные навыки);
•	отличать хороший и продающий дизайн от плохого;
•	тестировать готовый дизайн сайта и исправлять некоторые ошибки в нем;
•	анализировать рынок;
•	заниматься созданием инфографики и презентаций;
•	собирать и анализировать требования, прототипировать, вносить правки и т. д. – для этого нужны знания технологий создания цифрового продукта.
•	верстка и многое другое.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills дизайнера интерфейсов"):
        text = "Коммуникабельность , любопытство, аналитические способности, внимательность , самоорганизованность"
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию жизайнер интерфейсов?"):
        text = """Если вы хотите в будущем работать дизайнером интерфейсов, то обязательно должны получить специальность, которая напрямую связана со сферой IT-технологий:
веб-дизайн;
компьютерная графика и дизайн;
информационный дизайн и другие.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у дизайнера интерфейсов?"):
        text = """Перспектива трудоустройства:
•	UI-дизайнеры нужны в любой компании, которая так или иначе связана с IT: невозможно разрабатывать программное обеспечение, не уделяя внимания пользовательскому интерфейсу. Дизайнер также может быть фрилансером и работать в удаленном формате..
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif (message.text == "SMM-менеджер"):
        photo = open('smm.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        mess = """SMM-менеджер (с англ. Social Media Manager) – это специалист, который занимается продвижением бизнеса, а именно компаний, брендов и отдельных лиц в социальных медиа 
(Вконтакте, Facebook, Instagram, Одноклассники, YouTube, Twitter и других).
Профессия SMM-менеджера, с одной стороны, связана с рекламой и пиаром, а с другой – с IT-сферой.
В части продвижения продукта специалист по SMM обычно сотрудничает с рекламным отделом, но у него есть и свои отдельные задачи, связанные с ведением сообществ, аналитикой и взаимодействием с людьми.
"""
        bot.send_message(message.chat.id, mess, parse_mode= 'html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Какие навыки приобретает SMM-менеджер?")
        button2 = types.KeyboardButton("Soft-skills SMM-менеджера")
        button3 = types.KeyboardButton("Где получить профессию SMM-менеджер?")
        button4 = types.KeyboardButton("Какие перспективы трудоустройства у SMM-менеджера?")
        nav = types.KeyboardButton("Навигатор по рофессиям")
        markup.add(button1, button2,button3,button4, nav)
        bot.send_message(message.chat.id, text="Выберите пункт", reply_markup=markup)
        
    elif(message.text == "Какие навыки приобретает SMM-менеджер?"):
        text = """Приобретаемые навыки:
- ведение аккаунтов, блогов, страниц и групп определенной направленности;
- наполнение страниц полезным и интересным контентом, соответствующим требованиям SEO;
- работа с общественным мнением, повышение лояльности отношения целевой аудитории к работе компании, увеличение количества лайков, репостов, положительных отзывов;
- реализация рекламной кампании в крупных соцсетях: Одноклассники, Вконтакте, Фейсбук, Инстаграмм и т. д.;
- общение с пользователями Всемирной Сети, существующими и потенциальными клиентами.
"""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Soft-skills SMM-менеджера"):
        text = "Креативность, нацеленность на результат, коммуникабельность, чувство юмора, желание расти как профессионал, системное аналитическое мышление, навык работы с большим объемом информации, самодисциплина, инициативность и самостоятельность, умение четко формулировать свои мысли, отличное владение английским и русским языками, в особенностями письменными."
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Где получить профессию SMM-менеджер?"):
        text = """Наиболее эффективными в вопросе изучения основ SMM станут коммерческие курсы средней продолжительности и онлайн-школы."""
        bot.send_message(message.chat.id, text, parse_mode= 'html')

    elif(message.text == "Какие перспективы трудоустройства у SMM-менеджера?"):
        text = """Перспектива трудоустройства:
Практически каждой компании нужен свой SMM-специалист, чтобы привлекать внимание к своим услугам и товарам."""
        bot.send_message(message.chat.id, text, parse_mode= 'html')


    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)
