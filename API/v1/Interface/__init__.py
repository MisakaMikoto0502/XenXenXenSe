from pydantic import BaseModel


class VCpuArgs(BaseModel):
    vCPU_count: int


class MemoryArgs(BaseModel):
    memory: int


class NameArgs(BaseModel):
    name: str


class DescriptionArgs(BaseModel):
    description: str


class UUIDArgs(BaseModel):
    uuid: str
