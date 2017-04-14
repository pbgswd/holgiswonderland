from moviepy.editor import *

audioclip = AudioFileClip("bensound-funnysong.mp3").subclip(0, 144)

intro = VideoFileClip('DSC_0022.AVI').subclip(5, 8) #3
clip1 = VideoFileClip('DSC_0001.AVI').subclip(3,15) #12
clip2 = VideoFileClip('DSC_0001.AVI').subclip(38,55) #17
clip3 = VideoFileClip('DSC_0003.AVI').subclip(4,8) #4
clip4 = VideoFileClip('DSC_0004.AVI').subclip(3,16) #13
clip5 = VideoFileClip('DSC_0005.AVI').subclip(3,16) #13
clip6 = VideoFileClip('DSC_0006.AVI').subclip(3,7) #4
clip71 = VideoFileClip('DSC_0007.AVI').subclip(2,9) #7
clip72 = VideoFileClip('DSC_0007.AVI').subclip(16,32) #16
clip8  = VideoFileClip('DSC_0008.AVI').subclip(11,16) #5
clip9  = VideoFileClip('DSC_0009.AVI').subclip(4,10) #6
clip10 = VideoFileClip('DSC_0010.AVI').subclip(4,7) # 3
clip11 = VideoFileClip('DSC_0011.AVI').subclip(9,15) # 6
clip12 = VideoFileClip('DSC_0012.AVI').subclip(4,13)# 9
clip13 = VideoFileClip('DSC_0013.AVI').subclip(5,10) #5
clip14 = VideoFileClip('DSC_0014.AVI').subclip(2,7) #5
clip15 = VideoFileClip('DSC_0015.AVI').subclip(62,72) # 10
clip16 = VideoFileClip('DSC_0016.AVI').subclip(8,13) # 5
clip17 = VideoFileClip('DSC_0017.AVI').subclip(14,24) #10
clip18 = VideoFileClip('DSC_0018.AVI').subclip(18,23) #5
clip19 = VideoFileClip('DSC_0019.AVI').subclip(8,20) # 12
clip20 = VideoFileClip('DSC_0020.AVI').subclip(11,14) # 3
clip21 = VideoFileClip('DSC_0021.AVI').subclip(31,44) # 13
#171 seconds
content = concatenate_videoclips([intro.fadein(1).crossfadeout(1),
                                  clip1.crossfadein(1),
                                  clip2.crossfadein(0.5),
                                  clip3.crossfadein(0.5),
                                  clip4.crossfadein(0.5),
                                  clip5.crossfadein(0.5),
                                  clip6.crossfadein(0.5),
                                  clip71.crossfadein(0.5),
                                  clip72.crossfadein(0.5),                                  
                                  clip8.crossfadein(0.5),
                                  clip9.crossfadein(0.5),
                                  clip10.crossfadein(0.5),
                                  clip11.crossfadein(0.5),
                                  clip12.crossfadein(0.5),
                                  clip13.crossfadein(0.5),
                                  clip14.crossfadein(0.5),
                                  clip15.crossfadein(0.5),
                                  clip16.crossfadein(0.5),
                                  clip17.crossfadein(0.5),
                                  clip18.crossfadein(0.5)],
                                  padding=-1, method="compose"                                  
                                  )

video_credit  = TextClip("Video: Peter Gordon",fontsize=30, font="DejaVu-Sans-Bold", kerning=3, color='black')
vcredit       = video_credit.set_duration(2)

music_credit  = TextClip("Music: http://www.bensound.com", fontsize=30, font="DejaVu-Sans-Bold", kerning=3, color='black')
mcredit       = music_credit.set_duration(2)

software_credit = TextClip("Made with MoviePy", fontsize=30, font="DejaVu-Sans-Bold", kerning=3, color='black')
scredit         = software_credit.set_duration(2)

credits = concatenate_videoclips([vcredit,
                                  mcredit,
                                  scredit])

end = concatenate_videoclips([intro, intro]) 

allcredits = CompositeVideoClip([end, credits.set_pos(('center','bottom'))]) #6

video      = concatenate_videoclips([content, allcredits]) #171 + 6 seconds = 177 seconds
final      = video.set_audio(audioclip)

final.write_videofile("holgis_wonderland.avi",fps=24, codec='libx264')
