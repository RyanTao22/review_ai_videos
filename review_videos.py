import streamlit as st
import pandas as pd

# File names
# result_csv_name = 'review_results_250102.csv'
# result_csv_kling = 'review_results_kling_250123.csv'
result_csv_name = 'combined_results_df_250203_part1.csv'

# Load data with caching
@st.cache_data
def load_data():
    full_df = pd.read_csv(result_csv_name, encoding='utf-8')
    # full_df = pd.read_excel(result_df)
    
    full_df.reset_index(drop=True, inplace=True)
    
    # exclude_indices = list(range(22, 88)) + list(range(97, 135))
    # full_df = full_df[~full_df.index.isin(exclude_indices)]
    # full_df = full_df[full_df['sid'] != 0]
    
    # full_df = full_df.sort_values(by=['sid', 'order'])
    # full_df.reset_index(drop=True, inplace=True)


    # kling = pd.read_csv(result_csv_kling, encoding='utf-8')
    # kling = kling.iloc[15:]
    # kling.reset_index(drop=True, inplace=True)

    # return full_df, kling
    return full_df

#df_org,kling_df = load_data()
df_org = load_data()

# on = st.toggle("Kling On")
# if on:
#     df = kling_df
#     st.empty()
# else: 
#     df = df_org
#     st.empty()

df = df_org

# Initialize session state
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Placeholder for video
video_placeholder = st.empty()

# Functions
def next_video():
    if st.session_state.current_index < len(df) - 1:
        st.session_state.current_index += 1
        #update_video()

def previous_video():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        #update_video()

def update_video():
    # video_url = df.iloc[st.session_state.current_index]['video_urls']
    video_url = df.iloc[st.session_state.current_index]['final_url']
    st.empty()
    with video_placeholder:
        st.video(video_url)
        # st.video(video_url, autoplay=True, muted=True)

def go_to_video():
    try:
        index = int(st.session_state.video_index_input) - 1  # Convert to zero-based index
        if 0 <= index < len(df):
            st.session_state.current_index = index
            #update_video()
        else:
            st.error("Please enter a valid index.")
    except ValueError:
        st.error("Please enter a valid number.")

# Streamlit UI
#st.title("Video Review App")
st.info(f"Marked as {df.iloc[st.session_state.current_index]['status']}")

# Display video
update_video()

# Display video information
#st.info(f"Prompt: {df.iloc[st.session_state.current_index]['scene_prompt']}")



col1, col2, col3= st.columns(3)
with col1:
    st.button("Previous", on_click=previous_video,key='minus_one'+str(st.session_state.current_index))
    
with col2:
    st.button("Next", on_click=next_video,key='add_one'+str(st.session_state.current_index))
with col3:
    st.text_input("Enter video index:", key="video_index_input", on_change=go_to_video)



    

#st.caption(f"SID: {df.iloc[st.session_state.current_index]['sid']} Order: {df.iloc[st.session_state.current_index]['order']}")
st.caption(f"SID: {df.iloc[st.session_state.current_index]['sid']}")
st.caption(f"Reviewing {st.session_state.current_index + 1} out of {len(df)}")
