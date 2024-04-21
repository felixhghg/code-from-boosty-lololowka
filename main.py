import sys
import time

import requests
from progress import Progress
from moviepy.utils import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
class rickroller:

     def make(
             self,
             clip_path: str,
             output_path: str = "output.mp4",
             rickroll_path: str = "rickroll.mp4",
             rickroll_len: int = 15,
             cut_len: int = 15
     ):
          clip_path = self.__download_if_url(clip_path)
          rickroll_path = self.__download_if_url(rickroll_path)
          rickroll = VideoFileClip(rickroll_path)

          clip2 = VideoFileClip(clip_path)
          clip2 = clip2.subclip(0, clip2.duration - cut_len)

          rickroll = rickroll.subclip(0.5, rickroll_len)

          final_clip = concatenate_videoclips([clip2,rickroll], method="compose")

          final_clip.write_videofile(output_path)

          print(f"[bold green]Rickroll saved to {output_path}[/bold green]")


     def __do_download(self,url) -> str:

          r = requests.get(url,stream=True)
          time.sleep(5)
          total = int(r.headers.get("content-length"), 0)
          with open("raw.mp4","wb") as f:
               for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                         f.write(chunk)
          return "raw.mp4"

     def __download_if_url(self,url:str):
          if url.startswith("http"):
               url = self.__do_download(url)

          return url

if __name__ == '__main__':
     rickrolle = rickroller()
     rickrolle.make(sys.argv[1])