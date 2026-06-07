import logging

#Setting Up Basic Configuration For Logging
logging.basicConfig(
    filename="project.log",
    level=logging.DEBUG,
    format="%(asctime)s -  %(levelname)s - %(name)s -  %(message)s"
    )


