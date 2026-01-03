from optimum.intel import OVModelForCausalLM
from transformers import AutoTokenizer, TextStreamer
import torch

# Model Configuration
# We use a pre-optimized OpenVINO version of the Phi-3 model.
# INT4 quantization is used to reduce memory footprint and increase throughput.
model_id = "OpenVINO/Phi-3-mini-4k-instruct-int4-ov"

# Tokenizer Initialization
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Model Loading & Hardware Selection
# 'export=False' indicates the model is already in OpenVINO IR format.
# 'device="GPU"' offloads mathematical operations to the hardware accelerator.
# 'compile=True' optimizes the execution graph for the specific hardware target.
model = OVModelForCausalLM.from_pretrained(
    model_id,
    export=False,
    device="CPU",
    compile=True
)

# Streamer Implementation
# A streamer allows for real-time output by decoding tokens as they are generated,
# rather than waiting for the entire sequence to complete.
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

# Conversation State Management
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

print("\n--- Local AI Chatbot is Active ---")

while True:
    # Capture user input
    user_input = input("\nUser: ")
    if user_input.lower() in ["exit", "quit"]: break

    # Update conversation history with user prompt
    messages.append({"role": "user", "content": user_input})

    # Prompt Engineering & Template Application
    # Formats the message list into a specific string structure required by the model.
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # Encode the text into tensors on the CPU (the model handles the transfer to GPU).
    inputs = tokenizer(prompt, return_tensors="pt")

    print("Assistant: ", end="", flush=True)

    # Autoregressive Generation
    # The model predicts the next token in the sequence until an EOS (End of String) is reached.
    output_tokens = model.generate(
        **inputs,
        streamer=streamer,
        max_new_tokens=512,
        temperature=0.7,
        do_sample=True
    )

    # Post-Processing & History Update
    # Decode only the generated response to maintain a clean conversation log.
    full_response = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    ai_only = full_response.split("assistant")[-1].strip()
    messages.append({"role": "assistant", "content": ai_only})