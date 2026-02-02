import gradio as gr
from huggingface_hub import HfFolder

def add_numbers(Num1, Num2):
    return Num1 + Num2

# Define the interface
demo = gr.Interface(
    fn=add_numbers, 
    inputs=[gr.Number(), gr.Number()], # Create two numerical input fields where users can enter numbers
    outputs=gr.Number() # Create numerical output fields
)

def add_strings(str1, str2):
    return str1 + " " + str2

demo_2 = gr.Interface(
    fn=add_strings, 
    inputs=[gr.Textbox(label = "Enter first string"), 
            gr.Textbox(label="Enter second string")
    ], # Create two text input fields where users can enter sentences
    outputs=gr.Textbox(label ="output") # Create numerical output fields
)

# Launch the interface
demo_2.launch(server_name="127.0.0.1", server_port= 7860)