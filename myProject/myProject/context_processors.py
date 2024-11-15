from order.models import AddFavourite


def favori_check(request):
    if request.user.is_authenticated:
        request.session['favori_items'] = (AddFavourite.objects.filter(user_id = request.user.id).count())
        return {'favori_itemss': request.session['favori_items']}
    else:
        request.session['favori_items'] = 0
        return {'favori_itemss': request.session['favori_items']}