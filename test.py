import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': '''Please look at this image and extract all the text content. 
        Format the output properly based on the specified mode:
        
        - **Markdown**: Use headers, bullet points, and proper formatting.
        - **Plain text**: Maintain the original layout and line breaks.
        - **JSON**: Structure the text hierarchically with appropriate keys.
        - **Structured**: Extract tables, lists, and preserve relationships.
        - **Key-Value**: Identify and format paired data like 'key: value'.
        ''',
        'images': ['./img.png']
    }]
)

print(response.content)
