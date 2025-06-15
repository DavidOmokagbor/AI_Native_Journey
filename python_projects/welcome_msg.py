import datetime

# --- THIS IS A TEST PRINT TO CONFIRM EXECUTION ---
print("Attempting to run welcome script...")
# -------------------------------------------------

def generate_welcome_message(beatzbyjava, BeatzbyjavaProductions):
    """
    Generates a personalized welcome message for a music producer and audio engineer.

    Args:
        producer_name (str): The name of the music producer/audio engineer.
        studio_name (str): The name of their studio.

    Returns:
        str: The formatted welcome message.
    """
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    message = f"""
{greeting}, {beatzbyjava}!

Welcome back to {BeatzbyjavaProductions}.

As a music producer and audio engineer, you're constantly shaping soundscapes and bringing sonic visions to life. Every fader, knob, and waveform is a tool in your creative arsenal.

Ready to craft some magic today? Let's make some waves!

Best,
Gani 

"""
    return message

if __name__ == "__main__":
    # --- Input from the user for personalization ---
    my_producer_name = input("Enter your producer name or alias: ")
    my_studio_name = input("Enter your studio name: ")
    # -------------------------------------------------------------

    welcome_message = generate_welcome_message(my_producer_name, my_studio_name)
    print(welcome_message)
    print("\nScript finished successfully.") # Added this to confirm end of execution

