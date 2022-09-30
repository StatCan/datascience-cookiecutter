import typer

app = typer.Typer()


@app.command()
def cli():
    print("Hello, data science.")


if __name__ == "__main__":
    app()
