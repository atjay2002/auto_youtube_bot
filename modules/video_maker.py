from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, ColorClip
from datetime import datetime
import os

def create_video(script_text, voice_path, output_dir="videos/", watermark="AutoTeech Tamil"):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create a simple background clip (10 sec)
    clip = ColorClip(size=(720, 1280), color=(20, 20, 20), duration=10)

    # Add animated text for script
    txt_clip = TextClip(script_text, fontsize=40, color='white', font='Arial-Bold', method='caption', size=(700, None))
    txt_clip = txt_clip.set_position(('center', 'center')).set_duration(10)

    # Add watermark
    watermark_clip = TextClip(watermark, fontsize=30, color='yellow', font='Arial-Bold')
    watermark_clip = watermark_clip.set_position(('right', 'bottom')).set_duration(10)

    # Add voice
    audio_clip = AudioFileClip(voice_path)
    clip = clip.set_audio(audio_clip)

    # Compose final video
    final_clip = CompositeVideoClip([clip, txt_clip, watermark_clip])
    
    # Output file
    filename = f"short_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    output_path = os.path.join(output_dir, filename)
    final_clip.write_videofile(output_path, fps=24)
    return output_path
