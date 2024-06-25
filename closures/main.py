def outer_func():
  text ="hello"

  def inner_func():
    print(text)
  # inner_func()
  return inner_func

# outer_func()
# クロージャーとは入れ子関数のこと（ここでは関数が再代入さらたvarのこと）
var = outer_func()
print(var)
print(var.__name__)
# 外側の関数（outer_func）がすでに呼び出されて実行が完了していても、内側で呼び出されるはずだったクロージャーは戻り値になったので外側の関数なしで単体で実行可能になる
var()
