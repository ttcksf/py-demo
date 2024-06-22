import random

words = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
    "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
    "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
    "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
    "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla",
    "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
    "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id",
    "est", "laborum"
]

def generate_text(num, per):
    paragraphs = []

    for _ in range(num):
        # perの数だけランダムにピックアップする
        paragraph = " ".join(random.choices(words, k=per))
        paragraphs.append(paragraph)

    return "\n\n".join(paragraphs)


dummy_text = generate_text(3, 100)
    
with open('test.txt', 'w') as file:
  file.write(dummy_text)
