class Test:
  def __init__(self):
    print("初期設定です")
  
  def test_func(self,a,b):
    print(a + b)

test = Test()
# コンストラクターは設定すると自動的に必ず最初に実行される関数
test.test_func(1,2)

# クラスは継承できる
class Hoge(Test):
  # 継承した時のコンストラクターにはsuper関数を書くルール
  def __init__(self):
    super().__init__()
  hoge_var = "hogehoge"

hoge = Hoge()
# コンストラクターを含めてTestの関数を借りることができる
hoge.test_func(1,2)
# 独自のデータにもアクセスできる
print(hoge.hoge_var)
