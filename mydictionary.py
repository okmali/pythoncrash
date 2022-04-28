favourite_langs={
    'sarah':'C++',
    'mike':'C',
    'john':'C#',
    'jane':'java'
}

print('Sarah''s favourite programming '\
        'language is:',
        favourite_langs['sarah'])

print('let''s loop')

for key,value in favourite_langs.items():
    print('key:',key, 'value:',value)



users={'einstein':{'first':'Albert','last':'Einstein','location':'Princeton'},
       'marie':{'first':'Marie','last':'Curie','location':'Paris'},
       }

for name,user_details in users.items():
    print('name of the user:',name,' details of user:',user_details)

from myfuncs import create_profile

print('Create Profile:',create_profile('Albert','Einstein',location='Princeton',field='Physics',age=80))
