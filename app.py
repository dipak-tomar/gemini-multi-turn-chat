import os
import google.generativeai as genai
from dotenv import load_dotenv  

def main():
    """
    A simple, context-aware, multi-turn console chatbot using the Gemini API.
    """

    load_dotenv() 


    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please create a .env file with GOOGLE_API_KEY=\"your_api_key\"")

    genai.configure(api_key=api_key)

    
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    
    print("Gemini Chat Initialized.")
    print("=========================")

    # Ask user for temperature
    try:
        temperature = float(input("Set model temperature (e.g., 0.8): "))
    except ValueError:
        print("Invalid input. Using default temperature 0.8.")
        temperature = 0.8
    generation_config = genai.types.GenerationConfig(temperature=temperature)

    conversation_active = True
    turn = 1
    while conversation_active:
        user_input = input(f"You (turn {turn}, type 'exit' to quit): ")
        if user_input.strip().lower() == 'exit':
            conversation_active = False
            break
        response = chat.send_message(user_input, generation_config=generation_config)
        print(f"\n--- Gemini's Response (turn {turn}) ---\n{response.text}\n")
        turn += 1
    print("\nConversation ended.")


if __name__ == "__main__":
    main()