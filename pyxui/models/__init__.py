from pydantic import BaseModel, Field
from typing import List


class Model(BaseModel):
    class Config:
        populate_by_name = True

class Client(Model):
    id: str
    email: str
    enable: bool
    expire_time: int = Field(alias="expiryTime")
    flow: int
    limit_ip: int
    reset: int
    sub_id: str = Field(alias="subId")
    tg_id: str = Field(alias="tgId")
    total_gb: int = Field(alias="totalGB")
    
class ClientStats(Model):
    id: int
    inbound_id: int = Field(alias="inboundId")
    enable: bool
    email: str
    up: int
    down: int
    expire_time: int= Field(alias="expiryTime")
    total: int
    reset: int
   
class Settings(Model):  
    clients: List[Client]
    description: str
    fallbacks: list
    
class Inbound(Model):
    id: int
    up: int
    down: int
    total: int
    remark: str
    enable: bool
    expire_time: int = Field(alias="expiryTime")
    client_stats: ClientStats = Field(alias="clientStats")
    listen: str
    port: int
    protocol: str
    settings: Settings
    stream_settings: dict = Field(alias="streamSettings")
    tag: str
    sniffing: str
    allocate: dict

class InboundResponse(Model):
    success: bool
    msg: str
    obj: List[Inbound]