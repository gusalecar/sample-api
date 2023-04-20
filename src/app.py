from mangum import Mangum
from litestar import Litestar, get
from litestar.openapi.config import OpenAPIConfig
from pydantic import BaseModel


class Greet(BaseModel):
    message: str


@get("/greet/{name:str}", description="Greets you")
async def greet(name: str) -> Greet:
    return Greet(message=f"Hello {name}")


app = Litestar([greet], openapi_config=OpenAPIConfig(title="API", version="1.0.0"))
handler = Mangum(app, lifespan="off")
