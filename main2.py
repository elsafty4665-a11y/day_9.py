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




#1
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)




bids={}




