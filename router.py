def route_input(text):
    text = text.lower()

    if any(w in text for w in ["sad", "upset", "anxious", "panic", "overwhelmed", "stress"]):
        return "emotional"

    if any(w in text for w in ["study", "exam", "assignment", "deadline", "timetable"]):
        return "academic"

    if any(w in text for w in ["decide", "decision", "option", "confused"]):
        return "decision"

    if any(w in text for w in ["focus", "productive", "motivation", "lazy"]):
        return "productivity"

    if any(w in text for w in ["friend", "talk", "social", "roommate"]):
        return "social"

    if any(w in text for w in ["journal", "reflect", "today i"]):
        return "reflection"

    return "general"

