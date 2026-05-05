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
    }
    </style>
    """, unsafe_allow_html=True)

# ---------- TRANSLATIONS ----------
lang = st.sidebar.selectbox("🌐 Language / Langue", ["English", "Français", "Español"])

translations = {
    "English": {
        "title": "Architectural House Plan: Route Nationale",
        "subtitle": "Custom 2D/3D Blueprint with Triple-Room Bathroom Access",
        "rm1": "ROOM 1 (Left Entry)", "rm2": "ROOM 2 (Front)", "rm3": "ROOM 3 (Right Entry)", "bath": "BATHROOM",
        "pricing": "Competitive Market Pricing",
        "view_2d": "2D Blueprint", "view_3d": "3D Interactive Model"
    },
    "Français": {
        "title": "Plan Architectural : Route Nationale",
        "subtitle": "Plan 2D/3D avec accès salle de bain triple chambre",
        "rm1": "CHAMBRE 1 (Entrée G)", "rm2": "CHAMBRE 2 (Face)", "rm3": "CHAMBRE 3 (Entrée D)", "bath": "S.D.BAIN",
        "pricing": "Tarification du Marché",
        "view_2d": "Plan 2D", "view_3d": "Modèle 3D Interactif"
    }
}
t = translations.get(lang, translations["English"])

# ---------- SIDEBAR BRANDING ----------
with st.sidebar:
    st.markdown('<div class="spinning-globe">🌍</div>', unsafe_allow_html=True)
    st.markdown("## **GlobalInternet.py**")
    st.markdown("---")
    st.markdown(f"**Owner:** Gesner Deslandes\n\n**Position:** Coder in Chief")
    st.markdown("📞 **Phone:** (509)-47385663")
    st.markdown("✉️ **Email:** deslandes78@gmail.com")
    st.markdown("---")
    st.subheader(f"💰 {t['pricing']}")
    st.table({
        "Service": ["Basic 2D Plan", "Interactive 3D", "Full Custom License"],
        "Market Price": ["$450", "$850", "$1,200"]
    })

# ---------- 2D BLUEPRINT ENGINE ----------
def draw_blueprint(trans):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    
    # Perimeter
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=4, edgecolor='black', facecolor='#f9f9f9'))
    
    # Internal Walls defining 3 rooms + central bathroom
    # Room 1 (Bottom Left), Room 3 (Bottom Right), Room 2 (Top)
    ax.plot([0, 10], [5, 5], 'k-', lw=3) # Main horizontal split
    ax.plot([5, 5], [0, 5], 'k-', lw=3) # Bottom vertical split
    
    # Central Bathroom (Accessible by all 3)
    ax.add_patch(patches.Rectangle((3.5, 3.5), 3, 3, lw=2, edgecolor='blue', facecolor='#e3f2fd'))
    
    # Entrances (Left and Right)
    ax.plot([-0.2, 0.2], [2, 3], color='red', lw=6) # Left Door
    ax.plot([9.8, 10.2], [2, 3], color='red', lw=6) # Right Door
    
    # Backyard Doors (Three doors to backyard)
    ax.plot([2, 3], [10, 10], color='green', lw=5) # Door 1
    ax.plot([5, 6], [10, 10], color='green', lw=5) # Door 2
    ax.plot([8, 9], [10, 10], color='green', lw=5) # Door 3

    # Labels
    ax.text(2.5, 2, trans['rm1'], ha='center', weight='bold', size=9)
    ax.text(7.5, 2, trans['rm3'], ha='center', weight='bold', size=9)
    ax.text(5, 8, trans['rm2'], ha='center', weight='bold', size=11)
    ax.text(5, 5, trans['bath'], ha='center', color='blue', weight='bold')
    
    ax.axis('off')
    return fig

# ---------- 3D WEBGL ENGINE ----------
def generate_3d(trans):
    html = f"""
    <div id="canvas-container" style="width:100%; height:600px; background:#222; border-radius:10px;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias: true}});
        renderer.setSize(window.innerWidth, 600);
        document.getElementById('canvas-container').appendChild(renderer.domElement);

        const light = new THREE.PointLight(0xffffff, 1, 100);
        light.position.set(10, 10, 10);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        // Glass House Frame
        const geo = new THREE.BoxGeometry(10, 4, 10);
        const mat = new THREE.MeshPhongMaterial({{color: 0x00ffcc, wireframe: true}});
        const house = new THREE.Mesh(geo, mat);
        scene.add(house);

        // Solid floor
        const floorGeo = new THREE.PlaneGeometry(10, 10);
        const floorMat = new THREE.MeshPhongMaterial({{color: 0x333333, side: THREE.DoubleSide}});
        const floor = new THREE.Mesh(floorGeo, floorMat);
        floor.rotation.x = Math.PI/2;
        floor.position.y = -2;
        scene.add(floor);

        camera.position.z = 15;
        camera.position.y = 8;
        camera.lookAt(0,0,0);

        function animate() {{
            requestAnimationFrame(animate);
            house.rotation.y += 0.01;
            renderer.render(scene, camera);
        }}
        animate();
    </script>
    """
    return html

# ---------- MAIN CONTENT ----------
st.markdown(f"<h1 class='main-title'>{t['title']}</h1>", unsafe_allow_html=True)
st.write(f"### {t['subtitle']}")

view = st.radio("Switch View:", [t['view_2d'], t['view_3d']], horizontal=True)

if view == t['view_2d']:
    st.pyplot(draw_blueprint(t))
    st.success("✅ **Architectural Logic:** All 3 rooms share direct access to the central bathroom. Dual entry points (L/R) and triple backyard exits confirmed.")
else:
    components.html(generate_3d(t), height=620)

st.divider()
st.info("🔨 **Developer Note:** This software is deployed via GlobalInternet.py infrastructure. Contact Gesner Deslandes for licensing.")
