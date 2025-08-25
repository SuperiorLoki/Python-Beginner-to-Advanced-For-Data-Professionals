import logging


logging.basicConfig(
    filename="web_app.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

def login(username):
    logging.info(f"User {username} logged in")

def process_data(data):
    try:
        if data == "bad_data":
            raise ValueError("Invalid data")
        logging.info(f"Data processed: {data}")
    except ValueError as e:
        #exc_info will print the error as you see it in the console
        logging.error(f"Error processing data: {e}", exc_info=True)

def logout(username):
    logging.info(f"User {username} logged out")

if __name__ == "__main__":
    user_name = "Hirithik Pranav"
    login(user_name)
    process_data("bad_data")
    logout(user_name)