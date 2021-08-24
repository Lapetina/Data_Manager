from fastapi import status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router_data = InferringRouter()


@cbv(router_data)
class DataRouters:
    @router_data.post("/", status_code=status.HTTP_200_OK)
    async def root(self):
        return status.HTTP_200_OK
