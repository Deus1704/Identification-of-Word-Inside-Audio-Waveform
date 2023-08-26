import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.io import wavfile
from matplotlib.font_manager import FontProperties

# CTM file processing
ctm_file_path = r"ctm.ctm"
sys.stdout.reconfigure(encoding='utf-8')
font_path = r"Mangal Regular.ttf"
custom_font = FontProperties(fname=font_path)
word_alignments = []
audio_files=["1S00011-64de11fdd1033954ee0031f4", "1S00011-64528549bbb039e9f20eab01"]
colory = ['red', 'blue', 'green', 'pink', 'orange', 'purple', 'cyan', 'brown', 'gray', 'lime','magenta','olive','bisque','burlywood','gold','indigo','navy','yellowgreen']
z=False
with open(ctm_file_path, "r", encoding="utf-8") as ctm_file:
    for line in ctm_file:
        parts = line.strip().split()

        audio_id = parts[0]
        channel_index = int(parts[1])
        start_time = float(parts[2])
        duration = float(parts[3])
        word = " ".join(parts[4:])  # Combine remaining parts as the word

        # Process the extracted information
        if (audio_id==audio_files[0] or audio_id==audio_files[1):
            word_alignments.append([audio_id, start_time, duration, word])
            # Load the .wav file
            wav_file = r"audio_data\64de11fdd1033954ee0031f4.wav"
            sample_rate, audio_data = wavfile.read(wav_file)
            time_axis = np.arange(0, len(audio_data)) / sample_rate
            z=True
    if z:
        plt.figure(figsize=(10, 8))
        plt.plot(time_axis, audio_data)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title(f"Audio ID: {(word_alignments[0][0])[9:]}")
        plt.rcParams['font.family'] = 'Mangal'
        for i in range(len(word_alignments)):
            plt.xlim(0, word_alignments[i][1] + word_alignments[i][2]+0.1)
            plt.axvspan(word_alignments[i][1], word_alignments[i][1] + word_alignments[i][2], color=colory[i], alpha=0.3)  ## Mark the word interval

            # Annotate the word on the plot
            annotation_text = word_alignments[i][3]
            plt.annotate(annotation_text, xy=(word_alignments[i][1] + word_alignments[i][2] / 2, 0), xytext=(0, -50),textcoords='offset points', ha='center', fontsize=10, color='black',fontproperties=custom_font)
        plt.show()
