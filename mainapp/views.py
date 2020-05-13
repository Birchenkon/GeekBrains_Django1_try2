from django.shortcuts import render


def main(request):
    same_products = [
        {"img": "product-71.jpg", "name": "стул фанбюн", "desc": "Расположитесь комфортно."},
        {"img": "product-20.jpg", "name": "стул линрабд", "desc": "Не оторваться."}
    ]
    content = {"same_products": same_products}
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    links_menu = [
        {"href": "products_all", "name": "все"},
        {"href": "products_home", "name": "дом"},
        {"href": "products_office", "name": "офис"},
        {"href": "products_modern", "name": "модерн"},
        {"href": "products_classic", "name": "классика"},
    ]
    slider_products = [
        {"img": "prod-2.jpg"},
        {"img": "prod-3.jpg"},
        {"img": "prod-4.jpg"},
    ]
    same_products = [
        {"name": "Отличный стул", "img": "product-22.jpg", "alt": "product-22"},
        {"name": "Улучшенный стул", "img": "product-20.jpg", "alt": "product-20"},
        {"name": "Гроссмейстерский стул", "img": "product-71.jpg", "alt": "product-71"},
    ]
    content = {"links_menu": links_menu, "slider_products": slider_products, "same_products": same_products}
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    contacts_info = [
        {"city": 'Москва', "phone": '+7-888-888-8888',
         "imail": 'myshop_msc@gmail.com', "adres": "3-я улица Строителей д. 25"},
        {"city": 'Санкт-Петербург', "phone": '+7-888-888-9999',
         "imail": 'myshop_psb@gmail.com', "adres": "3-я улица Строителей д. 25"},
        {"city": 'Ярославль', "phone": '+7-888-888-5555',
         "imail": 'myshop_yar@gmail.com', "adres": "ул. Московская д.10"}
    ]
    content = {"contacts_info": contacts_info}
    return render(request, 'mainapp/contact.html', context=content)


# Create your views here.
