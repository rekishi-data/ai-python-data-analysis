# ===== ① ライブラリのインストール =====
# Colab にはじめから入っていないライブラリだけを入れる（! はコマンドの実行）
# !pip install japanize-matplotlib   ← 今回は不要なので、行頭の # でコメントにしている

# ===== ② ライブラリの読み込み =====
import pandas as pd
import matplotlib.pyplot as plt

# ===== ③ 設定（変数の定義） =====
DATA_FILE = "sales_data.csv"          # 読み込むファイル
UNIT = 10000                          # 金額を万円で表示するための単位
TARGET_CATEGORIES = ["Outerwear", "Shoes", "Tops"]   # グラフにするカテゴリ

# ===== ④ 関数の定義 =====
def to_man_yen(yen):
    """円を万円に変換して、小数点以下1桁に丸める"""
    return round(yen / UNIT, 1)

# ===== ⑤ データの読み込み =====
df = pd.read_csv(DATA_FILE)
print("行数・列数:", df.shape)

# ===== ⑥ 前処理 =====
df["order_date"] = pd.to_datetime(df["order_date"])   # 文字列を日付に変換
df["month"] = df["order_date"].dt.to_period("M")      # 年月の列を作る

# ===== ⑦ 分析・計算 =====
monthly = df.groupby(["month", "category"])["amount"].sum().unstack()
for cat in TARGET_CATEGORIES:
    total = monthly[cat].sum()
    if total >= 5000000:
        print(cat, "の売上合計:", to_man_yen(total), "万円（500万円以上）")
    else:
        print(cat, "の売上合計:", to_man_yen(total), "万円")

# ===== ⑧ 出力（表示と保存） =====
styles = ["-", "--", ":"]
for cat, style in zip(TARGET_CATEGORIES, styles):
    plt.plot(monthly.index.astype(str), monthly[cat] / UNIT, color="black", linestyle=style, label=cat)
plt.xticks(rotation=90)
plt.ylabel("Sales (10,000 yen)")
plt.legend()
plt.tight_layout()
plt.savefig("monthly_by_category.png")
plt.show()
monthly.to_csv("monthly_by_category.csv")
