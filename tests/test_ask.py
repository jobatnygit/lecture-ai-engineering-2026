from types import SimpleNamespace

import app.ask as app_ask


class DummyModels:
    def generate_content(self, model, contents):
        return SimpleNamespace(
            text="これはテスト応答です",
            usage_metadata=SimpleNamespace(
                prompt_token_count=123,
                candidates_token_count=45,
            ),
        )


class DummyClient:
    def __init__(self, api_key):
        self.models = DummyModels()


def test_ask_prints_input_and_output_tokens(monkeypatch, capsys):
    monkeypatch.setattr(app_ask, "get_api_key", lambda: "dummy-key")
    monkeypatch.setattr(app_ask.genai, "Client", DummyClient)

    result = app_ask.ask("テスト質問")

    assert result == "これはテスト応答です"
    captured = capsys.readouterr().out
    assert "入力トークン数: 123" in captured
    assert "出力トークン数: 45" in captured
