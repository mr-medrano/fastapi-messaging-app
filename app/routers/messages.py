from fastapi import APIRouter

router = APIRouter(prefix="/messages", tags=["messages"])


@router.get("")
async def read_messages():
    return [
        {
            "id": 1,
            "from": "john.doe@gmail.com",
            "subject": "Hi!",
            "body": "Just wanted to say hi!",
        }
    ]
