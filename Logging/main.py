import logging

#The level indicates what messages should show so with INFO, debug won't show because debug is the lowest level
#On the other hand, critical would only show critical errors because that is the highest level

#Coders typically file the logging into a file with timestamps and stuff
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


#Types of logging messages
logging.info("this is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")





