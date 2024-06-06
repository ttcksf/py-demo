class Test:
  # 変数や関数などいろんな種類のコードを保管できる
  test_var = "hello"
  test_list = [1,2,3]

  # 関数には引数にselfが必要
  def test_func(self, a, b):
    print(a + b)
    # selfはクラス自身のこと
    print(self.test_var)

# インスタンス化して初めて使える
test = Test()
print(test.test_var)
print(test.test_list)
test.test_func(1,2)

# 関数と違って違う名前で複製することが可能
# inst = Test()
# print(inst.test_var)
