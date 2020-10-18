from django import forms


class ClothesSearchForm(forms.Form):
    search_word = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': '상품명, 브랜드명, 옷종류 검색'}))
