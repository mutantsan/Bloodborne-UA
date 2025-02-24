# Локалізація гри "Bloodborne"

Переклад гри "Bloodborne" на українську мову. Переклад ведеться з англійської мови. Спірні моменти звіряються з японською версією гри. Якщо ви знайшли помилку або хочете допомогти, то робіть Pull Request.

Для розпаковки внутрішньоігрових файлів використовується програма [WitchyBND](https://github.com/ividyon/WitchyBND).

Планується замінити російську мову, так як мені лінь розбиратися чи можна додати нову мову в гру. Кириличний шрифт вже є в грі і він підтримує українські літери (іІ їЇ єЄ ґҐ).

Цей мод в першу чергу націлений на роботу з емулятором [shadPS4](https://github.com/shadps4-emu/shadPS4), але при правильній установці може працювати і на консолі. Як встановити мод на консоль можна прочитати [тут](https://consolemods.org/wiki/PS4:FAQ).

## Структура файлів гри

Файли з локалізацією знаходяться за шляхом `\CUSA03173\dvdroot_ps4\msg\rusru`, де `CUSA03173` - це код гри, а `rusru` - код мови.

Всередині теки `rusru` знаходяться файли з розширенням `.dcx`. Це один зі стандартних форматів, який використовується в іграх від FromSoftware для компресії файлів. Ці файли можна розпакувати за допомогою програми WitchyBND. Нас цікавлять оці два файли:

- item.msgbnd.dcx
- menu.msgbnd.dcx

Розпакувавші ці файли ми отримаємо дві теки: `item-msgbnd-dcx` та `menu-msgbnd-dcx`. В кожній з цих тек знаходяться файли з розширенням `.fmg`. Ці файли містять в собі текстові дані, які відображаються в грі, у форматі `.xml`. Їх теж треба розпакувати, щоб працювати з текстом.

Назви файлів в обох теках змінювати **не можна**, вони мають залишитися японською.

Також слідкуйте за тим, щоб не змінити атрибут `id` чи не зламати структуру xml документу:

```xml
<text id="429100">Select appearance of tattoo/mark.</text>
```

Зробивши зміни в тексті, його потрібно знову упакувати в формат `.fmg` і потім у формат `.dcx`. Отримавши назад два файли `item.msgbnd.dcx` та `menu.msgbnd.dcx`, їх треба повернути назад в теку з грою. Після цього можна запускати гру і перевіряти зміни.

## Словник термінів

Власні назви та специфічні терміни мають перекладатися відповідно до контектсту гри. Також, треба по можливості звірятися з японською версією гри. Щоб не запам'ятовувати всі терміни, створений словник, який буде оновлюватися з часом - `names.txt`.

## Автоматизація

Щоб спростити процес тестування, запаковування було автоматизовано. Для цього використовується скрипт `main.py`. Він автоматично запаковує файли з перекладом та копіює їх в потрібну теку гри. Для роботи скрипта потрібно вкахати шлях до програми WitchyBND та шлях до теки з грою (безпосередньо до теки мови, яку хочете замінити).

Так як я працюю під WSL2, то я можу викликати `.exe` файли напряму. Якщо ви працюєте на Windows, то з цим у вас теж не повинно бути проблем. В іншому випадку, вам доведеться розібратися самостійно. Коли переклад буде у грабельному стані, я опублікую файли, які можна буде просто скопіювати в гру.

## Прогрес перекладу

Деякі файли вже повністю перекладені, але є ще багато роботи. Деякі файли містять повторювані рядки, які можна перекласти один раз.

Нижче наведений список файлів, які ще не перекладені з прогресом перекладу:

There are 4661 untranslated lines in `血文字.fmg.xml`
There are 681 untranslated lines in `SP_メニューテキスト.fmg.xml`
There are 2501 untranslated lines in `魔石効果.fmg.xml`
There are 3546 untranslated lines in `魔石うんちく.fmg.xml`
There are 20 untranslated lines in `魔石説明.fmg.xml`
There are 408 untranslated lines in `イベントテキスト.fmg.xml`
There are 120 untranslated lines in `キーガイド.fmg.xml`
There are 2500 untranslated lines in `会話.fmg.xml`
There are 83 untranslated lines in `SP_一行ヘルプ.fmg.xml`
There are 161 untranslated lines in `ダイアログ.fmg.xml`
There are 164 untranslated lines in `SP_ダイアログ.fmg.xml`
There are 712 untranslated lines in `メニュー共通テキスト.fmg.xml`
There are 73 untranslated lines in `インゲームメニュー.fmg.xml`
There are 41 untranslated lines in `システムメッセージ_win64.fmg.xml`
There are 3114 untranslated lines in `魔石名.fmg.xml`
There are 134 untranslated lines in `アイテム説明.fmg.xml`
There are 704 untranslated lines in `武器名.fmg.xml`
There are 37 untranslated lines in `地名.fmg.xml`
There are 257 untranslated lines in `アイテム名.fmg.xml`
There are 46 untranslated lines in `NPC名.fmg.xml`
There are 231 untranslated lines in `アイテムうんちく.fmg.xml`
There are 1025 untranslated lines in `武器うんちく.fmg.xml`
There are 114 untranslated lines in `防具うんちく.fmg.xml`

There are 21333 untranslated lines in total so far, which is 52.35%
