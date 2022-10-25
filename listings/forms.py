from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "price", "num_bedrooms",
                  "num_bathrooms", "square_footage", "address", "image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        styling = {
            "class": "rounded-md p-1 border border-gray-200 flex-1"
        }
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(styling)
