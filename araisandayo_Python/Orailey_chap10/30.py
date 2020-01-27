import locale
from datetime import date
halloween = date(2014, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    print(locale.setlocale(locale.LC_TIME, lang_country))
    print(halloween.strftime('%A, %B %d'))
