from django import forms

from Bookland.books.models import Book, Category


choice_list = [
    ('Romance', 'Romance'),
    ('Fantasy', 'Fantasy'),
    ('Criminal', 'Criminal'),
    ('Historical novel', 'Historical novel'),
    ('Thriller', 'Thriller'),
    ('Science fiction', 'Science fiction'),
    ('Poetry', 'Poetry'),
    ('Biography/autobiography', 'Biography/autobiography'),
    ('Health', 'Health'),
    ('Psychology', 'Psychology'),
    ('Esoteric', 'Esoteric'),
    ('Home, Family, Hobby', 'Home, Family, Hobby'),
    ("Children's literature", "Children's literature"),
    ('Other', 'Other'),
]


CONDITION_CHOICES = [
    ('', '------'),
    ('Perfect', 'Perfect'),
    ('Good', 'Good'),
    ('Not very good', 'Not very good'),
]


class BookAddForm(forms.ModelForm):
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, required=True)

    class Meta:
        model = Book
        exclude = ('user','upload_date',)
        widgets = {
            'category': forms.Select(choices=choice_list),
            'description': forms.Textarea,
        }

    # CATEGORIES = (
    #     ('Romance', 'Romance'),
    #     ('Fantasy', 'Fantasy'),
    #     ('Criminal', 'Criminal'),
    #     ('Historical novel', 'Historical novel'),
    #     ('Thriller', 'Thriller'),
    #     ('Science fiction', 'Science fiction'),
    #     ('Poetry', 'Poetry'),
    #     ('Biography/autobiography', 'Biography/autobiography'),
    #     ('Health', 'Health'),
    #     ('Psychology', 'Psychology'),
    #     ('Esoteric', 'Esoteric'),
    #     ('Home, Family, Hobby', 'Home, Family, Hobby'),
    #     ("Children's literature", "Children's literature"),
    #     ('Other', 'Other'),
    # )

    # category = forms.ChoiceField(choices=CATEGORIES)


class BuyBookForm(forms.ModelForm):
    DELIVERY_METHODS = (
        ('FedEx', 'FedEx'),
        ('DHL', 'DHL'),
        ('UPS', 'UPS'),
    )

    PAYMENT_METHODS = (
        ('Bank payment', 'Bank payment'),
        ('Direct debit - VISA, MasterCard', 'Direct debit - VISA, MasterCard'),
    )

    class Meta:
        model = Book
        fields = ('title', 'condition', 'price',)
        widgets = {
            'book_photo': forms.FileInput(attrs={
                'class': 'image-wrap',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['book_photo'].disabled = True
        self.fields['title'].disabled = True
        self.fields['condition'].disabled = True
        self.fields['price'].disabled = True

    first_name = forms.CharField(
        max_length=50,
        required=True,
        label='Fisrt name',
    )

    last_name = forms.CharField(
        max_length=50,
        required=True,
        label='Last name',
    )

    phone_number = forms.IntegerField(
        required=True,
        label='Phone number',
    )

    address_for_delivery = forms.CharField(
        max_length=150,
        required=True,
        label='Shipping address',
    )

    delivery_method = forms.ChoiceField(
        choices=DELIVERY_METHODS,
        label='Delivery method',
        widget=forms.RadioSelect(
            attrs={
                'class': 'methods',
            }
        ),
    )

    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHODS,
        label='Payment method',
        widget=forms.RadioSelect(
            attrs={
                'class': 'methods',
            },
        ),
    )
