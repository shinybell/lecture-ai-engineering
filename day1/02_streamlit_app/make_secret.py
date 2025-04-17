# .streamlit/secrets.toml ファイルを作成
import os
import toml

# 設定ファイルのディレクトリ確保
os.makedirs('.streamlit', exist_ok=True)

# 環境変数から取得したトークンを設定ファイルに書き込む
secrets = {
    "huggingface": {
        "token": os.environ.get("HUGGINGFACE_TOKEN", "")
    }
}

# 設定ファイルを書き込む
with open('.streamlit/secrets.toml', 'w') as f:
    toml.dump(secrets, f)
