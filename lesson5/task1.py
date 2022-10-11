import os
os.system('cls')

s = 'фыпрабввчосорвпывр фыарвыпаро поПРЛРОпПЛпадПЛблПЛпдвл РПорпПппрпОРПо6к7А6П7пм7А6А7м 132абв456478976абв53472563а48б75в9'

def filter_string(s):
    x = s.split()
    new_s = ' '.join((filter(lambda e: 'абв' not in e, x)))
    return new_s
print(filter_string(s))