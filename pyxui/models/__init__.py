from pydantic import BaseModel, Field

class Model(BaseModel):
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

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
   
class Settings:  
    clients: list[Client]
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
    obj: list[Inbound]