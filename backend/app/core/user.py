from app.data.models import User


async def registrate_user(email: str, hashed_password):
    
    user = User(
        email=email,
        password=hashed_password
    )
    await user.create()
    return user

async def find_user(email: str):
    
    user = await User.find_one(User.email == email)
    return user