## dictionaries 

mo={"key":"values"}
print (mo)

user={
       "name":"mohamed",
       "age":"19"
       }
print(user.get("name"))
print (user.get('age'))
print(len(user))
print (len(user['age']))

user.update({'names':'re'})
user['country']='egypt'

print (user)
print(user.clear())

mo={'s':{
     'e':'w',
     'q': 'w'
},
'c':{
    'k':1
}

}
print (mo)


s={'name':'mohamed',
   'age':19
   ,'country':'egypt'}

for key in s:
    
    print (s[key])



