import datetime


brut = '14:04:45.177000'

#for b in brut:
#    if b == '.':
#        print(brut. split(b))

brut = brut.split(':')
h = brut[0]
m = brut[1]

print(h + 'h' + m)
