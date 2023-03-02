django-admin startproject web_project .
python manage.py startapp shop
python manage.py makemigrations
python manage.py migrate

python manage.py shell
from shop.models import Item, Purchase

item_1 = Item(id=1, name="Phone", price="20000")
item_1.save()
item_2 = Item(id=2, name="TV", price="30000")
item_2.save()
item_3 = Item(id=3, name="Toster", price="5000")
item_3.save()
item_4 = Item(id=4, name="Mixer", price="2000")
item_4.save()
Item.objects.create(id=5, name="Teapot", price=500)

Purchase.objects.create(id=1, name="Nursultan", age=30, item=item_1)
Purchase.objects.create(id=2, name="Veronica", age=18, item=item_2)
Purchase.objects.create(id=3, name="Sam", age=20, item=item_3)
Purchase.objects.create(id=4, name="Rusla", age=35, item=item_4)
item_5 = Item.objects.get(id=5)
Purchase.objects.create(id=5, name="Ata", age=35, item=item_5)




