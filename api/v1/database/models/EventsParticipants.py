from beanie import Document
from typing import TypedDict

class EventsParticipants(Document):
    participant_id : str
    event_id : str
    details: dict # just match the keys of the list of field details and details