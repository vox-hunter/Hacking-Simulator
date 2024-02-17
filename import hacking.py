import time

def loading_bar(duration, message):
    print(message)
    for i in range(duration):
        print("#", end="", flush=True)
        time.sleep(0.1)
    print("\n")

def simulate_hack():
    print("Hacker Tool v1.0")
    username = input("Enter the any social media username to hack: ")
    time.sleep(1)
    print(f"Target: {username}")
    loading_bar(10, "Connecting to Snapchat servers...")
    loading_bar(10, "Connecting to Instagram servers...")
    loading_bar(10, "Connecting to Facebook servers...")
    loading_bar(10, "Connecting to Tiktok servers...")
    loading_bar(10, "Connecting to Twitter servers...")
    loading_bar(10, "Connecting to Youtube servers...")
    loading_bar(10, "Connecting to Discord servers...")
    loading_bar(10, "Connecting to Spotify servers...")

    print("Searching for user...")
    loading_bar(5, f"Locating {username}...")

    # Always finds the user
    user_found = True

    if user_found:
        loading_bar(15, "Accessing account...")
        print("Access Granted.\nInjecting custom script...")
        loading_bar(20, "Script Injection Complete.")

        while True:
            action = input("Enter command (delete/ban/send_message/exit): ").lower()
            if action == "delete":
                loading_bar(10, "Executing account deletion sequence...")
                print("Account deleted.")
                break
            elif action == "ban":
                loading_bar(10, "Initiating ban protocol...")
                loading_bar(10, "Decrypting security protocols...")
                loading_bar(10, "Engaging cyber stealth mode...")
                loading_bar(10, "Compromising account defenses...")
                loading_bar(10, "Launching digital offensive...")
                loading_bar(10, "Infiltrating data streams...")
                loading_bar(10, "Bypassing firewall barriers...")
                loading_bar(10, "Activating shadow network...")
                loading_bar(10, "Executing ghost protocol...")
                loading_bar(10, "Overriding user permissions...")
                loading_bar(10, "Harnessing dark web resources...")

                
                print("Account banned.")
                break
            elif action == "send_message":
                message = input("Enter your message: ")
                loading_bar(10, "Sending encrypted message...")
                print(f"Message '{message}' sent.")
            elif action == "exit":
                print("Exiting...")
                break
            else:
                print("Invalid command.")
    else:
        print(f"User {username} not found.")

simulate_hack()
