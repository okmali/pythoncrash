unconfirmed_users=['mali','erhan','turan','ahmet']
confirmed_users=[]
while unconfirmed_users:
    cur_user=unconfirmed_users.pop()
    if cur_user.strip().lower() !='mali':
        confirmed_users.append(cur_user)

print(confirmed_users)
