
from .models import Car,Auction
from modeltranslation.translator import TranslationOptions,register

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('car','fuel_type','description','transmission')

@register(Auction)
class AuctionTranslationOptions(TranslationOptions):
    fields = ('car','status')