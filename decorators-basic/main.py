# デコレーターは拡張したい関数（下にある関数）を引数にとる
def cough_dec(func):
  # 引数にとった拡張される関数を呼び出す関数
  def func_wrapper():
    print("こんにちは")
    func()
    print("こんにちは")
  return func_wrapper

@cough_dec
def question():
  print("おはよう")

# デコレーターはDjangoやFlaskなどフレームワークで使用される拡張機能
# デコレーターをつけなければ通常の関数として使用されるだけ
# def question():
#   print("おはよう")

question()
