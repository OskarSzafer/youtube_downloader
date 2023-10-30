import os

import tkinter as tk

from youtube_downloader import save_cut


def gui_main(
        font_type: str="Calibri",
        content_scale: int=15,
        ):
    global quality
    quality = 0

    root = tk.Tk()
    root.title('video downloader')

    entry_var_default_url = tk.StringVar()
    entry_var_default_url.set("https://www.youtube.com/")  # set default url
    entry_var_default_path = tk.StringVar()
    entry_var_default_path.set(os.path.dirname(__file__))  # set default path

    def download_button_action(): #download button
        download_button['state'] = tk.DISABLED

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
        
        download_button['state'] = tk.NORMAL
        print('ready!')

    def switch_quality(): # quality buttons
        global quality
        if quality == 0:
            quality = 1
            quality_button_H['state'] = tk.DISABLED
            quality_button_L['state'] = tk.NORMAL
        else:
            quality = 0
            quality_button_L['state'] = tk.DISABLED
            quality_button_H['state'] = tk.NORMAL

    #WIDGETS:
    #url
    url_text = tk.Label(root, font=(font_type, content_scale), text='video URL:')
    url_input = tk.Entry(root, font=(font_type, content_scale), fg="gray", width=content_scale*3)
    url_input.insert(0, entry_var_default_url.get()) # default url

    def url_input_click(event):
        if url_input.get() == entry_var_default_url.get():
            url_input.delete(0, tk.END)
            url_input.configure(fg="black")

    def url_input_leave(event):
        if url_input.get() == "":
            url_input.configure(fg="gray")
            url_input.insert(0, entry_var_default_url.get())

    url_input.bind("<FocusIn>", url_input_click)
    url_input.bind("<FocusOut>", url_input_leave)

    #path
    path_text = tk.Label(root, font=(font_type, content_scale), text='path:')
    path_input = tk.Entry(root, font=(font_type, content_scale), fg="gray", width=content_scale*3)
    path_input.insert(0, entry_var_default_path.get()) # default path

    def path_input_click(event):
        if path_input.get() == entry_var_default_path.get():
            path_input.delete(0, tk.END)
            path_input.configure(fg="black")

    def path_input_leave(event):
        if path_input.get() == "":
            path_input.configure(fg="gray")
            path_input.insert(0, entry_var_default_path.get())
    
    path_input.bind("<FocusIn>", path_input_click)
    path_input.bind("<FocusOut>", path_input_leave)

    #file name
    file_name_text = tk.Label(root, font=(font_type, content_scale), text='file name:')
    file_name_input = tk.Entry(root, font=(font_type, content_scale), width=content_scale*3)

    #quality
    quality_text = tk.Label(root, font=(font_type, content_scale), text='quality:')
    quality_button_H = tk.Button(root, font=(font_type, content_scale), padx=content_scale*6, text='high', command=switch_quality)
    quality_button_L = tk.Button(root, font=(font_type, content_scale), padx=content_scale*6, text='low', command=switch_quality, state=tk.DISABLED)
    
    #clip timing
    vid_start_text = tk.Label(root, font=(font_type, content_scale), text='start time:')
    vid_start_input = tk.Entry(root, font=(font_type, content_scale), width=content_scale)
    vid_end_text = tk.Label(root, font=(font_type, content_scale), text='end time:')
    vid_end_input = tk.Entry(root, font=(font_type, content_scale), width=content_scale)
    
    #download button
    download_button = tk.Button(root, font=(font_type, content_scale), text='download', command=download_button_action, padx=content_scale*2)


    #GRID:
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
    quality_button_H.grid(row=3, column=1, sticky=tk.E)
    quality_button_L.grid(row=3, column=2, sticky=tk.W)
    #clip timing placement
    vid_start_text.grid(row=4, column=0)
    vid_start_input.grid(row=4, column=1,columnspan=1, sticky=tk.W)
    vid_end_text.grid(row=5, column=0)
    vid_end_input.grid(row=5, column=1,columnspan=1, sticky=tk.W)
    #download button placement
    download_button.grid(row=6, column=1,columnspan=2, sticky=tk.S)

    root.mainloop()