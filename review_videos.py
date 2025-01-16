##%%
import streamlit as st
import pandas as pd
import os

# File names
# result_csv_name = 'review_results_0_216_1230.csv'
# input_csv_name = 'splited_videos_0_216_1230.csv'
# input_csv_name = 'splited_videos_0_216_250102.csv'
result_csv_name = 'review_results_250102.csv'

# Load data with caching
@st.cache_data
def load_data():
    full_df = pd.read_csv(result_csv_name, encoding='utf-8')
    full_df = full_df.sort_values(by=['sid', 'order'])
    full_df = full_df[full_df['sid'] != 0]
    full_df.reset_index(drop=True, inplace=True)
    return full_df

df = load_data()


# Initialize session state
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Placeholder for video
video_placeholder = st.empty()

# Functions


def next_video():
    if st.session_state.current_index < len(df) - 1:
        st.session_state.current_index += 1
        video_url = df.iloc[st.session_state.current_index]['video_urls']
        video_placeholder.video(video_url, autoplay=True, muted=True)

def previous_video():
    if st.session_state.current_index < len(df) - 1:
        st.session_state.current_index += 1
        video_url = df.iloc[st.session_state.current_index]['video_urls']
        video_placeholder.video(video_url, autoplay=True, muted=True)


# Streamlit UI
# st.title("Video Review App")
video_url = df.iloc[st.session_state.current_index]['video_urls']
video_placeholder.video(video_url, autoplay=True, muted=True)

# Display video information
st.info(f"Prompt: {df.iloc[st.session_state.current_index]['scene_prompt']}")

st.info(f"Marked as {df.iloc[st.session_state.current_index]['status']}")
col1, col2 = st.columns(2)
with col1:
    st.button("Next", on_click=next_video, args=())
with col2:
    st.button("Previous", on_click=previous_video, args=())
    
st.caption(f"SID:{df.iloc[st.session_state.current_index]['sid']} order:{df.iloc[st.session_state.current_index]['order']}")
st.caption(f"Reviewing {st.session_state.current_index} out of {len(df)}")


# Control buttons


# %%
