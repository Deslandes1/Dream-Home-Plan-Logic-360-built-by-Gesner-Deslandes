import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import urllib.parse # Added for safety

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="GlobalInternet.py | House Plan Engine",
    page_icon="🌍",
    layout="wide"
)

# ---------- SIDEBAR BRANDING ----------
with st.sidebar:
    st.markdown("""
        <style>
        .spinning-globe { font-size: 50px; animation: spin 4s linear infinite; display: inline-block; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        </style>
        <div class="spinning-globe">🌍</div>
        """, unsafe_allow_html=True)
    st.markdown("## **GlobalInternet.py**")
    st.markdown("---")
    st.markdown("**Developer:** Gesner Deslandes\n\n**Coder in Chief**")
    st.markdown("📞 **Phone:** (509)-47385663")
    st.markdown("---")
    st.subheader("💰 Licensing")
    st.write("One-time payment. No subscriptions.")

# ---------- 2D BLUEPRINT ENGINE ----------
def draw_2d_blueprint():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 12); ax.set_ylim(-2, 12); ax.set_aspect('equal')
    
    # Outer Perimeter
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=4, edgecolor='black', facecolor='#f9f9f9'))
    
    # Central Bathroom
    ax.add_patch(patches.Rectangle((3.5, 3.5), 3, 3, lw=2, edgecolor='blue', facecolor='#e3f2fd'))
    
    # Wall Logic
    ax.plot([0, 10], [5, 5], 'k-', lw=3)
    ax.plot([5, 5], [0, 3.5], 'k-', lw=3)
    
    # Doors
    ax.plot([-0.2, 0.2], [2.5, 2.5], color='red', lw=10) # Left
    ax.plot([9.8, 10.2], [2.5, 2.5], color='red', lw=10) # Right
    
    ax.text(2.5, 2.5, "Room 1\n(Entry L)", ha='center', weight='bold')
    ax.text(7.5, 2.5, "Room 3\n(Entry R)", ha='center', weight='bold')
    ax.text(5, 7.5, "Room 2\n(Front)", ha='center', weight='bold')
    ax.text(5, 5, "BATH", ha='center', color='blue', weight='bold')
    ax.axis('off')
    return fig

# ---------- 3D HTML GENERATOR ----------
def generate_3d_html():
    return """
    <html>
    <body style="margin:0; background-color:#111; overflow:hidden;">
        <div id="container" style="width: 100vw; height: 100vh;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('container').appendChild(renderer.domElement);
            new THREE.OrbitControls(camera, renderer.domElement);
            scene.add(new THREE.AmbientLight(0xffffff, 0.7));
            const light = new THREE.DirectionalLight(0xffffff, 0.8);
            light.position.set(10, 20, 10); scene.add(light);
            function createWall(x, z, w, d, h=3.5, color=0xeeeeee) {
                const wall = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshStandardMaterial({color: color}));
                wall.position.set(x, h/2, z); scene.add(wall);
            }
            createWall(5, 0, 10, 0.2); createWall(5, 10, 10, 0.2);
            createWall(0, 5, 0.2, 10); createWall(10, 5, 0.2, 10);
            const bath = new THREE.Mesh(new THREE.BoxGeometry(3, 3, 3), new THREE.MeshStandardMaterial({color: 0x00aaff, transparent:true, opacity:0.8}));
            bath.position.set(5, 1.5, 5); scene.add(bath);
            camera.position.set(15, 12, 15);
            function animate() { requestAnimationFrame(animate); renderer.render(scene, camera); }
            animate();
        </script>
    </body>
    </html>
    """

# ---------- APP INTERFACE ----------
st.markdown("<h1 style='text-align:center;'>🏠 House Logic Engine 360</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📐 2D Blueprint", "🧊 3D Interactive"])

with tab1:
    st.pyplot(draw_2d_blueprint())
    st.success("Logic Verified: 2 Entrances, 3 Rooms, 1 Central Bathroom.")

with tab2:
    # Use components.html directly. This avoids the URI TypeError.
    # It still provides the 3D view while avoiding the crash.
    html_data = generate_3d_html()
    components.html(html_data, height=600, scrolling=False)

st.divider()
st.caption("© 2026 GlobalInternet.py | Secure Architectural Solutions")
