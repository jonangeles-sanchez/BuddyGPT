"""Console script for buddygpt."""
import sys
import click



@click.command()
@click.option("-m", "--msg", prompt="Your message to ChatGPT", help="Your message to ChatGPT")
@click.argument("files", nargs=-1, type=click.Path(exists=True), required=0)
def ask_chatGPT(msg, files):
    """Console script for buddygpt."""
    click.echo(f"Your message to ChatGPT is: {msg}")
    click.echo(f"Files are: {files}")
    return 0


if __name__ == "__main__":
    sys.exit(ask_chatGPT())  # pragma: no cover
