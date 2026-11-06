# Flashcards for A&P Quiz #3 (Lectures 7-9). Each card: (topic, front, back, source).
# Diagram cards for topics 12-25 are generated from the SKULL and SPINE keys in quiz3.py.
CARDS = [
    # 1. Bone cells
    (1, "Osteoprogenitor cell", "Bone STEM cell; becomes an osteoblast", "L7, slide 12"),
    (1, "Osteoblast", "BUILDS bone ('construction'): Ca from blood onto collagen; becomes an osteocyte", "L7, slide 12"),
    (1, "Osteocyte", "MATURE bone cell ('general contractor'); maintains bone, oversees blasts and clasts", "L7, slide 13"),
    (1, "Osteoclast", "BREAKS DOWN bone ('demolition'): Ca from bone into blood; multinucleate", "L7, slide 13"),
    (1, "Blast vs. clast", "Blast = Build; Clast = break down", "L7, slides 12–13"),
    # 2. Ribs
    (2, "True ribs", "Pairs 1–7: costal cartilage attaches DIRECTLY to the sternum", "L9, slide 27"),
    (2, "False ribs", "Pairs 8–12: do NOT attach directly; join the cartilage of rib 7", "L9, slide 27"),
    (2, "Floating ribs", "Pairs 11–12: NO costal cartilage at all", "L9, slide 27"),
    (2, "Total ribs", "24 (12 pairs)", "L9, slide 27"),
    # 3. Wolff's Law / homeostasis
    (3, "Wolff's Law", "Bone is deposited where mechanical stress is HIGHER and removed where stress is lessened", "L7, slide 45"),
    (3, "Bone homeostasis", "Bone is constantly broken down AND replaced", "L7, slide 45"),
    (3, "Three hormones controlling bone", "Vitamin D (cholecalciferol), calcitonin, PTH", "L7, slide 45"),
    (3, "Calcitonin ('Calci-bone-in')", "Moves Ca from blood INTO bone", "L7, slide 47"),
    (3, "Vitamin D3 (cholecalciferol)", "Made by skin in sunlight; needed to absorb Ca from food", "L7, slide 46"),
    (3, "Where long bones grow in length", "Epiphyseal (growth) plate, hyaline cartilage", "L7, slide 25"),
    # 4. Calcitonin vs. PTH
    (4, "Calcitonin", "Thyroid · Ca blood → bone · stimulates blasts, inhibits clasts", "L7, slide 47"),
    (4, "Parathyroid hormone (PTH)", "Parathyroids · Ca bone → blood · stimulates clasts, inhibits blasts", "L7, slide 48"),
    (4, "Hormone that stimulates osteoblasts", "Calcitonin", "L7, slide 47"),
    (4, "Hormone that stimulates osteoclasts", "PTH", "L7, slide 48"),
    (4, "Calcitonin and PTH are…", "Antagonists (opposites)", "L7, slide 48"),
    # 5. Fracture repair
    (5, "Fracture repair, 4 steps", "Hematoma → fibrocartilage callus → bony callus → remodeling (Happy Fibro Bones Remodel)", "L7, slides 56–57"),
    (5, "Step 1: Hematoma", "Broken vessels bleed; a big blood clot forms", "L7, slide 56"),
    (5, "Step 2: Fibrocartilage callus", "Fibrocartilage connects the broken ends", "L7, slide 56"),
    (5, "Step 3: Bony callus", "Osteoblasts replace the callus with bone", "L7, slide 57"),
    (5, "Step 4: Remodeling", "Osteoclasts reshape the bone; weeks to years", "L7, slide 57"),
    # 6. Hard vs. strong
    (6, "What makes bone HARD", "Hydroxyapatites: mineral salts (Ca, Mg, P) in the ground substance; inorganic; 2/3 of matrix", "L7, slide 15"),
    (6, "What makes bone STRONG", "Osteoid: collagen fibers; organic; 1/3 of matrix", "L7, slide 16"),
    (6, "Hydroxyapatites", "Ground substance → hardness", "L7, slide 15"),
    (6, "Osteoid", "Fibers → strength and resilience", "L7, slide 16"),
    # 7. Fracture types
    (7, "Compression fracture", "Bone crushed, height decreases; vertebrae, osteoporosis", "L7, slide 52"),
    (7, "Depressed fracture", "Bone pressed inward; skull", "L7, slide 52"),
    (7, "Comminuted fracture", "3+ pieces; needs hardware", "L7, slide 52"),
    (7, "Impacted fracture", "One end driven into the other; breaking a fall", "L7, slide 54"),
    (7, "Spiral fracture", "Twisting force; sports", "L7, slide 54"),
    (7, "Greenstick fracture", "Incomplete break; children", "L7, slide 54"),
    (7, "Simple (closed) vs. compound (open)", "Closed = skin intact; open = skin broken (infection risk)", "L7, slide 50"),
    # 8. Foramen magnum
    (8, "Foramen magnum", "'Great hole' in the occipital bone; spinal cord passes through", "L8, slide 21"),
    (8, "Foramen / meatus / fissure", "Round hole / tunnel / slit", "L8, slide 5"),
    (8, "Occipital condyles", "Beside the foramen magnum; joint with the atlas (C1)", "L8, slide 23"),
    # 9. Sutures
    (9, "Coronal suture", "Frontal ↔ both parietals", "L8, slide 12"),
    (9, "Sagittal suture", "Left parietal ↔ right parietal (top midline)", "L8, slide 13"),
    (9, "Squamosal suture", "Temporal ↔ parietal (above the ear)", "L8, slide 16"),
    (9, "Lambdoid suture", "Occipital ↔ both parietals (back of head)", "L8, slide 20"),
    (9, "Zygomatic arch", "Zygomatic bone ↔ temporal bone", "L8, slide 35"),
    (9, "TMJ", "Mandible (condyle) ↔ temporal bone (mandibular fossa)", "L8, slide 43"),
    # 10. Atlas and axis
    (10, "C1", "Atlas: no body, no spinous process; a ring; meets the occipital condyles", "L9, slide 15"),
    (10, "C2", "Axis: has the dens (odontoid process)", "L9, slide 16"),
    (10, "Dens (odontoid process)", "Projects up from C2's body; articulates with the atlas", "L9, slide 16"),
    # 11. Curves
    (11, "Primary curves", "Kyphotic; present from birth; thoracic and sacrococcygeal", "L9, slide 25"),
    (11, "Secondary curves", "Lordotic; form after birth; cervical and lumbar", "L9, slide 24"),
    (11, "Kyphosis", "Convex posteriorly, concave anteriorly; PRIMARY", "L9, slide 25"),
    (11, "Lordosis", "Concave posteriorly, convex anteriorly; SECONDARY", "L9, slide 24"),
    (11, "Scoliosis", "Any LATERAL (side-to-side) curve", "L9, slide 23"),
]
