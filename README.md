# auto ai subtitle

## 简介
ai字幕生成，字幕翻译 基于openai/whisper、translate、ffmpeg，自动为视频生成翻译过后的srt字幕文件，支持自定义各种语言、支持使用huggingface下载的自定义model

## 功能
1.基于视频中的语音直接生成字幕文件  
2.翻译字幕文件

## 使用方法
基础环境为 python v3.10

安装 `ffmpeg`，安装方式详见[官网](https://ffmpeg.org/download.html)

（可选）使用gpu计算请官网安装[CUDA](https://developer.nvidia.com/cuda-downloads)和[cuDNN](https://developer.nvidia.com/cudnn-downloads)

安装依赖 `pip install -r requirements.txt`，使用gpu请安装CUDA相关内容后在[PyTorch官网](https://pytorch.org/get-started/locally/)自行安装对应CUDA的gpu版本

`config_example.yaml`复制改名为 `config.yaml` 将视频相关配置信息填入 

执行 `python main.py`

## 效果
原视频：

![](docs\img\without_subtitle.png)

执行脚本后生成以下文件：

![](docs\img\list.png)

添加生成的字幕文件后：

![](docs\img\with_subtitle.png)

## TODO
提高结果准确度
 - whisper换用转文字精度更高的model
 - 接入大模型实现翻译功能替换translate模块，对翻译质量进行提高
 - 实现实时输出翻译内容，可参照使用whisperX

GUI支持（待定）
