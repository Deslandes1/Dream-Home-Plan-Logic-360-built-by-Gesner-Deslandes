import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- PAGE CONFIG ---
st.set_page_config(page_title="House Plan 2.0 | GlobalInternet.py", layout="wide")

# --- TRANSLATIONS ---
lang = st.sidebar.selectbox("🌐 Language", ["English", "Español", "Français"])

trans = {
    "English": {
        "title": "🏠 Architectural Plan: Integrated 2D & 3D",
        "living": "LIVING ROOM", "kitchen": "KITCHEN", "bed1": "BEDROOM 1", 
        "bed2": "BEDROOM 2", "bath": "BATH", "porch": "PORCH", 
        "dog": "DOGHOUSE", "park": "PARKING", "labels": "Labels"
    },
    "Español": {
        "title": "🏠 Plano Arquitectónico: 2D y 3D Integrados",
        "living": "SALA", "kitchen": "COCINA", "bed1": "DORMITORIO 1", 
        "bed2": "DORMITORIO 2", "bath": "BAÑO", "porch": "PORCHE", 
        "dog": "CASETA PERRO", "park": "PARKING", "labels": "Etiquetas"
    },
    "Français": {
        "title": "🏠 Plan Architectural : 2D et 3D Intégrés",
        "living": "SALON", "kitchen": "CUISINE", "bed1": "CHAMBRE 1", 
        "bed2": "CHAMBRE 2", "bath": "SDB", "porch": "PORCHE", 
        "dog": "NICHE", "park": "PARKING", "labels": "Étiquettes"
    }
}[lang]

# --- 2D BLUEPRINT ENGINE ---
def draw_2d_plan(t):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(-2, 20)
    ax.set_ylim(-5, 15)
    ax.set_aspect('equal')
    
    # Main Structure (18x12)
    rect = patches.Rectangle((0,0), 18, 12, linewidth=3, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    
    # Internal Walls
    ax.plot([10, 10], [0, 7], 'k-', lw=3)   # Vertical wall
    ax.plot([10, 18], [7, 7], 'k-', lw=3)   # Horizontal wall
    
    # Rooms
    ax.text(5, 6, t['living'], ha='center', fontweight='bold')
    ax.text(14, 3.5, t['kitchen'], ha='center', fontweight='bold')
    ax.text(5, 10, t['bed2'], ha='center', fontweight='bold')
    ax.text(14, 10, t['bed1'], ha='center', fontweight='bold')
    
    # Exterior Features
    ax.add_patch(patches.Rectangle((4, -2), 4, 2, color='peru', alpha=0.3)) # Porch
    ax.text(6, -1, t['porch'], ha='center', size=8)
    
    ax.add_patch(patches.Circle((16, -2), 1, color='brown', alpha=0.5)) # Doghouse
    ax.text(16, -3.5, t['dog'], ha='center', size=8)
    
    ax.set_axis_off()
    return fig

# --- 3D MODEL ENGINE ---
def generate_3d_view(t):
    html_code = f"""
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <div id="container" style="width: 100%; height: 600px; background: #111; border-radius: 15px;"></div>
    <script>
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x1a1a1a);
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth/600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias: true}});
        renderer.setSize(window.innerWidth, 600);
        document.getElementById('container').appendChild(renderer.domElement);

        // Lights
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(10, 20, 10);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        // Ground (Grass)
        const ground = new THREE.Mesh(new THREE.PlaneGeometry(40, 40), new THREE.MeshStandardMaterial({{color: 0x223311}}));
        ground.rotation.x = -Math.PI/2;
        scene.add(ground);

        // Walls Helper
        function createWall(x, z, w, d, h=3, color=0xeeeeee) {{
            const geo = new THREE.BoxGeometry(w, h, d);
            const mat = new THREE.MeshStandardMaterial({{color: color}});
            const mesh = new THREE.Mesh(geo, mat);
            mesh.position.set(x, h/2, z);
            scene.add(mesh);
        }}

        // Exterior Walls (Matching 2D 18x12)
        createWall(9, 0, 18, 0.2);   // Back
        createWall(9, 12, 18, 0.2);  // Front
        createWall(0, 6, 0.2, 12);   // Left
        createWall(18, 6, 0.2, 12);  // Right

        // Interior (Matching 2D)
        createWall(10, 3.5, 0.2, 7); // Partition

        // Porch (Matching 2D location)
        createWall(6, 13, 4, 2, 0.2, 0x8b4513); 

        // Doghouse
        createWall(16, 14, 1.5, 1.5, 1.2, 0x5d4037);

        camera.position.set(25, 20, 25);
        camera.lookAt(9, 0, 6);

        function animate() {{
            requestAnimationFrame(animate);
            scene.rotation.y += 0.002; // Slow auto-rotate
            renderer.render(scene, camera);
        }}
        animate();
    </script>
    """
    return html_code

# --- MAIN INTERFACE ---
st.title(trans['title'])

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 2D Technical Plan")
    st.pyplot(draw_2d_plan(trans))

with col2:
    st.subheader("🧊 3D Interactive Model")
    components.html(generate_3d_view(trans), height=620)

st.info(f"**Project Status:** 2D Layout mirrored to 3D environment. {trans['porch']} and {trans['dog']} positions synchronized.")
