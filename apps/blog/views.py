# blog/views.py
from django.shortcuts import render

def home(request):
    # 1) Сообщение после отправки формы (без forms.py)
    message = None
    if request.method == "POST":
        # забираем поля из формы (для примера — имя и отзыв)
        name = request.POST.get("name", "")
        feedback = request.POST.get("feedback", "")
        # тут можно что-то сделать с данными (сохранить в БД и т.д.)
        message = "Спасибо за отзыв!"

    # 2) Список товаров
    products = [
        {"name": "Телефон", "price": 10000},
        {"name": "Ноутбук", "price": 50000},
        {"name": "Наушники", "price": 2000},
    ]

    # 3) Оценка (можно передать через ?score=85 в URL для проверки)
    score_default = 83
    try:
        score = int(request.GET.get("score", score_default))
    except (TypeError, ValueError):
        score = score_default

    context = {
        "message": message,
        "products": products,
        "score": score,
    }
    return render(request, "blog/home.html", context)


def profile(request):
    # 4) Данные пользователя
    context = {
        "username": "ivan",
        "email": "ivan@example.com",
        "is_active": True,   # Поменяй на False, чтобы увидеть другое сообщение
    }
    return render(request, "blog/profile.html", context)


# Create your views here.
