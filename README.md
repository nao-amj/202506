# 202506 Blog Example

このリポジトリは簡単なブログ生成スクリプトのサンプルです。

## 使い方

1. `posts/` ディレクトリに Markdown 形式のファイルを追加します。最初の行はタイトルとして扱われます。
2. `python3 blog_generator.py` を実行すると `site/` ディレクトリに HTML が生成されます。
3. 生成された `site/index.html` をブラウザで開くとブログを閲覧できます。
※ `site/` ディレクトリは `blog_generator.py` の実行時に自動生成されます。

## 依存

標準ライブラリのみを使用しており、追加のパッケージは不要です。
