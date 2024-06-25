# 数値の文字列への変換
test = 100
# シンプルな例だと同じ結果になる
print(str(test))
print(repr(test))

import datetime
today = datetime.datetime.now()
# 画面に表示するときなどに使う（データを読みやすく表現している）
print(str(today))
# 開発時のデータの詳細情報を確認するときに使う（公式フォーマットなど）
print(repr(today))
  