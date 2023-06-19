"""Main module."""
import openai
import click

"""
openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role" : "user", "content" : "Write an essay about penguins"}])
print(completion.choices[0].message.content)
"""

def messenger(msg,files):
    """Console script for buddygpt."""
    click.echo(f"Your message to ChatGPT is: {msg}")
    click.echo(f"Files are: {files}")
    return 0