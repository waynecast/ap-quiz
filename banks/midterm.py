# A&P Midterm practice bank (Lectures 1-15). Built by build.py.
# Topics 1-17 follow Wayne's midterm topic list; 18-40 cover the rest of Lectures 1-15,
# weighted toward Muscle Tissue (L13-14) and Endocrine (L15), which had no quiz.
# Topics 41-50 are the diagram section: each practice exam picks 2 of the 4 class diagrams
# (pelvis/os coxae, scapula, tibia/fibula, humerus) and asks 5 questions on each.
# Many topics reuse questions from the Quiz #1-4 banks; new questions are written below.
# Hormone questions follow the instructor's "Hormones" chart (scanned 11/20, A&P-15) where it
# differs from the slides (e.g. renin -> body vasculature, controls BP).
import copy
from banks import quiz1, quiz2, quiz3, quiz4
from banks.common import Bank

SRC = {"q1": quiz1.QUIZ, "q2": quiz2.QUIZ, "q3": quiz3.QUIZ, "q4": quiz4.QUIZ}

TOPICS = {
    1: "Body planes (sagittal, frontal, transverse)",
    2: "Which term does NOT mean head (cranial, cephalad…)",
    3: "Compact bone structure (osteon)",
    4: "Anatomy (structure) vs. physiology (function)",
    5: "Chemistry: LEO GER, ionic vs. covalent bonds",
    6: "Landmarks: which bone is it on?",
    7: "Organelles (e.g. ATP = mitochondria)",
    8: "Body membranes (serous, mucous, cutaneous, synovial)",
    9: "Cell cycle (G1, S, G2, M)",
    10: "Skin layers (lucidum = palms & soles only)",
    11: "Corpuscles and skin receptors",
    12: "Skin glands: sebaceous, sudoriferous",
    13: "Characteristics of epithelial tissue",
    14: "Skin glands: ceruminous, eccrine, apocrine",
    15: "Hormones and blood pressure (renin…)",
    16: "Hormones: source, target, effect",
    17: "Epithelium types (which one stretches)",
    18: "Homeostasis and feedback",
    19: "Directional terms",
    20: "Atoms, molecules and compounds",
    21: "Biochemistry: carbs, water, pH",
    22: "Cell membrane and transport",
    23: "DNA, RNA and mitosis",
    24: "Tissues: CT fibers, junctions, goblet cells",
    25: "Bone cells and calcium (blasts, clasts, PTH)",
    26: "Bone: fractures, hard vs. strong, repair",
    27: "Skull and spine",
    28: "Ribs, girdles, hand and foot",
    29: "Joints",
    30: "Muscle: skeletal, cardiac, smooth",
    31: "Muscle fiber and the sarcomere",
    32: "Muscle CT wrappings, tendon, origin/insertion",
    33: "Neuromuscular junction and contraction",
    34: "Motor units, twitch, tetanus, contraction types",
    35: "Muscle energy, fiber types, nervous system",
    36: "Endocrine basics: glands and hormone types",
    37: "Pituitary, pineal, thymus",
    38: "Thyroid and parathyroid",
    39: "Pancreas, kidneys, gonads",
    40: "Adrenal glands",
}
DG_TOPICS = list(range(41, 51))
for t in DG_TOPICS:
    TOPICS[t] = "Diagram: pelvis, scapula, tibia/fibula or humerus"
DG_NAMES = {"pelvis": "Pelvis (os coxae)", "scapula": "Scapula", "leg": "Tibia / fibula", "humerus": "Humerus"}

B = Bank()
add = B.add

# ---------- Reused questions from the quiz banks ----------
POOLS = {
    1: [("q1", 1), ("q1", 23)],
    2: [("q1", 6), ("q1", 20)],
    4: [("q1", 2)],
    5: [("q1", 3), ("q1", 5), ("q1", 17)],
    6: [("q4", 1), ("q4", 9)],
    7: [("q2", 6), ("q2", 18), ("q2", 25), ("q1", 15)],
    8: [("q2", 3)],
    9: [("q2", 21), ("q2", 1)],
    10: [("q2", 12), ("q2", 10), ("q2", 15)],
    11: [("q2", 13)],
    12: [("q2", 11)],
    13: [("q2", 9)],
    17: [("q2", 14), ("q2", 4)],
    18: [("q1", 8), ("q1", 14)],
    19: [("q1", 24)],
    20: [("q1", 7), ("q1", 11), ("q1", 13)],
    21: [("q1", 16), ("q1", 19), ("q1", 9)],
    22: [("q1", 22), ("q1", 10)],
    23: [("q2", 17), ("q2", 5)],
    24: [("q2", 19), ("q2", 2), ("q2", 24), ("q2", 8)],
    25: [("q3", 1), ("q3", 3), ("q3", 4)],
    26: [("q3", 5), ("q3", 6), ("q3", 7)],
    27: [("q3", 8), ("q3", 9), ("q3", 10), ("q3", 11)],
    28: [("q3", 2), ("q4", 2), ("q4", 7), ("q4", 8)],
    29: [("q4", 3), ("q4", 6), ("q4", 5), ("q4", 10)],
}
for t, srcs in POOLS.items():
    for qz, st in srcs:
        for q in SRC[qz]["questions"]:
            if q["topic"] == st and not q.get("img"):
                c = copy.deepcopy(q)
                c["topic"] = t
                c.pop("u", None)
                B.Q.append(c)

# ---------- 3. Compact bone structure (L7, slides 32-41) ----------
add(3, "Which is the structural unit of compact bone?", "Osteon (Haversian system)",
    ["Trabecula", "Lamella", "Sarcomere"], "Osteons are long cylinders running the length of the bone. Spongy bone has trabeculae instead.", "L7, slides 32–41")
add(3, "The central (Haversian) canal of an osteon contains:", "Blood vessels, nerves and lymphatics",
    ["Osteocytes only", "Red bone marrow", "Hyaline cartilage"], "They nourish the osteon.", "L7, slides 32–41")
add(3, "Which canals run PERPENDICULAR to the osteons and connect the outside of the bone to the inside?", "Volkmann's (perforating) canals",
    ["Central (Haversian) canals", "Canaliculi", "Lacunae"], "Volkmann's canals carry vessels, nerves and lymphatics in from the periosteum.", "L7, slides 32–41")
add(3, "The concentric rings around the central canal that give compact bone strength are:", "Lamellae",
    ["Lacunae", "Canaliculi", "Trabeculae"], "Lamellae = rings; lacunae = 'little lakes' between them.", "L7, slides 32–41")
add(3, "Lacunae ('little lakes') house:", "Osteocytes",
    ["Osteoclasts", "Chondrocytes", "Red blood cells"], "Mature bone cells sit in lacunae between the lamellae.", "L7, slides 32–41")
add(3, "Canaliculi ('little canals') do what?", "Connect lacunae to the central canal for nutrients and waste",
    ["Connect the periosteum to the endosteum", "Store calcium for muscle contraction", "Form the growth plate"], "Tiny channels linking osteocytes to the blood supply.", "L7, slides 32–41")
add(3, "Which bone tissue has NO osteons and is made of thin plates called trabeculae?", "Spongy (cancellous) bone",
    ["Compact bone", "Woven bone", "Cortical bone"], "Spongy bone fills the ends of long bones and the inside of other bones.", "L7, slides 32–41")
add(3, "Compact bone is also called:", "Dense or cortical bone",
    ["Cancellous or trabecular bone", "Woven bone", "Spongy bone"], "Solid to the eye, around the outside of every bone.", "L7, slides 32–41")
add(3, "Woven bone is normal in:", "Children",
    ["Adults", "The elderly", "No one; it is always abnormal"], "Poorly mineralized, slightly flexible; abnormal in anyone else.", "L7, slides 32–41")

# ---------- 13. Characteristics of epithelial tissue (L5, slides 10-17) ----------
add(13, "Which is NOT a characteristic of epithelial tissue?", "Highly vascular",
    ["Highly cellular", "Highly mitotic", "Has an apical (free) surface"], "Epithelium is AVASCULAR. Connective tissue is the vascular one.", "L5, slides 10–17")
add(13, "Which is NOT a characteristic of epithelial tissue?", "Lots of matrix between cells",
    ["Cells tightly packed", "Avascular", "Readily replaces itself"], "Epithelium has very little matrix. Lots of matrix = connective tissue.", "L5, slides 10–17")
add(13, "Which is NOT a characteristic of epithelial tissue?", "Not mitotic (low turnover)",
    ["Avascular", "Has apical, lateral and basal surfaces", "Covers and lines surfaces"], "Epithelium is highly mitotic. Low turnover describes connective tissue.", "L5, slides 10–17")
add(13, "The three surfaces of an epithelial cell are:", "Apical, lateral and basal",
    ["Parietal, visceral and serous", "Superficial, deep and intermediate", "Proximal, middle and distal"], "Apical = free top, lateral = sides, basal = bottom on the basement membrane.", "L5, slides 10–17")
add(13, "Which type of epithelium is the exception to 'avascular'?", "Glandular epithelium",
    ["Transitional epithelium", "Simple squamous epithelium", "Keratinized stratified squamous"], "Little or no blood supply, except glandular epithelium.", "L5, slides 10–17")
add(13, "Which describes epithelial tissue?", "Highly cellular, highly mitotic, avascular",
    ["Little cellularity, lots of matrix, very vascular", "Multinucleated, striated, voluntary", "Liquid matrix that transports gases"], "Connective tissue is almost the exact opposite.", "L5, slides 10–17")

# ---------- 14. Skin glands: ceruminous, eccrine, apocrine (L6, slides 44-49) ----------
add(14, "Cerumen is better known as:", "Earwax",
    ["Skin oil", "Sweat", "Mucus"], "Made by ceruminous glands, which are modified sweat glands.", "L6, slide 49")
add(14, "Where are ceruminous glands found?", "External ear canal",
    ["Axillae and groin", "Palms and soles", "Eyelids"], "They lubricate the ear canal and repel insects.", "L6, slide 49")
add(14, "Which glands produce protein-rich sweat, open into hair follicles, and are not active until puberty?", "Apocrine sweat glands",
    ["Eccrine sweat glands", "Ceruminous glands", "Sebaceous glands"], "Apocrine: large, in axillary and urogenital regions.", "L6, slide 48")
add(14, "Which sweat glands are found all over the body and open onto the skin surface as 'pores'?", "Eccrine",
    ["Apocrine", "Sebaceous", "Ceruminous"], "Eccrine sweat = water, salt, urea; temperature control.", "L6, slide 47")
add(14, "Sebum is produced by which glands?", "Sebaceous (oil) glands",
    ["Ceruminous glands", "Eccrine glands", "Apocrine glands"], "Sebum lubricates hair and skin; contains lysozymes.", "L6, slide 45")
add(14, "Sweat glands are found almost everywhere EXCEPT:", "Margins of the lips and nipples",
    ["Palms", "Forehead", "Soles of the feet"], "Also absent from parts of the external genitalia.", "L6, slide 46")
add(14, "Cutaneous glands live mostly in the:", "Dermis",
    ["Epidermis", "Hypodermis", "Stratum corneum"], "All cutaneous glands are exocrine glands, mostly in the dermis.", "L6, slide 44")
add(14, "Ceruminous glands are modified ___ glands.", "Sweat",
    ["Oil", "Endocrine", "Mammary"], "Modified sweat glands that make earwax.", "L6, slide 49")

# ---------- 15. Hormones and blood pressure (L15 + Hormones handout) ----------
add(15, "Which substance, released by the kidneys when blood pressure or sodium drops, starts the RAAS?", "Renin",
    ["Erythropoietin", "Insulin", "Calcitonin"], "Renin → angiotensinogen → renin-angiotensin-aldosterone system → ↑ BP. Hormones chart: target body vasculature, effect control BP.", "L15, slides 35–47; Hormones handout #17")
add(15, "Per the hormones chart, renin's target is the:", "Body vasculature",
    ["Red bone marrow", "Adrenal medulla", "Thyroid gland"], "Renin: source kidney, target body vasculature, effect control blood pressure.", "L15, Hormones handout #17")
add(15, "Renin is technically a(n):", "Enzyme",
    ["Steroid hormone", "Neurotransmitter", "Mineral salt"], "The slide notes renin is an enzyme, not technically a hormone. It acts on angiotensinogen.", "L15, slides 35–47")
add(15, "Which posterior pituitary hormone raises blood pressure by retaining water and maintaining blood volume?", "Antidiuretic hormone (ADH)",
    ["Oxytocin", "Prolactin", "Melatonin"], "ADH (vasopressin): target kidneys, retention of water (less urination). In high amounts it causes vasoconstriction.", "L15, slides 11–21; Hormones handout #8")
add(15, "Aldosterone raises blood volume and pressure by causing the kidneys to:", "Retain sodium (and water with it)",
    ["Excrete sodium", "Retain potassium", "Make more red blood cells"], "Aldosterone: Na+ retention, K+ secretion. 'Salt retention = retaining water too.'", "L15, slides 35–47; Hormones handout #14")
add(15, "ADH is also called:", "Vasopressin",
    ["Thymosin", "Epinephrine", "Erythropoietin"], "In high amounts it causes vasoconstriction (raises BP).", "L15, slides 11–21; Hormones handout #8")
add(15, "Which hormone pair from the adrenal medulla raises heart rate and blood pressure in fight or flight?", "Epinephrine and norepinephrine",
    ["Cortisol and aldosterone", "Insulin and glucagon", "Calcitonin and PTH"], "Catecholamines: ↑ HR, ↑ BP, ↑ blood glucose; chart adds vasoconstriction.", "L15, slides 35–47; Hormones handout #13")
add(15, "Which hormone does NOT help raise blood pressure?", "Melatonin",
    ["Renin", "ADH", "Aldosterone"], "Melatonin (pineal) controls the sleep/wake cycle.", "L15, slides 22–24; Hormones handout #21")
add(15, "Aldosterone release is regulated by:", "The renin-angiotensin-aldosterone system (RAAS)",
    ["ACTH from the anterior pituitary", "Blood glucose levels", "Light"], "Cortisol is the one regulated by ACTH.", "L15, slides 35–47")

# ---------- 16. Hormones: source, target, effect (Hormones handout) ----------
add(16, "Which gland releases melatonin?", "Pineal gland",
    ["Pituitary gland", "Thymus", "Thyroid gland"], "Melatonin: pineal → brain → circadian rhythm (sleep/wake).", "L15, Hormones handout #21")
add(16, "Erythropoietin (EPO) is made by the ___ and targets the ___.", "Kidney; red bone marrow",
    ["Liver; spleen", "Pancreas; blood", "Adrenal cortex; kidney"], "EPO increases red blood cell production when blood O2 is low.", "L15, Hormones handout #18")
add(16, "Thymosin's effect is:", "Maturation of T lymphocytes",
    ["Production of red blood cells", "Release of milk", "Increasing metabolism"], "Thymus → blood → T lymphocytes (WBCs of the immune system).", "L15, Hormones handout #22")
add(16, "Oxytocin is made by the hypothalamus, stored in the posterior pituitary, and targets the:", "Smooth muscle of the uterus",
    ["Ovary", "Kidneys", "Thyroid"], "Contractions to birth the baby (slides add milk release).", "L15, Hormones handout #9")
add(16, "Which hormone targets the mammary glands to PRODUCE milk?", "Prolactin",
    ["Oxytocin", "Estrogen", "Progesterone"], "Prolactin = produce milk (anterior pituitary). Oxytocin = release milk.", "L15, Hormones handout #3")
add(16, "Which hormone is made by the hypothalamus but stored in and released from the posterior pituitary?", "ADH (vasopressin)",
    ["Growth hormone", "TSH", "Prolactin"], "ADH and oxytocin are both made in the hypothalamus and stored in the posterior pituitary.", "L15, Hormones handout #8")
add(16, "Which hormone's target is listed as 'N/A' on the chart because it acts on every cell to stimulate metabolism?", "Thyroid hormone (T3/T4, thyroxine)",
    ["Calcitonin", "Insulin", "Growth hormone"], "Thyroid hormone: thyroid gland → every cell → stimulate metabolism.", "L15, Hormones handout #10")
add(16, "Which hormone causes ovulation?", "Luteinizing hormone (LH)",
    ["FSH", "Prolactin", "Progesterone"], "LH: anterior pituitary → ovary → ovulation.", "L15, Hormones handout #5")
add(16, "Which hormone targets melanocytes in the skin?", "Melanocyte-stimulating hormone (MSH)",
    ["ACTH", "Melatonin", "TSH"], "MSH: anterior pituitary → melanocytes → melanin, which protects against UV light.", "L15, Hormones handout #7")
add(16, "Testosterone is made by the:", "Testes",
    ["Adrenal medulla", "Ovaries", "Anterior pituitary"], "Testes → male body → sperm formation and male secondary sex characteristics.", "L15, Hormones handout #25")

# ---------- 30. Types of muscle (L13, slides 4-20) ----------
add(30, "Which muscle type is found ONLY in the heart?", "Cardiac",
    ["Skeletal", "Smooth", "Visceral"], "Cardiac muscle is in the heart only.", "L13, slides 12–15")
add(30, "Which muscle type is voluntary, striated and multinucleated?", "Skeletal",
    ["Cardiac", "Smooth", "Multi-unit smooth"], "Myoblasts fuse during development, so skeletal fibers have many nuclei.", "L13, slides 8–11")
add(30, "Which muscle type is fusiform, uninucleate and NOT striated?", "Smooth",
    ["Skeletal", "Cardiac", "None of these"], "Smooth muscle: wide middle, tapered ends; walls of hollow organs.", "L13, slides 16–20")
add(30, "Which muscle type CAN divide (is mitotic)?", "Smooth",
    ["Skeletal", "Cardiac", "All three"], "Skeletal and cardiac are amitotic; smooth muscle can divide.", "L13, slides 8–20")
add(30, "Intercalated discs are found only in ___ muscle.", "Cardiac",
    ["Skeletal", "Smooth", "Multi-unit"], "They join adjacent cardiac cells; contain desmosomes and gap junctions.", "L13, slides 12–15")
add(30, "Intercalated discs contain which two junctions?", "Desmosomes and gap junctions",
    ["Tight junctions and hemidesmosomes", "Synapses and T-tubules", "Tight junctions and gap junctions"], "Desmosomes resist stress; gap junctions pass ions between cells.", "L13, slides 12–15")
add(30, "Which muscle type is branched (Y-shaped)?", "Cardiac",
    ["Skeletal", "Smooth", "Visceral smooth"], "Short, thick, branched cells.", "L13, slides 12–15")
add(30, "Which muscle type is the most abundant (30–40% of body mass)?", "Skeletal",
    ["Smooth", "Cardiac", "They are equal"], "Attached to bones and crosses joints.", "L13, slides 8–11")
add(30, "Multi-unit smooth muscle is found in the:", "Iris of the eye and arrector pili",
    ["Stomach and uterus", "Heart", "Biceps brachii"], "Rare; no gap junctions. Visceral (single-unit) is the common type.", "L13, slides 16–20")
add(30, "Which characteristic sets muscle apart from ALL other tissues?", "Contractility",
    ["Excitability", "Elasticity", "Extensibility"], "The ability to forcibly shorten.", "L13, slides 4–7")
add(30, "The ability of muscle to recoil to its resting length is:", "Elasticity",
    ["Extensibility", "Excitability", "Contractility"], "Extensibility = can be stretched; elasticity = springs back.", "L13, slides 4–7")

# ---------- 31. Muscle fiber and the sarcomere (L13, slides 21-37) ----------
add(31, "The plasma membrane of a muscle fiber is the:", "Sarcolemma",
    ["Sarcoplasm", "Sarcomere", "Endomysium"], "Sarcoplasm = cytoplasm; sarcomere = contractile unit.", "L13, slides 21–24")
add(31, "Which structure stores calcium in a muscle fiber?", "Sarcoplasmic reticulum",
    ["T-tubules", "Mitochondria", "Myofibrils"], "Smooth ER of muscle; terminal cisternae are its calcium reservoirs.", "L13, slides 21–24")
add(31, "The structural and functional unit of skeletal muscle is the:", "Sarcomere",
    ["Myofibril", "Fascicle", "Osteon"], "Smallest part that can contract.", "L13, slides 30–37")
add(31, "The THIN myofilament is:", "Actin",
    ["Myosin", "Collagen", "Keratin"], "Thin = actin (with tropomyosin and troponin). Thick = myosin.", "L13, slides 25–29")
add(31, "Which protein covers the myosin-binding sites on actin at rest?", "Tropomyosin",
    ["Troponin", "Myosin", "Titin"], "Troponin binds calcium and pulls tropomyosin out of the way.", "L13, slides 25–29")
add(31, "Which regulatory protein has a binding site for calcium?", "Troponin",
    ["Tropomyosin", "Actin", "Acetylcholinesterase"], "Ca2+ binds troponin → tropomyosin moves → binding sites exposed.", "L13, slides 25–29")
add(31, "Which band does NOT change length during contraction?", "A band",
    ["I band", "H zone", "None; all bands shorten"], "The A band is the full length of the thick filament.", "L13, slides 30–37")
add(31, "Which two regions disappear at maximum contraction?", "I band and H zone",
    ["A band and M line", "Z disc and A band", "M line and Z disc"], "Thin filaments slide over them toward the center.", "L13, slides 30–37")
add(31, "The zig-zag ends of a sarcomere that anchor the thin filaments are the:", "Z discs",
    ["M lines", "H zones", "A bands"], "Sarcomere = Z disc to Z disc.", "L13, slides 30–37")
add(31, "Put these in order from smallest to largest:", "Myofilaments → myofibrils → muscle fibers",
    ["Myofibrils → myofilaments → muscle fibers", "Muscle fibers → myofibrils → myofilaments", "Myofilaments → muscle fibers → myofibrils"], "Actin and myosin make myofibrils, which fill a muscle fiber (cell).", "L13, slides 25–29")
add(31, "T (transverse) tubules are:", "Invaginations of the sarcolemma that carry impulses deep into the fiber",
    ["Calcium storage sacs", "Bundles of muscle fibers", "Thick filaments"], "They reach the SR so the signal can trigger calcium release.", "L13, slides 21–24")

# ---------- 32. CT wrappings, tendons, origin/insertion (L13, slides 8-11, 38-48) ----------
add(32, "Which connective tissue wraps a SINGLE muscle fiber?", "Endomysium",
    ["Perimysium", "Epimysium", "Fascia"], "Endo = within ('paper around a straw').", "L13, slides 38–48")
add(32, "Which connective tissue wraps a fascicle?", "Perimysium",
    ["Endomysium", "Epimysium", "Aponeurosis"], "Peri = around a bundle ('cardboard box of straws').", "L13, slides 38–48")
add(32, "Which connective tissue wraps the WHOLE muscle?", "Epimysium",
    ["Perimysium", "Endomysium", "Periosteum"], "Epi = on top of ('shipping box of boxes').", "L13, slides 38–48")
add(32, "A fascicle is a:", "Bundle of muscle fibers",
    ["Single muscle cell", "Sheet of connective tissue", "Unit of the sarcomere"], "Wrapped by perimysium.", "L13, slides 38–48")
add(32, "A thick cord of dense regular CT connecting muscle to bone is a:", "Tendon",
    ["Ligament", "Aponeurosis", "Fascia"], "Ligaments connect bone to bone.", "L13, slides 38–48")
add(32, "A thin, broad, flat sheet connecting muscle to muscle or muscle to bone is an:", "Aponeurosis",
    ["Tendon", "Endomysium", "Intercalated disc"], "Dense regular CT, flat like a sheet.", "L13, slides 38–48")
add(32, "Which structure lies external to the epimysium and separates individual muscles?", "Fascia",
    ["Perimysium", "Endomysium", "Sarcolemma"], "Also binds muscles of similar function together.", "L13, slides 38–48")
add(32, "The end of a muscle that MOVES when it contracts is the:", "Insertion",
    ["Origin", "Belly", "Fascicle"], "Contraction pulls the insertion toward the origin. The origin stays put (usually proximal).", "L13, slides 8–11")
add(32, "The origin of a muscle is typically on the:", "Proximal or medial bone, which does not move",
    ["Distal bone, which moves", "Skin", "Tendon sheath"], "Insertion = distal bone that moves.", "L13, slides 8–11")

# ---------- 33. NMJ and contraction (L14, slides 26-40) ----------
add(33, "Which neurotransmitter is released at the neuromuscular junction?", "Acetylcholine (ACh)",
    ["Epinephrine", "Dopamine", "Acetylcholinesterase"], "Stored in synaptic vesicles in the synaptic knob.", "L14, slides 26–29")
add(33, "Which enzyme in the synaptic cleft breaks down acetylcholine?", "Acetylcholinesterase (AChE)",
    ["ATP synthase", "Renin", "Lysozyme"], "Clearing ACh lets the muscle relax.", "L14, slides 26–29")
add(33, "The junctional folds of the motor end plate:", "Increase surface area for ACh receptors",
    ["Store calcium", "Release ACh", "Break down ATP"], "Specialized sarcolemma with chemically gated ACh receptors.", "L14, slides 26–29")
add(33, "During excitation, calcium is released into the cytosol from the:", "Terminal cisternae of the sarcoplasmic reticulum",
    ["Synaptic vesicles", "Mitochondria", "Z discs"], "Triggered by the action potential traveling down the T-tubules.", "L14, slides 30–40")
add(33, "What happens when Ca2+ binds troponin?", "Tropomyosin is pulled away, exposing myosin-binding sites on actin",
    ["Myosin releases actin", "ACh is broken down", "The muscle relaxes"], "Then cross-bridges can form.", "L14, slides 30–40")
add(33, "In cross-bridge cycling, what does ATP binding to myosin do?", "Makes myosin release actin",
    ["Starts the power stroke", "Releases calcium", "Opens ACh receptors"], "Then ATP splits to ADP + P to re-cock the head.", "L14, slides 30–40")
add(33, "During the power stroke, myosin pulls actin:", "Toward the center of the sarcomere",
    ["Away from the center of the sarcomere", "Toward the sarcolemma", "Into the T-tubules"], "That shortens the sarcomere (sliding filament theory).", "L14, slides 30–40")
add(33, "Rigor mortis happens because:", "No ATP is left to release the myosin–actin cross-bridges",
    ["Too much ACh is released", "Calcium is pumped back into the SR", "Tropomyosin covers all binding sites"], "Muscles stay contracted until proteins break down.", "L14, slides 30–40, 67–70")
add(33, "Depolarization of the sarcolemma happens when:", "Na+ rushes into the muscle fiber",
    ["K+ rushes into the fiber", "Ca2+ leaves the cytosol", "ACh is broken down"], "More Na+ enters than K+ leaves, opening voltage-gated Na+ channels.", "L14, slides 30–40")

# ---------- 34. Motor units, twitch, tetanus, contraction types (L14, slides 21-25, 54-66) ----------
add(34, "A motor unit is:", "One motor neuron and all the muscle fibers it stimulates",
    ["One muscle fiber and all its nerves", "A single sarcomere", "All the muscles that cross a joint"], "Small motor units = fine control.", "L14, slides 21–25")
add(34, "Which muscles have very small motor units (few fibers per neuron) for fine control?", "Extrinsic eye muscles",
    ["Thigh muscles", "Gluteus maximus", "Back muscles"], "Many fibers per neuron (thigh) = less precise control.", "L14, slides 21–25")
add(34, "The all-or-nothing principle applies to:", "A single muscle fiber",
    ["A whole muscle", "Smooth muscle only", "Muscle tone"], "A whole muscle has a graded response.", "L14, slides 21–25, 54–66")
add(34, "Activating more and more motor units to increase force is called:", "Recruitment",
    ["Summation", "Tetanus", "Atrophy"], "Number of fibers stimulated → recruitment; frequency → summation.", "L14, slides 21–25, 54–66")
add(34, "What are the three stages of a muscle twitch, in order?", "Latent, contraction, relaxation",
    ["Contraction, latent, relaxation", "Excitation, relaxation, refractory", "Latent, relaxation, contraction"], "Latent = stimulus to onset of tension, no length change.", "L14, slides 54–66")
add(34, "Stimuli so rapid that the muscle cannot relax at all produce:", "Fused (complete) tetanus",
    ["Unfused tetanus", "A single twitch", "Muscle tone"], "Summation → unfused tetanus → fused tetanus.", "L14, slides 54–66")
add(34, "In an isometric contraction:", "The muscle contracts but its length does not change",
    ["The muscle shortens", "The muscle lengthens", "The muscle doesn't produce tension"], "e.g. pushing against a wall.", "L14, slides 54–66")
add(34, "A muscle that LENGTHENS while contracting is doing a(n) ___ contraction.", "Eccentric",
    ["Concentric", "Isometric", "Tetanic"], "Concentric = shortens; eccentric = lengthens (both isotonic).", "L14, slides 54–66")
add(34, "Resting tension in skeletal muscle that keeps it 'primed' is:", "Muscle tone",
    ["Rigor mortis", "Fused tetanus", "The latent period"], "Involuntary stimulation of a few motor units at a time.", "L14, slides 54–66")
add(34, "A subthreshold stimulus causes:", "No contraction",
    ["A full contraction", "A stronger-than-normal contraction", "Tetanus"], "Threshold = minimum needed; suprathreshold = contracts, nothing extra.", "L14, slides 21–25")

# ---------- 35. Energy, fiber types, nervous system (L14, slides 3-20, 41-53, 67-70) ----------
add(35, "What is the ONLY energy source a muscle uses directly for contraction?", "ATP",
    ["Glucose", "Creatine phosphate", "Lactic acid"], "The other pathways just regenerate ATP.", "L14, slides 41–49")
add(35, "Which ATP pathway is the FASTEST but lasts only about 10–15 seconds?", "Direct phosphorylation by creatine phosphate",
    ["Aerobic respiration", "Anaerobic glycolysis", "Gluconeogenesis"], "CP hands its phosphate to ADP: 1 ATP per CP.", "L14, slides 41–49")
add(35, "Which pathway makes about 95% of the ATP for muscle activity and requires oxygen?", "Aerobic respiration",
    ["Anaerobic glycolysis", "Creatine phosphate", "Lactic acid fermentation"], "~32 ATP per glucose in the mitochondria; byproducts CO2 + H2O.", "L14, slides 41–49")
add(35, "Anaerobic glycolysis yields ___ ATP per glucose and produces ___.", "2; lactic acid",
    ["32; CO2 and water", "1; creatine", "36; pyruvic acid only"], "Rapid but inefficient; lactic acid contributes to fatigue.", "L14, slides 41–49")
add(35, "Which fiber type is dark red, fatigue-resistant, and used for posture and endurance?", "Slow oxidative (Type I)",
    ["Fast glycolytic (Type IIb)", "Fast oxidative (Type IIa)", "Multi-unit smooth"], "Lots of myoglobin, mitochondria and blood supply.", "L14, slides 50–53")
add(35, "Which fiber type is white, fatigues quickly, and is used for sprinting and lifting?", "Fast glycolytic (Type IIb)",
    ["Slow oxidative (Type I)", "Fast oxidative (Type IIa)", "Cardiac"], "Anaerobic; few mitochondria and sparse blood supply.", "L14, slides 50–53")
add(35, "Sensory (afferent) neurons carry information:", "From receptors to the CNS",
    ["From the CNS to muscles", "Only within the brain", "From muscles to glands"], "Motor (efferent) = CNS to effectors.", "L14, slides 3–12")
add(35, "Which division of the nervous system controls skeletal muscle voluntarily?", "Somatic motor",
    ["Autonomic motor", "Visceral sensory", "Parasympathetic"], "Autonomic controls smooth muscle, cardiac muscle and glands.", "L14, slides 3–12")
add(35, "All motor neurons are which structural type?", "Multipolar",
    ["Bipolar", "Unipolar", "Anaxonic"], "One axon, many dendrites; the most common type.", "L14, slides 13–20")
add(35, "An increase in muscle size with increased function is:", "Hypertrophy",
    ["Atrophy", "Rigor mortis", "Tetanus"], "Resistance exercise adds actin and myosin.", "L14, slides 67–70")

# ---------- 36. Endocrine basics (L15, slides 3-10) ----------
add(36, "Endocrine glands differ from exocrine glands because they:", "Lack ducts and release hormones into the blood",
    ["Have ducts that open onto the skin", "Make digestive enzymes", "Are made of muscle tissue"], "Hormones go into interstitial fluid, then the blood.", "L15, slides 3–10")
add(36, "Steroid hormones are made from:", "Cholesterol",
    ["Amino acids", "Glucose", "Nucleotides"], "Small, nonpolar, lipid-soluble; diffuse into the cell for direct gene activation.", "L15, slides 3–10")
add(36, "MOST hormones are which type?", "Protein hormones",
    ["Steroid hormones", "Biogenic amines", "Lipid hormones"], "Water-soluble; can't cross the membrane, so they use a second messenger.", "L15, slides 3–10")
add(36, "How do protein hormones affect a target cell?", "Second-messenger system (signal transduction)",
    ["Direct gene activation inside the nucleus", "Diffusing through the membrane", "Traveling along nerves"], "First messenger binds outside → second messenger inside.", "L15, slides 3–10")
add(36, "A gland stimulated by changing levels of ions or nutrients in the blood is responding to a ___ stimulus.", "Humoral",
    ["Neural", "Hormonal", "Mechanical"], "e.g. parathyroids respond to blood calcium.", "L15, slides 3–10")
add(36, "The specific organ, tissue or cell a hormone affects is its:", "Target tissue",
    ["Source", "Receptor gland", "Effector duct"], "Know each hormone's source, target and effect.", "L15, slides 3–10")
add(36, "Which of these is a STEROID hormone?", "Testosterone",
    ["Insulin", "Epinephrine", "Growth hormone"], "Steroids: estrogen, progesterone, testosterone, corticosteroids.", "L15, slides 3–10")
add(36, "Epinephrine is classified as a:", "Biogenic amine (catecholamine)",
    ["Steroid hormone", "Protein hormone", "Enzyme"], "Biogenic amines: catecholamines, thyroid hormone, melatonin.", "L15, slides 3–10")

# ---------- 37. Pituitary, pineal, thymus (L15, slides 11-24, 32-34) ----------
add(37, "Which gland is called the 'master gland'?", "Pituitary (hypophysis)",
    ["Thyroid", "Pineal", "Adrenal"], "Pea-sized, under the hypothalamus, protected by the sella turcica.", "L15, slides 11–21")
add(37, "The pituitary gland sits in which bony structure?", "Sella turcica of the sphenoid",
    ["Foramen magnum", "Crista galli", "Mastoid process"], "Ties back to the skull lecture.", "L15, slides 11–21")
add(37, "The posterior pituitary stores and releases which two hormones?", "ADH and oxytocin",
    ["GH and prolactin", "TSH and ACTH", "FSH and LH"], "Both are made by the hypothalamus.", "L15, slides 11–21")
add(37, "Too much growth hormone in an ADULT causes:", "Acromegaly",
    ["Gigantism", "Pituitary dwarfism", "Cretinism"], "In childhood it causes gigantism.", "L15, slides 11–21")
add(37, "TSH targets the ___ and ACTH targets the ___.", "Thyroid; adrenal cortex",
    ["Adrenal cortex; thyroid", "Kidney; liver", "Ovary; testes"], "ACTH → adrenal cortex → release of glucocorticoids.", "L15, slides 11–21; Hormones handout #2, #6")
add(37, "FSH and LH are called:", "Gonadotropins",
    ["Catecholamines", "Mineralocorticoids", "Glucocorticoids"], "They target the gonads (testes/ovaries).", "L15, slides 11–21")
add(37, "FSH's effect is:", "Production of sperm and egg",
    ["Ovulation", "Milk release", "Uterine contraction"], "FSH: anterior pituitary → testes/ovaries. LH causes ovulation.", "L15, Hormones handout #4")
add(37, "The thymus releases thymosin, which matures:", "T lymphocytes",
    ["Red blood cells", "Osteoblasts", "Melanocytes"], "The thymus shrinks to fat after puberty.", "L15, slides 32–34")
add(37, "The pineal gland is stimulated by ___ and releases ___.", "Light; melatonin",
    ["Blood calcium; calcitonin", "Blood glucose; insulin", "Stress; cortisol"], "Melatonin regulates the circadian (sleep/wake) rhythm.", "L15, slides 22–24")

# ---------- 38. Thyroid and parathyroid (L15, slides 25-31) ----------
add(38, "Which is the body's major metabolic hormone?", "Thyroid hormone (T3/T4)",
    ["Calcitonin", "Insulin", "Prolactin"], "Targets every cell; increases metabolism and heat production.", "L15, slides 25–31; Hormones handout #10")
add(38, "Calcitonin ___ blood calcium by stimulating osteoblasts and inhibiting osteoclasts.", "Lowers",
    ["Raises", "Doesn't change", "Doubles"], "Calcitonin takes Ca2+ from blood and deposits it into bone.", "L15, slides 25–31; Hormones handout #11")
add(38, "Parathyroid hormone (PTH) ___ blood calcium.", "Raises",
    ["Lowers", "Doesn't affect", "Stores"], "PTH takes Ca2+ from bone into blood: stimulates osteoclasts, inhibits osteoblasts.", "L15, slides 25–31; Hormones handout #12")
add(38, "How many parathyroid glands are there, and where?", "4, on the posterior thyroid",
    ["2, on top of the kidneys", "1, in the brain", "4, in the pancreas"], "Small nodules humorally stimulated by blood calcium.", "L15, slides 25–31")
add(38, "Graves' disease is an example of:", "Hyperthyroidism",
    ["Hypothyroidism", "Diabetes insipidus", "Addison's disease"], "Hypothyroidism: goiter, cretinism (child), myxedema (adult).", "L15, slides 25–31")
add(38, "Hypothyroidism in childhood is called ___; in adults it's called ___.", "Cretinism; myxedema",
    ["Gigantism; acromegaly", "Graves' disease; goiter", "Addison's; Cushing's"], "Both are low thyroid hormone.", "L15, slides 25–31")
add(38, "Thyroid follicles are made of which epithelium?", "Simple cuboidal",
    ["Transitional", "Simple squamous", "Stratified columnar"], "Ties back to tissues: simple cuboidal = secretion.", "L15, slides 25–31")
add(38, "Calcitonin and PTH are ___ to each other.", "Antagonists",
    ["Identical", "Both made by the parathyroids", "Both steroid hormones"], "One lowers blood calcium, the other raises it.", "L15, slides 25–31")

# ---------- 39. Pancreas, kidneys, gonads (L15, slides 35-58) ----------
add(39, "Insulin is made by ___ cells and ___ blood sugar.", "Beta; decreases",
    ["Alpha; increases", "Beta; increases", "Alpha; decreases"], "Insulin moves sugar from the blood into tissue.", "L15, slides 48–52; Hormones handout #19")
add(39, "Glucagon is made by ___ cells and ___ blood sugar.", "Alpha; increases",
    ["Beta; decreases", "Alpha; decreases", "Beta; increases"], "Glucagon moves stored glucose from tissue into the blood.", "L15, slides 48–52; Hormones handout #20")
add(39, "The endocrine cell clusters of the pancreas are the:", "Islets of Langerhans",
    ["Haversian systems", "Dermal papillae", "Zona glomerulosa"], "Made of alpha and beta cells; respond to blood glucose.", "L15, slides 48–52")
add(39, "Type 1 diabetes vs. Type 2 diabetes:", "Type 1 makes no insulin; Type 2 makes insulin but receptors don't respond",
    ["Type 1 makes too much insulin; Type 2 makes none", "Both make no insulin", "Type 1 is a thyroid disorder"], "Diabetes insipidus is different: an ADH problem.", "L15, slides 48–52")
add(39, "Most of the pancreas's function is:", "Exocrine (digestive enzymes)",
    ["Endocrine (hormones)", "Making red blood cells", "Storing bile"], "Only a small part (the islets) is endocrine.", "L15, slides 48–52")
add(39, "Erythropoietin is released when kidney receptors detect:", "Low blood oxygen",
    ["High blood sugar", "Low blood calcium", "High blood pressure"], "e.g. bleeding, high altitude, aerobic exercise, COPD.", "L15, slides 35–47")
add(39, "Which hormone maintains pregnancy by keeping the uterine lining from shedding?", "Progesterone",
    ["Estrogen", "Oxytocin", "Testosterone"], "Ovary → uterus.", "L15, slides 53–58; Hormones handout #24")
add(39, "Estrogen is made by the ___ and stimulates ___.", "Ovary; uterine lining growth and secondary sex characteristics",
    ["Anterior pituitary; ovulation", "Adrenal medulla; fight or flight", "Ovary; milk release"], "Hormones chart #23.", "L15, slides 53–58; Hormones handout #23")

# ---------- 40. Adrenal glands (L15, slides 35-47) ----------
add(40, "The adrenal medulla releases:", "Epinephrine and norepinephrine",
    ["Cortisol and aldosterone", "Insulin and glucagon", "ADH and oxytocin"], "Catecholamines for fight or flight; stimulated by the sympathetic nervous system.", "L15, slides 35–47")
add(40, "Order the zones of the adrenal cortex from OUTER to INNER:", "Glomerulosa, fasciculata, reticularis",
    ["Reticularis, fasciculata, glomerulosa", "Fasciculata, glomerulosa, reticularis", "Medulla, glomerulosa, reticularis"], "'GFR' from outside in. Salt, sugar, sex.", "L15, slides 35–47")
add(40, "Aldosterone (a mineralocorticoid) comes from which zone?", "Zona glomerulosa",
    ["Zona fasciculata", "Zona reticularis", "Adrenal medulla"], "Outermost zone; targets the kidney.", "L15, slides 35–47")
add(40, "Cortisol (a glucocorticoid) comes from the ___ and is regulated by ___.", "Zona fasciculata; ACTH",
    ["Zona glomerulosa; RAAS", "Adrenal medulla; sympathetic nerves", "Zona reticularis; TSH"], "Cortisol raises blood glucose to resist stress.", "L15, slides 35–47")
add(40, "Cortisol's main effect is to:", "Increase blood glucose to resist stress",
    ["Lower blood glucose", "Retain sodium", "Mature T lymphocytes"], "Also raises fatty acids and amino acids in the blood.", "L15, slides 35–47; Hormones handout #15")
add(40, "Hyposecretion of adrenal cortex hormones causes:", "Addison's disease",
    ["Cushing's disease", "Graves' disease", "Acromegaly"], "Cushing's = HYPERsecretion of glucocorticoids.", "L15, slides 35–47")
add(40, "Cushing's disease is caused by:", "Too much glucocorticoid (cortisol)",
    ["Too little cortisol", "Too much thyroid hormone", "Too little insulin"], "Addison's is the opposite (too little).", "L15, slides 35–47")
add(40, "The adrenal glands are also called the ___ glands.", "Suprarenal",
    ["Parathyroid", "Pineal", "Retroperitoneal"], "Pyramid-shaped, on top of each kidney.", "L15, slides 35–47")
add(40, "Androgens (gonadocorticoids) come from the zona reticularis and, per the chart, also mainly from the:", "Gonads (testes or ovaries)",
    ["Thymus", "Pancreas", "Kidneys"], "Adrenal cortex is a minor contributor; gonads are the major source.", "L15, slides 35–47; Hormones handout #16")

# ---------- 41-50. Diagram section ----------
# Every question carries "dg" (which diagram). The app picks 2 diagrams per practice exam
# and asks 5 questions from each.
dq = {
    "pelvis": quiz4.diagram_qs(quiz4.PELVIS, quiz4.PELVIS_GROUPS, "img/pelvis.jpg", "Pelvis handout"),
    "scapula": quiz4.diagram_qs(quiz4.SCAPULA, quiz4.SCAPULA_GROUPS, "img/scapula.jpg", "Scapula handout (posterior left, anterior right)"),
    "humerus": [], "leg": [],
}
for q in quiz4.QUIZ["questions"]:
    if q.get("img") == "img/humerus.jpg":
        dq["humerus"].append((q["q"], q["a"], q["w"], q["e"], q["s"], q["img"]))
    elif q.get("img") == "img/leg.jpg":
        dq["leg"].append((q["q"], q["a"], q["w"], q["e"], q["s"], q["img"]))
for g, qs in dq.items():
    for i, (q, a, w, e, s, img) in enumerate(qs):
        add(DG_TOPICS[i % len(DG_TOPICS)], q, a, list(w), e, s)
        B.Q[-1]["img"] = img
        B.Q[-1]["dg"] = g

QUIZ = {"id": "mid", "title": "A&P Midterm", "lectures": "Lectures 1–15",
        "note": "50 questions like the real midterm: 40 written questions, then 10 diagram questions on 2 of these 4 diagrams: pelvis (os coxae), scapula, tibia/fibula, humerus. Each practice exam picks a new pair.",
        "units": {"L1": "Intro to A&P", "L2": "Atoms & Molecules", "L3": "Biochemistry & Cells", "L4": "Cells",
                  "L5": "Tissues", "L6": "Skin & Body Membranes", "L7": "Skeletal System", "L8": "Skull",
                  "L9": "Spine", "L10": "Upper Extremity", "L11": "Lower Extremity", "L12": "Joints",
                  "L13": "Muscle Tissue", "L14": "Muscle Physiology & Nervous System", "L15": "Endocrine System"},
        "topics": TOPICS, "dgTopics": DG_TOPICS, "dgNames": DG_NAMES, "questions": B.Q}
