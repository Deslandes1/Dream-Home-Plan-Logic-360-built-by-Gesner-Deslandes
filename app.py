import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import math
import numpy as np

st.set_page_config(
    page_title="GlobalInternet.py | House Logic Engine 360",
    page_icon="🌍",
    layout="wide"
)

# ---------- SIDEBAR (spinning globe, info, licensing) ----------
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
    st.write("One-time payment. No subscriptions.")
    st.markdown("---")
    st.info("💡 High-fidelity line‑plan modifications to 2D & 3D.")

# ---------- HELPER: Draw door arc ----------
def draw_arc_door(ax, center, radius, orient_deg, swing_sign, lw):
    orient_rad = math.radians(orient_deg)
    p_end = (center[0] + radius * math.cos(orient_rad),
             center[1] + radius * math.sin(orient_rad))
    ax.plot([center[0], p_end[0]], [center[1], p_end[1]], 'k-', lw=lw, solid_capstyle='round')
    t1 = min(orient_deg, orient_deg + swing_sign * 90)
    t2 = max(orient_deg, orient_deg + swing_sign * 90)
    arc = patches.Arc(center, 2*radius, 2*radius, theta1=t1, theta2=t2, color='k', lw=lw)
    ax.add_patch(arc)

# ---------- 2D BLUEPRINT ----------
def draw_2d_blueprint():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-2, 22)
    ax.set_ylim(-2, 15)
    ax.set_aspect('equal')
    ax.axis('off')

    # Outer walls (thick)
    walls = [((0,0),(18,0)), ((18,0),(18,12)), ((18,12),(0,12)), ((0,12),(0,0))]
    for (x1,y1),(x2,y2) in walls:
        ax.plot([x1,x2],[y1,y2], 'k-', lw=4, solid_capstyle='round')

    # Inner walls
    ax.plot([10,10],[0,7], 'k-', lw=2)
    ax.plot([10,18],[7,7], 'k-', lw=2)
    ax.plot([14,18],[4,4], 'k-', lw=2)
    ax.plot([14,14],[4,7], 'k-', lw=2)

    # Doors
    draw_arc_door(ax, (10,3), 0.6, 0, +1, 1.5)
    ax.plot([10,10.6],[3,3], 'b-', lw=1.5)
    draw_arc_door(ax, (14,7), 0.6, 90, +1, 1.5)
    ax.plot([14,14],[7,7.6], 'b-', lw=1.5)
    draw_arc_door(ax, (10,8.5), 0.6, 0, +1, 1.5)
    ax.plot([10,10.6],[8.5,8.5], 'b-', lw=1.5)
    draw_arc_door(ax, (16,7), 0.6, 90, +1, 1.5)
    ax.plot([16,16],[7,7.6], 'b-', lw=1.5)
    draw_arc_door(ax, (14,4), 0.6, 180, +1, 1.5)
    ax.plot([14,14],[4,3.4], 'b-', lw=1.5)

    # Windows
    ax.plot([0,0],[4,6], 'b-', lw=3)
    ax.plot([11,13],[0,0], 'b-', lw=3)
    ax.plot([12,14],[12,12], 'b-', lw=3)
    ax.plot([18,18],[9,11], 'b-', lw=3)

    # Room labels
    font = FontProperties(weight='bold', size=10)
    ax.text(5,6,"LIVING ROOM",ha='center',va='center',fontproperties=font,bbox=dict(facecolor='white',alpha=0.7))
    ax.text(14,3,"KITCHEN",ha='center',va='center',fontproperties=font,bbox=dict(facecolor='white',alpha=0.7))
    ax.text(14,9.5,"BEDROOM 1",ha='center',va='center',fontproperties=font,bbox=dict(facecolor='white',alpha=0.7))
    ax.text(6,9.5,"BEDROOM 2",ha='center',va='center',fontproperties=font,bbox=dict(facecolor='white',alpha=0.7))
    ax.text(16,5.5,"BATH",ha='center',va='center',fontproperties=font,bbox=dict(facecolor='white',alpha=0.7))
    ax.text(2,0.8,"ENTRY",ha='center',va='center',fontproperties=font,bbox=dict(facecolor='white',alpha=0.7))

    # Dimensions (simple lines)
    ax.annotate('', xy=(0,-1), xytext=(18,-1), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(9,-1.5,"18.0 m",ha='center',color='red',fontsize=9)
    ax.annotate('', xy=(19,0), xytext=(19,12), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(19.5,6,"12.0 m",ha='center',color='red',fontsize=9,rotation=90)
    ax.annotate('', xy=(0,-1.2), xytext=(10,-1.2), arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax.text(5,-1.7,"10.0 m",ha='center',color='red',fontsize=8)

    # Yard / parking boundaries
    ax.plot([-3,-3],[-2,14], 'g--', lw=1, alpha=0.6)
    ax.plot([21,21],[-2,14], 'g--', lw=1, alpha=0.6)
    ax.plot([-3,21],[14,14], 'g--', lw=1, alpha=0.6)
    ax.plot([-3,21],[-2,-2], 'g--', lw=1, alpha=0.6)
    ax.text(-2,6,"FRONT YARD", rotation=90, fontsize=8, color='green', alpha=0.7)
    ax.text(10,13,"BACKYARD", fontsize=8, color='green', alpha=0.7, ha='center')
    ax.text(19.5,4,"PARKING", rotation=90, fontsize=8, color='blue', alpha=0.7)

    return fig

# ---------- 3D MODEL (Three.js) with auto-rotate ----------
def generate_3d_html():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>body {margin:0; overflow:hidden;}</style>
    </head>
    <body>
        <div id="info" style="position:absolute; top:20px; left:20px; color:white; background:rgba(0,0,0,0.6); padding:8px 15px; border-radius:8px; font-family:Arial; z-index:100; pointer-events:none;">
            🏠 3D House – Auto‑spinning | Drag to rotate | Scroll to zoom
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
            camera.position.set(22, 14, 18);
            camera.lookAt(9, 0, 6);
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

            // OrbitControls with autoRotate enabled
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;          // smooth inertia
            controls.dampingFactor = 0.05;
            controls.autoRotate = true;
            controls.autoRotateSpeed = 1.0;        // speed (1.0 = ~8 seconds per full turn)
            controls.enableZoom = true;
            controls.enablePan = true;
            controls.target.set(9, 2, 6);

            // Lighting
            const ambient = new THREE.AmbientLight(0x404060);
            scene.add(ambient);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1);
            dirLight.position.set(10, 20, 5);
            dirLight.castShadow = true;
            scene.add(dirLight);
            const fill = new THREE.PointLight(0xccaa88, 0.3);
            fill.position.set(9, -1, 6);
            scene.add(fill);
            const rim = new THREE.PointLight(0xffaa66, 0.4);
            rim.position.set(0, 5, 15);
            scene.add(rim);

            // Ground & yards
            const grassMat = new THREE.MeshStandardMaterial({ color: 0x5a9e4e, roughness: 0.8 });
            const frontYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMat);
            frontYard.rotation.x = -Math.PI/2;
            frontYard.position.set(9, -0.1, -3);
            frontYard.receiveShadow = true;
            scene.add(frontYard);
            const backYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMat);
            backYard.rotation.x = -Math.PI/2;
            backYard.position.set(9, -0.1, 15);
            backYard.receiveShadow = true;
            scene.add(backYard);

            // Parking
            const asphalt = new THREE.MeshStandardMaterial({ color: 0x444444 });
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), asphalt);
            parking.rotation.x = -Math.PI/2;
            parking.position.set(20.5, -0.08, 4);
            parking.receiveShadow = true;
            scene.add(parking);
            for (let i=0; i<3; i++) {
                const line = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.05, 1.5), new THREE.MeshStandardMaterial({ color: 0xffffff }));
                line.position.set(20.5, -0.02, 2 + i*2.5);
                scene.add(line);
            }

            // Fence
            const fenceMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
            const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
            const fencePoints = [[-3,-2],[21,-2],[21,14],[-3,14],[-3,-2]];
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

            // Walls
            const wallMat = new THREE.MeshStandardMaterial({ color: 0xcdc9c9, roughness: 0.4 });
            const th=0.3, h=3.0;
            function addWall(x,z,w,d,rotY=0) {
                const box = new THREE.BoxGeometry(w,h,d);
                const mesh = new THREE.Mesh(box, wallMat);
                mesh.position.set(x, h/2, z);
                mesh.rotation.y = rotY;
                mesh.castShadow = mesh.receiveShadow = true;
                scene.add(mesh);
            }
            addWall(9,0,18,th); addWall(18,6,th,12); addWall(9,12,18,th); addWall(0,6,th,12);
            addWall(10,3.5,th,7); addWall(14,7,8,th); addWall(16,4,4,th); addWall(14,5.5,th,3);

            // Doors
            const doorMat=new THREE.MeshStandardMaterial({ color:0x8B5A2B });
            const knobMat=new THREE.MeshStandardMaterial({ color:0xFFD700 });
            const doorFront=new THREE.Mesh(new THREE.BoxGeometry(1,2,0.1),doorMat);
            doorFront.position.set(5,1,0.05); doorFront.castShadow=true; scene.add(doorFront);
            const knobFront=new THREE.Mesh(new THREE.SphereGeometry(0.08),knobMat);
            knobFront.position.set(5,1,0.12); scene.add(knobFront);
            const doorInt=new THREE.Mesh(new THREE.BoxGeometry(0.1,2,1),doorMat);
            doorInt.position.set(10.05,1,3); doorInt.castShadow=true; scene.add(doorInt);
            const knobInt=new THREE.Mesh(new THREE.SphereGeometry(0.08),knobMat);
            knobInt.position.set(10.12,1,3); scene.add(knobInt);
            const doorBath=new THREE.Mesh(new THREE.BoxGeometry(0.1,2,0.8),doorMat);
            doorBath.position.set(14.05,1,4); doorBath.castShadow=true; scene.add(doorBath);
            const knobBath=new THREE.Mesh(new THREE.SphereGeometry(0.08),knobMat);
            knobBath.position.set(14.12,1,4); scene.add(knobBath);

            // Porch
            const porchMat=new THREE.MeshStandardMaterial({ color:0xc2b280 });
            const porchBase=new THREE.Mesh(new THREE.BoxGeometry(4,0.2,2.5),porchMat);
            porchBase.position.set(5,0,-1.2); porchBase.castShadow=true; scene.add(porchBase);
            const porchRoof=new THREE.Mesh(new THREE.BoxGeometry(4.2,0.1,2.7),new THREE.MeshStandardMaterial({ color:0xaa7c4a }));
            porchRoof.position.set(5,2.4,-1.2); porchRoof.castShadow=true; scene.add(porchRoof);
            [[3,-1.2],[7,-1.2]].forEach(pos => {
                const post=new THREE.Mesh(new THREE.BoxGeometry(0.2,2.2,0.2),new THREE.MeshStandardMaterial({ color:0x8B5A2B }));
                post.position.set(pos[0],1.1,pos[1]); post.castShadow=true; scene.add(post);
            });

            // Doghouse
            const dogMat=new THREE.MeshStandardMaterial({ color:0xaa8c5e });
            const dogBase=new THREE.Mesh(new THREE.BoxGeometry(1,0.5,1.2),dogMat);
            dogBase.position.set(14,0.25,14); dogBase.castShadow=true; scene.add(dogBase);
            const dogRoof=new THREE.Mesh(new THREE.CylinderGeometry(0.9,0.9,0.5,4),dogMat);
            dogRoof.rotation.y=Math.PI/4; dogRoof.position.set(14,0.7,14); dogRoof.castShadow=true; scene.add(dogRoof);
            const dogDoor=new THREE.Mesh(new THREE.BoxGeometry(0.4,0.4,0.05),new THREE.MeshStandardMaterial({ color:0xffaa66 }));
            dogDoor.position.set(14.3,0.3,14); scene.add(dogDoor);

            // Floor
            const floorMat=new THREE.MeshStandardMaterial({ color:0xbc9a6c, roughness:0.6, metalness:0.05, transparent:true, opacity:0.5 });
            const floor=new THREE.Mesh(new THREE.BoxGeometry(18,0.1,12),floorMat);
            floor.position.set(9,-0.05,6); floor.receiveShadow=true; scene.add(floor);

            // Roof
            const roofMat=new THREE.MeshStandardMaterial({ color:0xaa7777 });
            const roof=new THREE.Mesh(new THREE.CylinderGeometry(9.5,9.5,1.2,4),roofMat);
            roof.rotation.y=Math.PI/4; roof.position.set(9,2.9,6); roof.castShadow=true; scene.add(roof);

            // Labels
            function makeLabel(text,x,z,yOff=0.2) {
                const div=document.createElement('div');
                div.textContent=text;
                div.style.cssText='color:#ffdd99; font-size:16px; font-weight:bold; background:rgba(0,0,0,0.5); padding:2px 8px; border-radius:16px; border:1px solid #ffaa66;';
                const label=new CSS2DObject(div);
                label.position.set(x,yOff,z);
                scene.add(label);
            }
            makeLabel('LIVING ROOM',5,6); makeLabel('KITCHEN',14,3); makeLabel('BEDROOM 1',14,9.5);
            makeLabel('BEDROOM 2',6,9.5); makeLabel('BATH',16,5.5); makeLabel('ENTRY',2,1);
            makeLabel('FRONT YARD',9,-3,0.5); makeLabel('BACKYARD',9,16,0.5); makeLabel('PARKING',22,4,0.5);
            makeLabel('DOGHOUSE',14,14.8,0.5);

            // Animation loop
            function animate() {
                requestAnimationFrame(animate);
                controls.update();   // updates autoRotate and damping
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }
            animate();

            // Resize handler
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
st.title("🏠 House Logic Engine 360")
st.markdown("Professional architectural plans – **2D blueprint** & **3D interactive model**.")

view = st.radio("Select view:", ["2D Blueprint", "3D Model"], horizontal=True)

if view == "2D Blueprint":
    fig = draw_2d_blueprint()
    st.pyplot(fig)
    with st.expander("📐 Legend & Instructions"):
        st.markdown("""
        - **Black thick lines**: Walls  
        - **Blue arcs & lines**: Doors (arc shows swing direction)  
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries (yard, parking)  
        """)
else:
    st.markdown("### 🏡 3D Interactive Model – Full Property View")
    st.markdown("🔄 **Auto‑rotating** – Drag to rotate manually | Scroll to zoom")
    components.html(generate_3d_html(), height=700, scrolling=False)
