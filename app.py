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
        "rm1": "ROOM 1 (Entry)", "rm2": "ROOM 2", "rm3": "ROOM 3", "bath": "BATHROOM",
        "legend": "📐 Blueprint Legend",
        "logic": "Layout: 3 Rooms + 1 central Bath. All rooms have direct bathroom access. Two front entrances."
    },
    "Français": {
        "view_2d": "Plan 2D",
        "view_3d": "Modèle 3D Interactif",
        "rm1": "CHAMBRE 1 (Entrée)", "rm2": "CHAMBRE 2", "rm3": "CHAMBRE 3", "bath": "S.D.BAIN",
        "legend": "📐 Légende du Plan",
        "logic": "Disposition : 3 chambres + 1 bain central. Accès direct au bain pour toutes les chambres."
    }
}
t = translations.get(lang, translations["English"])

# ---------- APPLICATION HEADER ----------
st.markdown('<div class="main-title">Dream Home PlanLogic 360</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Built by Gesner Deslandes</div>', unsafe_allow_html=True)

# ---------- 2D DRAFTING ENGINE ----------
def draw_2d_blueprint(trans):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=3, edgecolor='black', facecolor='none'))
    ax.plot([0, 10], [5, 5], 'k-', lw=3) 
    ax.plot([5, 5], [0, 5], 'k-', lw=3) 
    ax.plot([5, 5], [7, 10], 'k-', lw=3) 
    ax.add_patch(patches.Rectangle((4, 4), 2, 2, lw=2, color='skyblue', alpha=0.3))
    ax.plot([1, 2.5], [0, 0], 'r-', lw=6) 
    ax.plot([7.5, 9], [0, 0], 'r-', lw=6) 
    
    ax.text(2.5, 2.5, trans['rm1'], ha='center', weight='bold')
    ax.text(7.5, 2.5, trans['rm3'], ha='center', weight='bold')
    ax.text(5, 8, trans['rm2'], ha='center', weight='bold')
    ax.text(5, 5, trans['bath'], ha='center', size=9, color='blue', weight='bold')

    ax.axis('off')
    return fig

# ---------- 3D WEBGL ENGINE ----------
def generate_3d_view():
    html_code = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <div id="container" style="width: 100%; height: 600px; border-radius: 15px; overflow: hidden;"></div>
    <script>
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x222222);
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({antialias: true});
        renderer.setSize(window.innerWidth, 600);
        document.getElementById('container').appendChild(renderer.domElement);
        const light = new THREE.PointLight(0xffffff, 1, 100);
        light.position.set(10, 10, 10);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x888888));
        const geometry = new THREE.BoxGeometry(10, 3, 10);
        const material = new THREE.MeshPhongMaterial({color: 0x44aaee, wireframe: true});
        const house = new THREE.Mesh(geometry, material);
        scene.add(house);
        camera.position.set(8, 8, 8);
        camera.lookAt(0,0,0);
        function animate() {
            requestAnimationFrame(animate);
            house.rotation.y += 0.01;
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
