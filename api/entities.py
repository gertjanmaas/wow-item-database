import enum

from app import db

class ItemQuality(str, enum.Enum):
    LEGENDARY = "Legendary"
    EPIC = "Epic"
    RARE = "Rare"
    UNCOMMON = "Uncommon"
    COMMON = "Common"
    JUNK = "Junk"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    quality = db.Column(db.Enum(ItemQuality))
    icon = db.Column(db.String(50))

    def __init__(self,id=None, name=None, quality=None, icon=None):
        self.id = id
        self.name = name
        self.quality = quality
        self.icon = icon

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quality': self.quality,
            'icon': f"/static/icons/{self.icon}.jpg"
        }
