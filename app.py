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

# ---------- BRANDING & STYLES ----------
st.markdown("""
    <style>
    .spinning-globe {
        font-size: 50px;
        animation: spin 4s linear infinite;
        display: inline-block;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .main-title {
        color: #1E88E5;
        font-family: 'Arial Black', sans-serif;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------- TRANSLATIONS ----------
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "Español"])

translations = {
    "English": {
        "title": "Architectural Plan: Route Nationale Logic",
        "subtitle": "High-Fidelity 3D Visualization (Click & Drag to Rotate)",
        "rm1": "ROOM 1 (Entry L)", "rm2": "ROOM 2 (Front)", "rm3": "ROOM 3 (Entry R)", "bath": "BATHROOM",
        "pricing": "Market Competitive Pricing",
        "view_2d": "2D Blueprint", "view_3d": "3D Interactive Model"
    },
    "Français": {
        "title": "Plan Architectural : Logique Route Nationale",
        "subtitle": "Visualisation 3D (Cliquer et glisser pour pivoter)",
        "rm1": "CHAMBRE 1 (Entrée G)", "rm2": "CHAMBRE 2 (Face)", "rm3": "CHAMBRE 3 (Entrée D)", "bath": "S.D.BAIN",
        "pricing": "Tarification Concurrentielle",
        "view_2d": "Plan 2D", "view_3d": "Modèle 3D Interactif"
    }
}
t = translations.get(lang, translations["English"])

# ---------- SIDEBAR BRANDING ----------
with st.sidebar:
    st.markdown('<div class="spinning-globe">🌍</div>', unsafe_allow_html=True)
    st.markdown("## **GlobalInternet.py**")
    st.markdown("---")
    st.markdown("**Owner:** Gesner Deslandes\n\n**Coder in Chief**")
    st.markdown("📞 **Phone:** (509)-47385663")
    st.markdown("✉️ **Email:** deslandes78@gmail.com")
    st.markdown("---")
    st.subheader(f"💰 {t['pricing']}")
    st.table({
        "Service": ["2D Plan", "3D Model", "License"],
        "Price": ["$450", "$950", "$1,450"]
    })

# ---------- 2D BLUEPRINT ENGINE ----------
def draw_2d_blueprint(trans):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=4, edgecolor='black', facecolor='#f9f9f9'))
    ax.plot([0, 10], [5, 5], 'k-', lw=3)
    ax.plot([5, 5], [0, 5], 'k-', lw=3)
    ax.add_patch(patches.Rectangle((3.5, 3.5), 3, 3, lw=2, edgecolor='blue', facecolor='#e3f2fd'))
    
    # Doors
    ax.plot([-0.3, 0.3], [2, 3], color='red', lw=8) # Left Entry
    ax.plot([9.7, 10.3], [2, 3], color='red', lw=8) # Right Entry
    ax.plot([2, 3], [10, 10], color='green', lw=6) # Backyard 1
    ax.plot([5, 6], [10, 10], color='green', lw=6) # Backyard 2
    ax.plot([8, 9], [10, 10], color='green', lw=6) # Backyard 3

    ax.text(2.5, 2, trans['rm1'], ha='center', weight='bold')
    ax.text(7.5, 2, trans['rm3'], ha='center', weight='bold')
    ax.text(5, 8, trans['rm2'], ha='center', weight='bold')
    ax.text(5, 5, trans['bath'], ha='center', color='blue', weight='bold', size=8)
    ax.axis('off')
    return fig

# ---------- 3D ENGINE (STABLE VERSION) ----------
def generate_3d_view(trans):
    html_code = f"""
    <html>
    <body style="margin:0; background-color:#111;">
        <div id="rd-container" style="width: 100vw; height: 100vh;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
        <script>
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x111111);
            const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{ antialias: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('rd-container').appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            
            const light = new THREE.DirectionalLight(0xffffff, 1.2);
            light.position.set(10, 20, 10);
            scene.add(light);
            scene.add(new THREE.AmbientLight(0x444444));

            // Ground
            const ground = new THREE.Mesh(new THREE.PlaneGeometry(30, 30), new THREE.MeshStandardMaterial({{color: 0x222222}}));
            ground.rotation.x = -Math.PI/2;
            scene.add(ground);

            function createWall(x, z, w, d, h=3.5, color=0xffffff) {{
                const wall = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshStandardMaterial({{color: color}}));
                wall.position.set(x, h/2, z);
                scene.add(wall);
            }}

            // House Perimeter (10x10)
            createWall(5, 0, 10, 0.2); createWall(5, 10, 10, 0.2);
            createWall(0, 5, 0.2, 10); createWall(10, 5, 0.2, 10);
            createWall(5, 5, 10, 0.1); // Inner split
            createWall(5, 2.5, 0.1, 5); // Room split

            // Bathroom (Blue Central)
            createWall(5, 5, 3, 3, 3, 0x00aaff);

            camera.position.set(15, 15, 15);
            controls.update();

            function animate() {{
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
            }}
            animate();
        </script>
    </body>
    </html>
    """
    return html_code

# ---------- MAIN INTERFACE ----------
st.markdown(f"<h1 class='main-title'>{t['title']}</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs([t['view_2d'], t['view_3d']])

with tab1:
    st.pyplot(draw_2d_blueprint(t))

with tab2:
    # Use a fixed height and let the component handle the internal 3D scene
    components.html(generate_3d_view(t), height=650, scrolling=False)

st.divider()
st.caption("🔨 Built by GlobalInternet.py | Gesner Deslandes - Software on Demand")
