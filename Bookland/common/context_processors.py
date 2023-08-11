def dropdown_categories(request):
    cat_menu = [
        'Romance', 'Fantasy', 'Criminal',
        'Historical novel', 'Thriller', 'Science fiction',
        'Poetry', 'Health',
        'Psychology', 'Esoteric', 'Home, Family, Hobby',
        'Children\'s literature', 'Other',
    ]
    return {'cat_menu': cat_menu}