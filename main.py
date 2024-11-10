import yaml

from script import translate_tool, audio_tool, whisper_tool
from datetime import datetime

if __name__ == '__main__':
    # 读取配置文件
    with open('config.yaml', encoding='utf-8') as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)

    # 调用ffmpeg实现视频转音频功能
    start_time = datetime.now()
    print("视频转音频开始")
    audio_tool.audio_extract(config['input'], config['output'])
    end_time = datetime.now()
    time_difference = end_time - start_time
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60
    seconds = time_difference.seconds % 60
    print(f"视频转音频成功，耗时{hours}小时{minutes}分钟{seconds}秒")

    # 使用whisper实现音频转字幕文件
    print("音频转字幕文件开始")
    start_time = datetime.now()
    whisper_tool.do_whisper(config['output'], config['srt_path'], config['from'], config['hf_model_path'],
                            config['device'])
    end_time = datetime.now()
    time_difference = end_time - start_time
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60
    seconds = time_difference.seconds % 60
    print("音频转字幕文件成功，耗时{hours}小时{minutes}分钟{seconds}秒")

    # 使用translate库对字幕文件进行翻译（未来是否可以考虑使用大模型实现精度更好的翻译？）
    print("翻译开始")
    start_time = datetime.now()
    translate_tool.do_translate(config['srt_path'], config['srt_translate_path'], config['from'], config['to'],
                                config['translate_threads'])
    end_time = datetime.now()
    time_difference = end_time - start_time
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60
    seconds = time_difference.seconds % 60
    print("翻译成功，耗时{hours}小时{minutes}分钟{seconds}秒")

    print("成功")
