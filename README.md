# get-connpass-participants

## About

Connpassのイベントから参加者をマークダウンのリスト形式で取得するスクリプトです。

## 使い方

### コンテナを起動

```bash
$ docker-compose up -d --build
```

### コンテナへ接続

```bash
$ docker-compose exec python3 bash
```

### 実行

```bash
$ python opt/get-participants.py <コンパスのイベントページURL>
```

### コンテナの削除

```bash
$ docker-compose down
```

## 例

```bash
$ python opt/get-participants.py https://phper-oop.connpass.com/event/171008/
```

### 出力結果

```md
## 参加者

### 現地参加する人

- [ ] philomagi
- [ ] soonoki
- [ ] yapto6412
- [ ] ikkun
- [ ] stmtk

### オンライン参加する人

- [ ] 脱脂綿
- [ ] deniyung
- [ ] idani
- [ ] nunulk

### 開催する人

- [ ] hirodragon
- [ ] ucan-lab

### ブログ書く人（じゅり）

- [ ] juriful
```
