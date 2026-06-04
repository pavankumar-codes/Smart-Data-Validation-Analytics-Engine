import logging

#Setting Up Basic Configuration For Logging
logging.basicConfig(
    filename="project.log",
    level=logging.DEBUG,
    format="%(asctime)s -  %(levelname)s - %(name)s -  %(message)s"
    )

#Create A logging object so we can reuse it in other files
logger = logging.getLogger(__name__)

