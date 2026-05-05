import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import math
import numpy as np

st.set_page_config(
    page_title="GlobalInternet.py | House Plan 360",
    page_icon="🌍",
    layout="wide"
)

# ---------- SIDEBAR ----------
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
    st.markdown("**Developer:** Gesner Deslandes  \n**Coder in Chief**")
    st.markdown("📞 **Phone:** (509)-47385663")
    st.markdown("✉️ **Email:** deslandes78@gmail.com")
    st.markdown("---")
    st.subheader("💰 Licensing")
    st.write("One‑time payment. No subscriptions.")
    st.markdown("---")
    st.info("💡 Custom 3‑room design with multiple backyard & entrance doors.")

# ---------- DOOR ARC HELPER ----------
def draw_arc_door(ax, center, radius, orient_deg, swing_sign, lw):
    orient_rad = math.radians(orient_deg)
    p_end = (center[0] + radius * math.cos(orient_rad),
             center[1] + radius * math.sin(orient_rad))
    ax.plot([center[0], p_end[0]], [center[1], p_end[1]], 'k-', lw=lw, solid_capstyle='round')
    t1 = min(orient_deg, orient_deg + swing_sign * 90)
    t2 = max(orient_deg, orient_deg + swing_sign * 90)
    arc = patches.Arc(center, 2*radius, 2*radius, theta1=t1, theta2=t2, color='k', lw=lw)
    ax.add_patch(arc)

# ---------- 2D BLUEPRINT (new layout) ----------
def draw_2d_blueprint():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-2, 18)
    ax.set_ylim(-2, 14)
    ax.set_aspect('equal')
    ax.axis('off')

    # Outer walls (house footprint: width 14m, depth 10m)
    # Let's place house from x=0 to 14, y=0 to 10
    # Entrance (main road) at y=0 (bottom)
    # Backyard at y=10 (top)
    # Left and right walls at x=0 and x=14
    outer = [((0,0),(14,0)), ((14,0),(14,10)), ((14,10),(0,10)), ((0,10),(0,0))]
    for (x1,y1),(x2,y2) in outer:
        ax.plot([x1,x2],[y1,y2], 'k-', lw=4, solid_capstyle='round')

    # Internal walls
    # Two vertical walls dividing into three rooms (approx widths: 5, 4, 5)
    # Room 1 (left): x 0-5, Room 2 (middle): x 5-9, Room 3 (right): x 9-14
    # Horizontal walls at y=5 create corridor? No, the rooms span full depth, but we need doors to backyard.
    # Simpler: three rooms side by side, each with door to backyard (top wall) and two entrance doors (bottom wall) for left and right rooms.
    # Bathroom shared? Actually "all 3 rooms connected to bathroom" – best to place bathroom in the middle of the back wall.
    # Let's place bathroom as a small room at top center, with three doors (one from each room).
    # Bathroom dimensions: x=5 to 9, y=7 to 10 (3m deep)
    ax.plot([5,5],[7,10], 'k-', lw=2)   # left wall of bathroom
    ax.plot([9,9],[7,10], 'k-', lw=2)   # right wall of bathroom
    ax.plot([5,9],[7,7], 'k-', lw=2)    # front wall of bathroom (facing rooms)

    # Walls separating the three main rooms (full height from y=0 to y=7)
    ax.plot([5,5],[0,7], 'k-', lw=2)    # between room1 and room2 (up to bathroom)
    ax.plot([9,9],[0,7], 'k-', lw=2)    # between room2 and room3 (up to bathroom)

    # ----- DOORS -----
    # 2 entrance doors on main road (bottom wall)
    draw_arc_door(ax, (2.5,0), 0.6, -90, +1, 1.5)   # left entrance (room1)
    draw_arc_door(ax, (11.5,0), 0.6, -90, +1, 1.5)  # right entrance (room3)

    # Door between room1 and room2 (on the wall x=5 at y≈3)
    draw_arc_door(ax, (5,3), 0.6, 0, +1, 1.5)

    # Doors from each room to bathroom (on the wall y=7)
    # Room1 to bathroom: door at (x≈3, y=7)
    draw_arc_door(ax, (3,7), 0.6, 90, +1, 1.5)
    # Room2 to bathroom: door at (x≈7, y=7)
    draw_arc_door(ax, (7,7), 0.6, 90, +1, 1.5)
    # Room3 to bathroom: door at (x≈11, y=7)
    draw_arc_door(ax, (11,7), 0.6, 90, +1, 1.5)

    # Three doors to backyard (top wall, y=10)
    # Room1 backyard door at (x≈2.5, y=10)
    draw_arc_door(ax, (2.5,10), 0.6, 90, +1, 1.5)
    # Room2 backyard door at (x≈7, y=10)
    draw_arc_door(ax, (7,10), 0.6, 90, +1, 1.5)
    # Room3 backyard door at (x≈11.5, y=10)
    draw_arc_door(ax, (11.5,10), 0.6, 90, +1, 1.5)

    # Windows (optional, for realism)
    ax.plot([0,0],[2,4], 'b-', lw=3)      # left wall window
    ax.plot([14,14],[2,4], 'b-', lw=3)    # right wall window
    # bathroom window on back wall
    ax.plot([6,8],[10,10], 'b-', lw=3)

    # Room labels
    font = FontProperties(weight='bold', size=10)
    ax.text(2.5, 3.5, "ROOM 1", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))
    ax.text(7, 3.5, "ROOM 2", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))
    ax.text(11.5, 3.5, "ROOM 3", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))
    ax.text(7, 8.5, "BATHROOM", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))

    # Entrance labels
    ax.text(2.5, -0.5, "ENTRANCE\n(Left)", ha='center', fontsize=8, color='blue')
    ax.text(11.5, -0.5, "ENTRANCE\n(Right)", ha='center', fontsize=8, color='blue')
    ax.text(7, 10.5, "BACKYARD", ha='center', fontsize=8, color='green')

    # Simple dimensions
    ax.annotate('', xy=(0,-1.2), xytext=(14,-1.2), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(7,-1.7,"14.0 m", ha='center', color='red', fontsize=9)
    ax.annotate('', xy=(15,0), xytext=(15,10), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(15.5,5,"10.0 m", ha='center', color='red', fontsize=9, rotation=90)

    # Yard / fence boundary (simple property line)
    ax.plot([-2,-2],[-2,12], 'g--', lw=1, alpha=0.6)
    ax.plot([16,16],[-2,12], 'g--', lw=1, alpha=0.6)
    ax.plot([-2,16],[12,12], 'g--', lw=1, alpha=0.6)
    ax.plot([-2,16],[-2,-2], 'g--', lw=1, alpha=0.6)
    ax.text(-1,5,"FRONT YARD (Main Road)", rotation=90, fontsize=8, color='green', alpha=0.7)
    ax.text(8,11.5,"BACKYARD", fontsize=8, color='green', alpha=0.7, ha='center')

    return fig

# ---------- 3D MODEL (walls, doors, openings) ----------
def generate_3d_html():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>body {margin:0; overflow:hidden;}</style>
    </head>
    <body>
        <div id="info" style="position:absolute; top:20px; left:20px; color:white; background:rgba(0,0,0,0.6); padding:8px 15px; border-radius:8px; font-family:Arial; z-index:100; pointer-events:none;">
            🏠 3D House – Drag to rotate | Right‑click pan | Scroll zoom
        </div>
        <script type="importmap">
            {
                "imports": {
                    "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                    "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
                }
            }
        </script>
        <script type="module">
            import * as THREE from 'three';
            import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
            import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x111122);
            scene.fog = new THREE.FogExp2(0x111122, 0.008);
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 1000);
            camera.position.set(18, 12, 15);
            camera.lookAt(7, 0, 5);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.body.appendChild(renderer.domElement);
            const labelRenderer = new CSS2DRenderer();
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.domElement.style.position = 'absolute';
            labelRenderer.domElement.style.top = '0px';
            labelRenderer.domElement.style.left = '0px';
            document.body.appendChild(labelRenderer.domElement);
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.autoRotate = false;  // manual only
            controls.enableZoom = true;
            controls.enablePan = true;
            controls.target.set(7, 2, 5);

            // Lighting
            const ambient = new THREE.AmbientLight(0x404060);
            scene.add(ambient);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1);
            dirLight.position.set(10, 20, 5);
            dirLight.castShadow = true;
            scene.add(dirLight);
            const fill = new THREE.PointLight(0xccaa88, 0.3);
            fill.position.set(7, -1, 5);
            scene.add(fill);
            const rim = new THREE.PointLight(0xffaa66, 0.4);
            rim.position.set(0, 5, 15);
            scene.add(rim);

            // Ground (grass)
            const grassMat = new THREE.MeshStandardMaterial({ color: 0x5a9e4e, roughness: 0.8 });
            const ground = new THREE.Mesh(new THREE.PlaneGeometry(22, 18), grassMat);
            ground.rotation.x = -Math.PI/2;
            ground.position.y = -0.1;
            ground.receiveShadow = true;
            scene.add(ground);

            // Fence (simple property boundary)
            const fenceMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
            const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
            const fencePoints = [[-2,-2],[16,-2],[16,12],[-2,12],[-2,-2]];
            for(let i=0; i<fencePoints.length-1; i++) {
                const p1=fencePoints[i], p2=fencePoints[i+1];
                const dx=p2[0]-p1[0], dz=p2[1]-p1[1];
                const len = Math.hypot(dx,dz), ang = Math.atan2(dz,dx);
                const rail = new THREE.Mesh(new THREE.BoxGeometry(len, 0.1, 0.2), fenceMat);
                rail.position.set(p1[0]+dx/2, 0.8, p1[1]+dz/2);
                rail.rotation.y = ang;
                rail.castShadow = true;
                scene.add(rail);
                const num = Math.floor(len/2);
                for(let j=0; j<=num; j++) {
                    const t=j/num;
                    const px=p1[0]+dx*t, pz=p1[1]+dz*t;
                    const post = new THREE.Mesh(new THREE.BoxGeometry(0.2,1.2,0.2), postMat);
                    post.position.set(px,0.6,pz);
                    post.castShadow=true;
                    scene.add(post);
                }
            }

            // Walls (solid stucco)
            const wallMat = new THREE.MeshStandardMaterial({ color: 0xcdc9c9, roughness: 0.4 });
            const th=0.3, h=3.0;
            function addWall(x,z,w,d,rotY=0) {
                const box = new THREE.BoxGeometry(w, h, d);
                const mesh = new THREE.Mesh(box, wallMat);
                mesh.position.set(x, h/2, z);
                mesh.rotation.y = rotY;
                mesh.castShadow = mesh.receiveShadow = true;
                scene.add(mesh);
            }
            // Outer walls (x from 0 to 14, z from 0 to 10)
            addWall(7, 0, 14, th);   // bottom (entrance)
            addWall(14, 5, th, 10);  // right
            addWall(7, 10, 14, th);  // top (backyard)
            addWall(0, 5, th, 10);   // left

            // Internal walls
            // vertical walls at x=5 and x=9 (full depth except bathroom area)
            addWall(5, 3.5, th, 7);    // wall from z=0 to z=7 (between room1 & room2)
            addWall(9, 3.5, th, 7);    // wall from z=0 to z=7 (between room2 & room3)
            // bathroom walls (back section)
            addWall(7, 8.5, 4, th);    // front wall of bathroom at z=7 (from x=5 to 9)
            // side walls of bathroom (already partly covered by outer walls, but we need full height)
            addWall(5, 8.5, th, 3);    // left bathroom wall (z=7 to 10)
            addWall(9, 8.5, th, 3);    // right bathroom wall

            // Door openings: we don't draw solid walls where doors exist, so we omit those wall segments.
            // The internal walls above are continuous; but doors are indicated by absence of a wall section.
            // For simplicity, we keep walls as boxes and rely on visual of doors (3D door models) placed over openings.
            // We'll add simple door models (boxes) at each door location.

            const doorMat = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
            const knobMat = new THREE.MeshStandardMaterial({ color: 0xFFD700 });

            // Helper: add a door at (x, z, orientation: 'horizontal' or 'vertical')
            function addDoor(x, z, orient) {
                let door;
                if (orient === 'horizontal') {
                    door = new THREE.Mesh(new THREE.BoxGeometry(0.9, 2.0, 0.1), doorMat);
                    door.position.set(x, 1.0, z);
                } else {
                    door = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.0, 0.9), doorMat);
                    door.position.set(x, 1.0, z);
                }
                door.castShadow = true;
                scene.add(door);
                // add knob
                const knob = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
                if (orient === 'horizontal') knob.position.set(x + (Math.abs(x-2.5)<0.5 ? 0.3 : -0.3), 1.0, z);
                else knob.position.set(x, 1.0, z + (Math.abs(z-3)<0.5 ? 0.3 : -0.3));
                scene.add(knob);
            }

            // Entrance doors (x=2.5 and x=11.5 at z=0)
            addDoor(2.5, 0, 'horizontal');
            addDoor(11.5, 0, 'horizontal');
            // Door between room1 and room2 (x=5, z=3)
            addDoor(5, 3, 'vertical');
            // Doors from each room to bathroom (z=7)
            addDoor(3, 7, 'horizontal');   // room1
            addDoor(7, 7, 'horizontal');   // room2
            addDoor(11, 7, 'horizontal');  // room3
            // Three doors to backyard (z=10)
            addDoor(2.5, 10, 'horizontal');
            addDoor(7, 10, 'horizontal');
            addDoor(11.5, 10, 'horizontal');

            // Simple floor slab (semi-transparent)
            const floorMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c, roughness: 0.6, metalness: 0.05, transparent: true, opacity: 0.5 });
            const floor = new THREE.Mesh(new THREE.BoxGeometry(14, 0.1, 10), floorMat);
            floor.position.set(7, -0.05, 5);
            floor.receiveShadow = true;
            scene.add(floor);

            // Roof (simple gabled)
            const roofMat = new THREE.MeshStandardMaterial({ color: 0xaa7777 });
            const roof = new THREE.Mesh(new THREE.CylinderGeometry(8, 8, 1.2, 4), roofMat);
            roof.rotation.y = Math.PI/4;
            roof.position.set(7, 3.2, 5);
            roof.castShadow = true;
            scene.add(roof);

            // Labels (room names)
            function makeLabel(text,x,z,yOff=0.2) {
                const div=document.createElement('div');
                div.textContent=text;
                div.style.cssText='color:#ffdd99; font-size:16px; font-weight:bold; background:rgba(0,0,0,0.5); padding:2px 8px; border-radius:16px; border:1px solid #ffaa66;';
                const label=new CSS2DObject(div);
                label.position.set(x, yOff+1.0, z);
                scene.add(label);
            }
            makeLabel('ROOM 1', 2.5, 3);
            makeLabel('ROOM 2', 7, 3);
            makeLabel('ROOM 3', 11.5, 3);
            makeLabel('BATHROOM', 7, 8.5);
            makeLabel('BACKYARD', 7, 12, 0.5);
            makeLabel('ENTRANCE', 2.5, -1, 0);
            makeLabel('ENTRANCE', 11.5, -1, 0);

            // Simple front yard grass extension
            const frontYardMat = new THREE.MeshStandardMaterial({ color: 0x5a9e4e });
            const frontYard = new THREE.Mesh(new THREE.PlaneGeometry(14, 2), frontYardMat);
            frontYard.rotation.x = -Math.PI/2;
            frontYard.position.set(7, -0.12, -1.5);
            frontYard.receiveShadow = true;
            scene.add(frontYard);

            function animate() {
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }
            animate();
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                labelRenderer.setSize(window.innerWidth, window.innerHeight);
            });
        </script>
    </body>
    </html>
    """

# ---------- MAIN APP ----------
st.title("🏠 Custom House Logic Engine")
st.markdown("**3 rooms | Bathroom connected to all rooms | 3 backyard doors | 2 entrance doors**")

view = st.radio("Select view:", ["2D Blueprint", "3D Model"], horizontal=True)

if view == "2D Blueprint":
    fig = draw_2d_blueprint()
    st.pyplot(fig)
    with st.expander("📐 Legend & Instructions"):
        st.markdown("""
        - **Black thick lines**: Walls  
        - **Blue arcs**: Doors (arc shows swing direction)  
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries  
        - **Three rooms** – each connects to bathroom and backyard. Two entrance doors from main road.
        """)
else:
    st.markdown("### 🏡 3D Interactive Model")
    st.markdown("🖱️ **Left‑click + drag** to rotate | **Right‑click + drag** to pan | **Scroll** to zoom")
    components.html(generate_3d_html(), height=700, scrolling=False)
