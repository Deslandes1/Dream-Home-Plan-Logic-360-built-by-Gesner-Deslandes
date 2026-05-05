import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties

st.set_page_config(
    page_title="House Plan | 2D Blueprint & 3D Model",
    page_icon="🏠",
    layout="wide"
)

# ---------- LANGUAGE SELECTION ----------
lang = st.sidebar.selectbox("🌐 Language / Idioma / Langue", ["English", "Español", "Français"])

# ---------- TRANSLATIONS ----------
translations = {
    "English": {
        "title": "🏠 Architectural House Plan",
        "subtitle": "Switch between **2D engineering drawing** and **3D interactive model**.",
        "sidebar_logo": "🌍 GlobalInternet.py",
        "sidebar_name": "**Gesner Deslandes** – Coder in Chief",
        "sidebar_contact": "📞 (509)-47385663  |  ✉️ deslandes78@gmail.com",
        "pricing_title": "### 💰 Market Pricing (Competitive)",
        "pricing_basic": "- **Full house plan (2D + 3D):** **$1,500 USD**",
        "pricing_mod": "- **Custom modifications:** +$300",
        "pricing_landscape": "- **Landscape & exterior design:** +$500",
        "pricing_permit": "- **Permit‑ready drawings:** +$700",
        "pricing_package": "- **Complete package (all of the above):** **$2,800 USD**",
        "pricing_note": "💡 _Prices negotiable for volume or charity projects._",
        "land_title": "### 🌎 Required Land Size",
        "land_min": "The house shown here (18m × 12m footprint) plus yards, parking, and fence **requires approximately:**  \n- **0.25 acres** (1,000m²) for the house + immediate garden.",
        "land_comfort": "- **0.35 – 0.5 acres** for a comfortable layout with front/back yards, parking, and doghouse.",
        "land_reco": "- **Recommendation:** **0.4 acres** (1,600m²) for full privacy and room to expand.",
        "land_caption": "_Based on typical suburban zoning._",
        "footer": "🔨 **Built by GlobalInternet.py – Python software on demand**",
        "view_selector": "Select view:",
        "view_2d": "2D Blueprint",
        "view_3d": "3D Model",
        "legend_title": "📐 Legend & Instructions",
        "legend_text": """
        - **Black thick lines**: Walls  
        - **Blue arcs & lines**: Doors (arc = swing direction)  
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries (yard, parking)  
        - This is an architectural floor plan (top‑down view).
        """,
        "room_living": "LIVING ROOM",
        "room_kitchen": "KITCHEN",
        "room_bed1": "BEDROOM 1",
        "room_bed2": "BEDROOM 2",
        "room_bath": "BATH",
        "room_entry": "ENTRY",
        "yard_front": "FRONT YARD",
        "yard_back": "BACKYARD",
        "parking_label": "PARKING",
        "doghouse_label": "DOGHOUSE",
        "door_front_label": "FRONT DOOR",
        "info_title": "3D House Model",
        "info_features": "✅ Porch | ✅ Front/Back yards | ✅ Fence | ✅ Parking | ✅ Doghouse | ✅ Doors"
    },
    "Español": {
        "title": "🏠 Plano Arquitectónico",
        "subtitle": "Cambie entre **dibujo de ingeniería 2D** y **modelo interactivo 3D**.",
        "sidebar_logo": "🌍 GlobalInternet.py",
        "sidebar_name": "**Gesner Deslandes** – Jefe de Programación",
        "sidebar_contact": "📞 (509)-47385663  |  ✉️ deslandes78@gmail.com",
        "pricing_title": "### 💰 Precios de Mercado (Competitivos)",
        "pricing_basic": "- **Plano completo (2D + 3D):** **$1,500 USD**",
        "pricing_mod": "- **Modificaciones personalizadas:** +$300",
        "pricing_landscape": "- **Diseño de paisajismo y exteriores:** +$500",
        "pricing_permit": "- **Planos listos para permisos:** +$700",
        "pricing_package": "- **Paquete completo (todo lo anterior):** **$2,800 USD**",
        "pricing_note": "💡 _Precios negociables para proyectos comunitarios o de gran volumen._",
        "land_title": "### 🌎 Tamaño de Terreno Requerido",
        "land_min": "La casa mostrada (18m × 12m) más patios, estacionamiento y cerca **requiere aproximadamente:**  \n- **0.25 acres** (1,000m²) para la casa + jardín inmediato.",
        "land_comfort": "- **0.35 – 0.5 acres** para una distribución cómoda con patios delantero/trasero, estacionamiento y caseta para perro.",
        "land_reco": "- **Recomendación:** **0.4 acres** (1,600m²) para total privacidad y espacio para expandir.",
        "land_caption": "_Basado en zonificación suburbana típica._",
        "footer": "🔨 **Construido por GlobalInternet.py – Software Python bajo demanda**",
        "view_selector": "Seleccionar vista:",
        "view_2d": "Plano 2D",
        "view_3d": "Modelo 3D",
        "legend_title": "📐 Leyenda e Instrucciones",
        "legend_text": """
        - **Líneas negras gruesas**: Paredes  
        - **Líneas y arcos azules**: Puertas (el arco muestra dirección de apertura)  
        - **Segmentos azules gruesos**: Ventanas  
        - **Flechas rojas**: Dimensiones (metros)  
        - **Líneas verdes discontinuas**: Límites de propiedad (jardín, estacionamiento)  
        - Plano arquitectónico (vista superior).
        """,
        "room_living": "SALA DE ESTAR",
        "room_kitchen": "COCINA",
        "room_bed1": "DORMITORIO 1",
        "room_bed2": "DORMITORIO 2",
        "room_bath": "BAÑO",
        "room_entry": "ENTRADA",
        "yard_front": "JARDÍN DELANTERO",
        "yard_back": "JARDÍN TRASERO",
        "parking_label": "ESTACIONAMIENTO",
        "doghouse_label": "CASETA PARA PERRO",
        "door_front_label": "PUERTA PRINCIPAL",
        "info_title": "Modelo de Casa 3D",
        "info_features": "✅ Porche | ✅ Jardín delantero/trasero | ✅ Cerca | ✅ Estacionamiento | ✅ Caseta | ✅ Puertas"
    },
    "Français": {
        "title": "🏠 Plan Architectural",
        "subtitle": "Passez du **dessin technique 2D** au **modèle interactif 3D**.",
        "sidebar_logo": "🌍 GlobalInternet.py",
        "sidebar_name": "**Gesner Deslandes** – Chef Programmeur",
        "sidebar_contact": "📞 (509)-47385663  |  ✉️ deslandes78@gmail.com",
        "pricing_title": "### 💰 Tarifs Concurrentiels",
        "pricing_basic": "- **Plan complet (2D + 3D) :** **1 500 USD**",
        "pricing_mod": "- **Modifications personnalisées :** +300 USD",
        "pricing_landscape": "- **Aménagement paysager et extérieurs :** +500 USD",
        "pricing_permit": "- **Plans pour permis de construire :** +700 USD",
        "pricing_package": "- **Forfait complet (tout inclus) :** **2 800 USD**",
        "pricing_note": "💡 _Prix négociables pour projets caritatifs ou en volume._",
        "land_title": "### 🌎 Superficie de Terrain Nécessaire",
        "land_min": "La maison présentée (18m × 12m) plus jardins, parking et clôture **nécessite environ :**  \n- **0,25 acre** (1 000m²) pour la maison + jardin immédiat.",
        "land_comfort": "- **0,35 – 0,5 acre** pour une configuration confortable avec jardin avant/arrière, parking et niche.",
        "land_reco": "- **Recommandation :** **0,4 acre** (1 600m²) pour une intimité totale et de l'espace pour agrandir.",
        "land_caption": "_Basé sur un zonage suburbain typique._",
        "footer": "🔨 **Construition par GlobalInternet.py – Logiciels Python à la demande**",
        "view_selector": "Choisir la vue :",
        "view_2d": "Plan 2D",
        "view_3d": "Modèle 3D",
        "legend_title": "📐 Légende et Instructions",
        "legend_text": """
        - **Lignes noires épaisses** : Murs  
        - **Lignes et arcs bleus** : Portes (l'arc indique le sens d'ouverture)  
        - **Segments bleus épais** : Fenêtres  
        - **Flèches rouges** : Dimensions (mètres)  
        - **Lignes vertes pointillées** : Limites de propriété (jardin, parking)  
        - Plan architectural (vue de dessus).
        """,
        "room_living": "SALON",
        "room_kitchen": "CUISINE",
        "room_bed1": "CHAMBRE 1",
        "room_bed2": "CHAMBRE 2",
        "room_bath": "SALLE DE BAIN",
        "room_entry": "ENTRÉE",
        "yard_front": "JARDIN AVANT",
        "yard_back": "JARDIN ARRIÈRE",
        "parking_label": "PARKING",
        "doghouse_label": "NICHE",
        "door_front_label": "PORTE D'ENTRÉE",
        "info_title": "Modèle 3D de la Maison",
        "info_features": "✅ Porche | ✅ Jardins avant/arrière | ✅ Clôture | ✅ Parking | ✅ Niche | ✅ Portes"
    }
}

t = translations[lang]

# ---------- SIDEBAR CONTENT ----------
with st.sidebar:
    st.markdown(f"## {t['sidebar_logo']}")
    st.markdown(t['sidebar_name'])
    st.markdown(t['sidebar_contact'])
    st.markdown("---")
    st.markdown(t['pricing_title'])
    st.markdown(t['pricing_basic'])
    st.markdown(t['pricing_mod'])
    st.markdown(t['pricing_landscape'])
    st.markdown(t['pricing_permit'])
    st.markdown(t['pricing_package'])
    st.info(t['pricing_note'])
    st.markdown("---")
    st.markdown(t['land_title'])
    st.markdown(t['land_min'])
    st.markdown(t['land_comfort'])
    st.markdown(t['land_reco'])
    st.caption(t['land_caption'])
    st.markdown("---")
    st.markdown(t['footer'])

view = st.sidebar.radio(t['view_selector'], [t['view_2d'], t['view_3d']])

# ---------- 2D DRAWING FUNCTION ----------
def draw_house_plan(trans):
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-5, 25)
    ax.set_ylim(-5, 18)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    
    # Outer walls
    walls = [((0,0), (18,0)), ((18,0), (18,12)), ((18,12), (0,12)), ((0,12), (0,0))]
    for (x1,y1), (x2,y2) in walls:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=4, solid_capstyle='round')

    # Inner walls
    ax.plot([10, 10], [0, 7], 'k-', linewidth=4)
    ax.plot([10, 18], [7, 7], 'k-', linewidth=4)
    ax.plot([14, 18], [4, 4], 'k-', linewidth=4)
    ax.plot([14, 14], [4, 7], 'k-', linewidth=4)

    # Room labels
    font = FontProperties(weight='bold', size=10)
    ax.text(5, 6, trans['room_living'], ha='center', va='center', fontproperties=font)
    ax.text(14, 3, trans['room_kitchen'], ha='center', va='center', fontproperties=font)
    ax.text(14, 9.5, trans['room_bed1'], ha='center', va='center', fontproperties=font)
    ax.text(6, 9.5, trans['room_bed2'], ha='center', va='center', fontproperties=font)
    ax.text(16, 5.5, trans['room_bath'], ha='center', va='center', fontproperties=font)
    
    return fig

# ---------- 3D MODEL HTML ----------
def generate_3d_house(trans):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; overflow: hidden; }}
            #info {{
                position: absolute; top: 20px; left: 20px; color: white;
                background: rgba(0,0,0,0.7); padding: 15px; border-radius: 8px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                pointer-events: none; z-index: 100; border: 1px solid #444;
            }}
        </style>
    </head>
    <body>
        <div id="info">
            <strong style="color: #4CAF50; font-size: 1.2em;">{trans['info_title']}</strong><br>
            <span style="font-size: 0.9em; opacity: 0.8;">Drag: Rotate | Right-Click: Pan | Scroll: Zoom</span><br>
            <hr style="border: 0; border-top: 1px solid #555; margin: 10px 0;">
            {trans['info_features']}
        </div>
        <script type="importmap">
            {{
                "imports": {{
                    "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                    "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
                }}
            }}
        </script>
        <script type="module">
            import * as THREE from 'three';
            import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';
            import {{ CSS2DRenderer, CSS2DObject }} from 'three/addons/renderers/CSS2DRenderer.js';

            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x1a1a2e);
            
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(25, 20, 25);

            const renderer = new THREE.WebGLRenderer({{ antialias: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.body.appendChild(renderer.domElement);

            const labelRenderer = new CSS2DRenderer();
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.domElement.style.position = 'absolute';
            labelRenderer.domElement.style.top = '0px';
            labelRenderer.domElement.style.pointerEvents = 'none';
            document.body.appendChild(labelRenderer.domElement);

            const controls = new OrbitControls(camera, renderer.domElement);
            controls.target.set(9, 0, 6);

            // Lighting
            scene.add(new THREE.AmbientLight(0xffffff, 0.6));
            const sun = new THREE.DirectionalLight(0xffffff, 0.8);
            sun.position.set(20, 30, 10);
            sun.castShadow = true;
            scene.add(sun);

            // Ground & Landscape
            const grass = new THREE.Mesh(new THREE.PlaneGeometry(40, 40), new THREE.MeshStandardMaterial({{ color: 0x2d5a27 }}));
            grass.rotation.x = -Math.PI / 2;
            grass.receiveShadow = true;
            scene.add(grass);

            // House Walls
            const wallMat = new THREE.MeshStandardMaterial({{ color: 0xf0f0f0, roughness: 0.5 }});
            function createWall(x, z, w, d, h=3) {{
                const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), wallMat);
                mesh.position.set(x, h/2, z);
                mesh.castShadow = true;
                mesh.receiveShadow = true;
                scene.add(mesh);
            }}

            // Main Structure
            createWall(9, 0, 18, 0.3);   // Back
            createWall(9, 12, 18, 0.3);  // Front
            createWall(0, 6, 0.3, 12);   // Left
            createWall(18, 6, 0.3, 12);  // Right
            
            // Interior Partition
            createWall(10, 3.5, 0.2, 7); 

            // Porch
            const porch = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2), new THREE.MeshStandardMaterial({{color: 0x8b4513}}));
            porch.position.set(5, 0.1, 13);
            scene.add(porch);

            // Doghouse
            const doghouse = new THREE.Group();
            const dBase = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshStandardMaterial({{color: 0x5d4037}}));
            dBase.position.y = 0.5;
            doghouse.add(dBase);
            doghouse.position.set(15, 0, 14);
            scene.add(doghouse);

            // Labels
            function addLabel(name, x, z) {{
                const div = document.createElement('div');
                div.textContent = name;
                div.style.color = 'white';
                div.style.background = 'rgba(0,0,0,0.6)';
                div.style.padding = '2px 8px';
                div.style.borderRadius = '4px';
                div.style.fontSize = '12px';
                const label = new CSS2DObject(div);
                label.position.set(x, 3.5, z);
                scene.add(label);
            }}
            addLabel("{trans['room_living']}", 5, 6);
            addLabel("{trans['room_kitchen']}", 14, 3);
            addLabel("{trans['doghouse_label']}", 15, 14);

            function animate() {{
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }}
            animate();
            window.onresize = () => {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                labelRenderer.setSize(window.innerWidth, window.innerHeight);
            }};
        </script>
    </body>
    </html>
    """
    return html

# ---------- DISPLAY ----------
st.title(t['title'])
if view == t['view_2d']:
    st.pyplot(draw_house_plan(t))
else:
    components.html(generate_3d_house(t), height=700)
