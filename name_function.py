def get_formatted_name(firstName,lastName,middleName=''):
    if middleName:
        formattedName=firstName+" "+middleName+" "+ lastName    
    else:
        formattedName=firstName+" "+lastName
    return formattedName.title()