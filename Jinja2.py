from jinja2 import Template
from markupsafe import escape

"""Jinja training material
first lesson"""

name = "Ronaldo"
age = 38

tm = Template("Hello {{name}} {{a}}")
msg = tm.render(name=name, a=age)
# print(msg)


"""Пример работы с  классами"""


class Computer:
    def __init__(self, model: str, maker: str, year: int):
        self.model = model
        self.maker = maker
        self.year = year

    def get_model(self):
        return self.model

    def get_maker(self):
        return self.maker

    def get_year(self):
        return self.year


comp = Computer("MacBook10", "Apple", 2023)
cm = Template(
    "notebook {{c.get_model()}} was realised by {{c.get_maker()}} in {{c.get_year()}}"
)
msg2 = cm.render(c=comp)
# print(msg2)


"""Со словарями """
any_dict = {"model": "LX500", "maker": "Asus", "year": 2021}

dc = Template("notebook {{a.model}} was realised by {{a.maker}} in {{a.year}}")
msg3 = dc.render(a=any_dict)
# print(msg3)


"""Экранирование ссылок"""

link = "<a href='#'>Link</a>"


lk = escape(link)

# print(lk)


"""Цикл for"""

cities = [
    {"id": 1, "city": "LA"},
    {"id": 2, "city": "Las-Vegas"},
    {"id": 3, "city": "New-York"},
    {"id": 4, "city": "Boston"},
    {"id": 5, "city": "Chicago"},
]

link2 = '''<select name="cities">
{% for i in cities -%}
    <option value="{{i['id']}}">{{i['city']}}</option>
}
{% endfor -%}
</select>'''

fr1 = Template(link2)
prfor1 = fr1.render(cities=cities)
#print(prfor1)


"""Exapmles for filtering"""
cars = [
    {"model": "Tesla", "price": 60000},
    {"model": "BMW", "price": 12000},
    {"model": "Audi", "price": 15500},
    {"model": "Suzuki", "price": 21000},
]

tpl = "Total price of the cars {{c | sum(attribute='price')}}"
tpl1 = "Replace {{c | replace('o', 'O')}}"
rep = Template(tpl1)
summ = Template(tpl)
message = summ.render(c=cars)
message1 = rep.render(c=cars)
# print(message1, message, end=" ")


"""macro"""

html = '''
{% macro input(name,value="", type="text",size=20) -%}
    <input type= "{{type}}" name = "{{name}}" value = "{{value | e}}" size = "{{size}}" >
{% endmacro -%}

<p>{{input('username') }}
<p>{{input('email') }}
<p>{{input('password') }}


'''


mc = Template(html)
msg4 = mc.render()
#print(msg4)



'''call'''

persons = [
{'name': 'Ronaldo','old': 38,'height': 188},
{'name': 'Messi','old': 35,'height': 168},
{'name': 'Benzema','old': 35,'height': 185},
{'name': 'Mbappe','old': 24,'height': 178}]


html1 = '''
{% macro list_users(list_users) -%}
<ul>
{% for i in list_users -%}
    <li>{{i.name}} {{caller(i)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age:{{users.old}}
    <li>height :{{user.height}}
    </ul>
{% endcall -%}
'''

fb = Template(html1)
msg5 = fb.render(users = persons)
print(msg5)