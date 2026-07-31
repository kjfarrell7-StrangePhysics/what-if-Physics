import streamlit as st
# Import the custom audio module
from audio_effects import play_sfx, render_ambient_audio

# 1. Render background ambience in sidebar
render_ambient_audio()

# 2. Trigger click sound when navigation radio option changes
if "last_mode" not in st.session_state:
    st.session_state.last_mode = None

app_mode = st.sidebar.radio("Select Clearance Mode:", ["🕵️ Mission Terminal", "🔬 Multiverse Sandbox", "📚 Field Manual"])

if st.session_state.last_mode != app_mode:
    st.session_state.last_mode = app_mode
    play_sfx("click")  # Terminal click sound on tab switch

# 3. Trigger victory or alert sound effects during puzzle validation
if st.button("🚀 SUBMIT RE-CALIBRATION BEAM", use_container_width=True):
    param_key = selected_param.split(" ")[0]
    
    if param_key == case_data["target_constant"] and abs(guessed_mult - case_data["target_multiplier"]) < 0.06:
        play_sfx("success")  # 🎶 Victory Major 7th chord chime
        st.markdown("<div class='success-alert'>✅ TIMELINE STABILIZED! Anomaly successfully collapsed.</div>", unsafe_allow_html=True)
        st.balloons()
    else:
        play_sfx("error")  # 🚨 Low pitch sawtooth alarm drop
        st.markdown("<div class='anomaly-alert'>❌ CALIBRATION REJECTED! Timeline feedback loop destabilizing.</div>", unsafe_allow_html=True)
