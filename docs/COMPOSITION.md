# Raspberry Pi 5 Productのコンポジション

[product.json](../product.json)が、アプリ・共通機構・基板を組み合わせます。

| 役割 | submodule |
| --- | --- |
| センサーデモのアプリ | `sources/gar-adhoc-app` |
| 構成検査・ビルドなどの共通機構 | `sources/gar-tools` |
| Raspberry Pi 5の基板・OS資源 | `sources/board-raspberry-pi-5` |

GarStreamTx-RPI5と同じ基板コミットを利用します。
接続するMFRC522、SSD1306、VL53L0X、ボタンとLEDの用途・配線は、このProductの
`hardware/`に置きます。基板repoはアプリやセンサーの意味を知りません。

```sh
git clone --branch refactor/board-composition --recurse-submodules https://github.com/ThousandsOfTies/GarAdhocApp.git
cd GarAdhocApp
python tools/product.py describe
python tools/product.py validate
```

`validate`はGPIO・SPI・I2Cの割当を、選択した基板プロファイルへ照合します。
対応するプロファイルはRP1が`/dev/gpiochip0`であるRaspberry Pi OS arm64です。
実機のポート完成や認識成功を証明するコマンドではありません。

## 未完成状態の保持

このProductの実機対応は従来どおり`planned`です。`describe`もその状態を表示します。
物理ターゲット用のビルドとpackageは、理由を表示して明示的に失敗します。
組み合わせの設定だけを追加して、未検証の配布物を成功扱いにすることはありません。

```sh
python tools/product.py build
# Physical target is planned ... と表示して失敗する
```

実機用hookは共通compositionへ委譲します。実機への導入処理や新しいサービスは追加していません。
既存のシミュレーション用テンプレートとCアプリの実装範囲も維持します。
SDK・コンパイラー本体、生成物、SSH接続先を基板repoや公開設定へ含めません。
