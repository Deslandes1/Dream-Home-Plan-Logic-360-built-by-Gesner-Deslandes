import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Route Nationale House | 2D & 3D",
    page_icon="🏠",
    layout="wide"
)

# ---------- SIDEBAR & TRANSLATIONS ----------
# Added "Español" to the logic so it doesn't default to English unexpectedly
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "Español"])

translations = {
    "English": {
        "title": "🏠 House Concept: Route Nationale",
        "subtitle": "Interactive 2D/3D visualization based on your sketch.",
        "view_2d": "2D Blueprint",
        "view_3d": "3D Interactive Model",
        "rm1": "ROOM 1 (Entry)", "rm2": "ROOM 2", "rm3": "ROOM 3", "bath": "BATHROOM",
        "legend": "📐 Blueprint Legend",
        "logic": "All 3 rooms have direct doors to the bathroom. Two front entrances (Left/Right)."
    },
    "Français": {
        "title": "🏠 Concept de Maison : Route Nationale",
        "subtitle": "Visualisation interactive 2D/3D basée sur votre croquis.",
        "view_2d": "Plan 2D",
        "view_3d": "Modèle 3D Interactif",
        "rm1": "CHAMBRE 1 (Entrée)", "rm2": "CHAMBRE 2", "rm3": "CHAMBRE 3", "bath": "S.D.BAIN",
        "legend": "📐 Légende du Plan",
        "logic": "Les 3 chambres ont des portes directes vers la salle de bain. Deux entrées (Gauche/Droite)."
    },
    "Español": {
        "title": "🏠 Concepto de Casa: Route Nationale",
        "subtitle": "Visualización interactiva 2D/3D basada en su boceto.",
        "view_2d": "Plano 2D",
        "view_3d": "Modelo 3D Interactivo",
        "rm1": "HABITACIÓN 1 (Entrada)", "rm2": "HABITACIÓN 2", "rm3": "HABITACIÓN 3", "bath": "BAÑO",
        "legend": "📐 Leyenda del Plano",
        "logic": "Las 3 habitaciones tienen puertas directas al baño. Dos entradas frontales."
    }
}

t = translations.get(lang, translations["English"])

# ---------- 2D DRAFTING ENGINE ----------
def draw_2d_blueprint(trans):
    # Using 'plt.subplots' and returning 'fig' is the best practice for Streamlit
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    
    # Outer Perimeter
    ax.add_patch(patches.Rectangle((0, 0), 10, 10, linewidth=3, edgecolor='black', facecolor='none'))
    
    # Interior Walls
    ax.plot([0, 10], [5, 5], 'k-', lw=3) # Horizontal split
    ax.plot([5, 5], [0, 5], 'k-', lw=3) # Vertical split bottom
    ax.plot([5, 5], [7, 10], 'k-', lw=3) # Vertical split top
    
    # Central Bathroom Box
    ax.add_patch(patches.Rectangle((4, 4), 2, 2, lw=2, color='gray', alpha=0.3))
    
    # Entrances (Red segments)
    ax.plot([1, 2], [0, 0], 'r-', lw=5) # Left Entry
    ax.plot([8, 9], [0, 0], 'r-', lw=5) # Right Entry
    
    # Room Labels
    ax.text(2.5, 2.5, trans['rm1'], ha='center', weight='bold')
    ax.text(7.5, 2.5, trans['rm3'], ha='center', weight='bold')
    ax.text(5, 8, trans['rm2'], ha='center', weight='bold')
    ax.text(5, 5, trans['bath'], ha='center', size=8, color='blue')

    ax.axis('off')
    return fig

# ---------- 3D WEBGL ENGINE ----------
def generate_3d_view():
    # Streamlined JS for better performance
    html_code = """
    <div id="container" style="width: 100%; height: 600px; background-color: #f0f0f0;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xf0f0f0);
        const container = document.getElementById('container');
        const camera = new THREE.PerspectiveCamera(75, container.offsetWidth / 600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({antialias: true});
        renderer.setSize(container.offsetWidth, 600);
        container.appendChild(renderer.domElement);

        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(5, 10, 7.5).normalize();
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        // House Block
        const geometry = new THREE.BoxGeometry(10, 3, 10);
        const material = new THREE.MeshPhongMaterial({color: 0xcccccc, transparent: true, opacity: 0.7});
        const house = new THREE.Mesh(geometry, material);
        scene.add(house);

        // Ground
        const ground = new THREE.Mesh(new THREE.PlaneGeometry(20, 20), new THREE.MeshPhongMaterial({color: 0x999999}));
        ground.rotation.x = -Math.PI/2;
        ground.position.y = -1.5;
        scene.add(ground);

        camera.position.set(12, 12, 12);
        camera.lookAt(0,0,0);

        function animate() {
            requestAnimationFrame(animate);
            house.rotation.y += 0.005;
            renderer.render(scene, camera);
        }
        animate();
        
        window.addEventListener('resize', () => {
            renderer.setSize(container.offsetWidth, 600);
            camera.aspect = container.offsetWidth / 600;
            camera.updateProjectionMatrix();
        });
    </script>
    """
    return html_code

# ---------- APP UI ----------
st.sidebar.markdown(f"**Coder:** Gesner Deslandes")
view_mode = st.sidebar.radio("Navigation", [t['view_2d'], t['view_3d']])

st.title(t['title'])
st.write(t['subtitle'])

if view_mode == t['view_2d']:
    fig = draw_2d_blueprint(t)
    st.pyplot(fig)
    plt.close(fig) # Memory safety
    st.info(f"**{t['legend']}:** {t['logic']}")
else:
    # Removed the 't' argument as it wasn't being used inside the 3D function
    components.html(generate_3d_view(), height=600)

st.divider()
st.caption("🔨 Built by GlobalInternet.py | Reference: Route Nationale Project 2026")
