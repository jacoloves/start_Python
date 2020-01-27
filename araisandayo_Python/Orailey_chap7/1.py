def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('valeu="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('A')
unicode_test('$')
unicode_test('\u20ac')
unicode_test('\u2603')
unicode_test('\u00e9')