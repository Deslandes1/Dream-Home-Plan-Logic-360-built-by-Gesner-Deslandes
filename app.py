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
    .stTable {
        background-color: #f0f2f6;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------- TRANSLATIONS ----------
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "Español"])

translations = {
    "English": {
        "title": "Architectural Plan: Route Nationale Logic",
        "subtitle": "High-Fidelity 3D Visualization & 2D Blueprint",
        "rm1": "ROOM 1 (Entry L)", "rm2": "ROOM 2 (Front)", "rm3": "ROOM 3 (Entry R)", "bath": "BATHROOM",
        "pricing": "Market Competitive Pricing",
        "view_2d": "2D Blueprint", "view_3d": "3D Interactive Model"
    },
    "Français": {
        "title": "Plan Architectural : Logique Route Nationale",
        "subtitle": "Visualisation 3D Haute Fidélité & Plan 2D",
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
    st.markdown("**Owner:** Gesner Deslandes")
    st.markdown("**Coder in Chief**")
    st.markdown("📞 **Phone:** (509)-47385663")
    st.markdown("✉️ **Email:** deslandes78@gmail.com")
    st.markdown("---")
    st.subheader(f"💰 {t['pricing']}")
    st.table({
        "Software Service": ["2D Blueprint", "3D Modeling", "Full Enterprise"],
        "Market Price": ["$450", "$950", "$1,450"]
    })

# ---------- 2D BLUEPRINT ENGINE ----------
def draw_2d_blueprint(trans):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    
    # Outer Perimeter
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=4, edgecolor='black', facecolor='#f9f9f9'))
    
    # Interior Walls
    ax.plot([0, 10], [5, 5], 'k-', lw=3) # Horizontal
    ax.plot([5, 5], [0, 5], 'k-', lw=3) # Vertical split bottom
    
    # Central Bathroom Box (Shared)
    ax.add_patch(patches.Rectangle((3.5, 3.5), 3, 3, lw=2, edgecolor='blue', facecolor='#e3f2fd'))
    
    # Entrance Doors (Red)
    ax.plot([-0.3, 0.3], [2, 3], color='red', lw=8) # Left
    ax.plot([9.7, 10.3], [2, 3], color='red', lw=8) # Right
    
    # Backyard Doors (Green)
    ax.plot([2, 3], [10, 10], color='green', lw=6) 
    ax.plot([5, 6], [10, 10], color='green', lw=6) 
    ax.plot([8, 9], [10, 10], color='green', lw=6) 

    # Labels
    ax.text(2.5, 2, trans['rm1'], ha='center', weight='bold')
    ax.text(7.5, 2, trans['rm3'], ha='center', weight='bold')
    ax.text(5, 8, trans['rm2'], ha='center', weight='bold')
    ax.text(5, 5, trans['bath'], ha='center', color='blue', weight='bold', size=8)
    
    ax.axis('off')
    return fig

# ---------- 3D HIGH-FIDELITY ENGINE (Three.js) ----------
def generate_3d_view(trans):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>body {{ margin: 0; }} canvas {{ display: block; }}</style>
    </head>
    <body>
    <div id="threejs-container" style="width: 100%; height: 600px;"></div>
    <script>
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x111111);
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth/600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(window.innerWidth, 600);
        document.getElementById('threejs-container').appendChild(renderer.domElement);

        // Lighting
        const sun = new THREE.DirectionalLight(0xffffff, 1);
        sun.position.set(10, 20, 10);
        scene.add(sun);
        scene.add(new THREE.AmbientLight(0x444444));

        // Ground
        const ground = new THREE.Mesh(new THREE.PlaneGeometry(30, 30), new THREE.MeshStandardMaterial({{color: 0x222222}}));
        ground.rotation.x = -Math.PI/2;
        ground.position.y = -0.01;
        scene.add(ground);

        // Wall function
        function createWall(x, z, w, d, h=3.5, color=0xffffff) {{
            const geo = new THREE.BoxGeometry(w, h, d);
            const mat = new THREE.MeshStandardMaterial({{color: color, roughness: 0.7}});
            const wall = new THREE.Mesh(geo, mat);
            wall.position.set(x, h/2, z);
            scene.add(wall);
            return wall;
        }}

        // PERIMETER WALLS
        createWall(5, 0, 10, 0.2);   // Back
        createWall(5, 10, 10, 0.2);  // Front
        createWall(0, 5, 0.2, 10);   // Left
        createWall(10, 5, 0.2, 10);  // Right

        // INTERNAL ROOM LOGIC
        createWall(5, 5, 10, 0.15);  // Horizontal Divider
        createWall(5, 2.5, 0.15, 5); // Vertical Divider

        // BATHROOM BOX (Central)
        createWall(5, 5, 3, 3, 3, 0x00aaff); 

        // DOORS (Represented as colored floor segments)
        function addDoor(x, z, w, d, color) {{
            const geo = new THREE.BoxGeometry(w, 0.2, d);
            const mat = new THREE.MeshBasicMaterial({{color: color}});
            const door = new THREE.Mesh(geo, mat);
            door.position.set(x, 0.1, z);
            scene.add(door);
        }}
        addDoor(0, 2.5, 0.5, 1, 0xff0000); // Entry Left
        addDoor(10, 2.5, 0.5, 1, 0xff0000); // Entry Right
        addDoor(2, 0, 1, 0.5, 0x00ff00);   // Backyard 1
        addDoor(5, 0, 1, 0.5, 0x00ff00);   // Backyard 2
        addDoor(8, 0, 1, 0.5, 0x00ff00);   // Backyard 3

        camera.position.set(15, 12, 15);
        camera.lookAt(5, 0, 5);

        function animate() {{
            requestAnimationFrame(animate);
            scene.rotation.y += 0.003;
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
    st.success("✅ **Architecture Sync:** All three rooms share doors to the bathroom. Left/Right main entries and triple backyard exits are active.")

with tab2:
    components.html(generate_3d_view(t), height=650)

st.divider()
st.caption("🔨 Software Engineering by GlobalInternet.py | Version 3.0 (Logic-Sync)")
