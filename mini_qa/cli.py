import click

from mini_qa import vector_db


@click.command()
@click.option("--arg", type=str)
def cli(arg: str) -> None:
    vector_db.main()


if __name__ == "__main__":  # デバッガでの実行用
    cli()
