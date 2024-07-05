pip install transformers torch
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
 
# Load pre-trained model and tokenizer
model_name = "distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Ensure the model is set to evaluation mode
model.eval()

# If you have a GPU, uncomment the following line
# model.to('cuda')
def generate_response(prompt, model, tokenizer, max_length=150):
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # If you have a GPU, uncomment the following line
    # inputs = inputs.to('cuda')

    with torch.no_grad():
        outputs = model.generate(inputs, max_length=max_length, pad_token_id=tokenizer.eos_token_id, num_return_sequences=1)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
def chatbot():
    print("Chatbot: Hello! I'm an AI chatbot. Type 'exit' to end the conversation.")
    
    conversation_history = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        conversation_history += f"User: {user_input}\nChatbot: "
        prompt = conversation_history

        response = generate_response(prompt, model, tokenizer)
        
        # Extract the response part that the chatbot should say
        response = response[len(prompt):].strip()
        
        print(f"Chatbot: {response}")
        
        conversation_history += f"{response}\n"

# Start the chatbot
if _name_ == "_main_":
    chatbot()