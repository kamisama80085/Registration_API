from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.link_id import router as link_id_router
from routes.joins import router as joins_router
from routes.chain_delete import router as chain_delete_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(link_id_router, prefix="/link")
app.include_router(joins_router, prefix="/joins")
app.include_router(chain_delete_router, prefix="/delete")
