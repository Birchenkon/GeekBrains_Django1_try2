from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product, Contact
from basketapp.models import Basket
from django.conf import settings
from django.utils import timezone


def main(request):
    title = "Главная"
    all_products = Product.objects.all()[:2]
    content = {"title": title, "products": all_products}
    return render(request, "mainapp/index.html", context=content)


def products(request, pk=None):
    title = "Продукты"
    links_menu = ProductCategory.objects.all()
    slider_products = [
        {"img": "prod-2.jpg"},
        {"img": "prod-3.jpg"},
        {"img": "prod-4.jpg"},
    ]
    basket = []
    basket_cnt = 0
    basket_price = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": "все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")

        for bas in basket:
            basket_cnt += bas.quantity
            basket_price += basket_cnt * bas.product.price

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products,
            "basket": basket,
            "basket_cnt": basket_cnt,
            "basket_price": basket_price,
        }
        return render(request, "mainapp/products_list.html", content)

    same_products = Product.objects.all()[:3]

    content = {
        "title": title,
        "slider_products": slider_products,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
    }

    return render(request, "mainapp/products.html", context=content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", context=content)
