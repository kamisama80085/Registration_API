from fastapi import FastAPI
from route import auth 
app = FastAPI()

app.include_router(auth.router, prefix="/auth")
# app.include_router(chain_delete.router, prefix="/link")
# app.include_router(joins.router, prefix="/joins")
# app.include_router(link_id.router, prefix="/delete")
#abe bc isme same line q dikha raha hai yeah baar baar 
#aut#to main kya urdu bhasha m keh raha hui :_:
#pc restart karke dekhoon?
#bc restsart hi karke dekh 
