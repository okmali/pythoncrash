alien_0={'color':'green','points':5}
alien_1={'color':'blue','points':4}
alien_2={'color':'yellow','points':15}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print('total number of aliens:',len(aliens))

for alien in aliens[0:3]:
    alien['color']='yellow'
    alien['points']=15
    alien['speed']='fast'

print('first 5 aliens now')    
for alien in aliens[:5]:
    print(alien)

print('------------all reset aliens--------------')

for alien in aliens:
    if alien['color'].lower()=='yellow':
        alien['color']='red'
        alien['points']=20
        alien['speed']='super fast'
    elif alien['color'].lower()=='green':
        alien['color']='orange'
        alien['points']=18
        alien['speed']='medium fast'

for alien in aliens[:10]:
    print(alien)