import streamlit as st
import streamlit.components.v1 as components

def play_sfx(sound_type: str):
    """
    Injects a JavaScript Web Audio API synthesizer to play real-time 
    sci-fi sound effects directly in the user's browser.
    """
    sfx_scripts = {
        # High-tech confirmation chime (Major 7th chord arpeggio)
        "success": """
            <script>
            (() => {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const now = ctx.currentTime;
                const freqs = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
                freqs.forEach((f, i) => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(f, now + i * 0.07);
                    gain.gain.setValueAtTime(0.12, now + i * 0.07);
                    gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.07 + 0.35);
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.start(now + i * 0.07);
                    osc.stop(now + i * 0.07 + 0.35);
                });
            })();
            </script>
        """,
        
        # Low-frequency pitch drop (Alarm/Rejection tone)
        "error": """
            <script>
            (() => {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(220, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(55, ctx.currentTime + 0.45);
                gain.gain.setValueAtTime(0.15, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.45);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 0.45);
            })();
            </script>
        """,
        
        # Crisp high-tech terminal click/beep
        "click": """
            <script>
            (() => {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(1200, ctx.currentTime);
                gain.gain.setValueAtTime(0.08, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.06);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 0.06);
            })();
            </script>
        """,
        
        # Warp speed sweep (for slider adjustments or scan triggers)
        "scan": """
            <script>
            (() => {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(300, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(1800, ctx.currentTime + 0.25);
                gain.gain.setValueAtTime(0.1, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.25);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 0.25);
            })();
            </script>
        """
    }

    if sound_type in sfx_scripts:
        # Height and width set to 0 to keep the element invisible
        components.html(sfx_scripts[sound_type], height=0, width=0)


def render_ambient_audio():
    """
    Renders an unobtrusive ambient background synth stream in the sidebar.
    """
    st.sidebar.markdown("### 🎧 AGENCY COMMS & AMBIENCE")
    
    # Direct streaming sci-fi synth atmospheric drone loop (Royalty-free open stream)
    ambient_url = "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=sci-fi-ambient-110822.mp3"
    
    st.sidebar.audio(ambient_url, format="audio/mp3", loop=True)
    st.sidebar.caption("💡 *Enable audio playback to hear environmental synth drone.*")
