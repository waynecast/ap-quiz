# A&P Quiz #4 question bank (Lectures 10-12: Upper Extremity, Lower Extremity, Joints). Built by build.py.
# Format per question: topic, q (prompt), a (correct answer), w (wrong answers), e (explanation), s (source)
# Sources cite slide POSITION in the deck. L10 = Upper Extremity, L11 = Lower Extremity, L12 = Joints.
# Diagram topics (11-25) are generated from the label keys below and show the class handout image from img/.
import random

TOPICS = {
    1: "Landmarks: which bone is it on? (A)",
    2: "Shoulder (pectoral) girdle: its parts",
    3: "Joints by movement: immovable, slightly movable, freely movable",
    4: "Landmarks + articulations: what fits into what",
    5: "The ankle joints",
    6: "Types of synovial joints (ball & socket, hinge, saddle…)",
    7: "Bones of the hand and where they sit",
    8: "Medial vs. lateral bones of the arm/forearm and leg",
    9: "Landmarks: which bone is it on? (B)",
    10: "Articulations: what joins with what (e.g. medial clavicle)",
}
for t in range(11, 15):
    TOPICS[t] = "Diagram: humerus or femur"
for t in range(15, 21):
    TOPICS[t] = "Diagram: forearm or leg (radius/ulna, tibia/fibula)"
for t in range(21, 26):
    TOPICS[t] = "Diagram: hand or foot"

from banks.common import Bank
B = Bank()
add = B.add

# ---------- 1. Landmarks: which bone (A) ----------
add(1, "The acromion process is on which bone?", "Scapula",
    ["Clavicle", "Humerus", "Sternum"], "The acromion is the high point of the shoulder, at the lateral end of the scapula's spine.", "L10, slide 14")
add(1, "The coracoid process is on which bone?", "Scapula",
    ["Clavicle", "Ulna", "Humerus"], "Finger-like projection off the ANTERIOR scapula, lower than the acromion. (Don't mix it up with the coroNoid process of the ulna.)", "L10, slide 17")
add(1, "The glenoid fossa is on which bone?", "Scapula",
    ["Humerus", "Clavicle", "Coxal bone"], "Shallow socket on the superior lateral border of the scapula; holds the humeral head.", "L10, slide 11")
add(1, "The deltoid tuberosity is on which bone?", "Humerus",
    ["Scapula", "Femur", "Radius"], "Rough bump halfway down the lateral humerus.", "L10, slide 31")
add(1, "The capitulum and trochlea are on which bone?", "Humerus",
    ["Ulna", "Radius", "Femur"], "Both are on the distal humerus: capitulum (lateral) meets the radius, trochlea meets the ulna.", "L10, slides 34–35")
add(1, "The olecranon process is on which bone?", "Ulna",
    ["Humerus", "Radius", "Tibia"], "Forms the point of the elbow. (The humerus has the olecranon FOSSA, where it fits.)", "L10, slide 42")
add(1, "The trochlear notch is on which bone?", "Ulna",
    ["Humerus", "Radius", "Scapula"], "The C-shaped notch of the ulna that wraps the trochlea of the humerus.", "L10, slide 43")
add(1, "The radial tuberosity is just below the neck of which bone?", "Radius",
    ["Ulna", "Humerus", "Tibia"], "Head → neck → radial tuberosity, all on the proximal radius.", "L10, slide 40")
add(1, "Lister's tubercle is on which bone?", "Radius",
    ["Ulna", "Scapula", "Fibula"], "Posterior distal bump on the radius; a pulley for the extensor pollicis longus tendon.", "L10, slide 41")
add(1, "The supraspinous and infraspinous fossae are on which bone?", "Scapula",
    ["Coxal bone", "Humerus", "Clavicle"], "Above and below the spine of the scapula (posterior surface).", "L10, slides 19–20")
add(1, "The greater and lesser tubercles are on which bone?", "Humerus",
    ["Femur", "Scapula", "Tibia"], "Tubercles = humerus. The femur's matching bumps are called TROCHANTERS.", "L10, slides 28–29")
add(1, "The coronoid fossa is on which bone?", "Humerus",
    ["Ulna", "Radius", "Scapula"], "Shallow depression on the distal ANTERIOR humerus. The ulna has the coronoid PROCESS that fits into it.", "L10, slide 32")
add(1, "Which bone has a styloid process on its distal LATERAL end (thumb side)?", "Radius",
    ["Ulna", "Fibula", "Humerus"], "Radius = thumb side. The ulna's styloid is distal, medial and posterior.", "L10, slide 41")

# ---------- 2. Shoulder girdle ----------
add(2, "The pectoral (shoulder) girdle is made of which two bones?", "Clavicle and scapula",
    ["Clavicle and humerus", "Scapula and humerus", "Sternum and clavicle"], "Pectoral girdle = clavicle (collarbone) + scapula (shoulder blade). The humerus is the arm, not the girdle.", "L10, slide 3")
add(2, "What is the job of the pectoral girdle?", "Attaches the upper extremity to the trunk",
    ["Attaches the lower extremity to the axial skeleton", "Protects the heart and lungs", "Forms the elbow joint"], "The pelvic girdle does the same job for the lower extremity.", "L10, slide 3")
add(2, "How many pectoral girdles does a person have?", "Two: a left and a right",
    ["One", "Four", "Two, but they are fused at the sternum"], "We have a left and a right shoulder girdle.", "L10, slide 3")
add(2, "The clavicle runs from:", "The manubrium of the sternum to the acromion of the scapula",
    ["The xiphoid process to the coracoid process", "The manubrium to the head of the humerus", "The 1st rib to the glenoid fossa"], "A small S-shaped bone between the sternum and the scapula.", "L10, slide 4")
add(2, "Which bone of the shoulder girdle is S-shaped?", "Clavicle",
    ["Scapula", "Humerus", "Manubrium"], "The clavicle is a small S-shaped bone.", "L10, slide 4")
add(2, "Which of these is NOT part of the shoulder girdle?", "Humerus",
    ["Clavicle", "Scapula", "Acromion"], "The girdle is clavicle + scapula. The acromion is part of the scapula. The humerus is the arm bone.", "L10, slides 3, 23")
add(2, "Which two joints are at either end of the clavicle?", "Sternoclavicular (medial) and acromioclavicular (lateral)",
    ["Glenohumeral and acromioclavicular", "Sternoclavicular and glenohumeral", "Costoclavicular and humeroulnar"], "SC joint medially, AC joint laterally.", "L10, slides 5–6")
add(2, "The shoulder involves how many joints (per the joints lecture)?", "3: sternoclavicular, acromioclavicular, glenohumeral",
    ["1: glenohumeral", "2: SC and AC", "4: SC, AC, glenohumeral, scapulothoracic"], "The three joints associated with shoulder movement.", "L12, slides 37–39")
add(2, "The common site of a 'shoulder separation' is the:", "Acromioclavicular (AC) joint",
    ["Glenohumeral joint", "Sternoclavicular joint", "Humeroulnar joint"], "Separation = AC joint. DISLOCATION = glenohumeral joint.", "L12, slide 38")
add(2, "The glenoid labrum is a cartilage rim that:", "Deepens the glenoid fossa for stability",
    ["Connects the clavicle to the sternum", "Covers the acromion", "Lines the olecranon fossa"], "Accessory structure of the shoulder joint.", "L12, slide 41")

# ---------- 3. Joints by movement (functional) ----------
add(3, "A synarthrotic joint is:", "Immovable",
    ["Slightly movable", "Freely movable", "Only found in the limbs"], "SAD–ISM: Synarthrotic = Immovable.", "L12, slides 6, 8")
add(3, "An amphiarthrotic joint is:", "Slightly movable",
    ["Immovable", "Freely movable", "Always synovial"], "SAD–ISM: Amphiarthrotic = Slightly movable.", "L12, slides 7–8")
add(3, "A diarthrotic joint is:", "Freely movable",
    ["Immovable", "Slightly movable", "Held by fibrocartilage"], "SAD–ISM: Diarthrotic = Movable (elbows, wrists, shoulders, knees, hips, ankles).", "L12, slide 8")
add(3, "Sutures of the skull are which functional type?", "Synarthrotic (immovable)",
    ["Amphiarthrotic (slightly movable)", "Diarthrotic (freely movable)", "Synovial"], "Sutures between the flat skull bones don't move.", "L12, slide 6")
add(3, "A gomphosis (tooth in its socket) is:", "Synarthrotic (immovable)",
    ["Amphiarthrotic (slightly movable)", "Diarthrotic (freely movable)", "A hinge joint"], "Cone-shaped process holds the tooth in its socket.", "L12, slide 6")
add(3, "The pubic symphysis and intervertebral discs are which functional type?", "Amphiarthrotic (slightly movable)",
    ["Synarthrotic (immovable)", "Diarthrotic (freely movable)", "Ball and socket"], "Symphysis = fibrocartilage pad, slightly movable.", "L12, slide 7")
add(3, "The syndesmosis between the tibia and fibula (or radius and ulna) is:", "Amphiarthrotic (slightly movable)",
    ["Synarthrotic (immovable)", "Diarthrotic (freely movable)", "A pivot joint"], "Fibrous membrane sheet connecting 2 bones; slightly movable.", "L12, slide 7")
add(3, "Per the deck, an epiphyseal plate (synchondrosis) is classified as:", "Amphiarthrotic (slightly movable)",
    ["Diarthrotic (freely movable)", "A suture", "A gomphosis"], "The deck lists synchondroses under amphiarthrotic (the textbook calls them synarthrotic). Go with the deck.", "L12, slide 7")
add(3, "Elbows, knees, hips and shoulders are which functional type?", "Diarthrotic (freely movable)",
    ["Amphiarthrotic (slightly movable)", "Synarthrotic (immovable)", "Fibrous"], "Diarthrotic = freely movable. All synovial joints are diarthrotic.", "L12, slide 8")
add(3, "Functional classification of joints is based on:", "Degree of movement allowed",
    ["Type of tissue and presence of a joint cavity", "Number of bones involved", "Shape of the bone ends"], "Structural classification is the one based on tissue and joint cavity.", "L12, slide 4")
add(3, "The mnemonic for the functional joint types is:", "SAD – ISM",
    ["So Long To Pinky", "Tiger Cubs Need MILC", "Come Let's Get Sun Burned"], "Synarthrotic/Amphiarthrotic/Diarthrotic = Immovable/Slightly movable/Movable.", "L12, slide 8")

# ---------- 4. Landmarks + articulations ----------
add(4, "What articulates with the head of the humerus?", "Glenoid fossa of the scapula",
    ["Acromion process", "Coracoid process", "Acetabulum"], "Humeral head + glenoid fossa = glenohumeral (shoulder) joint.", "L10, slides 11, 24")
add(4, "The capitulum of the humerus articulates with the:", "Head of the radius",
    ["Trochlear notch of the ulna", "Olecranon process", "Coronoid process of the ulna"], "Capitulum and radius are both lateral. Hook: capitulum = 'little head' meets the radial head.", "L10, slide 34")
add(4, "The trochlea of the humerus articulates with the:", "Trochlear notch of the ulna",
    ["Head of the radius", "Glenoid fossa", "Radial tuberosity"], "Trochlea (spool) sits in the trochlear notch of the ulna.", "L10, slides 35, 43")
add(4, "The head of the femur articulates with the:", "Acetabulum",
    ["Glenoid fossa", "Obturator foramen", "Greater sciatic notch"], "Femoral head + acetabulum = femoroacetabular (hip) joint.", "L11, slide 17")
add(4, "The patella articulates with the:", "Patellar surface of the femur",
    ["Tibial tuberosity", "Head of the fibula", "Medial malleolus"], "The patellofemoral joint. The patella is the largest sesamoid bone.", "L11, slides 30–31")
add(4, "The medial and lateral condyles of the femur articulate with the:", "Medial and lateral condyles of the tibia",
    ["Head of the fibula", "Patellar surface", "Talus"], "Tibiofemoral joint (the knee).", "L11, slides 34–35")
add(4, "The talus articulates with which bones to form the ankle (talocrural) joint?", "Tibia and fibula",
    ["Calcaneus and navicular", "Femur and tibia", "Cuboid and calcaneus"], "Talus + tibia + fibula = talocrural joint, the actual ankle joint.", "L11, slide 45")
add(4, "The trochlear notch of the ulna wraps around the:", "Trochlea of the humerus",
    ["Capitulum of the humerus", "Head of the radius", "Olecranon fossa"], "Humeroulnar joint, the hinge part of the elbow.", "L10, slide 43")
add(4, "The glenoid fossa is found on the superior part of which border of the scapula?", "Lateral (axillary) border",
    ["Medial (vertebral) border", "Superior border at the superior angle", "Inferior angle"], "It sits at the top of the lateral border, facing the humerus.", "L10, slide 11")
add(4, "Which humeral fossa receives the olecranon process when the elbow is straight?", "Olecranon fossa (posterior)",
    ["Coronoid fossa (anterior)", "Glenoid fossa", "Iliac fossa"], "Deep depression on the distal posterior humerus.", "L10, slide 33")
add(4, "The PSIS articulates with the sacrum to form the (per the deck):", "Sacroiliac (SI) joint",
    ["Pubic symphysis", "Hip joint", "Lumbosacral joint"], "The deck links the PSIS to the SI joint.", "L11, slide 8")

# ---------- 5. Ankle joints ----------
add(5, "The actual ankle joint is called the:", "Talocrural joint",
    ["Subtalar joint", "Tibiofemoral joint", "Intertarsal joint"], "Talus + tibia + fibula = talocrural joint.", "L11, slide 45")
add(5, "Which three bones form the talocrural (ankle) joint?", "Talus, tibia, fibula",
    ["Calcaneus, talus, navicular", "Tibia, fibula, calcaneus", "Talus, calcaneus, cuboid"], "The tibia and fibula sit on top of the talus.", "L11, slide 45")
add(5, "Per the deck (and the NYS boards), the ankle is which type of synovial joint?", "Hinge",
    ["Gliding", "Pivot", "Ball and socket"], "The deck flags it: Ankle = hinge ***NYS Boards***.", "L12, slide 29")
add(5, "Which tarsal forms the ankle joint with the tibia and fibula?", "Talus",
    ["Calcaneus", "Navicular", "Cuboid"], "Talus = 'tallest'; sits on top of the calcaneus.", "L11, slide 45")
add(5, "Which tarsal is the largest and the weight-bearing bone of the ankle (heel bone)?", "Calcaneus",
    ["Talus", "Cuboid", "Navicular"], "Calcaneus = heel bone, largest tarsal. The talus is 2nd largest.", "L11, slide 44")
add(5, "The bump on the MEDIAL ankle is the medial malleolus of the:", "Tibia",
    ["Fibula", "Talus", "Calcaneus"], "Medial malleolus = tibia.", "L11, slide 38")
add(5, "The bump on the LATERAL ankle is the lateral malleolus of the:", "Fibula",
    ["Tibia", "Talus", "Cuboid"], "Lateral malleolus = fibula.", "L11, slide 41")
add(5, "Pointing the foot down is called:", "Plantar flexion",
    ["Dorsiflexion", "Eversion", "Inversion"], "Plantar = sole. Like pressing a gas pedal.", "L12, slide 34")
add(5, "Pulling the foot up toward the shin is called:", "Dorsiflexion",
    ["Plantar flexion", "Inversion", "Circumduction"], "Toes toward the dorsum (top) of the foot.", "L12, slide 34")
add(5, "Turning the sole of the foot to face medially (in) is called:", "Inversion",
    ["Eversion", "Pronation", "Abduction"], "Inversion = in; eversion = out.", "L12, slide 34")
add(5, "The joint between the distal tibia and fibula is a:", "Syndesmosis (fibrous, slightly movable)",
    ["Synovial hinge joint", "Symphysis", "Suture"], "Fibrous membrane joining the tibia and fibula.", "L12, slides 7, 12")
add(5, "The joints between the tarsal bones (intertarsal joints) are which type?", "Gliding (planar)",
    ["Hinge", "Saddle", "Condyloid"], "Gliding joints: intercarpal, intertarsal, spinal facets.", "L12, slide 27")

# ---------- 6. Types of synovial joints ----------
add(6, "The shoulder and hip are which type of synovial joint?", "Ball and socket",
    ["Hinge", "Condyloid", "Saddle"], "Ball and socket: multiaxial, the most movable, allows all movements including rotation.", "L12, slide 32")
add(6, "Elbows, knees, PIPs, DIPs and the ankle are which type of joint?", "Hinge",
    ["Pivot", "Gliding", "Ball and socket"], "Hinge: flexion and extension ONLY (uniaxial).", "L12, slide 29")
add(6, "The CMC joint of the thumb is which type of joint?", "Saddle",
    ["Condyloid", "Hinge", "Pivot"], "Saddle = thumb CMC; biaxial; same movements as condyloid.", "L12, slide 31")
add(6, "The MCP joints (knuckles) are which type of joint?", "Condyloid (ellipsoidal)",
    ["Saddle", "Hinge", "Gliding"], "Condyloid: flexion/extension, abduction/adduction, circumduction; biaxial.", "L12, slide 30")
add(6, "C1 rotating on C2 is an example of which joint type?", "Pivot",
    ["Hinge", "Gliding", "Saddle"], "Pivot: rotation ONLY. Also the radius on the ulna during pronation/supination.", "L12, slide 28")
add(6, "Intercarpal, intertarsal and spinal facet joints are which type?", "Gliding (planar)",
    ["Pivot", "Condyloid", "Hinge"], "Two flat bones slide over each other; nonaxial.", "L12, slide 27")
add(6, "Which synovial joint type is the MOST movable?", "Ball and socket",
    ["Saddle", "Condyloid", "Hinge"], "Multiaxial: allows all movements including rotation.", "L12, slide 32")
add(6, "A hinge joint allows:", "Flexion and extension only",
    ["Rotation only", "All movements including rotation", "Sliding only"], "Uniaxial.", "L12, slide 29")
add(6, "A pivot joint allows:", "Rotation only",
    ["Flexion and extension only", "Circumduction only", "Sliding only"], "Uniaxial.", "L12, slide 28")
add(6, "Which joint type is described as nonaxial?", "Gliding (planar)",
    ["Pivot", "Hinge", "Saddle"], "Gliding = nonaxial; pivot and hinge = uniaxial; condyloid and saddle = biaxial; ball and socket = multiaxial.", "L12, slide 27")
add(6, "Condyloid and saddle joints are both:", "Biaxial",
    ["Uniaxial", "Nonaxial", "Multiaxial"], "They allow the same movements; they differ in shape and location.", "L12, slides 30–31")
add(6, "The radius rotating on the ulna during pronation and supination is which joint type?", "Pivot",
    ["Hinge", "Saddle", "Gliding"], "Pivot joints: C1 on C2, and radius on ulna.", "L12, slide 28")
add(6, "The glenohumeral (shoulder) joint is diarthrotic, synovial and:", "Ball and socket",
    ["Hinge", "Pivot", "Gliding"], "Most movable joint in the body, so a common site of dislocation.", "L12, slide 39")

# ---------- 7. Bones of the hand ----------
add(7, "How many carpal bones are in each wrist?", "8, in 2 rows of 4",
    ["7, in 2 rows", "5, one per finger", "14"], "8 carpals; 7 tarsals in the ankle.", "L10, slide 48")
add(7, "The proximal row of carpals, lateral (thumb) to medial (pinky), is:", "Scaphoid, lunate, triquetrum, pisiform",
    ["Trapezium, trapezoid, capitate, hamate", "Pisiform, triquetrum, lunate, scaphoid", "Scaphoid, trapezium, lunate, capitate"], "'So Long To Pinky' = Scaphoid, Lunate, Triquetrum, Pisiform.", "L10, slide 49")
add(7, "The distal row of carpals, medial (pinky) to lateral (thumb), is:", "Hamate, capitate, trapezoid, trapezium",
    ["Trapezium, trapezoid, capitate, hamate", "Pisiform, hamate, capitate, scaphoid", "Capitate, hamate, trapezium, trapezoid"], "'Here Comes The Thumb' = Hamate, Capitate, Trapezoid, Trapezium.", "L10, slide 49")
add(7, "The most MEDIAL bone of the PROXIMAL row of carpals is the:", "Pisiform",
    ["Scaphoid", "Hamate", "Triquetrum"], "So Long To Pinky: the pisiform is last, on the pinky side.", "L10, slides 49, 53")
add(7, "The most MEDIAL bone of the DISTAL row of carpals is the:", "Hamate",
    ["Pisiform", "Trapezium", "Capitate"], "Here Comes The Thumb starts on the pinky side with the Hamate. (The pisiform is medial in the PROXIMAL row.)", "L10, slides 49, 54")
add(7, "The most LATERAL bone of the PROXIMAL row of carpals is the:", "Scaphoid",
    ["Pisiform", "Trapezium", "Lunate"], "So Long To Pinky starts on the thumb side with the Scaphoid.", "L10, slides 49–50")
add(7, "The most LATERAL bone of the DISTAL row (at the base of the thumb) is the:", "Trapezium",
    ["Trapezoid", "Scaphoid", "Hamate"], "Trapezi-UM sits under the thUMb.", "L10, slides 49, 57")
add(7, "Which carpal sits in the CENTER of the distal row?", "Capitate",
    ["Lunate", "Trapezoid", "Triquetrum"], "Distal row M→L: hamate, CAPITATE, trapezoid, trapezium. The capitate is the largest carpal.", "L10, slide 55")
add(7, "The tunnel of Guyon runs between which two carpals?", "Pisiform and the hook of the hamate",
    ["Scaphoid and lunate", "Trapezium and trapezoid", "Capitate and lunate"], "The ulnar nerve and ulnar artery pass through it.", "L10, slide 49")
add(7, "Which metacarpal goes to the thumb?", "The 1st (lateral)",
    ["The 5th (lateral)", "The 1st (medial)", "The 5th (medial)"], "Metacarpals are numbered 1 (thumb, lateral) to 5 (pinky, medial).", "L10, slide 58")
add(7, "How many phalanges are in one hand?", "14",
    ["10", "15", "27"], "3 in each finger (proximal, middle, distal) and 2 in the thumb (proximal, distal).", "L10, slide 60")
add(7, "The thumb has which phalanges?", "Proximal and distal only",
    ["Proximal, middle and distal", "Middle and distal only", "Proximal and middle only"], "No middle phalanx in the thumb, so it has one IP joint.", "L10, slide 60")
add(7, "The joint between the middle and distal phalanges is the:", "DIP (distal interphalangeal)",
    ["PIP (proximal interphalangeal)", "MCP (metacarpophalangeal)", "CMC (carpometacarpal)"], "PIP = proximal–middle; DIP = middle–distal.", "L10, slides 62–63")
add(7, "Which carpal is LATERAL to the lunate in the proximal row?", "Scaphoid",
    ["Triquetrum", "Pisiform", "Capitate"], "Proximal row L→M: scaphoid, lunate, triquetrum, pisiform.", "L10, slide 49")
add(7, "The trapezoid sits between which two carpals in the distal row?", "Trapezium and capitate",
    ["Hamate and capitate", "Scaphoid and lunate", "Pisiform and hamate"], "Distal row L→M: trapezium, trapezoid, capitate, hamate.", "L10, slide 49")

# ---------- 8. Medial vs. lateral bones ----------
add(8, "Which forearm bone is LATERAL (thumb side)?", "Radius",
    ["Ulna", "Fibula", "Tibia"], "Radius = thumb side. Hook: palm up holding a bowl of soup, the radius is on the outside.", "L10, slide 39")
add(8, "Which forearm bone is MEDIAL (pinky side)?", "Ulna",
    ["Radius", "Humerus", "Fibula"], "Ulna = pinky side; forms most of the elbow.", "L10, slide 42")
add(8, "Which leg bone is MEDIAL and weight-bearing?", "Tibia",
    ["Fibula", "Femur", "Patella"], "The tibia (shin bone) is the large medial, weight-bearing bone.", "L11, slide 33")
add(8, "Which leg bone is LATERAL and NON-weight-bearing?", "Fibula",
    ["Tibia", "Radius", "Patella"], "The fibula is the small lateral bone; it carries no weight.", "L11, slide 39")
add(8, "The arm (brachium, shoulder to elbow) has how many bones?", "One: the humerus",
    ["Two: radius and ulna", "Two: humerus and scapula", "Three"], "Arm = humerus only. Forearm = radius + ulna.", "L10, slide 23")
add(8, "The thigh (hip to knee) has how many bones?", "One: the femur",
    ["Two: tibia and fibula", "Two: femur and patella", "Three"], "Thigh = femur. Leg (knee to ankle) = tibia + fibula.", "L11, slide 19")
add(8, "Which pair is correctly matched?", "Radius–lateral; tibia–medial",
    ["Radius–medial; tibia–lateral", "Ulna–lateral; fibula–medial", "Ulna–lateral; tibia–lateral"], "Radius lateral, ulna medial; tibia medial, fibula lateral.", "L10, slide 39; L11, slide 32")
add(8, "The medial malleolus belongs to the ___ and the lateral malleolus belongs to the ___.", "Tibia; fibula",
    ["Fibula; tibia", "Talus; calcaneus", "Tibia; talus"], "Medial = tibia, lateral = fibula.", "L11, slides 38, 41")
add(8, "In anatomical position, the 1st metatarsal (big toe) is on which side of the foot?", "Medial",
    ["Lateral", "Posterior", "Superior"], "Metatarsal 1 = medial (big toe). Metacarpal 1 = lateral (thumb).", "L11, slide 49")
add(8, "In anatomical position, the 1st metacarpal (thumb) is on which side of the hand?", "Lateral",
    ["Medial", "Anterior", "Posterior"], "Thumb = lateral; pinky = medial.", "L10, slide 58")
add(8, "Which side of the humerus has the deltoid tuberosity and greater tubercle?", "Lateral",
    ["Medial", "Posterior only", "Distal"], "Greater tubercle = superior lateral; deltoid tuberosity = halfway down the lateral side.", "L10, slides 28, 31")
add(8, "Which side of the femur has the greater trochanter?", "Lateral",
    ["Medial", "Posterior", "Distal"], "Greater trochanter = proximal lateral; lesser trochanter = proximal medial.", "L11, slides 22–23")

# ---------- 9. Landmarks: which bone (B) ----------
add(9, "The greater trochanter is on which bone?", "Femur",
    ["Humerus", "Coxal bone", "Tibia"], "Trochanters = femur only. The humerus has tubercles.", "L11, slide 22")
add(9, "The linea aspera is on which bone?", "Femur",
    ["Tibia", "Humerus", "Fibula"], "Ridge on the back of the femur.", "L11, slide 24")
add(9, "The tibial tuberosity is on which bone?", "Tibia",
    ["Femur", "Fibula", "Patella"], "Proximal anterior tibia; quadriceps tendon/patellar ligament attaches.", "L11, slide 36")
add(9, "The medial malleolus is on which bone?", "Tibia",
    ["Fibula", "Talus", "Femur"], "Medial ankle bump = tibia.", "L11, slide 38")
add(9, "The lateral malleolus is on which bone?", "Fibula",
    ["Tibia", "Calcaneus", "Femur"], "Lateral ankle bump = fibula.", "L11, slide 41")
add(9, "The ASIS and PSIS are on which bone?", "Ilium",
    ["Ischium", "Pubis", "Sacrum"], "Anterior/posterior superior ILIAC spines.", "L11, slides 6, 8")
add(9, "The ischial tuberosity ('sit bone') is on which bone?", "Ischium",
    ["Ilium", "Pubis", "Femur"], "Large roughened bump on the inferior ischium.", "L11, slide 13")
add(9, "The pubic tubercle is on which bone?", "Pubis",
    ["Ischium", "Ilium", "Femur"], "Small bumps on the superior pubic bones.", "L11, slide 15")
add(9, "The adductor tubercle is on which bone?", "Femur",
    ["Tibia", "Humerus", "Pubis"], "Attachment site above the medial epicondyle of the femur.", "L11, slide 29")
add(9, "The fovea capitis is a pit in the head of which bone?", "Femur",
    ["Humerus", "Radius", "Fibula"], "A ligament (ligament of the head of the femur) attaches there.", "L11, slide 21")
add(9, "The iliac crest is on which bone?", "Ilium",
    ["Ischium", "Pubis", "Sacrum"], "The main superior ridge of the ilium.", "L11, slide 5")
add(9, "The acetabulum is formed by which bone(s)?", "Ilium, ischium and pubis (all three)",
    ["Ilium only", "Ischium and pubis only", "Femur"], "Acetabulum = where all three meet and fuse. Obturator foramen = ischium + pubis only.", "L11, slide 17")
add(9, "The obturator foramen is formed by which bones?", "Ischium and pubis",
    ["Ilium and ischium", "Ilium and pubis", "Ilium, ischium and pubis"], "Largest foramen in the body, 'the eyes of the pelvis.'", "L11, slide 18")
add(9, "The ischial spine sits between:", "The greater and lesser sciatic notches",
    ["The ASIS and AIIS", "The PSIS and PIIS", "The pubic tubercle and symphysis"], "Top to bottom: greater sciatic notch → ischial spine → lesser sciatic notch → ischial tuberosity.", "L11, slide 12")
add(9, "The greater sciatic notch lies between:", "The PIIS (above) and the ischial spine (below)",
    ["The ASIS and AIIS", "The ischial spine and ischial tuberosity", "The iliac crest and PSIS"], "Passage for nerves, the piriformis muscle and vessels.", "L11, slide 11")

# ---------- 10. Articulations: what joins with what ----------
add(10, "What articulates with the MEDIAL end of the clavicle?", "Manubrium of the sternum",
    ["Acromion process", "Coracoid process", "1st thoracic vertebra"], "Medial clavicle + manubrium = sternoclavicular (SC) joint.", "L10, slide 5")
add(10, "What articulates with the LATERAL end of the clavicle?", "Acromion process of the scapula",
    ["Manubrium", "Coracoid process", "Head of the humerus"], "Lateral clavicle + acromion = acromioclavicular (AC) joint.", "L10, slide 6")
add(10, "The sternoclavicular joint is between:", "The medial clavicle and the manubrium",
    ["The lateral clavicle and the acromion", "The humeral head and glenoid fossa", "The 1st rib and the sternum"], "SC joint. Extremely stable.", "L10, slide 5; L12, slide 37")
add(10, "The acromioclavicular (AC) joint is between:", "The acromion and the lateral clavicle",
    ["The coracoid and the medial clavicle", "The manubrium and the medial clavicle", "The acromion and the humerus"], "AC joint: common site of shoulder separation.", "L10, slide 6; L12, slide 38")
add(10, "The glenohumeral joint is between:", "The head of the humerus and the glenoid fossa",
    ["The acromion and the clavicle", "The humerus and the ulna", "The head of the femur and the acetabulum"], "The shoulder joint.", "L10, slide 24")
add(10, "The femoroacetabular joint is the:", "Hip joint",
    ["Knee joint", "Sacroiliac joint", "Ankle joint"], "Head of the femur + acetabulum of the coxal bone.", "L11, slide 17; L12, slide 45")
add(10, "The elbow is made of which two articulations (per the joints lecture)?", "Humeroulnar and humeroradial",
    ["Tibiofemoral and patellofemoral", "Sternoclavicular and acromioclavicular", "Radiocarpal and intercarpal"], "Hinge between ulna and humerus; pivot between ulna and radius.", "L12, slide 42")
add(10, "The knee is made of which two articulations?", "Tibiofemoral and patellofemoral",
    ["Humeroulnar and humeroradial", "Talocrural and subtalar", "Femoroacetabular and sacroiliac"], "Femoral + tibial condyles; patella + patellar surface.", "L12, slide 48")
add(10, "The carpometacarpal (CMC) joints are between:", "The carpals and the metacarpals",
    ["The metacarpals and the phalanges", "The radius and the carpals", "Two phalanges"], "MCP = metacarpals–phalanges.", "L10, slide 59")
add(10, "The metacarpophalangeal (MCP) joints are between:", "The metacarpals and the proximal phalanges",
    ["The carpals and the metacarpals", "The proximal and middle phalanges", "The middle and distal phalanges"], "Sometimes called 'knuckles,' an inexact term.", "L10, slide 61")
add(10, "The PIP joint joins which bones?", "Proximal and middle phalanges",
    ["Middle and distal phalanges", "Metacarpal and proximal phalanx", "The two thumb phalanges"], "The thumb has an IP joint instead.", "L10, slide 62")
add(10, "The pubic symphysis is where:", "The right and left pubic bones meet",
    ["The ilium meets the sacrum", "The femur meets the acetabulum", "The ischium meets the pubis"], "A cartilaginous joint (fibrocartilage), not a bone marking.", "L11, slide 16")
add(10, "The talocrural joint is between:", "The talus, tibia and fibula",
    ["The talus and calcaneus", "The tibia and femur", "The calcaneus and cuboid"], "The actual ankle joint.", "L11, slide 45")
add(10, "Each of the 1st three metatarsals sits on which tarsal? (1st, 2nd, 3rd)", "Medial, intermediate, lateral cuneiform",
    ["Navicular, cuboid, talus", "Cuboid, medial cuneiform, navicular", "Talus, navicular, cuboid"], "M-I-L cuneiforms sit at the bases of metatarsals 1, 2, 3.", "L11, slide 48")

# ---------- Diagram keys (class handouts) ----------
# key: number -> (name, hint, source). GROUPS = sets of look-alike labels used as nearby distractors.
HUMERUS = {
    1: ("Head of the humerus", "Smooth, rounded top; points medially.", "L10, slide 25"),
    2: ("Anatomical neck", "Ridge right around the head (old growth plate).", "L10, slide 26"),
    3: ("Surgical neck", "Below the tubercles; common fracture site.", "L10, slide 27"),
    4: ("Greater tubercle", "Large bump, superior lateral.", "L10, slide 28"),
    5: ("Lesser tubercle", "Small bump, superior anterior.", "L10, slide 29"),
    6: ("Intertubercular (bicipital) groove", "Channel between the tubercles.", "L10, slide 30"),
    7: ("Deltoid tuberosity", "Rough bump halfway down the lateral shaft.", "L10, slide 31"),
    8: ("Lateral supracondylar ridge", "Sharp ridge on the lateral shaft just above the lateral epicondyle (on the class handout; not on the slides).", "L10 handout diagram"),
    9: ("Lateral epicondyle", "Bump on the distal lateral humerus.", "L10, slide 37"),
    10: ("Capitulum", "Ball on the distal lateral end; meets the radial head.", "L10, slide 34"),
    11: ("Trochlea", "Spool beside the capitulum; meets the ulna's trochlear notch.", "L10, slide 35"),
    12: ("Medial epicondyle", "Bump on the distal medial humerus.", "L10, slide 36"),
    13: ("Coronoid fossa", "Shallow depression, distal ANTERIOR.", "L10, slide 32"),
    14: ("Olecranon fossa", "Deep depression, distal POSTERIOR.", "L10, slide 33"),
}
HUMERUS_GROUPS = [{1, 2, 3}, {4, 5, 6}, {8, 9, 12}, {9, 12, 10}, {10, 11}, {13, 14}, {7, 4}]

FEMUR = {
    1: ("Head of the femur", "Rounded top; points medially into the acetabulum.", "L11, slide 20"),
    2: ("Neck of the femur", "Just distal to the head.", "L11, slide 20"),
    3: ("Greater trochanter", "Large bump, proximal lateral.", "L11, slide 22"),
    4: ("Lesser trochanter", "Small bump, proximal medial.", "L11, slide 23"),
    5: ("Fovea capitis", "Pit in the femoral head for a ligament.", "L11, slide 21"),
    6: ("Linea aspera", "Ridge down the back of the femur.", "L11, slide 24"),
    7: ("Adductor tubercle", "Bump above the medial epicondyle.", "L11, slide 29"),
    8: ("Patellar surface", "Anterior groove where the patella sits.", "L11, slide 30"),
    9: ("Medial epicondyle", "Attachment bump above the medial condyle.", "L11, slide 27"),
    10: ("Lateral epicondyle", "Attachment bump above the lateral condyle.", "L11, slide 28"),
    11: ("Medial condyle", "Smooth distal medial surface (joint with the tibia).", "L11, slide 25"),
    12: ("Lateral condyle", "Smooth distal lateral surface (joint with the tibia).", "L11, slide 26"),
}
FEMUR_GROUPS = [{1, 2, 5}, {3, 4}, {7, 9, 10}, {11, 12, 9, 10}, {6, 8}]

FOREARM = {
    1: ("Trochlear notch (ulna)", "C-shaped notch that wraps the trochlea.", "L10, slide 43"),
    2: ("Head of the radius", "Rounded proximal end, like a bat handle.", "L10, slide 39"),
    3: ("Neck of the radius", "Just distal to the radial head.", "L10, slide 40"),
    4: ("Radial tuberosity", "Bump just below the radial neck.", "L10, slide 40"),
    5: ("Styloid process of the radius", "Distal lateral bump (thumb side).", "L10, slide 41"),
    6: ("Styloid process of the ulna", "Distal medial, posterior bump (pinky side).", "L10, slide 45"),
    7: ("Interosseous membrane", "Fibrous sheet joining the radius and ulna.", "L10, slide 46"),
    8: ("Coronoid process (ulna)", "Just distal to the trochlear notch, anterior.", "L10, slide 44"),
    9: ("Olecranon process (ulna)", "Forms the point of the elbow.", "L10, slide 42"),
    10: ("Head of the ulna", "Distal end of the ulna, just above its styloid.", "L10, slide 45"),
}
FOREARM_GROUPS = [{2, 3, 4}, {1, 8, 9}, {5, 6, 10}, {7, 4}]

LEG = {
    1: ("Lateral condyle of the tibia", "Proximal lateral tibia; meets the femur's lateral condyle.", "L11, slide 35"),
    2: ("Head of the fibula", "Most proximal part of the fibula.", "L11, slide 40"),
    3: ("Neck of the fibula", "Just distal to the fibular head.", "L11, slide 40"),
    4: ("Medial condyle of the tibia", "Proximal medial tibia; meets the femur's medial condyle.", "L11, slide 34"),
    5: ("Tibial tuberosity", "Proximal anterior bump; patellar ligament attaches.", "L11, slide 36"),
    6: ("Anterior crest of the tibia", "Raised ridge down the front: the shin.", "L11, slide 37"),
    7: ("Medial malleolus (tibia)", "Medial ankle bump.", "L11, slide 38"),
    8: ("Lateral malleolus (fibula)", "Lateral ankle bump.", "L11, slide 41"),
}
LEG_GROUPS = [{1, 4, 5}, {2, 3, 1}, {7, 8}, {5, 6}]

HAND = {
    1: ("Distal phalanx", "Fingertip bone.", "L10, slide 60"),
    2: ("Middle phalanx", "Between the proximal and distal phalanges (not in the thumb).", "L10, slide 60"),
    3: ("Proximal phalanx", "Closest to the palm.", "L10, slide 60"),
    4: ("Phalanges", "Finger bones: 14 per hand.", "L10, slide 60"),
    5: ("Metacarpals", "Palm bones, numbered 1 (thumb) to 5 (pinky).", "L10, slide 58"),
    6: ("Carpals", "8 wrist bones in 2 rows of 4.", "L10, slide 48"),
    7: ("Hamate", "Distal row, most medial (pinky side); has a hook.", "L10, slide 54"),
    8: ("Pisiform", "Proximal row, most medial (pinky side); pea-shaped.", "L10, slide 53"),
    9: ("Triquetrum", "Proximal row, beside the pisiform.", "L10, slide 52"),
    10: ("Lunate", "Proximal row, between the scaphoid and triquetrum.", "L10, slide 51"),
    11: ("Ulna", "Medial (pinky-side) forearm bone.", "L10, slide 42"),
    12: ("Radius", "Lateral (thumb-side) forearm bone.", "L10, slide 39"),
    13: ("Capitate", "Center of the distal row.", "L10, slide 55"),
    14: ("Scaphoid", "Proximal row, most lateral (thumb side).", "L10, slide 50"),
    15: ("Trapezium", "Distal row, most lateral: under the thumb.", "L10, slide 57"),
    16: ("Trapezoid", "Distal row, between the trapezium and capitate.", "L10, slide 56"),
    17: ("Proximal phalanx of the thumb", "Thumb has only proximal and distal phalanges.", "L10, slide 60"),
    18: ("Distal phalanx of the thumb", "Tip of the thumb.", "L10, slide 60"),
}
HAND_GROUPS = [{1, 2, 3}, {17, 18, 2}, {4, 5, 6}, {7, 8, 9, 13}, {10, 14, 9, 8}, {15, 16, 13, 14}, {11, 12}]

FOOT = {
    1: ("Medial cuneiform", "Base of the 1st metatarsal (big toe).", "L11, slide 48"),
    2: ("Intermediate cuneiform", "Base of the 2nd metatarsal.", "L11, slide 48"),
    3: ("Navicular", "Medial, in front of the talus.", "L11, slide 46"),
    4: ("Talus", "On top of the calcaneus; forms the ankle joint.", "L11, slide 45"),
    5: ("Calcaneus", "Heel bone; largest tarsal.", "L11, slide 44"),
    6: ("Cuboid", "Lateral, in front of the calcaneus.", "L11, slide 47"),
    7: ("Lateral cuneiform", "Base of the 3rd metatarsal.", "L11, slide 48"),
    8: ("Metatarsals", "Bones of the arch, numbered 1 (big toe) to 5.", "L11, slide 49"),
    9: ("Proximal phalanx", "Toe bone closest to the metatarsal.", "L11, slide 50"),
    10: ("Middle phalanx", "Toes 2–5 only; the big toe has no middle phalanx.", "L11, slide 50"),
    11: ("Distal phalanx", "Tip of the toe (also labeled on the big toe).", "L11, slide 50"),
    12: ("Phalanges", "Toe bones: 14 per foot.", "L11, slide 50"),
}
FOOT_GROUPS = [{1, 2, 7}, {3, 6, 1}, {4, 5}, {8, 12, 9}, {9, 10, 11}]

SCAPULA = {
    1: ("Medial (vertebral) border", "Edge closest to the spine.", "L10, slide 7"),
    2: ("Lateral (axillary) border", "Edge toward the armpit.", "L10, slide 8"),
    3: ("Acromion process", "High point of the shoulder; end of the spine.", "L10, slide 14"),
    4: ("Coracoid process", "Finger-like ANTERIOR projection.", "L10, slide 17"),
    5: ("Inferior angle", "Bottom corner where the borders meet.", "L10, slide 9"),
    6: ("Superior angle", "Top corner of the medial border.", "L10, slide 10"),
    7: ("Glenoid fossa", "Shallow socket for the humeral head.", "L10, slide 11"),
    8: ("Infraglenoid tubercle", "Bump just below the glenoid fossa.", "L10, slide 12"),
    10: ("Spine of the scapula", "Posterior ridge running medial to lateral.", "L10, slide 15"),
    11: ("Root of the spine", "Medial start of the spine (about T4).", "L10, slide 16"),
    12: ("Infraspinous fossa", "Below the spine (posterior).", "L10, slide 20"),
    13: ("Supraspinous fossa", "Above the spine (posterior).", "L10, slide 19"),
    14: ("Subscapular fossa", "Anterior surface, against the ribs.", "L10, slide 21"),
    15: ("Scapular notch", "Notch just medial to the coracoid.", "L10, slide 22"),
}
SCAPULA_GROUPS = [{1, 2}, {3, 4, 7}, {5, 6}, {7, 8}, {10, 11}, {12, 13, 14}, {15, 4}]

GIRDLE = {
    "A": ("Acromion process", "Lateral tip of the scapula; high point of the shoulder.", "L10, slide 14"),
    "B": ("Acromioclavicular (AC) joint", "Lateral clavicle meets the acromion.", "L10, slide 6"),
    "C": ("Glenohumeral joint", "Head of the humerus meets the glenoid fossa: the shoulder joint.", "L10, slide 24"),
    "D": ("Clavicle", "S-shaped collarbone.", "L10, slide 4"),
    "E": ("Sternoclavicular (SC) joint", "Medial clavicle meets the manubrium.", "L10, slide 5"),
}
GIRDLE_GROUPS = [{"B", "C", "E"}, {"A", "D"}]

PELVIS = {
    "A": ("Ilium", "Large upper wing of the coxal bone.", "L11, slide 4"),
    "B": ("Ischium", "Lower posterior part of the coxal bone.", "L11, slide 4"),
    "C": ("Pubis", "Anterior part; meets its partner at the symphysis.", "L11, slide 4"),
    "D": ("Acetabulum", "Hip socket where all three bones fuse.", "L11, slide 17"),
    "E": ("Obturator foramen", "Hole framed by the ischium and pubis.", "L11, slide 18"),
    1: ("Iliac crest", "Main ridge along the top of the ilium.", "L11, slide 5"),
    2: ("Iliac fossa", "Shallow depression on the inner ilium.", "L11, slide 10"),
    3: ("PSIS (posterior superior iliac spine)", "Where the crest ends in back.", "L11, slide 8"),
    4: ("PIIS (posterior inferior iliac spine)", "Below the PSIS.", "L11, slide 9"),
    6: ("ASIS (anterior superior iliac spine)", "Where the crest ends in front.", "L11, slide 6"),
    7: ("AIIS (anterior inferior iliac spine)", "Below the ASIS.", "L11, slide 7"),
    10: ("Greater sciatic notch", "Between the PIIS and ischial spine.", "L11, slide 11"),
    11: ("Ischial tuberosity", "Large rough 'sit bone.'", "L11, slide 13"),
    12: ("Ischial spine", "Between the greater and lesser sciatic notches.", "L11, slide 12"),
    13: ("Lesser sciatic notch", "Between the ischial spine and tuberosity.", "L11, slide 14"),
    14: ("Pubic symphysis", "Cartilaginous joint between the pubic bones.", "L11, slide 16"),
    15: ("Pubic tubercle", "Small bump on the superior pubis.", "L11, slide 15"),
}
PELVIS_GROUPS = [{"A", "B", "C"}, {"D", "E"}, {3, 4, 6, 7}, {10, 12, 13, 11}, {14, 15}, {1, 2}]

rng = random.Random(4)

# Pairs that must never appear as each other's distractors (same structure name on another digit).
CONFLICTS = {frozenset(p) for p in [(1, 18), (3, 17)]}

def distractors(key, n, groups):
    bad = {k for k in key if frozenset((k, n)) in CONFLICTS} if key is HAND else set()
    near = set().union(*[g for g in groups if n in g]) - {n} - bad
    picks = list(near)
    rng.shuffle(picks)
    picks = picks[:2]
    rest = [k for k in key if k != n and k not in picks and k not in bad]
    rng.shuffle(rest)
    return (picks + rest)[:3]

def tag(n):
    return f"#{n}" if isinstance(n, int) else n

def diagram_qs(key, groups, img, label):
    qs = []
    for n, (name, hint, src) in key.items():
        lead = name[0].lower() + name[1:]
        if lead.startswith(("psis", "pIIS", "asis", "aiis")) or name[:4].isupper():
            lead = name
        d = distractors(key, n, groups)
        qs.append((f"{label}: what does {tag(n)} point to?", name, [key[k][0] for k in d], f"{tag(n)} = {name}. {hint}", src, img))
        d = distractors(key, n, groups)
        qs.append((f"{label}: which label is the {lead}?", tag(n), [tag(k) for k in d], f"{tag(n)} = {name}. {hint}", src, img))
    return qs

def spread(qs, topics):
    rng.shuffle(qs)
    for i, (q, a, w, e, s, img) in enumerate(qs):
        add(topics[i % len(topics)], q, a, w, e, s)
        B.Q[-1]["img"] = img

# Humerus or femur (11-14)
HF = (diagram_qs(HUMERUS, HUMERUS_GROUPS, "img/humerus.jpg", "Humerus handout (anterior left, posterior right)")
      + diagram_qs(FEMUR, FEMUR_GROUPS, "img/femur.jpg", "Femur handout (anterior left, posterior right)"))
HF += [
    ("Humerus handout: the left drawing is the anterior view. Which numbers appear ONLY on the posterior (right) drawing?", "#14 (olecranon fossa)", ["#13 (coronoid fossa)", "#5 (lesser tubercle)", "#10 (capitulum)"], "The olecranon fossa is posterior; the coronoid fossa (#13) is anterior.", "L10, slides 32–33", "img/humerus.jpg"),
    ("Humerus handout: #10 (capitulum) articulates with which bone?", "Radius (its head)", ["Ulna (trochlear notch)", "Scapula", "Clavicle"], "Capitulum = lateral = radius.", "L10, slide 34", "img/humerus.jpg"),
    ("Humerus handout: #11 (trochlea) articulates with which bone?", "Ulna (trochlear notch)", ["Radius (head)", "Scapula (glenoid fossa)", "Femur"], "Trochlea = ulna.", "L10, slide 35", "img/humerus.jpg"),
    ("Humerus handout: #1 fits into which structure?", "Glenoid fossa of the scapula", ["Acetabulum", "Acromion", "Olecranon fossa"], "Humeral head + glenoid fossa = glenohumeral joint.", "L10, slide 24", "img/humerus.jpg"),
    ("Femur handout: #1 fits into which structure?", "Acetabulum", ["Glenoid fossa", "Obturator foramen", "Tibial condyles"], "Femoral head + acetabulum = hip joint.", "L11, slide 17", "img/femur.jpg"),
    ("Femur handout: #6 (linea aspera) is seen on which view?", "Posterior (right drawing)", ["Anterior (left drawing)", "Both equally", "Neither"], "Linea aspera = ridge on the BACK of the femur.", "L11, slide 24", "img/femur.jpg"),
    ("Femur handout: #11 and #12 articulate with the:", "Condyles of the tibia", ["Patella", "Head of the fibula", "Acetabulum"], "Tibiofemoral joint.", "L11, slides 34–35", "img/femur.jpg"),
    ("Femur handout: #8 (patellar surface) articulates with the:", "Patella", ["Tibial tuberosity", "Fibular head", "Medial malleolus"], "Patellofemoral joint.", "L11, slides 30–31", "img/femur.jpg"),
]
spread(HF, list(range(11, 15)))

# Forearm or leg (15-20)
FL = (diagram_qs(FOREARM, FOREARM_GROUPS, "img/forearm.jpg", "Forearm handout (anterior view)")
      + diagram_qs(LEG, LEG_GROUPS, "img/leg.jpg", "Leg handout (anterior view)"))
FL += [
    ("Forearm handout: which bone is on the LEFT (with #2–#5)?", "Radius", ["Ulna", "Humerus", "Fibula"], "Radial head, neck, tuberosity and styloid: the lateral (thumb-side) bone.", "L10, slide 39", "img/forearm.jpg"),
    ("Forearm handout: which bone has #1, #8 and #9?", "Ulna", ["Radius", "Humerus", "Tibia"], "Trochlear notch, coronoid process and olecranon process are all on the ulna.", "L10, slides 42–44", "img/forearm.jpg"),
    ("Forearm handout: #1 (trochlear notch) articulates with the:", "Trochlea of the humerus", ["Capitulum of the humerus", "Head of the radius", "Carpals"], "Humeroulnar joint.", "L10, slide 43", "img/forearm.jpg"),
    ("Forearm handout: #2 (radial head) articulates with the:", "Capitulum of the humerus", ["Trochlea of the humerus", "Olecranon fossa", "Glenoid fossa"], "Capitulum meets the radial head.", "L10, slide 34", "img/forearm.jpg"),
    ("Forearm handout: the joint formed by #7 (interosseous membrane) is a:", "Syndesmosis (slightly movable)", ["Synovial hinge", "Suture", "Symphysis"], "Fibrous sheet between the radius and ulna = syndesmosis, amphiarthrotic.", "L12, slide 7", "img/forearm.jpg"),
    ("Leg handout: which bone is on the LEFT (with #2, #3, #8)?", "Fibula", ["Tibia", "Femur", "Radius"], "The thin lateral, non-weight-bearing bone.", "L11, slide 39", "img/leg.jpg"),
    ("Leg handout: which bone has #4, #5, #6 and #7?", "Tibia", ["Fibula", "Femur", "Ulna"], "Medial condyle, tibial tuberosity, anterior crest and medial malleolus.", "L11, slides 33–38", "img/leg.jpg"),
    ("Leg handout: #7 and #8 together hold which tarsal to form the ankle joint?", "Talus", ["Calcaneus", "Navicular", "Cuboid"], "Talocrural joint = tibia + fibula + talus.", "L11, slide 45", "img/leg.jpg"),
    ("Leg handout: which bone in this drawing is weight-bearing?", "Tibia (right)", ["Fibula (left)", "Both equally", "Neither"], "Tibia = weight-bearing; fibula = non-weight-bearing.", "L11, slides 33, 39", "img/leg.jpg"),
    ("Leg handout: the patellar ligament (quadriceps tendon) attaches at:", "#5 (tibial tuberosity)", ["#6 (anterior crest)", "#2 (head of the fibula)", "#4 (medial condyle)"], "Tibial tuberosity.", "L11, slide 36", "img/leg.jpg"),
]
spread(FL, list(range(15, 21)))

# Hand or foot (21-25)
HFt = (diagram_qs(HAND, HAND_GROUPS, "img/hand.jpg", "Hand handout")
       + diagram_qs(FOOT, FOOT_GROUPS, "img/foot.jpg", "Foot handout"))
HFt += [
    ("Hand handout: which side of this drawing is the thumb (lateral) side?", "Right side (#14–#18)", ["Left side (#7–#11)", "Top", "Bottom"], "Scaphoid, trapezium, trapezoid and the thumb are on the right.", "L10, slide 49", "img/hand.jpg"),
    ("Hand handout: #8, #9, #10 and #14 make up which row of carpals?", "Proximal row", ["Distal row", "Metacarpals", "Phalanges"], "Proximal row: scaphoid (14), lunate (10), triquetrum (9), pisiform (8).", "L10, slide 49", "img/hand.jpg"),
    ("Hand handout: #7, #13, #15 and #16 make up which row of carpals?", "Distal row", ["Proximal row", "Metacarpals", "Forearm"], "Distal row: hamate (7), capitate (13), trapezoid (16), trapezium (15).", "L10, slide 49", "img/hand.jpg"),
    ("Hand handout: the tunnel of Guyon lies between #8 and the hook of which bone?", "#7 (hamate)", ["#13 (capitate)", "#9 (triquetrum)", "#15 (trapezium)"], "Pisiform + hook of the hamate; ulnar nerve and artery pass through.", "L10, slide 49", "img/hand.jpg"),
    ("Hand handout: why does the thumb show only #17 and #18?", "The thumb has no middle phalanx", ["The middle phalanx is fused to the metacarpal", "The thumb has no proximal phalanx", "It's hidden behind the trapezium"], "Thumb = proximal + distal phalanges only.", "L10, slide 60", "img/hand.jpg"),
    ("Foot handout: which numbers are the 7 tarsals?", "#1–#7", ["#1–#8", "#8–#12", "#3–#9"], "Talus, calcaneus, navicular, cuboid and the three cuneiforms.", "L11, slide 43", "img/foot.jpg"),
    ("Foot handout: #1, #2 and #7 together are the:", "Cuneiforms (medial, intermediate, lateral)", ["Metatarsals 1–3", "Navicular, cuboid, talus", "Phalanges"], "M-I-L cuneiforms sit at the bases of metatarsals 1–3.", "L11, slide 48", "img/foot.jpg"),
    ("Foot handout: which number forms the ankle joint with the tibia and fibula?", "#4 (talus)", ["#5 (calcaneus)", "#3 (navicular)", "#6 (cuboid)"], "Talocrural joint.", "L11, slide 45", "img/foot.jpg"),
    ("Foot handout: which side of the drawing is medial (big toe side)?", "Left", ["Right", "Top", "Bottom"], "Metatarsal 1 and the great toe are medial.", "L11, slide 49", "img/foot.jpg"),
    ("Foot handout: the big toe (left) has which phalanges?", "Proximal and distal only", ["Proximal, middle and distal", "Middle and distal only", "Only a proximal phalanx"], "The great toe has 2 phalanges; toes 2–5 have 3.", "L11, slide 50", "img/foot.jpg"),
]
spread(HFt, list(range(21, 26)))

# Shoulder girdle diagrams feed topic 2; pelvis feeds topic 9; scapula feeds topic 1
spread(diagram_qs(GIRDLE, GIRDLE_GROUPS, "img/girdle.jpg", "Right pectoral girdle (anterior)"), [2])
spread(diagram_qs(SCAPULA, SCAPULA_GROUPS, "img/scapula.jpg", "Scapula handout (posterior left, anterior right)")[:12], [1])
spread(diagram_qs(PELVIS, PELVIS_GROUPS, "img/pelvis.jpg", "Pelvis handout")[:12], [9])

QUIZ = {"id": "q4", "title": "A&P Quiz #4", "lectures": "Lectures 10–12",
        "units": {"L10": "Upper Extremity", "L11": "Lower Extremity", "L12": "Joints"},
        "topics": TOPICS, "questions": B.Q}
