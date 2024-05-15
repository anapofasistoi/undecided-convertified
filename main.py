import streamlit as st
from lib.convertion import *

# tutorial
with st.popover("tutorial"):
    st.write("How to convert a file:")
    st.write("1. Upload a file, you can choose between 4 formats (mp4, mp3, wav, flac)")
    st.write("2. Choose the format you want your file to convert to (you cannot convert audio to video for obvious reasons)")
    st.write("3. Press the download button and you are ready to go!")
    st.write("Important note: Files that contain the character “.” cannot be converted.")
    st.write("[learn more](url)")

type_of_audio_files = ['.mp3','.wav','.flac','.mp4']
uploaded_file = st.file_uploader(label="choose a music file", type=type_of_audio_files)

if uploaded_file != None:
    st.write("filename: ", uploaded_file.name)

    # get the filename and the extention of it so it will automatically show  
    filename, extetion = uploaded_file.name.split('.')

    # menu of user to choose casa pegged
    match extetion:
        case "mp4":
            # playback feature?
            st.video( uploaded_file.read(), format="video/mp4" )
            #conversion of mp4 to ...
            file_converted_type = st.radio(
                "In what format do you want the mp4 file?",
                ["mp3", "flac", "wav"],
                index=None)

        case "mp3":
            file_converted_type = st.radio(
                "In what format do you want the mp3 file?",
                ["flac", "wav"],
                index=None)

        case "wav":
            file_converted_type = st.radio(
                "In what format do you want the wav file?",
                ["mp3", "flac"],
                index=None)

        case "flac":
            file_converted_type = st.radio(
                "In what format do you want the flac file?",
                ["mp3", "wav"],
                index=None)

    if file_converted_type !=  None:
        filename += "." + file_converted_type

    match file_converted_type:
        case "mp3":
            if extetion == "mp4":
                music_file = video_to_audio(uploaded_file.getvalue(),file_converted_type)
            else:
                music_file = test_audio(uploaded_file.getvalue(),file_converted_type)
            # convertion to mp3

        case "wav":
            if extetion == "mp4":
                music_file = video_to_audio(uploaded_file.getvalue(),file_converted_type)

            else:
                music_file = test_audio(uploaded_file.getvalue(),file_converted_type)
            # convertion to wav

        case "flac":
            if extetion == "mp4":
                music_file = video_to_audio(uploaded_file.getvalue(),file_converted_type)
            else:
                music_file = test_audio(uploaded_file.getvalue(),file_converted_type)
            # convertion to flac

    if file_converted_type != None:
        st.download_button("Downlaod me", data=music_file, file_name=filename, mime=None)

# libmp3lame mp3
# pcm_s16le wav
# flac