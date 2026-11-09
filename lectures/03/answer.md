# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：LLMよりも端的に回答してくれている。
- `--trace` で見えたツール呼び出し（ツール名と引数）：
- 1つの質問での LLM 呼び出し回数（`requests`）：search_glossary 2回、LoRA,QLoRA
- 追加したツールと、docstring に書いた説明：make_quiz,指定した回の用語から1つ選び、確認問題と答えを返す。『第2回の確認問題を出して』など、指定した回の復習問題を求められたときに使う

## 宿題

- 取り組んだレベル：実装
- やったこと：`app/tools.py` に `save_learning_log(entry: str) -> str` を追加し、学習記録を日付ごとの Markdown ファイルとして `learning_log/` に追記するようにした。空の記録は保存しない。`app/agent.py` では `DeferredToolRequests` を出力型に加え、`save_learning_log` を `requires_approval=True` で登録した。保存依頼がある場合は CLI で内容を表示して確認し、承認・拒否の結果を `DeferredToolResults` として渡してエージェントを再開するようにした。保存先と承認前後の動作を確認するテストも追加した。
- 結果：承認前にはファイルが作られず、承認後に記録が保存されることをテストで確認できた。`--list-tools` に `save_learning_log` が表示され、`uv run pytest -q` は 21 件すべて成功した。
- 気づき・疑問：承認が必要なツールは、通常の文字列回答ではなく `DeferredToolRequests` として返るため、利用者の判断後に `DeferredToolResults` を渡して実行を再開する必要があった。最初のテストでは、一時ディレクトリに保存先を差し替えたとき、成功メッセージのパスをプロジェクトルート基準で作っていたためエラーになった。保存先の設定に依存しない表示に直して解消した。
