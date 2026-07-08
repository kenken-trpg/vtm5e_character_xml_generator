# vtm5e_character_udonarium_xml_generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Description
**English:**  
A web-based character data generator for *Vampire: The Masquerade 5th Edition (V5)*. This Streamlit application provides a GUI for inputting character data and generates XML files compatible with Udonarium, a popular Japanese VTT (Virtual Tabletop).

**日本語:**  
『ヴァンパイア：ザ・マスカレード第5版 (VtM 5e)』用のキャラクターデータXML生成ツールです。Streamlitを使用したWebベースのGUIでキャラクターデータを入力し、日本のVTT（オンラインセッションツール）「Udonarium」で使用可能なXMLファイルを生成します。

## Features (特徴)
* **Web GUI**: Streamlitによる直感的なブラウザインターフェース
* **VtM 5e 準拠**: 氏族、世代、資質、技能、訓え（Discipline）、血格などのV5ルールセットに完全対応
* **Udonarium XML出力**: Udonariumで直接インポート可能なXML形式で出力
* **チャットパレット対応**: ダイスロール用マクロを含むチャットパレットの生成・編集機能
* **日本語UI**: 全ての項目を日本語で入力可能

## Requirements (要件)
* Python 3.8+
* streamlit

## Installation (インストール方法)

1. リポジトリをクローンします。
```bash
git clone https://github.com/[your_username]/vtm5e_character_udonarium_xml_generator.git
cd vtm5e_character_udonarium_xml_generator
```

2. 必要なパッケージをインストールします。
```bash
pip install streamlit
```

## Usage (使い方)

Streamlitアプリケーションを起動します。

```bash
streamlit run vtm5e_character_udonarium_xml_generator.py
```

ブラウザが自動的に開き、キャラクターデータを入力するフォームが表示されます。各項目を入力後、「XMLファイルをダウンロード」ボタンをクリックしてXMLファイルをダウンロードしてください。

## Supported Data Fields (対応データ項目)

### 基本情報
- 名前、氏族、世代、捕食の流儀
- 夜の年代記のタイトル、大望、コンセプト
- 親御、私欲

### 資質 (Attributes)
- 身体的：筋力、持久、敏捷
- 社会的：自制、魅力、誘導
- 精神的：機知、集中、知性

### リソース
- 体力、意志力、人間性、汚点、飢え、気質

### 技能 (Skills)
- 運転、運動、隠密、格闘、近接武器、銃器
- 制作、生存術、窃盗、裏社会、脅迫、虚言
- 芸事、指揮、推察、説得、動物理解、礼儀作法
- 医学、隠秘学、科学、教養、財務、政治、先端技術、探偵、知覚

### 血格・吸血鬼の特徴
- 血格、血による増強の追加ダイス、訓えへの追加ダイス
- 食餌への制限、飢餓チェック1回ごとの回復量
- 飢餓チェックを振り直せる訓えのレベル、悪癖の深刻さ
- 氏族の悪癖、夜の年代記の良心、試金石と徳心

### 訓え (Disciplines)
- 6つの訓えスロット（自由入力）

### 特長と欠点
- 11つの特長・欠点スロット（自由入力）

### 経験点・経歴
- 総経験点、使用した経験点
- 真の年齢、外見年齢、誕生日、命日

### 詳細設定
- 見た目、目立つ特長、これまでの出来事、メモ

### チャットパレット
- ダイスロール用マクロ（編集・追加可能）

## Contributing (コントリビュート)
バグ報告や機能追加の要望は、Issues にて受け付けています。プルリクエストも大歓迎です。

## License (ライセンス)
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer (免責事項)
Vampire: The Masquerade is a registered trademark of Paradox Interactive AB. This project is a fan-made tool and is not officially affiliated with, or endorsed by, Paradox Interactive or World of Darkness.
