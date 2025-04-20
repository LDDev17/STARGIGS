

import uuid
from datetime import datetime

def create_review_item(performer_id, client_id, rating, comment, event_type=None):
    return {
        "performer_id": performer_id,
        "review_id": str(uuid.uuid4()),
        "client_id": client_id,
        "rating": rating,
        "comment": comment,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event_type": event_type or "General"
    }
