from jinja2 import Template, Environment,FileSystemLoader 
from markupsafe import escape
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
print(msg4)



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