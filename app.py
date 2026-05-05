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
    st.info("💡 Professional 3D model with detailed door objects (no labels).")

# ---------- DOOR ARC HELPER (for 2D) ----------
def draw_arc_door(ax, center, radius, orient_deg, swing_sign, lw):
    orient_rad = math.radians(orient_deg)
    p_end = (center[0] + radius * math.cos(orient_rad),
             center[1] + radius * math.sin(orient_rad))
    ax.plot([center[0], p_end[0]], [center[1], p_end[1]], 'k-', lw=lw, solid_capstyle='round')
    t1 = min(orient_deg, orient_deg + swing_sign * 90)
    t2 = max(orient_deg, orient_deg + swing_sign * 90)
    arc = patches.Arc(center, 2*radius, 2*radius, theta1=t1, theta2=t2, color='k', lw=lw)
    ax.add_patch(arc)

# ---------- 2D BLUEPRINT (unchanged) ----------
def draw_2d_blueprint():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-2, 18)
    ax.set_ylim(-2, 14)
    ax.set_aspect('equal')
    ax.axis('off')

    # Outer walls
    outer = [((0,0),(14,0)), ((14,0),(14,10)), ((14,10),(0,10)), ((0,10),(0,0))]
    for (x1,y1),(x2,y2) in outer:
        ax.plot([x1,x2],[y1,y2], 'k-', lw=4, solid_capstyle='round')

    # Internal walls
    ax.plot([5,5],[7,10], 'k-', lw=2)   # left bathroom wall
    ax.plot([9,9],[7,10], 'k-', lw=2)   # right bathroom wall
    ax.plot([5,9],[7,7], 'k-', lw=2)    # front bathroom wall
    ax.plot([5,5],[0,7], 'k-', lw=2)    # between room1 & room2
    ax.plot([9,9],[0,7], 'k-', lw=2)    # between room2 & room3

    # Doors (2D representation)
    draw_arc_door(ax, (2.5,0), 0.6, -90, +1, 1.5)   # left entrance
    draw_arc_door(ax, (11.5,0), 0.6, -90, +1, 1.5)  # right entrance
    draw_arc_door(ax, (5,3), 0.6, 0, +1, 1.5)       # between room1 & room2
    draw_arc_door(ax, (3,7), 0.6, 90, +1, 1.5)      # room1 to bathroom
    draw_arc_door(ax, (7,7), 0.6, 90, +1, 1.5)      # room2 to bathroom
    draw_arc_door(ax, (11,7), 0.6, 90, +1, 1.5)     # room3 to bathroom
    draw_arc_door(ax, (2.5,10), 0.6, 90, +1, 1.5)   # room1 to backyard
    draw_arc_door(ax, (7,10), 0.6, 90, +1, 1.5)     # room2 to backyard
    draw_arc_door(ax, (11.5,10), 0.6, 90, +1, 1.5)  # room3 to backyard

    # Windows
    ax.plot([0,0],[2,4], 'b-', lw=3)
    ax.plot([14,14],[2,4], 'b-', lw=3)
    ax.plot([6,8],[10,10], 'b-', lw=3)

    # Labels
    font = FontProperties(weight='bold', size=10)
    ax.text(2.5, 3.5, "ROOM 1", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))
    ax.text(7, 3.5, "ROOM 2", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))
    ax.text(11.5, 3.5, "ROOM 3", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))
    ax.text(7, 8.5, "BATHROOM", ha='center', fontproperties=font, bbox=dict(facecolor='white',alpha=0.7))
    ax.text(2.5, -0.5, "ENTRANCE\n(Left)", ha='center', fontsize=8, color='blue')
    ax.text(11.5, -0.5, "ENTRANCE\n(Right)", ha='center', fontsize=8, color='blue')
    ax.text(7, 10.5, "BACKYARD", ha='center', fontsize=8, color='green')

    # Dimensions
    ax.annotate('', xy=(0,-1.2), xytext=(14,-1.2), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(7,-1.7,"14.0 m", ha='center', color='red', fontsize=9)
    ax.annotate('', xy=(15,0), xytext=(15,10), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(15.5,5,"10.0 m", ha='center', color='red', fontsize=9, rotation=90)

    # Property boundary
    ax.plot([-2,-2],[-2,12], 'g--', lw=1, alpha=0.6)
    ax.plot([16,16],[-2,12], 'g--', lw=1, alpha=0.6)
    ax.plot([-2,16],[12,12], 'g--', lw=1, alpha=0.6)
    ax.plot([-2,16],[-2,-2], 'g--', lw=1, alpha=0.6)
    ax.text(-1,5,"FRONT YARD (Main Road)", rotation=90, fontsize=8, color='green', alpha=0.7)
    ax.text(8,11.5,"BACKYARD", fontsize=8, color='green', alpha=0.7, ha='center')

    return fig

# ---------- 3D MODEL with detailed doors (no labels) ----------
def generate_3d_html():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; font-family: Arial, Helvetica, sans-serif; }
            #controls-note {
                position: absolute;
                bottom: 20px;
                left: 20px;
                color: white;
                background: rgba(0,0,0,0.6);
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 14px;
                pointer-events: none;
                z-index: 100;
            }
        </style>
    </head>
    <body>
        <div id="controls-note">
            🖱️ Left drag → rotate | Right drag → pan | Scroll → zoom
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

            // --- setup ---
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x111122);
            scene.fog = new THREE.FogExp2(0x111122, 0.008);
            
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(20, 12, 15);
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
            labelRenderer.domElement.style.pointerEvents = 'none';
            document.body.appendChild(labelRenderer.domElement);
            
            // --- OrbitControls ---
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.rotateSpeed = 1.0;
            controls.zoomSpeed = 1.2;
            controls.panSpeed = 0.8;
            controls.enableZoom = true;
            controls.enablePan = true;
            controls.enableRotate = true;
            controls.mouseButtons = {
                LEFT: THREE.MOUSE.ROTATE,
                RIGHT: THREE.MOUSE.PAN,
                MIDDLE: THREE.MOUSE.ZOOM
            };
            controls.target.set(7, 2, 5);
            
            // --- Lighting ---
            const ambient = new THREE.AmbientLight(0x404060);
            scene.add(ambient);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
            dirLight.position.set(10, 20, 5);
            dirLight.castShadow = true;
            scene.add(dirLight);
            const fill = new THREE.PointLight(0xccaa88, 0.3);
            fill.position.set(7, -1, 5);
            scene.add(fill);
            const rim = new THREE.PointLight(0xffaa66, 0.4);
            rim.position.set(0, 5, 15);
            scene.add(rim);
            
            // --- Ground (grass) ---
            const grassMat = new THREE.MeshStandardMaterial({ color: 0x5a9e4e, roughness: 0.8 });
            const ground = new THREE.Mesh(new THREE.PlaneGeometry(22, 18), grassMat);
            ground.rotation.x = -Math.PI/2;
            ground.position.y = -0.1;
            ground.receiveShadow = true;
            scene.add(ground);
            
            // --- Simple fence (posts + rails) ---
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
            
            // --- Walls (stucco) ---
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
            addWall(7, 0, 14, th);
            addWall(14, 5, th, 10);
            addWall(7, 10, 14, th);
            addWall(0, 5, th, 10);
            addWall(5, 3.5, th, 7);
            addWall(9, 3.5, th, 7);
            addWall(7, 8.5, 4, th);
            addWall(5, 8.5, th, 3);
            addWall(9, 8.5, th, 3);
            
            // ----- DETAILED DOOR MODEL (no labels, just 3D objects) -----
            const doorWood = new THREE.MeshStandardMaterial({ color: 0xc99e6f, roughness: 0.3 });
            const doorFrameMat = new THREE.MeshStandardMaterial({ color: 0xaa8866 });
            const handleMat = new THREE.MeshStandardMaterial({ color: 0xffaa66, metalness: 0.8 });
            const thresholdMat = new THREE.MeshStandardMaterial({ color: 0xcc8866 });
            
            function addDetailedDoor(x, z, orientation) {
                // orientation: 'horizontal' means door plane is vertical (rotated around Y) – for walls along X axis (front/back walls)
                // 'vertical' means door plane is horizontal – for walls along Z axis (side walls)
                // For simplicity, we model door as a box with a recessed panel and a handle.
                const doorWidth = 0.9;
                const doorHeight = 2.0;
                const doorThick = 0.08;
                const frameThick = 0.05;
                const frameMargin = 0.03;
                
                let doorMesh;
                if (orientation === 'horizontal') {
                    doorMesh = new THREE.Mesh(new THREE.BoxGeometry(doorWidth, doorHeight, doorThick), doorWood);
                    doorMesh.position.set(x, 1.0, z);
                } else {
                    doorMesh = new THREE.Mesh(new THREE.BoxGeometry(doorThick, doorHeight, doorWidth), doorWood);
                    doorMesh.position.set(x, 1.0, z);
                }
                doorMesh.castShadow = true;
                scene.add(doorMesh);
                
                // Add a recessed panel detail: a thinner, slightly inset box
                const panelMat = new THREE.MeshStandardMaterial({ color: 0xb88a5a });
                const panelWidth = doorWidth - 0.2;
                const panelHeight = doorHeight - 0.4;
                let panel;
                if (orientation === 'horizontal') {
                    panel = new THREE.Mesh(new THREE.BoxGeometry(panelWidth, panelHeight, 0.02), panelMat);
                    panel.position.set(x, 1.0, z + (doorThick/2 + 0.01));
                } else {
                    panel = new THREE.Mesh(new THREE.BoxGeometry(0.02, panelHeight, panelWidth), panelMat);
                    panel.position.set(x + (doorThick/2 + 0.01), 1.0, z);
                }
                panel.castShadow = true;
                scene.add(panel);
                
                // Door frame (4 sides)
                if (orientation === 'horizontal') {
                    const top = new THREE.Mesh(new THREE.BoxGeometry(doorWidth+frameMargin*2, frameThick, doorThick+0.02), doorFrameMat);
                    top.position.set(x, 1.0 + doorHeight/2 - frameThick/2, z); scene.add(top);
                    const bottom = new THREE.Mesh(new THREE.BoxGeometry(doorWidth+frameMargin*2, frameThick, doorThick+0.02), doorFrameMat);
                    bottom.position.set(x, 1.0 - doorHeight/2 + frameThick/2, z); scene.add(bottom);
                    const left = new THREE.Mesh(new THREE.BoxGeometry(frameThick, doorHeight, doorThick+0.02), doorFrameMat);
                    left.position.set(x - doorWidth/2 - frameMargin, 1.0, z); scene.add(left);
                    const right = new THREE.Mesh(new THREE.BoxGeometry(frameThick, doorHeight, doorThick+0.02), doorFrameMat);
                    right.position.set(x + doorWidth/2 + frameMargin, 1.0, z); scene.add(right);
                } else {
                    const top = new THREE.Mesh(new THREE.BoxGeometry(doorThick+0.02, frameThick, doorWidth+frameMargin*2), doorFrameMat);
                    top.position.set(x, 1.0 + doorHeight/2 - frameThick/2, z); scene.add(top);
                    const bottom = new THREE.Mesh(new THREE.BoxGeometry(doorThick+0.02, frameThick, doorWidth+frameMargin*2), doorFrameMat);
                    bottom.position.set(x, 1.0 - doorHeight/2 + frameThick/2, z); scene.add(bottom);
                    const left = new THREE.Mesh(new THREE.BoxGeometry(doorThick+0.02, doorHeight, frameThick), doorFrameMat);
                    left.position.set(x, 1.0, z - doorWidth/2 - frameMargin); scene.add(left);
                    const right = new THREE.Mesh(new THREE.BoxGeometry(doorThick+0.02, doorHeight, frameThick), doorFrameMat);
                    right.position.set(x, 1.0, z + doorWidth/2 + frameMargin); scene.add(right);
                }
                
                // Handle (knob)
                const knob = new THREE.Mesh(new THREE.SphereGeometry(0.07, 16, 16), handleMat);
                if (orientation === 'horizontal') knob.position.set(x + 0.3, 1.0, z + 0.09);
                else knob.position.set(x + 0.09, 1.0, z + 0.3);
                scene.add(knob);
                
                // Threshold (small step on the floor)
                const threshold = new THREE.Mesh(new THREE.BoxGeometry(doorWidth+0.1, 0.05, 0.2), thresholdMat);
                if (orientation === 'horizontal') {
                    threshold.position.set(x, -0.02, z);
                } else {
                    threshold.rotation.y = Math.PI/2;
                    threshold.position.set(x, -0.02, z);
                }
                threshold.receiveShadow = true;
                scene.add(threshold);
            }
            
            // Place all 9 doors with proper orientation
            addDetailedDoor(2.5, 0, 'horizontal');    // left entrance
            addDetailedDoor(11.5, 0, 'horizontal');   // right entrance
            addDetailedDoor(5, 3, 'vertical');        // between room1 & room2
            addDetailedDoor(3, 7, 'horizontal');      // room1 -> bathroom
            addDetailedDoor(7, 7, 'horizontal');      // room2 -> bathroom
            addDetailedDoor(11, 7, 'horizontal');     // room3 -> bathroom
            addDetailedDoor(2.5, 10, 'horizontal');   // room1 -> backyard
            addDetailedDoor(7, 10, 'horizontal');     // room2 -> backyard
            addDetailedDoor(11.5, 10, 'horizontal');  // room3 -> backyard
            
            // --- Bathroom fixtures (toilet, sink, shower) ---
            const bathFloorMat = new THREE.MeshStandardMaterial({ color: 0x88aaff, roughness: 0.3, metalness: 0.1 });
            const bathFloor = new THREE.Mesh(new THREE.BoxGeometry(4, 0.05, 3), bathFloorMat);
            bathFloor.position.set(7, -0.08, 8.5);
            bathFloor.receiveShadow = true;
            scene.add(bathFloor);
            
            const toiletBase = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.6, 0.8), new THREE.MeshStandardMaterial({ color: 0xffffff }));
            toiletBase.position.set(5.5, 0.1, 9);
            toiletBase.castShadow = true;
            scene.add(toiletBase);
            const toiletTank = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.4, 0.5), new THREE.MeshStandardMaterial({ color: 0xeeeeee }));
            toiletTank.position.set(5.5, 0.5, 9);
            toiletTank.castShadow = true;
            scene.add(toiletTank);
            
            const sink = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 0.2, 16), new THREE.MeshStandardMaterial({ color: 0xccccdd, metalness: 0.6 }));
            sink.position.set(8.5, 0.2, 9);
            sink.castShadow = true;
            scene.add(sink);
            
            const showerGlass = new THREE.MeshStandardMaterial({ color: 0x88aaff, transparent: true, opacity: 0.4 });
            const showerPanel = new THREE.Mesh(new THREE.BoxGeometry(0.05, 2.0, 1.2), showerGlass);
            showerPanel.position.set(7.7, 1.0, 9.3);
            showerPanel.castShadow = true;
            scene.add(showerPanel);
            
            // --- Wood floors for rooms ---
            const woodMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c, roughness: 0.6 });
            const room1Floor = new THREE.Mesh(new THREE.BoxGeometry(5, 0.05, 7), woodMat);
            room1Floor.position.set(2.5, -0.08, 3.5);
            room1Floor.receiveShadow = true;
            scene.add(room1Floor);
            const room2Floor = new THREE.Mesh(new THREE.BoxGeometry(4, 0.05, 7), woodMat);
            room2Floor.position.set(7, -0.08, 3.5);
            room2Floor.receiveShadow = true;
            scene.add(room2Floor);
            const room3Floor = new THREE.Mesh(new THREE.BoxGeometry(5, 0.05, 7), woodMat);
            room3Floor.position.set(11.5, -0.08, 3.5);
            room3Floor.receiveShadow = true;
            scene.add(room3Floor);
            
            // --- Roof (pyramid-like, similar to before) ---
            const roofMat = new THREE.MeshStandardMaterial({ color: 0xaa7777 });
            const roof = new THREE.Mesh(new THREE.CylinderGeometry(8, 8, 1.2, 4), roofMat);
            roof.rotation.y = Math.PI/4;
            roof.position.set(7, 3.2, 5);
            roof.castShadow = true;
            scene.add(roof);
            
            // --- Room labels (only room names, no door labels) ---
            function makeLabel(text, x, z, yOff=1.2) {
                const div = document.createElement('div');
                div.textContent = text;
                div.style.cssText = 'color:#ffdd99; font-size:16px; font-weight:bold; background:rgba(0,0,0,0.5); padding:2px 8px; border-radius:16px; border:1px solid #ffaa66;';
                const label = new CSS2DObject(div);
                label.position.set(x, yOff, z);
                scene.add(label);
            }
            makeLabel('ROOM 1', 2.5, 3.5);
            makeLabel('ROOM 2', 7, 3.5);
            makeLabel('ROOM 3', 11.5, 3.5);
            makeLabel('BATHROOM', 7, 8.5);
            makeLabel('BACKYARD', 7, 12.5, 0.8);
            makeLabel('ENTRANCE', 2.5, -1, 0.5);
            makeLabel('ENTRANCE', 11.5, -1, 0.5);
            
            // --- Front yard grass patch ---
            const frontGrass = new THREE.Mesh(new THREE.PlaneGeometry(14, 3), grassMat);
            frontGrass.rotation.x = -Math.PI/2;
            frontGrass.position.set(7, -0.12, -1.8);
            frontGrass.receiveShadow = true;
            scene.add(frontGrass);
            
            // --- Animation ---
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
st.title("🏠 Professional House Logic Engine")
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
        - Three rooms – each connects to bathroom and backyard. Two entrance doors from main road.
        """)
else:
    st.markdown("### 🏡 3D Interactive Model – Detailed Doors, No Labels")
    st.markdown("🖱️ **Left‑click + drag** to rotate | **Right‑click + drag** to pan | **Scroll** to zoom")
    components.html(generate_3d_html(), height=700, scrolling=False)
