from random import choice

def get_bot_response(user_message: str) -> str:
    lowered: str = user_message.lower()
    
    return choice(["SIR, YES SIR!", "AFFIRMATIVE!", "SIR!", "ADMIRAL ON DECK!", "THE ADMIRAL HAS SPOKEN!", "FOR THE SPACE FEDERATION!"])