import ollama

# 1. Configuration
# Note: Ollama manages the model files for us.
# We just need the name of the model we pulled via 'ollama pull phi3'.
model_name = "phi3"

# 2. Conversation State
# Just like the previous example, we maintain a history list to provide context.
messages = [
    {"role": "system", "content": "You are a helpful assistant running via Ollama."}
]

print(f"\n--- Ollama Chat Engine Active (Model: {model_name}) ---")

while True:
    # Capture user input
    user_input = input("\nUser: ")
    if user_input.lower() in ["exit", "quit"]: break

    # Append user message to history
    messages.append({"role": "user", "content": user_input})

    print("Assistant: ", end="", flush=True)

    # 3. Requesting a Streaming Response
    # Instead of managing tensors and devices, we call 'ollama.chat'.
    # 'stream=True' returns an iterable object that yields the response piece by piece.
    full_response = ""
    stream = ollama.chat(
        model=model_name,
        messages=messages,
        stream=True,
    )

    # 4. Processing the Stream
    # We iterate through the 'chunks' sent by the Ollama server.
    for chunk in stream:
        content = chunk['message']['content']
        print(content, end="", flush=True)
        full_response += content

    # 5. History Update
    # We save the complete answer so the model "remembers" it in the next turn.
    messages.append({"role": "assistant", "content": full_response})
    print() # New line for the next turn