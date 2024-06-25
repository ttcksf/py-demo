users = ["yamada","tanaka","yoshida"]
# print(users)
# users.append("suzuki")
# print(users)

members = ["takahashi","suzuki","sato"]
# users.append(members)
# appendではリストは一つの要素として扱われるのでextendの方が良い
# print(users)
# extendでは分解されて扱われる
users.extend(members)
print(users)
# 単体データは文字ごとに分解してしまうのでappendの方が良い
# users.extend("takahashi")
# print(users)
