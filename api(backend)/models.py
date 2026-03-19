from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    query : str
    u_id  : str
    timestamp : datetime
    token :str

