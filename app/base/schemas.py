from pydantic import BaseModel, ConfigDict

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

# схема для чтения / возврата
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    
# схема для чтения / возврата
class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True

#UserWarning: действительные ключи конфигурации были изменены в V2: 
#* «orm_mode» переименован в «from_attributes» alerts.warn(message, UserWarning)