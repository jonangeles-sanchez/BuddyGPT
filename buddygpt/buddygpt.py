"""Main module."""
import openai
import click

"""

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role" : "user", "content" : "Write an essay about penguins"}])
print(completion.choices[0].message.content)
"""

def messenger(msg,files):
    """Console script for buddygpt."""
    connect_to_chatGPT(msg, files)
    
    return 0

def connect_to_chatGPT(msg, files):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[structure_message(msg, files)])
    print_message(completion)

def extract_file_content(files):
    file_contents = []
    for file in files:
        with open(file, "r") as f:
            file_contents.append({"name" : file, "content" : f.read()})
    return file_contents