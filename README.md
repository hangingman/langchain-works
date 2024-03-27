# langchain-works

## mini_qa

- 初回の仮想環境構築
- python 3.11.2でテストした

```shell
$ /usr/bin/python3.11 -V
Python 3.11.2
$ /usr/bin/python3.11 -m venv .venv --prompt MiniQA
$ source .venv/bin/activate
```

必要に応じて下記コマンドを実行

```shell
$ make pin
$ make install-dev
$ make lint
$ make format
$ make test
$ mini_qa --arg world  # cli 動作チェック
hello, world!!!
```