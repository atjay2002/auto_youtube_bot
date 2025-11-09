from apscheduler.schedulers.blocking import BlockingScheduler
from modules import idea_generator, voice_generator, video_maker
import json

# Load config
with open("config.json") as f:
    config = json.load(f)

def create_video_job():
    idea = idea_generator.get_random_idea()
    script = f"In this short, let's see {idea}!"
    voice_path = voice_generator.make_voice(script, lang=config["voice_lang"])
    video_maker.create_video(script, voice_path, output_dir=config["output_path"], watermark=config["watermark_text"])
    print(f"Video created for idea: {idea}")

sched = BlockingScheduler()
sched.add_job(create_video_job, 'interval', hours=config["video_schedule_hours"])
print("Auto Video Generator Bot started...")
sched.start()
