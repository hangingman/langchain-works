import click

from mini_qa import vector_db, vector_db_agent


@click.command()
@click.option("--mod", type=str, help='起動するモジュールの切り替え [vector_db, vector_db_agent]')
def cli(mod: str) -> None:
    if mod == "vector_db":
        vector_db.main()
    if mod == "vector_db_agent":
        vector_db_agent.main()


if __name__ == "__main__":  # デバッガでの実行用
    cli()
