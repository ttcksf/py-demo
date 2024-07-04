# デコレーターは関数を拡張する機能

def add_hello(func):
  def func_wrapper():
    print("こんにちは")
    func()
    print("こんにちは")
  return func_wrapper

@add_hello
def hello():
  print("おはよう")

hello()
