# from fastapi import FastAPI
# from routes import auth , chain_delete , joins,link_id

# # from routes.auth import router as auth_router
# # from routes.link_id import router as link_id_router
# # from routes.joins import router as joins_router
# # from routes.chain_delete import router as chain_delete_router

# app = FastAPI()

# app.include_router(auth.router, prefix="/auth")
# app.include_router(link_id.router, prefix="/link")
# app.include_router(joins.router, prefix="/joins")
# app.include_router(chain_delete.router, prefix="/delete")
from fastapi import FastAPI
from routes import auth , chain_delete , joins,link_id
app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(chain_delete.router, prefix="/link")
app.include_router(joins.router, prefix="/joins")
app.include_router(link_id.router, prefix="/delete")
