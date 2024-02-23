sen_1=True
sen_2=False
if sen_1 and sen_2:
    print('Both true and used "and"')
else:
    print('Both or either false and used "and"')
if sen_1 or sen_2:
    print('Both or either true and used "or"')
else:
    print('Both false and used "or"')
if sen_1 and not sen_2:
    print('Both true as sen_2 is changed and used "and" and "not"')
else:
    print('Both or either false as sen_2 is changed and used "and" and "not"')