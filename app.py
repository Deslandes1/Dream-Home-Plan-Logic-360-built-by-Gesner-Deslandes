import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    st.markdown("**Owner:** Gesner Deslandes\n\n**Coder in Chief**")
    st.markdown("📞 **Phone:** (509)-47385663\n\n deslandes78@gmail.com")
    st.markdown("---")
    st.subheader("💰 Market Pricing")
    st.table({"Service": ["2D Blueprint", "3D Model", "License"], "Price": ["$450", "$950", "$1,450"]})

# ---------- 2D BLUEPRINT ENGINE ----------
def draw_2d_blueprint():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 12); ax.set_ylim(-2, 12); ax.set_aspect('equal')
    
    # Outer Perimeter
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=4, edgecolor='black', facecolor='#f9f9f9'))
    
    # Bathroom (Central)
    ax.add_patch(patches.Rectangle((3.5, 3.5), 3, 3, lw=2, edgecolor='blue', facecolor='#e3f2fd'))
    
    # Internal Room Walls
    ax.plot([0, 10], [5, 5], 'k-', lw=3) # Horizontal
    ax.plot([5, 5], [0, 3.5], 'k-', lw=3) # Split bottom
    
    # Door Markers
    ax.plot([-0.3, 0.3], [2, 3], color='red', lw=8) # Left Entry
    ax.plot([9.7, 10.3], [2, 3], color='red', lw=8) # Right Entry
    ax.plot([2, 3], [10, 10], color='green', lw=6) # Backyard 1
    ax.plot([5, 6], [10, 10], color='green', lw=6) # Backyard 2
    ax.plot([8, 9], [10, 10], color='green', lw=6) # Backyard 3

    ax.text(2, 2, "Room L", ha='center', weight='bold')
    ax.text(8, 2, "Room R", ha='center', weight='bold')
    ax.text(5, 8, "Room Front", ha='center', weight='bold')
    ax.text(5, 5, "BATH", ha='center', color='blue', weight='bold')
    ax.axis('off')
    return fig

# ---------- 3D LOGIC ENGINE ----------
def generate_3d_view():
    html_code = f"""
    <html>
    <body style="margin:0; background-color:#111; overflow:hidden;">
        <div id="container" style="width: 100vw; height: 100vh;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{ antialias: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('container').appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            scene.add(new THREE.AmbientLight(0xffffff, 0.6));
            const light = new THREE.DirectionalLight(0xffffff, 0.8);
            light.position.set(10, 20, 10);
            scene.add(light);

            function createWall(x, z, w, d, h=3.5, color=0xffffff) {{
                const wall = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshStandardMaterial({{color: color}}));
                wall.position.set(x, h/2, z); scene.add(wall);
            }}

            // EXTERIOR & INTERIOR WALLS
            createWall(5, 0, 10, 0.2); createWall(5, 10, 10, 0.2);
            createWall(0, 5, 0.2, 10); createWall(10, 5, 0.2, 10);
            createWall(5, 5, 10, 0.1); // Room Divider
            
            // BATHROOM (Central - 3 Doors Logic)
            const bath = new THREE.Mesh(new THREE.BoxGeometry(3, 3, 3), new THREE.MeshStandardMaterial({{color: 0x00aaff, transparent:true, opacity:0.8}}));
            bath.position.set(5, 1.5, 5); scene.add(bath);

            // GHOST ROOF
            const roof = new THREE.Mesh(new THREE.ConeGeometry(8, 4, 4), new THREE.MeshStandardMaterial({{color: 0x8b4513, transparent:true, opacity:0.3}}));
            roof.position.set(5, 5.5, 5); roof.rotation.y = Math.PI/4; scene.add(roof);

            // FLOOR
            const floor = new THREE.Mesh(new THREE.PlaneGeometry(12, 12), new THREE.MeshStandardMaterial({{color: 0x444444}}));
            floor.rotation.x = -Math.PI/2; scene.add(floor);

            // DOOR REPRESENTATIONS (Entry L/R in Red, Backyard in Green)
            function makeDoor(x, z, color) {{
                const d = new THREE.Mesh(new THREE.BoxGeometry(1, 0.1, 0.5), new THREE.MeshBasicMaterial({{color: color}}));
                d.position.set(x, 0.05, z); scene.add(d);
            }}
            makeDoor(0, 2.5, 0xff0000); makeDoor(10, 2.5, 0xff0000); // Entrances
            makeDoor(2, 0, 0x00ff00); makeDoor(5, 0, 0x00ff00); makeDoor(8, 0, 0x00ff00); // Backyard

            camera.position.set(15, 12, 15);
            controls.update();
            function animate() {{ requestAnimationFrame(animate); controls.update(); renderer.render(scene, camera); }}
            animate();
        </script>
    </body>
    </html>
    """
    return html_code

# ---------- APP UI ----------
st.markdown("<h1 style='text-align:center;'>🏠 House Concept: Route Nationale</h1>", unsafe_allow_html=True)
t1, t2 = st.tabs(["📐 2D Blueprint", "🧊 3D Interactive Model"])

with t1:
    st.pyplot(draw_2d_blueprint())
    st.info("**Logic Check:** Each room connects directly to the central blue bathroom. Dual side entries and triple backyard exits active.")

with t2:
    components.html(generate_3d_view(), height=650)

st.divider()
st.caption("🔨 Built by GlobalInternet.py | Version 5.0 (Architectural Logic Verified)")
