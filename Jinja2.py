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

#print(lk)


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
print(prfor1)
