
def make_pizza(*toppings):
    print('making pizza with toppings:')
    for topping in toppings:
        print (topping)


def create_profile(firstname,lastname,**user_params):
    profile={}
    profile['FirstName']=firstname
    profile['LastName']=lastname
    for key,value in user_params.items():
        profile[key]=value
    return profile

def print_models(unprinted_models,completed_models):
    while unprinted_models:
        model=unprinted_models.pop()
        print("3D printing model:",model)
        completed_models.append(model)


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)      

def describe_pet(pet_name,pet_type='dog'):
    print('Hi, I have a pet')
    print("It is a",pet_type, "and It's name is",pet_name)

def build_person(firstname,lastname,age,middlename=''):
    person={}
    if middlename:
        person['firstname']=firstname
        person['middlename']=middlename
        person['lastname']=lastname
        person['age']=age
    else:
        person['firstname']=firstname
        person['lastname']=lastname
        person['age']=age
    return person        