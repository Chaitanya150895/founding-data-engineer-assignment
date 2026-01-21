from utils.logger import logger

def check_embedding(embedding):
    if not embedding or len(embedding) == 0:
        logger.warning("⚠️ Empty embedding detected!")

def check_relationship(user, campaign):
    if not user or not campaign:
        logger.warning("⚠️ Missing user-campaign relationship!")
