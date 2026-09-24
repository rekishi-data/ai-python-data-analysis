# データの出典と利用条件

このリポジトリの data/ フォルダのデータは、次の出典のデータを加工して作成したものです。利用するときは、それぞれの出典を表示してください。利用条件は変わることがあるため、各サイトの最新の利用規約もあわせてご確認ください。

## 架空のデータ（本書で作成）

sales_data.csv、survey_responses.csv、brand_image_responses.csv、student_life.csv、student_life_codebook.csv は、本書の学習用に作成した架空のデータです。実在の企業・人物とは関係ありません。クリエイティブ・コモンズ 表示 4.0 国際ライセンス（CC BY 4.0）で提供します。

出典の表示の例：「秋元健治『AIで動かす Pythonデータ分析』（歴史データ研究社）の配布データ」

## 政府統計・行政データ

- **国勢調査・経済センサス‐活動調査の地域メッシュ統計**（mesh250_population_tokyo23.csv、mesh250_households_tokyo23.csv、mesh250_mobility_tokyo23.csv、mesh500_establishments_tokyo23.csv、mesh500_industry_tokyo23.csv）
  出典：「政府統計の総合窓口（e-Stat）」（https://www.e-stat.go.jp/）令和2年国勢調査、令和3年経済センサス‐活動調査（総務省統計局）を加工して作成
- **国土数値情報**（tokyo23_wards.geojson、stations_tokyo23_2023.csv）
  出典：国土数値情報（行政区域データ、駅別乗降客数データ）（国土交通省）（https://nlftp.mlit.go.jp/ksj/）を加工して作成
- **推計昼間人口メッシュデータ**（mesh250_daytime_tokyo23.csv）
  出典：「政府統計の総合窓口（e-Stat）」提供の原典を、はんけトケ（https://hanketoke.com/）が利用・加工して作成した推計昼間人口メッシュデータ（CC BY 4.0）を、さらに加工して作成

ward_indicators_tokyo23.csv と shibuya_harajuku_mesh.csv は、上のデータを組み合わせて作成したものです。

## Google トレンド

trends_12m.csv、trends_5y.csv
出典：Google トレンド（https://trends.google.co.jp/）、2026年9月24日取得。日本、過去12か月・過去5年間。「UNIQLO」はトピック（ファッション レーベル）として、ほかの3語は検索キーワードとして取得しています。

## 地図の背景

サポートページのインタラクティブ地図の背景には、国土地理院の地理院タイル（淡色地図）を使用しています。
