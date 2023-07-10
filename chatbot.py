import tkinter as tk
import openai
import os

# Apply the API Key from the environment variables
openai_key = os.getenv('OPENAI_KEY')

# Generate a response using OpenAI GPT-3
def generate_response(prompt, character):
    # Adjust the prompt based on the character
    if character == "Doctor":
        prompt = "As a doctor with knowledge in general medicine, " + prompt
    elif character == "Lawyer":
        prompt = "As a lawyer knowledgeable about various legal frameworks, " + prompt
    elif character == "Developer":
        prompt = "As a software developer specializing in Python and web development, " + prompt
    elif character == "Beautician":
        prompt = "As a beautician knowledgeable about skin care and beauty treatments, " + prompt
    elif character == "Writer":
        prompt = "As a writer with a creative and descriptive approach, " + prompt
    elif character == "Philosopher":
        prompt = "As a philosopher specializing in ethics, " + prompt

    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024, ##3
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text.strip()
    return message

# GUI interface
def display_response():
    input_text = input_field.get()
    selected_character = character_variable.get()
    response = generate_response(input_text, selected_character)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("600x700")

# Create the input field
input_field = tk.Entry(root, font=("Arial", 14))
input_field.pack(pady=10)

# Create character selection
character_variable = tk.StringVar(root)
character_variable.set("Doctor") # default value
character_option = tk.OptionMenu(root, character_variable, "Doctor", "Lawyer", "Developer", "Beautician", "Writer", "Philosopher")
character_option.pack(pady=10)

# Create the submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=display_response)
submit_button.pack(pady=10)

# Create the output field
output_field = tk.Text(root, font=("Arial", 14), state='disabled')
output_field.pack(pady=10)

# Start the GUI event loop
root.mainloop()

