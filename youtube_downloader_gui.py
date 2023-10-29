from tkinter import *
from youtube_downloader import save_cut

def gui_main(
        font_type="Calibri",
        content_scale=15,
        ):
    global quality
    quality = 0

    root = Tk()
    root.title('video downloader')

    def download_button_action(): #download button
        download_button['state'] = DISABLED

        if vid_start_input.get() == "":
            start_time = None
        else:
            start_time = int(vid_start_input.get())
        if vid_end_input.get() == "":
            end_time = None
        else:
            end_time = int(vid_end_input.get())
        
        save_cut(
            url_input.get(), 
            path_input.get(),
            vid_name=file_name_input.get(),
            vid_start=start_time, 
            vid_end=end_time,
            quality=quality)
        
        download_button['state'] = NORMAL
        print('ready!')

    def switch_quality(): # quality buttons
        global quality
        if quality == 0:
            quality = 1
            quality_button_H['state'] = DISABLED
            quality_button_L['state'] = NORMAL
        else:
            quality = 0
            quality_button_L['state'] = DISABLED
            quality_button_H['state'] = NORMAL

    #widgets:
    #url
    url_text = Label(root, font=(font_type, content_scale), text='video URL:')
    url_input = Entry(root, font=(font_type, content_scale), width=content_scale*3)
    #path
    path_text = Label(root, font=(font_type, content_scale), text='path:')
    path_input = Entry(root, font=(font_type, content_scale), width=content_scale*3)
    #file name
    file_name_text = Label(root, font=(font_type, content_scale), text='file name:')
    file_name_input = Entry(root, font=(font_type, content_scale), width=content_scale*3)
    #quality
    quality_text = Label(root, font=(font_type, content_scale), text='quality:')
    quality_button_H = Button(root, font=(font_type, content_scale), padx=content_scale*6, text='high', command=switch_quality)
    quality_button_L = Button(root, font=(font_type, content_scale), padx=content_scale*6, text='low', command=switch_quality, state=DISABLED)
    #clip timing
    vid_start_text = Label(root, font=(font_type, content_scale), text='start time:')
    vid_start_input = Entry(root, font=(font_type, content_scale), width=content_scale)
    vid_end_text = Label(root, font=(font_type, content_scale), text='end time:')
    vid_end_input = Entry(root, font=(font_type, content_scale), width=content_scale)
    #download button
    download_button = Button(root, font=(font_type, content_scale), text='download', command=download_button_action, padx=content_scale*2)

    #grid:
    #url placement
    url_text.grid(row=0, column=0)
    url_input.grid(row=0, column=1,columnspan=2)
    #path placement
    path_text.grid(row=1, column=0)
    path_input.grid(row=1, column=1,columnspan=2)
    #file name placement
    file_name_text.grid(row=2, column=0)
    file_name_input.grid(row=2, column=1,columnspan=2)
    #quality placement
    quality_text.grid(row=3, column=0)
    quality_button_H.grid(row=3, column=1, sticky=E)
    quality_button_L.grid(row=3, column=2, sticky=W)
    #clip timing placement
    vid_start_text.grid(row=4, column=0)
    vid_start_input.grid(row=4, column=1,columnspan=1, sticky=W)
    vid_end_text.grid(row=5, column=0)
    vid_end_input.grid(row=5, column=1,columnspan=1, sticky=W)
    #download button placement
    download_button.grid(row=6, column=1,columnspan=2, sticky=S)

    root.mainloop()