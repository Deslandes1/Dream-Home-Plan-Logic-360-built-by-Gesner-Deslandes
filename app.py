import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Dream Home PlanLogic 360",
    page_icon="🏠",
    layout="wide"
)

# ---------- CUSTOM CSS FOR SPINNING GLOBE ----------
st.markdown("""
    <style>
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .spinning-globe {
        font-size: 50px;
        display: inline-block;
        animation: rotate 5s linear infinite;
        text-align: center;
    }
    .sidebar-header {
        text-align: center;
        margin-bottom: 20px;
    }
    .main-title {
        font-size: 32px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .main-subtitle {
        font-size: 18px;
        text-align: center;
        color: #4B5563;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR & BRANDING ----------
with st.sidebar:
    st.markdown('<div class="sidebar-header"><div class="spinning-globe">🌍</div></div>', unsafe_allow_html=True)
    st.title("GlobalInternet.py")
    st.subheader("Architecture & Software Solutions")
    st.markdown("---")
    st.markdown("**Owner:** Gerner Geslandes")
    st.markdown("**Coder in Chief:** Gesner Deslandes")
    st.markdown("📞 **Phone:** (509)-47385663")
    st.markdown("📧 **Email:** deslandes78@gmail.com")
    
    st.markdown("---")
    st.markdown("### 💰 Market Pricing")
    st.success("""
    **Standard Plan Package:**
    *   2D Technical Blueprints
    *   3D Interactive Model
    *   **Competitive Price: $1,500 USD**
    *   *Market Average: $2,200+*
    """)
    st.info("💡 *Custom modifications available on request.*")

# ---------- TRANSLATIONS ----------
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "Español"])

translations = {
    "English": {
        "view_2d": "2D Blueprint",
        "view_3d": "3D Interactive Model",
        "rm1": "MASTER BEDROOM", "rm2": "LIVING AREA", "rm3": "GUEST ROOM", "bath": "BATHROOM",
        "legend": "📐 Blueprint Legend",
        "logic": "Refined Layout: Professional wall thickness, window placements, and optimized flow."
    },
    "Français": {
        "view_2d": "Plan 2D",
        "view_3d": "Modèle 3D Interactif",
        "rm1": "CHAMBRE PRINCIPALE", "rm2": "SALON", "rm3": "CHAMBRE D'AMIS", "bath": "S.D.BAIN",
        "legend": "📐 Légende du Plan",
        "logic": "Disposition raffinée : Épaisseur des murs, fenêtres et circulation optimisée."
    }
}
t = translations.get(lang, translations["English"])

# ---------- APPLICATION HEADER ----------
st.markdown('<div class="main-title">Dream Home PlanLogic 360</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Designed by Gesner Deslandes</div>', unsafe_allow_html=True)

# ---------- 2D DRAFTING ENGINE (Refined) ----------
def draw_2d_blueprint(trans):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    
    # Exterior Walls (Thick)
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=6, edgecolor='#333333', facecolor='#f9f9f9'))
    
    # Interior Walls
    ax.plot([0, 10], [5, 5], color='#333333', lw=4) # Horizontal Split
    ax.plot([5, 5], [0, 5], color='#333333', lw=4) # Lower vertical split
    
    # Bathroom Box (Central)
    ax.add_patch(patches.Rectangle((4, 4), 2, 2, lw=2, edgecolor='blue', facecolor='#e0f2fe'))
    
    # Doors (Red indicators)
    ax.plot([1.5, 3], [0, 0], 'r-', lw=8) # Main Entrance
    ax.plot([5, 5], [1, 2.5], 'r-', lw=4) # Internal door
    
    # Windows (Blue indicators)
    ax.plot([0, 0], [7, 8.5], 'cyan', lw=4) # Window Left
    ax.plot([10, 10], [7, 8.5], 'cyan', lw=4) # Window Right

    # Room Labels
    ax.text(2.5, 2.5, trans['rm1'], ha='center', weight='bold', fontsize=10)
    ax.text(7.5, 2.5, trans['rm3'], ha='center', weight='bold', fontsize=10)
    ax.text(5, 7.5, trans['rm2'], ha='center', weight='bold', fontsize=12)
    ax.text(5, 5, trans['bath'], ha='center', size=8, color='blue', weight='bold')

    ax.axis('off')
    return fig

# ---------- 3D WEBGL ENGINE (Refined with Roof) ----------
def generate_3d_view():
    html_code = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <div id="container" style="width: 100%; height: 600px; border-radius: 15px; overflow: hidden; background: #111;"></div>
    <script>
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x1a1a1a);
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({antialias: true});
        renderer.setSize(window.innerWidth, 600);
        document.getElementById('container').appendChild(renderer.domElement);

        // Lights
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(5, 10, 7).normalize();
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        const group = new THREE.Group();

        // Floor
        const floorGeo = new THREE.BoxGeometry(10.5, 0.2, 10.5);
        const floorMat = new THREE.MeshPhongMaterial({color: 0x888888});
        const floor = new THREE.Mesh(floorGeo, floorMat);
        group.add(floor);

        // Main House Body (Solid Walls)
        const houseGeo = new THREE.BoxGeometry(10, 3, 10);
        const houseMat = new THREE.MeshPhongMaterial({color: 0xffffff, transparent: true, opacity: 0.9});
        const house = new THREE.Mesh(houseGeo, houseMat);
        house.position.y = 1.6;
        group.add(house);

        // Roof (Pyramid style)
        const roofGeo = new THREE.ConeGeometry(8, 4, 4);
        const roofMat = new THREE.MeshPhongMaterial({color: 0x8b0000});
        const roof = new THREE.Mesh(roofGeo, roofMat);
        roof.position.y = 5;
        roof.rotation.y = Math.PI / 4;
        group.add(roof);

        scene.add(group);

        camera.position.set(12, 10, 12);
        camera.lookAt(0, 2, 0);

        function animate() {
            requestAnimationFrame(animate);
            group.rotation.y += 0.005;
            renderer.render(scene, camera);
        }
        animate();
    </script>
    """
    return html_code

# ---------- APP UI ----------
view_mode = st.radio("Switch View:", [t['view_2d'], t['view_3d']], horizontal=True)

if view_mode == t['view_2d']:
    st.pyplot(draw_2d_blueprint(t))
    st.info(f"**{t['legend']}:** {t['logic']}")
else:
    components.html(generate_3d_view(), height=600)

st.divider()
st.markdown(f"© 2026 **GlobalInternet.py** | Dream Home PlanLogic 360 | Built by **Gesner Deslandes**")
