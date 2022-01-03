import os
# Discord Role ID's
ROLE1_ID = int(os.getenv("ROLE1_ID"))
ROLE2_ID = int(os.getenv("ROLE2_ID"))
ROLE3_ID = int(os.getenv("ROLE3_ID"))

BOT_NAME = os.getenv("BOT_NAME")






def custom_id(view: str, id: int) -> str:
    """create a custom id from the bot name : the view : the identifier"""
    return f"{BOT_NAME}:{view}:{id}"