#Write a program to log messages with timestamps and save them to a file

from datetime import datetime

def log_message(message, log_file="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"
    try:
        with open(log_file, "a") as file:
            file.write(log_entry)
        print("Log entry added successfully.")
    except Exception as e:
        print(f"Error logging message: {e}")

# Example usage
log_message("Application started.")
log_message("An error occurred.", "error.log")
log_message("User logged in.", "user_activity.log")