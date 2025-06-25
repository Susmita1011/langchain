from typing import TypedDict

# here a class is defined stating that what keys and values it need
class Person(TypedDict):
    name: str
    age: int
#Way to use the Person Class
new_person: Person = {'name':'Susmita','age': '33'}
# no validation is done -> if age is '35' it would still work
print(new_person)