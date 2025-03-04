import ollama
import base64
import os

print(' ' * 20 + '--Starting the OCR--' + ' ' * 20)

# Ensure OCR directory exists
ocr_output_dir = './OCR'
os.makedirs(ocr_output_dir, exist_ok=True)


# Convert image to base64
image_path = './images.jpg'
with open(image_path, 'rb') as img_file:
    image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# Call Ollama for OCR processing
response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': '''Please look at this image and extract all the text content. 
        Format the output properly based on the specified mode:
        
        - **Plain text**: Maintain the original layout and line breaks.
        - **Structured**: Extract tables, lists, and preserve relationships.
        - **Key-Value**: Identify and format paired data like 'key: value'.
        ''',
        'images': [image_base64]  
    }]
)

ocr_output_path = os.path.join(ocr_output_dir, 'ocr_output.txt')
with open(ocr_output_path, 'w', encoding='utf-8') as file:
    file.write(response['message']['content'])

print(type(response)) # <class 'ollama._types.ChatResponse'>
print(' ' * 20 + '--Ending the OCR--' + ' ' * 20)
