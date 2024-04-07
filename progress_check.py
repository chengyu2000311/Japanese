lessons_len = 58 * 60 * 60 + 31 * 60 + 59
from bs4 import BeautifulSoup 

video_list_html = ''
with open('./resource/video_list.html', 'r') as f:
    video_list_html = f.read().strip()

data = BeautifulSoup(video_list_html, 'html.parser').find('ul')
text = data.find_all("div", {"class": "duration"})

lessons = []
lessons_len = 0
for i in text:
    minute, second = [int(x) for x in i.contents[0].split(':')]
    lessons.append((minute, second))

lessons_len = sum(minute * 60 + second for minute, second in lessons)
def convert_second_format(second):
    hours = second//3600
    minutes = (second - (second//3600) * 3600 - second%60)//60
    seconds = second%60
    return f"{hours}:{minutes}:{seconds}"


with open("./resource/cur_progress.txt", "r") as f:
    progress = f.read().strip() # format will be x,y,z while x represents module and y reprents minute and z represents seconds
    module, minute, second =  (int(x) for x in progress.split(","))
    cur_progress = sum(minute * 60 + second for minute, second in lessons[:module]) + minute + second
    print(f"----------- Current Progress -----------")
    print(f"In Seconds: {cur_progress}/{lessons_len}")
    print(f"In Hours: {convert_second_format(cur_progress)}/{convert_second_format(lessons_len)}")
    print(f"Completed: {cur_progress/lessons_len}% ")
    print(f"Left: {1-cur_progress/lessons_len}")
