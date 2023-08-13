from beanie import Document
from typing import TypedDict

class EventsParticipantsSchema(Document):
    participant_id : str
    event_id : str
    details: dict # just match the keys of the list of field details and details