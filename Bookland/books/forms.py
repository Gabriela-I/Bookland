from django import forms

from Bookland.books.models import Book, BookComment, Purchase

choice_list = [
    ('', '------'),
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
    category = forms.ChoiceField(choices=choice_list, required=True)
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, required=True)

    class Meta:
        model = Book
        exclude = ('user', 'upload_date',)
        widgets = {
            'description': forms.Textarea(attrs={
                'cols': 50,
                'rows': 10,
                'style': 'resize: vertical; height: 100px; '
                         'background-color: rgb(227, 206, 206);'
                         'border: 1px solid black;',
            }),
        }


class BuyBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'condition', 'price',)
        widgets = {
            'book_photo': forms.FileInput(attrs={
                'class': 'image-wrap',
            }),
            'price': forms.NumberInput(attrs={
                'step': '0.01',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['condition'].disabled = True
        self.fields['price'].widget.format_value = self.format_price_value
        self.fields['price'].disabled = True

    def format_price_value(self, value):
        return f'{value:.2f}' if value is not None else ''


class PurchaseForm(forms.ModelForm):
    DELIVERY_METHODS = (
        ('', '------'),
        ('FedEx', 'FedEx'),
        ('DHL', 'DHL'),
        ('UPS', 'UPS'),
    )

    PAYMENT_METHODS = (
        ('', '------'),
        ('Cash on Delivery', 'Cash on Delivery'),
    )
    delivery_method = forms.ChoiceField(choices=DELIVERY_METHODS, required=True)
    payment_method = forms.ChoiceField(choices=PAYMENT_METHODS, required=True)

    class Meta:
        model = Purchase
        fields = (
        'first_name', 'last_name', 'phone_number', 'address_for_delivery', 'delivery_method', 'payment_method')
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'phone_number': 'Phone Number:',
            'address_for_delivery': 'Shipping Address:',
            'delivery_method': 'Delivery Method',
            'payment_method': 'Payment Method',
        }


class BookEditForm(forms.ModelForm):
    category = forms.ChoiceField(choices=choice_list, required=True)

    class Meta:
        model = Book
        fields = ('book_photo', 'title', 'author', 'publisher', 'description', 'category', 'condition', 'price',)
        widgets = {
            'book_photo': forms.FileInput(attrs={

            }),
            'price': forms.NumberInput(attrs={
                'step': '0.01',
                'style': 'color: rgb(200 154 154)',
            }),
            'description': forms.Textarea(attrs={
                'cols': 50,
                'rows': 10,
                'style': 'resize: vertical; height: 100px; '
                         'background-color: rgb(227, 206, 206);'
                         'border: 1px solid black;',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.format_value = self.format_price_value

    def format_price_value(self, value):
        return f'{value:.2f}' if value is not None else ''

    def save(self, commit=True):
        book = super().save(commit=False)

        new_book_photo = self.cleaned_data.get('book_photo', None)
        if new_book_photo:
            book.book_photo = new_book_photo

        if commit:
            book.save()

        return book


class BookDeleteForm(BookEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class BookCommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...', 'color: dimgray;'
                                                     'cols': 70,
                    'rows': 3,
                }
            ),
        }
