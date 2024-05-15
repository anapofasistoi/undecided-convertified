from ffmpeg import FFmpeg, Progress
import io


def video_to_audio(video_bytes, type_audio):
    # Create a new FFmpeg instance pcm_s16le = wav ,libmp3lame = mp3, flac = flac 

    if type_audio == "mp3":
        encodec="libmp3lame"
    elif type_audio == "wav":
        encodec="pcm_s16le"
    else:
        encodec="flac" 

    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("pipe:0", format="rawvideo")  # Input as raw video
        .output(
            "pipe:1",
            {"codec:a": encodec},  # Output as WAV encoded audio
            vn=None,
            f=type_audio,
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress):
        print(progress)

    audio_bytes = ffmpeg.execute(video_bytes)  # Pass video bytes to FFmpeg

    return audio_bytes

def test_audio(audio_bytes, type_audio):

    if type_audio == "mp3":
        encodec="libmp3lame"
    elif type_audio == "wav":
        encodec="pcm_s16le"
    elif type_audio == "flac":
        encodec="flac" 

    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("pipe:0")
        .output("pipe:1", f=type_audio, codec=encodec)
        
    )
    audio_bytes_out = ffmpeg.execute(audio_bytes)
    return audio_bytes_out
