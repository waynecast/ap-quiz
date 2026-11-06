# A&P Quiz #3 question bank (Lectures 7-9: Skeletal System, Skull, Spine). Built by build.py.
# Format per question: topic, q (prompt), a (correct answer), w (wrong answers), e (explanation), s (source)
# Sources cite slide POSITION in the deck. L7 = Skeletal System, L8 = Skull, L9 = Spine.
# Diagram topics (12-18 skull, 19-25 spine) are generated from the label keys below and show the handout image.
import random

TOPICS = {
    1: "Bone cells: osteoprogenitor, -blast, -cyte, -clast",
    2: "True ribs vs. false ribs",
    3: "Wolff's Law, bone homeostasis, calcitonin",
    4: "Calcitonin vs. PTH: blasts and clasts",
    5: "Steps of fracture repair",
    6: "What makes bone hard vs. strong",
    7: "Types of fractures",
    8: "\"Great hole\": foramen magnum",
    9: "How the skull bones connect (sutures)",
    10: "C1 and C2: atlas and axis",
    11: "Primary vs. secondary curves (kyphosis, lordosis)",
}
for t in range(12, 19):
    TOPICS[t] = "Skull diagram (know 1–17, 20)"
for t in range(19, 26):
    TOPICS[t] = "Spine diagram (know 1–13)"

from banks.common import Bank
B = Bank()
add = B.add

# ---------- 1. Bone cells ----------
add(1, "Which bone cell BUILDS bone?", "Osteoblast",
    ["Osteoclast", "Osteocyte", "Osteoprogenitor cell"], "Blast = build ('construction'). Osteoblasts take Ca from blood and deposit it onto collagen.", "L7, slide 12")
add(1, "Which bone cell BREAKS DOWN bone?", "Osteoclast",
    ["Osteoblast", "Osteocyte", "Osteoprogenitor cell"], "Clast = 'demolition'. Pulls Ca from bone back into blood.", "L7, slide 13")
add(1, "Which cell is the bone STEM cell that becomes an osteoblast?", "Osteoprogenitor cell",
    ["Osteocyte", "Osteoclast", "Chondrocyte"], "Osteoprogenitor = bone stem cell → osteoblast.", "L7, slide 12")
add(1, "The mature bone cell that maintains bone and oversees the 'blasts and 'clasts is the:", "Osteocyte",
    ["Osteoblast", "Osteoclast", "Osteoprogenitor cell"], "Osteocyte = 'general contractor'.", "L7, slide 13")
add(1, "Which bone cell is multinucleate?", "Osteoclast",
    ["Osteoblast", "Osteocyte", "Osteoprogenitor cell"], "Osteoclasts are large multinucleate cells.", "L7, slide 13")
add(1, "Osteoblasts eventually turn into:", "Osteocytes",
    ["Osteoclasts", "Osteoprogenitor cells", "Chondrocytes"], "Stem cell → osteoblast → osteocyte.", "L7, slide 12")
add(1, "Which cell withdraws calcium FROM bone and deposits it INTO the blood?", "Osteoclast",
    ["Osteoblast", "Osteocyte", "Osteoprogenitor cell"], "Clasts release Ca to the blood; blasts do the reverse.", "L7, slide 13")
add(1, "Which cell takes calcium FROM the blood and deposits it ONTO collagen fibers?", "Osteoblast",
    ["Osteoclast", "Osteocyte", "Red blood cell"], "Osteoblasts lay down mineral on collagen.", "L7, slide 12")
add(1, "In the construction analogy, the osteoclast is the:", "Demolition crew",
    ["Construction crew", "General contractor", "Building inspector"], "Blast = construction, cyte = general contractor, clast = demolition.", "L7, slides 12–13")

# ---------- 2. True vs. false ribs ----------
add(2, "Which rib pairs are TRUE ribs?", "1–7",
    ["1–10", "8–12", "11–12"], "True ribs attach directly to the sternum by their own costal cartilage.", "L9, slide 27")
add(2, "Which rib pairs are FALSE ribs?", "8–12",
    ["1–7", "11–12 only", "6–10"], "False ribs don't attach directly to the sternum.", "L9, slide 27")
add(2, "Which rib pairs are FLOATING ribs?", "11–12",
    ["8–10", "1–2", "10–12"], "Floating ribs have no costal cartilage.", "L9, slide 27")
add(2, "What makes a rib a TRUE rib?", "Its costal cartilage attaches directly to the sternum",
    ["It has no costal cartilage", "It attaches to the cartilage of rib 7", "It attaches to the lumbar spine"], "True = direct attachment to the sternum.", "L9, slide 27")
add(2, "The costal cartilage of false ribs 8–10 attaches to:", "The costal cartilage of rib 7",
    ["The manubrium", "The xiphoid process", "Nothing"], "They join the cartilage above instead of the sternum.", "L9, slide 27")
add(2, "Floating ribs are a type of:", "False rib",
    ["True rib", "Vertebra", "Sternal rib"], "Pairs 11–12 are false ribs with no costal cartilage at all.", "L9, slide 27")
add(2, "How many ribs does an adult have in total?", "24 (12 pairs)",
    ["12 (6 pairs)", "26 (13 pairs)", "20 (10 pairs)"], "12 pairs come off the 12 thoracic vertebrae.", "L9, slide 27")
add(2, "Rib 9 is classified as a:", "False rib",
    ["True rib", "Floating rib", "Cervical rib"], "8–12 are false; only 11–12 float.", "L9, slide 27")

# ---------- 3. Wolff's Law, homeostasis, calcitonin ----------
add(3, "Wolff's Law states that bone is deposited:", "In greater density where mechanical stress is higher",
    ["Only during childhood", "Where stress is lowest", "Only when PTH is released"], "Stress builds bone; bone is removed where stress is lessened.", "L7, slide 45")
add(3, "According to Wolff's Law, a bedridden patient's bones will:", "Lose density (bone is removed where stress is lessened)",
    ["Gain density", "Grow longer", "Stay exactly the same"], "Less mechanical stress → bone is removed.", "L7, slide 45")
add(3, "Which hormone puts calcium INTO bone ('Calci-bone-in')?", "Calcitonin",
    ["Parathyroid hormone", "Cortisol", "Insulin"], "Calcitonin moves Ca from blood into bone.", "L7, slide 47")
add(3, "Bone homeostasis means bone is:", "Constantly broken down AND replaced",
    ["Never replaced after age 18", "Only built, never broken down", "Only broken down in old age"], "Bone is in a constant state of maintenance.", "L7, slide 45")
add(3, "Which three hormones control bone homeostasis?", "Vitamin D (cholecalciferol), calcitonin, PTH",
    ["Insulin, glucagon, cortisol", "Estrogen, testosterone, insulin", "Adrenaline, calcitonin, melatonin"], "Listed on the homeostasis slide.", "L7, slide 45")
add(3, "Vitamin D (cholecalciferol) is needed to:", "Absorb calcium from food into the blood",
    ["Break down bone", "Make collagen", "Form the epiphyseal plate"], "Made by skin in sunlight; needed to absorb Ca.", "L7, slide 46")
add(3, "Weight-bearing exercise strengthens bone. This is explained by:", "Wolff's Law",
    ["Hematoma formation", "Intramembranous ossification", "Hematopoiesis"], "Mechanical stress → more bone deposited.", "L7, slides 45, 61")
add(3, "Long bones grow in LENGTH only at the:", "Epiphyseal (growth) plate",
    ["Diaphysis", "Periosteum", "Marrow cavity"], "Hyaline cartilage plate; becomes the epiphyseal line in adults.", "L7, slide 25")
add(3, "Bone replacement rate depends on blood calcium level, hormones, and:", "Mechanical stress and gravity",
    ["Hair color", "Blood type", "Body temperature"], "Stress/gravity is the Wolff's Law factor.", "L7, slide 45")

# ---------- 4. Calcitonin vs. PTH ----------
add(4, "Calcitonin ______ osteoblasts and ______ osteoclasts.", "Stimulates; inhibits",
    ["Inhibits; stimulates", "Stimulates; stimulates", "Inhibits; inhibits"], "Calcitonin builds bone: more blasts, fewer clasts.", "L7, slide 47")
add(4, "Parathyroid hormone (PTH) ______ osteoclasts and ______ osteoblasts.", "Stimulates; inhibits",
    ["Inhibits; stimulates", "Stimulates; stimulates", "Inhibits; inhibits"], "PTH pulls Ca out of bone: more clasts, fewer blasts.", "L7, slide 48")
add(4, "Which hormone takes calcium FROM bone and puts it into the blood?", "Parathyroid hormone (PTH)",
    ["Calcitonin", "Vitamin D", "Growth hormone"], "PTH is the antagonist of calcitonin.", "L7, slide 48")
add(4, "Calcitonin is made by the:", "Thyroid gland",
    ["Parathyroid glands", "Adrenal glands", "Pituitary gland"], "Calcitonin = thyroid; PTH = parathyroids.", "L7, slide 47")
add(4, "PTH is made by the:", "Parathyroid glands",
    ["Thyroid gland", "Pancreas", "Kidneys"], "Parathyroid glands sit on the back of the thyroid.", "L7, slide 48")
add(4, "Which hormone INHIBITS osteoclasts?", "Calcitonin",
    ["Parathyroid hormone", "Cortisol", "Thyroxine"], "Calcitonin inhibits clasts so Ca stays in bone.", "L7, slide 47")
add(4, "Which hormone INHIBITS osteoblasts?", "Parathyroid hormone (PTH)",
    ["Calcitonin", "Vitamin D", "Estrogen"], "PTH inhibits blasts and stimulates clasts.", "L7, slide 48")
add(4, "Calcitonin and PTH are described as:", "Antagonists (opposites)",
    ["The same hormone", "Both made by the thyroid", "Both bone-building"], "PTH is antagonist to calcitonin.", "L7, slide 48")
add(4, "When blood calcium is LOW, which hormone raises it by breaking down bone?", "PTH",
    ["Calcitonin", "Insulin", "Melatonin"], "PTH stimulates osteoclasts, releasing Ca to blood.", "L7, slide 48")

# ---------- 5. Fracture repair ----------
add(5, "What is the FIRST step of fracture repair?", "Hematoma formation",
    ["Fibrocartilage callus", "Bony callus", "Remodeling"], "Broken vessels bleed and a clot (hematoma) forms.", "L7, slide 56")
add(5, "What is the correct order of fracture repair?", "Hematoma → fibrocartilage callus → bony callus → remodeling",
    ["Fibrocartilage callus → hematoma → bony callus → remodeling", "Hematoma → bony callus → fibrocartilage callus → remodeling", "Remodeling → hematoma → bony callus → fibrocartilage callus"], "Happy Fibro Bones Remodel.", "L7, slides 56–57")
add(5, "What is the LAST step of fracture repair?", "Remodeling",
    ["Hematoma formation", "Bony callus", "Fibrocartilage callus"], "Osteoclasts reshape the bone; can take weeks to years.", "L7, slide 57")
add(5, "The callus that first connects the broken ends of bone is made of:", "Fibrocartilage",
    ["Hyaline cartilage", "Spongy bone", "Elastic cartilage"], "Step 2: fibrocartilage callus.", "L7, slide 56")
add(5, "During the bony callus stage, which cells deposit calcium onto the collagen of the callus?", "Osteoblasts",
    ["Osteoclasts", "Osteocytes", "Chondrocytes"], "Blasts build the bony callus.", "L7, slide 57")
add(5, "During remodeling, bone returns to its original shape as which cells remove unneeded calcium?", "Osteoclasts",
    ["Osteoblasts", "Fibroblasts", "Red blood cells"], "Clasts remove bone where support is no longer needed.", "L7, slide 57")
add(5, "What comes right AFTER the fibrocartilage callus?", "Bony callus",
    ["Hematoma", "Remodeling", "Epiphyseal plate"], "Step 3: callus replaced by bone.", "L7, slide 57")
add(5, "A fracture hematoma is essentially a:", "Large blood clot",
    ["Cartilage pad", "Bone spur", "Bruise on the skin only"], "It forms to stop bleeding from broken vessels.", "L7, slide 56")

# ---------- 6. Hardness vs. strength ----------
add(6, "What makes bone HARD?", "Hydroxyapatites (mineral salts in the ground substance)",
    ["Osteoid (collagen fibers)", "Bone marrow", "Periosteum"], "Hydroxyapatites = inorganic mineral salts, 2/3 of matrix.", "L7, slide 15")
add(6, "What gives bone STRENGTH and resilience?", "Osteoid (collagen fibers)",
    ["Hydroxyapatites", "Yellow marrow", "Articular cartilage"], "Osteoid = organic collagen fibers, 1/3 of matrix.", "L7, slide 16")
add(6, "Hydroxyapatites are part of the bone matrix's:", "Ground substance",
    ["Fibers", "Cells", "Marrow"], "Ground substance = hydroxyapatites; fibers = osteoid.", "L7, slide 14")
add(6, "Osteoid is part of the bone matrix's:", "Fibers",
    ["Ground substance", "Cells", "Periosteum"], "Fibers = osteoid, mainly collagen.", "L7, slide 14")
add(6, "Hydroxyapatites make up about how much of the bone matrix?", "2/3",
    ["1/3", "1/2", "All of it"], "Mineral salts = 2/3; osteoid = 1/3.", "L7, slide 15")
add(6, "The INORGANIC portion of bone matrix is:", "Hydroxyapatites (Ca, Mg, P salts)",
    ["Osteoid", "Collagen", "Osteocytes"], "Inorganic = minerals = hardness.", "L7, slide 15")
add(6, "The ORGANIC portion of bone matrix is:", "Osteoid (mostly collagen)",
    ["Hydroxyapatites", "Calcium phosphate", "Magnesium salts"], "Organic = collagen = strength.", "L7, slide 16")
add(6, "Hydroxyapatites are also called:", "Mineral salts",
    ["Collagen fibers", "Osteoid", "Lamellae"], "a.k.a. mineral salts (Ca, Mg, P).", "L7, slide 15")

# ---------- 7. Fracture types ----------
add(7, "A bone breaks into 3 or more pieces. This is a:", "Comminuted fracture",
    ["Greenstick fracture", "Spiral fracture", "Depressed fracture"], "Comminuted = 3+ pieces; needs hardware.", "L7, slide 52")
add(7, "An incomplete fracture typically seen in children is a:", "Greenstick fracture",
    ["Compression fracture", "Impacted fracture", "Comminuted fracture"], "Children's bones bend like a green twig.", "L7, slide 54")
add(7, "A fracture caused by twisting forces, common in sports, is a:", "Spiral fracture",
    ["Depressed fracture", "Greenstick fracture", "Compression fracture"], "Twisting → spiral.", "L7, slide 54")
add(7, "Broken bone pressed inward, typical of a skull fracture, is a:", "Depressed fracture",
    ["Compression fracture", "Impacted fracture", "Spiral fracture"], "Depressed = dented in.", "L7, slide 52")
add(7, "A crushed bone with decreased height, common in the vertebrae of post-menopausal women, is a:", "Compression fracture",
    ["Depressed fracture", "Greenstick fracture", "Spiral fracture"], "Usually from osteoporosis.", "L7, slide 52")
add(7, "One end of a bone is driven into the other, often when trying to break a fall. This is a:", "Impacted fracture",
    ["Comminuted fracture", "Spiral fracture", "Greenstick fracture"], "Impacted = jammed together.", "L7, slide 54")
add(7, "A compound (open) fracture is one in which:", "The skin is broken",
    ["The skin is not broken", "The bone breaks in 3+ pieces", "The break is incomplete"], "Open fractures carry greater infection risk.", "L7, slide 50")
add(7, "A simple (closed) fracture is one in which:", "The skin is NOT broken",
    ["The skin is broken", "The bone is crushed", "The bone twists"], "Closed = skin intact.", "L7, slide 50")
add(7, "Which fracture type usually needs 'hardware' to repair?", "Comminuted",
    ["Greenstick", "Simple", "Incomplete"], "3+ pieces need plates/screws.", "L7, slide 52")

# ---------- 8. Foramen magnum ----------
add(8, "Which landmark's name means 'great hole'?", "Foramen magnum",
    ["External auditory meatus", "Sella turcica", "Mental foramen"], "Magnum = great; foramen = hole.", "L8, slide 21")
add(8, "The foramen magnum is in which bone?", "Occipital",
    ["Temporal", "Sphenoid", "Parietal"], "At the base of the skull.", "L8, slide 21")
add(8, "What passes through the foramen magnum?", "The spinal cord",
    ["The optic nerve", "The olfactory nerves", "The vertebral artery only"], "Passage for the spinal cord through the skull.", "L8, slide 21")
add(8, "A 'foramen' is a bone marking that is:", "A round or oval hole",
    ["A tunnel-like passage", "A slit-like opening", "A sharp projection"], "Meatus = tunnel; fissure = slit.", "L8, slide 5")
add(8, "The structures on either side of the foramen magnum that articulate with the atlas are the:", "Occipital condyles",
    ["Mastoid processes", "Styloid processes", "Mandibular condyles"], "They form a joint with C1.", "L8, slide 23")
add(8, "'Turkish saddle' is the meaning of which skull landmark (not the 'great hole')?", "Sella turcica",
    ["Foramen magnum", "Crista galli", "Cribriform plate"], "Sella turcica holds the pituitary; foramen magnum = great hole.", "L8, slides 21, 27")

# ---------- 9. How the skull bones connect ----------
add(9, "The coronal suture joins the frontal bone to the:", "Parietal bones",
    ["Occipital bone", "Temporal bones", "Sphenoid bone"], "Coronal = frontal ↔ both parietals.", "L8, slide 12")
add(9, "The sagittal suture joins:", "The left and right parietal bones",
    ["Frontal and parietal bones", "Parietal and occipital bones", "Temporal and parietal bones"], "Runs front-to-back on top of the skull.", "L8, slide 13")
add(9, "The lambdoid suture joins the occipital bone to the:", "Parietal bones",
    ["Frontal bone", "Temporal bones", "Mandible"], "Back of the skull, shaped like λ.", "L8, slide 20")
add(9, "The squamosal suture joins the temporal bone to the:", "Parietal bone",
    ["Frontal bone", "Occipital bone", "Zygomatic bone"], "Curved line above the ear.", "L8, slide 16")
add(9, "Which bone touches the frontal, temporal AND occipital bones?", "Parietal",
    ["Sphenoid", "Nasal", "Mandible"], "Parietals connect via coronal, squamosal and lambdoid sutures.", "L8, slides 12, 16, 20")
add(9, "Which suture is between the frontal and parietal bones?", "Coronal",
    ["Sagittal", "Lambdoid", "Squamosal"], "Coronal = front.", "L8, slide 12")
add(9, "Which suture is between the occipital and parietal bones?", "Lambdoid",
    ["Coronal", "Sagittal", "Squamosal"], "Lambdoid = back.", "L8, slide 20")
add(9, "The zygomatic arch is formed where the zygomatic bone meets the:", "Temporal bone",
    ["Frontal bone", "Parietal bone", "Occipital bone"], "Temporal process of zygomatic + zygomatic process of temporal.", "L8, slide 35")
add(9, "The mandible forms the TMJ with which bone?", "Temporal",
    ["Maxilla", "Zygomatic", "Sphenoid"], "Mandibular condyle ↔ mandibular fossa of the temporal bone.", "L8, slide 43")

# ---------- 10. Atlas and axis ----------
add(10, "C1 is called the:", "Atlas",
    ["Axis", "Dens", "Sacrum"], "Atlas holds up the head.", "L9, slide 15")
add(10, "C2 is called the:", "Axis",
    ["Atlas", "Coccyx", "Centrum"], "Axis has the dens.", "L9, slide 16")
add(10, "Which vertebra has NO body and NO spinous process, just a ring of bone?", "Atlas (C1)",
    ["Axis (C2)", "C7", "L5"], "The atlas is a ring.", "L9, slide 15")
add(10, "The dens (odontoid process) belongs to which vertebra?", "Axis (C2)",
    ["Atlas (C1)", "C7", "T1"], "Dens projects up from C2's body to the atlas.", "L9, slide 16")
add(10, "The atlas articulates with the skull at the:", "Occipital condyles",
    ["Mastoid processes", "Foramen magnum's rim only", "Mandibular fossa"], "C1 ↔ occipital condyles.", "L9, slide 15")
add(10, "The dens of the axis articulates with the:", "Atlas",
    ["Occipital bone", "C3", "First rib"], "It projects superiorly to the atlas.", "L9, slide 16")
add(10, "Which statement is TRUE?", "C1 = atlas, C2 = axis",
    ["C1 = axis, C2 = atlas", "C1 and C2 are both called the axis", "C7 = atlas"], "Alphabetical: Atlas before Axis.", "L9, slides 15–16")

# ---------- 11. Spinal curves ----------
add(11, "Which curves are PRIMARY curves?", "Thoracic and sacrococcygeal",
    ["Cervical and lumbar", "Cervical and thoracic", "Lumbar and sacral"], "Primary = kyphotic, present from birth.", "L9, slide 25")
add(11, "Which curves are SECONDARY curves?", "Cervical and lumbar",
    ["Thoracic and sacrococcygeal", "Thoracic and lumbar", "Cervical and sacral"], "Secondary = lordotic, form after birth.", "L9, slide 24")
add(11, "Kyphosis (a kyphotic curve) is a:", "Primary curve",
    ["Secondary curve", "Lateral curve", "Curve that forms after walking"], "Present from birth.", "L9, slide 25")
add(11, "Lordosis (a lordotic curve) is a:", "Secondary curve",
    ["Primary curve", "Lateral curve", "Curve present at birth"], "Forms after birth.", "L9, slide 24")
add(11, "The lumbar spine normally has which type of curve?", "Lordosis",
    ["Kyphosis", "Scoliosis", "No curve"], "Cervical and lumbar = lordotic.", "L9, slide 24")
add(11, "The thoracic spine normally has which type of curve?", "Kyphosis",
    ["Lordosis", "Scoliosis", "No curve"], "Thoracic and sacrococcygeal = kyphotic.", "L9, slide 25")
add(11, "A kyphotic curve is:", "Convex posteriorly, concave anteriorly",
    ["Concave posteriorly, convex anteriorly", "Curved to the side", "Straight"], "It bulges toward the back.", "L9, slide 25")
add(11, "A lordotic curve is:", "Concave posteriorly, convex anteriorly",
    ["Convex posteriorly, concave anteriorly", "Curved to the side", "Straight"], "It bulges toward the front.", "L9, slide 24")
add(11, "Any LATERAL (side-to-side) curve of the spine is called:", "Scoliosis",
    ["Kyphosis", "Lordosis", "Spondylosis"], "From the front/back the spine should be straight.", "L9, slide 23")
add(11, "Primary curves are present:", "From birth",
    ["Only after walking", "Only in adults", "Only when sitting"], "Newborn is curled in a C.", "L9, slide 25")

# ---------- 12-18. Skull diagram (generated) ----------
SKULL = {
    1: ("Frontal bone", "Forehead.", "L8, slide 8"),
    2: ("Temporal bone", "Lower side of the head around the ear.", "L8, slide 14"),
    3: ("Parietal bone", "Top and upper sides of the head.", "L8, slide 10"),
    4: ("Occipital bone", "Back and base of the skull.", "L8, slide 18"),
    5: ("Nasal bone", "Bridge of the nose.", "L8, slide 33"),
    6: ("Maxilla", "Upper jaw; holds the upper teeth.", "L8, slide 31"),
    7: ("Mandible", "Lower jaw; only movable skull bone.", "L8, slide 41"),
    8: ("Sphenoid bone", "Butterfly bone; seen at the temple and inside the skull.", "L8, slide 24"),
    9: ("Zygomatic bone", "Cheekbone.", "L8, slide 35"),
    10: ("Mastoid process", "Large rounded bump behind the ear.", "L8, slide 17"),
    11: ("External auditory meatus", "The ear hole.", "L8, slide 16"),
    12: ("External occipital protuberance", "Midline bump on the back of the occipital.", "L8, slide 22"),
    13: ("Coronal suture", "Frontal ↔ parietal.", "L8, slide 12"),
    14: ("Squamosal suture", "Temporal ↔ parietal.", "L8, slide 16"),
    15: ("Lambdoid suture", "Occipital ↔ parietal.", "L8, slide 20"),
    16: ("Foramen magnum", "The 'great hole' for the spinal cord.", "L8, slide 21"),
    17: ("Styloid process", "Thin spike in front of the mastoid.", "L8, slide 17"),
    20: ("Occipital condyle", "Smooth knobs beside the foramen magnum; joint with C1.", "L8, slide 23"),
}
SKULL_GROUPS = [{1, 2, 3, 4, 8}, {5, 6, 7, 9, 8}, {10, 11, 17, 2}, {13, 14, 15}, {12, 16, 20, 4}]

SPINE = {
    1: ("Spinous process", "Most posterior projection; fused laminae.", "L9, slide 9"),
    2: ("Lamina", "Plate between the transverse and spinous processes.", "L9, slide 8"),
    3: ("Transverse process", "Projects laterally off the arch.", "L9, slide 11"),
    4: ("Pedicle", "Short stalk from the body to the arch.", "L9, slide 7"),
    5: ("Body (centrum)", "Large anterior weight-bearing part.", "L9, slide 6"),
    6: ("Vertebral foramen", "Hole for the spinal cord.", "L9, slide 11"),
    7: ("Superior articular process", "Points up; joints with the vertebra above.", "L9, slide 10"),
    8: ("Inferior articular process", "Points down; joints with the vertebra below.", "L9, slide 10"),
    9: ("Transverse foramen", "Hole in a cervical transverse process; vertebral artery.", "L9, slide 14"),
    10: ("Transverse costal facet (rib facet)", "Rib facet on a thoracic transverse process.", "L9, slides 12, 17"),
    11: ("Superior costal facet (rib facet)", "Rib facet on the top edge of a thoracic body.", "L9, slides 12, 17"),
    12: ("Inferior costal facet (rib facet)", "Rib facet on the bottom edge of a thoracic body.", "L9, slides 12, 17"),
    13: ("Intervertebral disc", "Fibrocartilage pad between vertebral bodies.", "L9, slide 13"),
}
SPINE_GROUPS = [{1, 2, 3, 4}, {6, 9, 5}, {7, 8, 3}, {10, 11, 12, 3}, {13, 5, 6}]

rng = random.Random(3)

def distractors(key, n, groups):
    near = set().union(*[g for g in groups if n in g]) - {n}
    pool = list(near) + [k for k in key if k != n and k not in near]
    picks = list(near)
    rng.shuffle(picks)
    picks = picks[:2]
    rest = [k for k in pool if k not in picks]
    rng.shuffle(rest)
    return (picks + rest)[:3]

def diagram(key, groups, topics, img, label, extra=()):
    qs = list(extra)
    for n, (name, hint, src) in key.items():
        d = distractors(key, n, groups)
        qs.append((f"{label}: what does #{n} point to?", name, [key[k][0] for k in d], f"#{n} = {name}. {hint}", src))
        d = distractors(key, n, groups)
        qs.append((f"{label}: which number is the {name.lower()}?", f"#{n}", [f"#{k}" for k in d], f"#{n} = {name}. {hint}", src))
    rng.shuffle(qs)
    for i, (q, a, w, e, s) in enumerate(qs):
        add(topics[i % len(topics)], q, a, w, e, s)
        B.Q[-1]["img"] = img

diagram(SKULL, SKULL_GROUPS, list(range(12, 19)), "img/skull.jpg", "Skull handout")
SPINE_EXTRA = [
    ("Spine handout: which numbers appear ONLY on the thoracic vertebra?", "#10, #11, #12 (rib facets)", ["#9 (transverse foramen)", "#7 and #8", "#2 and #4"], "Rib facets are ONLY on thoracic vertebrae.", "L9, slide 12"),
    ("Spine handout: #9 (transverse foramen) appears only on which vertebra?", "Cervical", ["Thoracic", "Lumbar", "Sacrum"], "Only cervical vertebrae have transverse foramina; the vertebral arteries pass through.", "L9, slide 14"),
    ("Spine handout: the vertebra with a bifid (split) spinous process at #1 is:", "Cervical", ["Thoracic", "Lumbar", "Coccyx"], "Bifid spinous process = cervical.", "L9, slide 14"),
    ("Spine handout: the vertebra with the largest body (#5) and a wide, spatulated spinous process is:", "Lumbar", ["Cervical", "Thoracic", "Atlas"], "Lumbar bodies carry the most weight.", "L9, slide 18"),
    ("Spine handout: the top bracket on the full spine marks which region (and how many vertebrae)?", "Cervical (7)", ["Thoracic (12)", "Lumbar (5)", "Sacrum (5 fused)"], "Cervical 7, thoracic 12, lumbar 5.", "L9, slide 5"),
    ("Spine handout: the second (longest) bracket marks which region?", "Thoracic (12)", ["Cervical (7)", "Lumbar (5)", "Coccyx (4 fused)"], "The thoracic region is the longest.", "L9, slide 5"),
    ("Spine handout: the third bracket marks which region?", "Lumbar (5)", ["Thoracic (12)", "Sacrum (5 fused)", "Cervical (7)"], "Lumbar = low back, 5 vertebrae.", "L9, slide 5"),
    ("Spine handout: #2 (lamina) and #4 (pedicle) together form the:", "Vertebral arch", ["Vertebral body", "Intervertebral disc", "Transverse foramen"], "Pedicles and laminae are both part of the vertebral arch.", "L9, slides 7–8"),
    ("Spine handout: #6 (vertebral foramen) is ROUND on which vertebra?", "Thoracic", ["Cervical", "Lumbar", "All of them"], "Thoracic = round; cervical and lumbar = triangular.", "L9, slides 14, 17, 18"),
    ("Spine handout: #13 (intervertebral discs) are made of:", "Fibrocartilage", ["Hyaline cartilage", "Compact bone", "Elastic cartilage"], "Fibrocartilage pads that help bear weight.", "L9, slide 13"),
]
diagram(SPINE, SPINE_GROUPS, list(range(19, 26)), "img/spine.jpg", "Spine handout", SPINE_EXTRA)

QUIZ = {"id": "q3", "title": "A&P Quiz #3", "lectures": "Lectures 7–9",
        "units": {"L7": "Skeletal System", "L8": "Skull", "L9": "Spine"},
        "topics": TOPICS, "questions": B.Q}
