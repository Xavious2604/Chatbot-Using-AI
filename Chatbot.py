import openai
import gradio as gr

# Set your OpenAI API key here
openai.api_key = 'sk-None-gcIOiMj81U8C4T65KoqHT3BlbkFJWlHA84EbDGVkJsauHGhX'

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)

iface = gr.Interface(
    fn=chat_with_gpt,
    inputs=gr.Textbox(lines=7, label="Enter your text here"),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Healthcare Chatbot",
    description="A simple chatbot using OpenAI's GPT-4 and Gradio",
)

if __name__ == "__main__":
    iface.launch()
