from scrapy.item import Item, Field


class faculty_contact(Item):
    name = Field()
    department = Field()
    title = Field()
    email = Field()
    phone = Field()
    building = Field()
    room = Field()
    campus = Field()
