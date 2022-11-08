from pydantic import BaseModel

class filter(BaseModel):
    orderBy:str
    order:str
    filter:list

    class Config:
        schema_extra = {
            "example": {
              "orderBy": "",
              "order": "",
              "filter": [{"value": "value", "field":"field"}],
            }
        }


