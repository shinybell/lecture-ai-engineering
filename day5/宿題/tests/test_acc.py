import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# パスの設定
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/Titanic.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/titanic_model.pkl")


def main():
    """モデルを読み込み、精度を評価して出力する"""
    # データの読み込み
    df = pd.read_csv(DATA_PATH)

    # 特徴量と目的変数の分離
    X = df.drop("Survived", axis=1)
    y = df["Survived"].astype(int)

    # テストデータの準備
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # モデルの読み込み
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)

        # 予測と精度計算
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # 精度のみを出力（GithubActionsで使用される）
        print(f"Accuracy: {accuracy:.6f}")
    else:
        print("Accuracy: 0.000000")  # モデルが存在しない場合


if __name__ == "__main__":
    main()
