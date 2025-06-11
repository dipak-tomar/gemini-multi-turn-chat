# Advanced Gemini Console Chat

This project provides a simple yet powerful, context-aware chatbot that runs in your terminal. It uses the Google Gemini API to hold a continuous conversation, remembering the context from previous turns.

This script is an interactive demonstration of the Gemini API's chat capabilities, with added features for a better user experience.

## Features
- **Continuous Conversation:** Engage in a multi-turn chat session that continues until you explicitly decide to exit.
- **Context-Aware:** The chatbot remembers the entire conversation history, allowing for natural follow-up questions.
- **Configurable Creativity:** Before the chat begins, you can set the model's temperature parameter to control the randomness and creativity of the responses.
- **Secure API Key Handling:** It uses a `.env` file to load your `GOOGLE_API_KEY` securely, so you don't have to expose it in the code or manually set it in your terminal each time.
- **Simple Exit:** Easily end the conversation at any time by typing `exit`.

## Requirements
All Python package dependencies are listed in the `requirements.txt` file.
- `google-generativeai`: The official Google Python SDK for the Gemini API.
- `python-dotenv`: To load the API key from a `.env` file.

## Setup Instructions
Follow these steps to get the chatbot running on your local machine.

### 1. Clone the Repository
First, clone the project to your local machine (if you haven't already).
```bash
git clone https://github.com/your-username/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat
```

### 2. Create the .env File
This is the most important step for connecting to the API. Create a file named `.env` in the root of the project directory. Add your API key to this file as follows:
```env
# .env
GOOGLE_API_KEY="your_actual_api_key_goes_here"
```
*Note: The `.gitignore` file is already configured to prevent this file from being committed to GitHub.*

### 3. Install Dependencies
Install all the required Python libraries using the `requirements.txt` file. It's recommended to do this within a virtual environment.
```bash
pip install -r requirements.txt
```

## How to Run the Script
With your `.env` file in place and dependencies installed, simply run the Python script from your terminal:
```bash
python app.py
```
The script will first ask you to set a temperature, and then you can begin the conversation.

## Example Session
Here is an example of what a session with the chatbot might look like:
```bash
$ python app.py
Gemini Chat Initialized.
=========================
Set model temperature (e.g., 0.8): 0.9
You (turn 1, type 'exit' to quit): What are the top three most populated countries in the world?

--- Gemini's Response (turn 1) ---
As of my last update, the three most populated countries in the world are:
1. India
2. China
3. The United States

You (turn 2, type 'exit' to quit): What is the official language of the first one?

--- Gemini's Response (turn 2) ---
The official language of India is Hindi, with English also having the status of a subsidiary official language. However, India has 22 other scheduled languages recognized at the state level and hundreds of other languages spoken across the country.

You (turn 3, type 'exit' to quit): exit

Conversation ended.
```