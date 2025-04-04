from fastapi import APIRouter
from api import YacineTV

ytv = YacineTV()
router = APIRouter(tags=["YacineTV"])


@router.get("/categories")
def categories():
    return ytv.get_categories()

@router.get("/categories/{category_id}/channels")
def channels(category_id: int):
    return ytv.get_category_channels(category_id)

@router.get("/channel/{channel_id}")
def channel(channel_id: int):
    return ytv.get_channel(channel_id)

@router.get("/events")
def events():
    return ytv.get_all_events()

@router.get("/event/{event_id}")
def event(event_id: int):
    return ytv.get_event(event_id)

@router.get("/search")
def search(query: str):
    return ytv.search(query)
