# whisper demo

Whisperのデモリポジトリ

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

### whieper_api_demo

Whisper APIを使った文字起こしのデモ

```bash
❯ python .\whisper_api_demo.py --help
usage: whisper_api_demo.py [-h] [--audio_file AUDIO_FILE]

options:
  -h, --help            show this help message and exit
  --audio_file AUDIO_FILE
```

`--audio-file`を指定するとそのオーディオファイルの文字起こしを、指定せず起動するとユーザーからの音声入力を受け付ける
