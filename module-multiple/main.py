# import lib
# 関数名やクラス名をインポート文に含めるとライブラリ名を省略できる
from lib import calc, Test

# lib.calc(1,2)
calc(1,2)

# test = lib.Test()
test = Test()
print(test.test_var)
test.test_func()

