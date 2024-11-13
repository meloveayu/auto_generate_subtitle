import whisperx
import torch
import gc
import yaml
import re 

#字幕时间格式
def reformat_time(second):
    m, s = divmod(second, 60)
    h, m = divmod(m, 60)
    hms = "%02d:%02d:%s" % (h, m, str('%.3f' % s).zfill(6))
    hms = hms.replace('.', ',')
    return hms

#写入字幕
def write_srt(seg, srt_path):
    with open(srt_path, 'w', encoding='utf-8') as f:
        write_content = [str(n + 1) + '\n'
                         + reformat_time(i['start'])
                         + ' --> '
                         + reformat_time(i['end']) + '\n'
                         + i['text'] + '\n\n'
                         for n, i in enumerate(seg)]
        f.writelines(write_content)

def do_whisper(audio_file, srt_path, language, device,compute_type="int8",batch_size = 8):
    model = whisperx.load_model("large-v2", device,compute_type=compute_type)
    audio = whisperx.load_audio(audio_file)
    print("whisper working...")
    result = model.transcribe(audio, batch_size= batch_size,language=language)
    print("whisper execute success")
    print("writing srt file...")
    write_srt(result['segments'], srt_path)
    print("write srt success")

    # delete model if low on GPU resources
    gc.collect()
    torch.cuda.empty_cache()
    del model




