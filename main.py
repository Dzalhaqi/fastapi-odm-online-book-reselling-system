from fastapi import FastAPI
from api import book, buyer, buyer_async, cart, receipt, order, login, profile, purchase, reference

app = FastAPI()
app.include_router(purchase.router)
app.include_router(buyer.router)
app.include_router(buyer_async.router)
app.include_router(receipt.router)
app.include_router(order.router)
app.include_router(cart.router)
app.include_router(login.router)
app.include_router(profile.router)
app.include_router(book.router)
app.include_router(reference.router)