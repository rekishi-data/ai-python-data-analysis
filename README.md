# AIで動かす Pythonデータ分析 ― サポートリポジトリ

書籍『AIで動かす Pythonデータ分析 ― Google Colabで東京のオープンデータを読み解く』（秋元健治、歴史データ研究社、2026年）のサポートリポジトリです。本書で使う**参照用ノートブック**と**配布データ**を公開しています。

サポートページ：https://YOUR_ACCOUNT.github.io/YOUR_REPO/

## 使い方

1. 下の表の「Colabで開く」のリンクをクリックすると、Google Colab でノートブックが開きます。
2. メニューの「File」→「Save a copy in Drive」で、自分のGoogleドライブにコピーを保存します。
3. 最初のセルの `LANG` を `"ja"`（日本語）または `"en"`（英語）にして、「Runtime」→「Run all」で上から実行します。データはこのリポジトリから自動で読み込まれます。

AIが書くコードは毎回少しずつ違うため、読者のみなさんの結果が本書の図と細かいところで違っていても問題ありません。うまくいかないときの答え合わせに使ってください。

## ノートブック

| 節 | 内容 | ノートブック |
|---|---|---|
| 1-6 | Pythonのスクリプトの流れ（サンプル） | [ch1-6_sample_script.py](notebooks/ch1-6_sample_script.py) |
| 2-1 | タイタニック号のデータで集計と可視化 | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch2-1_titanic.ipynb) |
| 2-2 | 回帰分析 | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch2-2_regression.ipynb) |
| 3-1 | 購買データ（RFM分析、売上予測、主成分分析） | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch3-1_sales_rfm.ipynb) |
| 3-2 | アンケート（因子分析、対応分析、テキストマイニング） | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch3-2_survey.ipynb) |
| 3-3 | Googleトレンド | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch3-3_google_trends.ipynb) |
| 3-4・3-5 | 業種の集まり方（特化係数）、住まいと世帯 | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch3-4_3-5_industry_households.ipynb) |
| 4-1〜4-4 | 23区の地図、250m区画、昼と夜の人口、商業地域 | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch4-1_4-4_maps.ipynb) |
| 4-5・4-6 | 人の入れ替わり、クラスター分析 | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch4-5_4-6_mobility_cluster.ipynb) |
| 5 | 総合演習：カフェの出店候補地 | [Colabで開く](https://colab.research.google.com/github/YOUR_ACCOUNT/YOUR_REPO/blob/main/notebooks/ch5_cafe_location.ipynb) |

## 配布データ（data/）

| ファイル | 節 | 内容 | 出典 |
|---|---|---|---|
| sales_data.csv | 1・3-1 | アパレルECショップの購買データ | 架空のデータ（本書で作成） |
| survey_responses.csv、brand_image_responses.csv | 3-2 | 顧客アンケート | 架空のデータ（本書で作成） |
| student_life.csv、student_life_codebook.csv | 2-2 | 大学生の生活調査とコードブック | 架空のデータ（本書で作成） |
| trends_12m.csv、trends_5y.csv | 3-3 | 検索インタレスト（2026年9月24日取得。UNIQLO はトピック「ファッション レーベル」として取得） | Google トレンド |
| mesh500_industry_tokyo23.csv | 3-4 | 500m区画の産業別の事業所数・従業者数 | 令和3年経済センサス‐活動調査（総務省統計局） |
| mesh250_households_tokyo23.csv | 3-5 | 250m区画の世帯と住まい | 令和2年国勢調査（総務省統計局） |
| tokyo23_wards.geojson | 4・5 | 23区の境界 | 国土数値情報（行政区域データ、2023年）（国土交通省） |
| mesh250_population_tokyo23.csv | 4 | 250m区画の人口 | 令和2年国勢調査（総務省統計局） |
| mesh250_daytime_tokyo23.csv | 4 | 250m区画の昼間・夜間人口（推計） | 推計昼間人口メッシュデータ（はんけトケ） |
| mesh500_establishments_tokyo23.csv | 4 | 500m区画の事業所数（飲食店・小売業など） | 令和3年経済センサス‐活動調査（総務省統計局） |
| stations_tokyo23_2023.csv | 4・5 | 駅の1日あたり乗降客数（2023年度） | 国土数値情報（駅別乗降客数データ）（国土交通省） |
| mesh250_mobility_tokyo23.csv | 4-5 | 250m区画の人の移動と通勤・通学 | 令和2年国勢調査（総務省統計局） |
| ward_indicators_tokyo23.csv | 4-6 | 区ごとの8つの指標 | 上のデータから本書で作成 |
| shibuya_harajuku_mesh.csv | 5 | 分析エリアの区画データ | 上のデータと令和2年国勢調査から本書で作成 |

データの出典と利用条件の詳細は [DATA_LICENSE.md](DATA_LICENSE.md) をご覧ください。タイタニック号のデータ（2-1）は、Python のライブラリ seaborn に付属する練習用データを使います。

## 動作確認環境

[VERSIONS.md](VERSIONS.md) をご覧ください。

## 正誤表・お知らせ

サポートページに掲載します。

## ライセンス

- ノートブックとスクリプト：MIT License（[LICENSE](LICENSE)）
- データ：[DATA_LICENSE.md](DATA_LICENSE.md)

---

## English

This is the support repository for the Japanese book 『AIで動かす Pythonデータ分析』 by Kenji Akimoto (2026). Click "Colabで開く" (Open in Colab) above, set `LANG = "en"` in the first cell, and run all cells. The data files are downloaded from this repository automatically.
