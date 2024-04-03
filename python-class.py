class SelfIntroduction:
  # コンストラクタ生成
  def __init__(self):
    self.company = ""
    self.name = ""
    self.hobby = ""
    self.end = "よろしくお願いします！"
  
  # 自己紹介
  def introduce(self):
    print(f"{self.company}から来ました {self.name} です。",
          f"\n\r趣味は {self.hobby} です。",
          f"\n\r{self.end}"
    )
  

# インスタンス生成
ichiro = SelfIntroduction()
mike = SelfIntroduction()
kevin = SelfIntroduction()

# Ichiro Info
ichiro.company = "日本"
ichiro.name = "一郎"
ichiro.hobby = "けん玉"

# Mike Info
mike.company = "アメリカ"
mike.name = "マイク"
mike.hobby = "野球"

# Kevin Info
kevin.company = "イギリス"
kevin.name = "ケビン"
kevin.hobby = "テニス"


# メソッド実行：Ichiro
ichiro.introduce()
"""出力結果
日本から来ました 一郎 です。
趣味は けん玉 です。
よろしくお願いします！
"""

# メソッド実行：Mike
mike.introduce()
"""出力結果
アメリカから来ました マイク です。
趣味は 野球 です。
よろしくお願いします！
"""

# メソッド実行：Kevin
kevin.introduce()
"""出力結果
イギリスから来ました ケビン です。
趣味は テニス です。
よろしくお願いします！
"""

# 最後の言葉を変える
ichiro.end = "以後お見知りおきを。"
ichiro.introduce()
"""出力結果
日本から来ました 一郎 です。
趣味は けん玉 です。
以後お見知りおきを。
"""
