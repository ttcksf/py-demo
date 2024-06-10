# クラス
# 変数や関数を保管できるコード
class Test:
  test_var = "hello"
  test_list = [1,2,3]
  # 関数を作成するときは第一引数にselfを設定する
  def test_func(self,a,b):
    print(a + b)

# クラスはインスタンス化することで中のコードにアクセスできる(無限に複製できる。)
test = Test()
print(test.test_func(1,2))

inst = Test()
print(inst.test_func(2,4))
