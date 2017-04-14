from moviepy.editor import *
intro = VideoFileClip('DSC_0022.AVI').subclip(5, 8)
clip1 = VideoFileClip('DSC_0001.AVI').subclip(3,15)
clip2 = VideoFileClip('DSC_0001.AVI').subclip(38,55)
clip3 = VideoFileClip('DSC_0003.AVI').subclip(4,8)
clip4 = VideoFileClip('DSC_0004.AVI').subclip(3,16)
clip5 = VideoFileClip('DSC_0005.AVI').subclip(3,16)

 
#DSC_0005.AVI DSC_0006.AVI DSC_0007.AVI DSC_0008.AVI DSC_0009.AVI DSC_0010.AVI DSC_0011.AVI DSC_0012.AVI
#DSC_0013.AVI DSC_0014.AVI DSC_0015.AVI DSC_0016.AVI DSC_0017.AVI DSC_0018.AVI DSC_0019.AVI  DSC_0020.AVI  DSC_0021.AVI

content = concatenate_videoclips([intro.crossfadein(1).crossfadeout(1),
                                  clip1.crossfadein(1).crossfadeout(0.5),
                                  clip2.crossfadein(0.5).crossfadeout(0.5),
                                  clip3.crossfadein(0.5).crossfadeout(0.5),
                                  clip4.crossfadein(0.5).crossfadeout(0.5)
                                  ])
 
content.write_videofile("holgis_wonderland.avi",fps=24, codec='libx264')