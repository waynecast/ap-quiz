# A&P Quiz #2 question bank (Lectures 4-6: Cells, Tissues, Skin & Body Membranes). Built by build.py.
# Format per question: topic, q (prompt), a (correct answer), w (wrong answers), e (explanation), s (source)
# Sources cite slide POSITION in the deck (speaker notes count). L4 = Cells, L5 = Tissues, L6 = Skin & Body Membranes.

TOPICS = {
    1: "Stages of the cell cycle",
    2: "Cell junctions",
    3: "Body membranes",
    4: "Simple squamous, cuboidal, columnar, transitional",
    5: "DNA / RNA base pairing",
    6: "Organelles: Golgi, peroxisome, ribosome",
    7: "Skin layers: top vs. bottom",
    8: "Mesenchyme",
    9: "Epithelium vs. connective tissue",
    10: "Epidermis layers (Come Let's Get Sun Burned)",
    11: "Sudoriferous, ceruminous, sebaceous glands",
    12: "Thick skin's extra layer",
    13: "Corpuscles and receptors",
    14: "Transitional epithelium",
    15: "Biggest vs. smallest layers",
    16: "Layers of the dermis and epidermis",
    17: "Phases of mitosis",
    18: "Lysosomes, ribosomes, Golgi, peroxisomes",
    19: "Collagen, elastic, reticular fibers",
    20: "Living vs. dead skin layers",
    21: "What happens in G1, S, G2, M",
    22: "The germinating layer",
    23: "Fingerprints",
    24: "Goblet cells",
    25: "Cytosol, nucleus, ribosomes, ER",
}

from banks.common import Bank
B = Bank()
add = B.add

# ---------- 1. Stages of the cell cycle ----------
add(1, "The cell cycle has two main stages. They are:", "Interphase and mitosis",
    ["Prophase and telophase", "G1 and G2", "Transcription and translation"], "Two stages: interphase, then mitosis (M phase).", "L4, slide 53")
add(1, "Which is the correct order of the cell cycle?", "G1 → S → G2 → Mitosis",
    ["S → G1 → G2 → Mitosis", "G1 → G2 → S → Mitosis", "Mitosis → G2 → S → G1"], "Interphase (G1, S, G2) comes first, then mitosis.", "L4, slides 53–54")
add(1, "Interphase is made up of which three sub-phases?", "G1, S, G2",
    ["Prophase, metaphase, anaphase", "G1, G2, M", "S, M, cytokinesis"], "Interphase = G1, S, G2. Mitosis = PMAT.", "L4, slide 53")
add(1, "G1, S and G2 are all sub-phases of:", "Interphase",
    ["Mitosis", "Prophase", "Cytokinesis"], "Interphase has 3 sub-phases: G1, S, G2.", "L4, slide 53")
add(1, "Which part of the cell cycle is the longest?", "Interphase",
    ["Mitosis", "Anaphase", "Metaphase"], "Interphase is the longest part; G1 is its first and longest phase.", "L4, slides 53, 55")
add(1, "Is interphase a 'resting' phase?", "No — the cell is growing, working and preparing to divide",
    ["Yes — the cell does nothing", "Yes — the cell is dividing", "No — the nucleus is dissolving"], "Marieb says 'metabolic phase' would be a better name.", "L4, slide 53 (notes)")
add(1, "Mitosis has how many sub-phases?", "4",
    ["3", "2", "5"], "Prophase, metaphase, anaphase, telophase (PMAT).", "L4, slides 53, 58")
add(1, "What does 'G' stand for in G1 and G2?", "Gap (or growth)",
    ["Genetic", "Golgi", "Germinating"], "G1 = Gap/Growth phase 1; G2 = Gap/Growth phase 2.", "L4, slides 55, 57")
add(1, "The cell cycle is defined as:", "The changes a cell goes through from when it forms until it divides",
    ["The copying of DNA only", "The making of proteins from mRNA", "Programmed cell death"], "Series of changes from formation to division.", "L4, slide 53")

# ---------- 2. Cell junctions ----------
add(2, "Which junction creates a leak-proof seal so nothing passes BETWEEN cells?", "Tight junction",
    ["Gap junction", "Desmosome", "Hemidesmosome"], "Tight junctions fuse membranes like a zipper: an impermeable 'diffusion barrier'.", "L5, slide 14")
add(2, "Which junction lets neighboring cells COMMUNICATE by sharing ions and signals?", "Gap junction",
    ["Tight junction", "Desmosome", "Hemidesmosome"], "Gap junctions = hollow connexon channels between two cells.", "L5, slide 15")
add(2, "Which junction acts like 'spot welds' to resist mechanical stress?", "Desmosome",
    ["Gap junction", "Tight junction", "Connexon"], "Desmosomes = calcium-dependent interlocking proteins; 'spot welds'.", "L5, slide 16")
add(2, "Which junction anchors the BASAL surface of an epithelial cell to the basement membrane?", "Hemidesmosome",
    ["Desmosome", "Tight junction", "Gap junction"], "Hemidesmosome = 'half' desmosome, connects cell to the CT below.", "L5, slide 16")
add(2, "The hollow protein channel that forms a gap junction is called a:", "Connexon",
    ["Cristae", "Centriole", "Microvillus"], "Gap junction = hollow tube protein (connexon).", "L5, slide 15")
add(2, "Gap junctions are especially important in the heart because they:", "Let the electrical signal spread so the muscle contracts as a unit",
    ["Seal the heart against leaks", "Anchor the heart to the sternum", "Produce serous fluid"], "Communication junction: heart, neurons, smooth muscle.", "L5, slide 15")
add(2, "Tight junctions in the blood-brain barrier and digestive tract act as a:", "Diffusion barrier",
    ["Communication channel", "Spot weld", "Lubricant"], "Tight = impermeable seal.", "L5, slide 14")
add(2, "Where are tight junctions located on a cell?", "Apical and lateral",
    ["Basal only", "Inside the nucleus", "Only on the basement membrane"], "Tight = apical & lateral; desmosome = lateral; hemidesmosome = basal.", "L5, slide 13")
add(2, "In the skin, hemidesmosomes hold the:", "Epidermis to the dermis",
    ["Dermis to the hypodermis", "Hair to the follicle", "Nail to the lunula"], "Hemidesmosome: between epidermis and dermis.", "L5, slide 16")
add(2, "Desmosomes are abundant in which two places?", "Heart and epidermis",
    ["Brain and bladder", "Blood and lymph", "Cartilage and bone"], "Places under high mechanical stress.", "L5, slide 16")

# ---------- 3. Body membranes ----------
add(3, "Which is the ONLY dry membrane in the body?", "Cutaneous membrane",
    ["Serous membrane", "Mucous membrane", "Synovial membrane"], "Cutaneous membrane = the skin.", "L6, slide 5")
add(3, "Which membrane lines body cavities CLOSED to the exterior?", "Serous membrane",
    ["Mucous membrane", "Cutaneous membrane", "Synovial membrane"], "Serous = sealed (closed) cavities.", "L6, slide 6")
add(3, "Which membrane lines body cavities OPEN to the exterior?", "Mucous membrane",
    ["Serous membrane", "Synovial membrane", "Cutaneous membrane"], "Mucosa: respiratory, digestive, urogenital tracts.", "L6, slide 8")
add(3, "Which membrane lines joint cavities, bursae and tendon sheaths?", "Synovial membrane",
    ["Serous membrane", "Mucous membrane", "Cutaneous membrane"], "Synovial membrane makes synovial fluid.", "L6, slide 10")
add(3, "Which membrane has NO epithelial tissue?", "Synovial membrane",
    ["Serous membrane", "Mucous membrane", "Cutaneous membrane"], "Synovial = loose areolar CT only; the connective tissue membrane.", "L6, slides 4, 10")
add(3, "Serous membranes are made of:", "Simple squamous epithelium on areolar CT",
    ["Stratified squamous epithelium on dense CT", "Areolar CT with no epithelium", "Transitional epithelium on cartilage"], "Serosa: simple squamous on top of areolar CT.", "L6, slide 6")
add(3, "The layer of a serous membrane that touches the organ is the:", "Visceral layer",
    ["Parietal layer", "Lamina propria", "Papillary layer"], "Visceral = viscera (organ); parietal = body wall.", "L6, slide 6")
add(3, "The pleura, pericardium and peritoneum are all:", "Serous membranes",
    ["Mucous membranes", "Synovial membranes", "Cutaneous membranes"], "Pleura (lungs), pericardium (heart), peritoneum (abdomen).", "L6, slide 7")
add(3, "The loose CT layer under a mucous membrane is called the:", "Lamina propria",
    ["Parietal layer", "Hypodermis", "Basement membrane"], "Mucosa = epithelium on loose CT (lamina propria).", "L6, slide 8")
add(3, "The cutaneous membrane is composed of:", "Epidermis (stratified squamous) and dermis (dense CT)",
    ["Simple squamous epithelium and areolar CT", "Areolar CT only", "Pseudostratified epithelium and cartilage"], "Skin = epidermis + dermis.", "L6, slide 5")

# ---------- 4. Simple squamous, cuboidal, columnar, transitional ----------
add(4, "Which epithelium is found in the alveoli (air sacs) of the lungs and capillaries?", "Simple squamous",
    ["Simple cuboidal", "Simple columnar", "Transitional"], "One thin, flat layer: rapid diffusion and filtration.", "L5, slide 21")
add(4, "Which epithelium lines the kidney tubules and covers the ovaries?", "Simple cuboidal",
    ["Simple squamous", "Simple columnar", "Transitional"], "One layer of cube cells: secretion and absorption.", "L5, slide 24")
add(4, "Which epithelium lines the digestive tract from the stomach to the rectum?", "Simple columnar",
    ["Simple cuboidal", "Simple squamous", "Transitional"], "Tall cells with goblet cells: secretion and absorption.", "L5, slide 27")
add(4, "Which epithelium lines the urinary bladder?", "Transitional",
    ["Simple columnar", "Simple cuboidal", "Simple squamous"], "Transitional stretches to hold urine.", "L5, slide 43")
add(4, "The main function of simple squamous epithelium is:", "Rapid diffusion and filtration",
    ["Protection from abrasion", "Stretching to hold fluid", "Producing mucus"], "Thin = fast diffusion.", "L5, slide 21")
add(4, "Simple cuboidal epithelium looks like:", "One layer of cube-shaped cells",
    ["One layer of thin, flat cells", "One layer of tall cells", "Many layers that change shape"], "Cuboidal = cube shaped; 'simple' = 1 layer.", "L5, slide 24")
add(4, "Which epithelium is associated with goblet cells and may have cilia, lining the uterus and fallopian tubes?", "Simple columnar",
    ["Simple squamous", "Simple cuboidal", "Transitional"], "Simple columnar: goblet cells, cilia specialization.", "L5, slide 27")
add(4, "In an epithelium's name, 'simple' means:", "One layer of cells",
    ["Two or more layers", "Flat cells", "No nucleus"], "First name = number of layers; last name = cell shape.", "L5, slides 19–20")
add(4, "'Squamous' describes cells that are:", "Thin and flat",
    ["Cube shaped", "Column shaped", "Dome shaped"], "Squamous = flat like fish scales.", "L5, slide 20")
add(4, "Which epithelium lines the ducts of some glands and functions in secretion and absorption?", "Simple cuboidal",
    ["Transitional", "Simple squamous", "Keratinized stratified squamous"], "Simple cuboidal: kidney tubules, ovaries, gland ducts.", "L5, slide 24")

# ---------- 5. DNA / RNA base pairing (app also generates sequence questions) ----------
add(5, "In DNA, adenine (A) pairs with:", "Thymine (T)",
    ["Uracil (U)", "Guanine (G)", "Cytosine (C)"], "DNA: A–T and G–C.", "L4, slides 33, 39")
add(5, "In RNA, adenine (A) pairs with:", "Uracil (U)",
    ["Thymine (T)", "Guanine (G)", "Cytosine (C)"], "RNA has no thymine; uracil replaces it.", "L4, slides 36, 39")
add(5, "Guanine (G) always pairs with:", "Cytosine (C)",
    ["Adenine (A)", "Thymine (T)", "Uracil (U)"], "G–C in both DNA and RNA.", "L4, slide 39")
add(5, "Which base is found in DNA but NOT in RNA?", "Thymine",
    ["Uracil", "Adenine", "Guanine"], "DNA: A, T, G, C. RNA: A, U, G, C.", "L4, slide 38")
add(5, "Which base is found in RNA but NOT in DNA?", "Uracil",
    ["Thymine", "Cytosine", "Adenine"], "Uracil replaces thymine in RNA.", "L4, slide 38")
add(5, "Complementary bases are held together by:", "Hydrogen bonds",
    ["Peptide bonds", "Ionic bonds", "Covalent bonds"], "Weak hydrogen bonds, easily broken for replication.", "L4, slide 33")
add(5, "A nucleotide is made of:", "Phosphate, sugar, nitrogenous base",
    ["Amino acid, sugar, fat", "Glycerol and fatty acids", "Phosphate, protein, lipid"], "Three parts: phosphate, sugar, base.", "L4, slide 31")
add(5, "The 'rungs' of the DNA ladder are made of:", "Paired bases",
    ["Sugar-phosphate", "Amino acids", "Phospholipids"], "Backbone = sugar-phosphate; rungs = bases.", "L4, slide 33")
add(5, "A memory trick for DNA pairing is that the straight letters pair and the curved letters pair. This means:", "A–T and G–C",
    ["A–G and T–C", "A–C and G–T", "A–U and T–G"], "Straight A & T; curved G & C.", "L4, slide 33 (notes)")

# ---------- 6. Organelles: Golgi, peroxisome, ribosome ----------
add(6, "Which organelle packages and ships proteins, hormones, enzymes and lysosomes?", "Golgi body",
    ["Ribosome", "Peroxisome", "Mitochondrion"], "Golgi = the cell's 'traffic director' / packaging center.", "L4, slide 16")
add(6, "Which organelle is the site of protein synthesis?", "Ribosome",
    ["Golgi body", "Peroxisome", "Lysosome"], "Ribosomes make protein.", "L4, slide 11")
add(6, "Which organelle neutralizes toxins and alcohol?", "Peroxisome",
    ["Ribosome", "Golgi body", "Nucleolus"], "Peroxisome: oxidase enzymes detoxify; abundant in the liver.", "L4, slide 20")
add(6, "The Golgi body looks like:", "A stack of flattened membranous sacs near the nucleus",
    ["A bean-shaped organelle with folded cristae", "Tiny red dots on the ER", "Two cylinders at right angles"], "Stacked sacs near the nucleus.", "L4, slide 16")
add(6, "Peroxisomes are abundant in the liver because:", "The liver does much of the body's detoxification",
    ["The liver makes most of the body's protein", "The liver needs the most ATP", "The liver divides constantly"], "Peroxisomes neutralize toxins and alcohol.", "L4, slide 20 (notes)")
add(6, "Ribosomes are produced by the:", "Nucleolus",
    ["Golgi body", "Peroxisome", "Smooth ER"], "Nucleolus makes ribosomes; ribosomes make protein.", "L4, slides 9, 11")
add(6, "Peroxisomes contain which type of enzyme?", "Oxidase enzymes",
    ["Hydrolytic (digestive) enzymes", "DNA polymerase", "RNA polymerase"], "Peroxisomes = oxidase sacs; lysosomes = hydrolytic sacs.", "L4, slide 20")
add(6, "Ribosomes may be found:", "Free in the cytoplasm or attached to the ER",
    ["Only inside the nucleus", "Only inside the Golgi", "Only in mitochondria"], "Free ribosomes make proteins used inside the cell; ER-bound ones make proteins for export.", "L4, slide 11")
add(6, "Peroxisomes convert dangerous free radicals into:", "Hydrogen peroxide (then water)",
    ["ATP", "Glucose", "Mucus"], "Free radicals → H₂O₂ → catalase turns it into water.", "L4, slide 20 (notes)")

# ---------- 7. Skin layers: top vs. bottom ----------
add(7, "Which is the TOP (most superficial) layer of the epidermis?", "Stratum corneum",
    ["Stratum basale", "Stratum spinosum", "Stratum granulosum"], "Come (corneum) is first in 'Come Let's Get Sun Burned'.", "L6, slide 28")
add(7, "Which is the BOTTOM (deepest) layer of the epidermis?", "Stratum basale",
    ["Stratum corneum", "Stratum lucidum", "Stratum granulosum"], "Burned (basale) is last; it sits on the basement membrane.", "L6, slides 28, 33")
add(7, "From superficial to deep, the three layers are:", "Epidermis, dermis, hypodermis",
    ["Dermis, epidermis, hypodermis", "Hypodermis, dermis, epidermis", "Epidermis, hypodermis, dermis"], "Epidermis on top, dermis beneath, hypodermis below the skin.", "L6, slide 24")
add(7, "The superficial layer of the skin is the:", "Epidermis",
    ["Dermis", "Hypodermis", "Reticular layer"], "Epidermis = superficial; dermis = deeper.", "L6, slide 25")
add(7, "Which dermal layer is on top, just under the epidermis?", "Papillary layer",
    ["Reticular layer", "Stratum basale", "Hypodermis"], "Papillary = superficial 1/5; reticular = deep 4/5.", "L6, slide 39")
add(7, "Which dermal layer is on the bottom?", "Reticular layer",
    ["Papillary layer", "Stratum corneum", "Stratum spinosum"], "Reticular = the deep 4/5 of the dermis.", "L6, slide 40")
add(7, "The stratum basale sits directly on the:", "Basement membrane",
    ["Stratum corneum", "Hypodermis", "Nail bed"], "Deepest epidermal layer, on the basement membrane above the dermis.", "L6, slide 33")
add(7, "What lies BELOW the dermis?", "Hypodermis (subcutaneous layer)",
    ["Epidermis", "Stratum corneum", "Papillary layer"], "The hypodermis is not part of the skin; it sits below the dermis.", "L6, slide 42")

# ---------- 8. Mesenchyme ----------
add(8, "All adult connective tissue develops from:", "Mesenchyme",
    ["Wharton's jelly", "Epithelium", "Keratin"], "Mesenchyme is the embryonic tissue all adult CT comes from.", "L5, slides 48–49")
add(8, "Mesenchyme is a type of:", "Embryonic connective tissue",
    ["Adult epithelium", "Muscle tissue", "Nervous tissue"], "Embryonic CT: mesenchyme and Wharton's jelly.", "L5, slide 48")
add(8, "Where is mesenchyme found?", "Only in the embryo",
    ["In adult tendons", "In the stratum basale", "In the urinary bladder"], "Embryonic CT is only found in the embryo.", "L5, slide 48")
add(8, "The two types of embryonic connective tissue are:", "Mesenchyme and Wharton's jelly",
    ["Areolar and adipose", "Hyaline and elastic", "Collagen and reticular"], "Embryonic CT: a) mesenchyme, b) Wharton's jelly.", "L5, slide 48")
add(8, "Wharton's jelly is found in the:", "Umbilical cord",
    ["Ear", "Trachea", "Urinary bladder"], "Keeps the cord from kinking (patent = open).", "L5, slide 48")
add(8, "Bone, cartilage, blood and CT proper all come from:", "Mesenchyme",
    ["Ectoderm epithelium", "Wharton's jelly", "Goblet cells"], "Remember: ALL adult CT develops from mesenchyme.", "L5, slide 49")
add(8, "Which statement about mesenchyme is TRUE?", "It is the embryonic tissue that gives rise to all adult connective tissue",
    ["It is the outer layer of the skin", "It is found in the adult umbilical cord", "It is a type of epithelium"], "Mesenchyme = embryonic CT, source of all adult CT.", "L5, slide 48")
add(8, "Wharton's jelly keeps the umbilical cord 'patent,' which means:", "Open",
    ["Closed", "Stretchy", "Dry"], "Patent = open.", "L5, slide 48")

# ---------- 9. Epithelium vs. connective tissue ----------
add(9, "Which tissue is highly cellular with very little matrix?", "Epithelium",
    ["Connective tissue", "Blood", "Bone"], "Epithelium: tightly packed cells, little matrix.", "L5, slide 12")
add(9, "Which tissue has LOTS of matrix and few cells?", "Connective tissue",
    ["Epithelium", "Stratified squamous", "Transitional epithelium"], "CT: not cellular, lots of matrix.", "L5, slide 47")
add(9, "Epithelium is avascular. This means it:", "Has little or no blood supply of its own",
    ["Has a rich blood supply", "Has no nerve supply", "Cannot divide"], "Gets nutrients by diffusion from CT below.", "L5, slide 12")
add(9, "Which tissue is highly mitotic and replaces itself readily?", "Epithelium",
    ["Connective tissue", "Cartilage", "Dense regular CT"], "Epithelium: highly mitotic. CT: not mitotic.", "L5, slides 12, 47")
add(9, "Which tissue is generally very vascular (good blood supply)?", "Connective tissue",
    ["Epithelium", "Stratified squamous epithelium", "Simple squamous epithelium"], "CT is very vascular (cartilage is an exception).", "L5, slide 47")
add(9, "Epithelium has which two surfaces?", "Apical (free) and basal",
    ["Visceral and parietal", "Papillary and reticular", "Dorsal and ventral only"], "Apical = free/exposed; basal = on the basement membrane.", "L5, slide 12")
add(9, "Connective tissue is described as almost the exact ___ of epithelial tissue.", "Opposite",
    ["Same", "Mirror copy", "Source"], "Epithelium: cellular, mitotic, avascular. CT: matrix, not mitotic, vascular.", "L5, slide 47")
add(9, "The main function of connective tissue is to:", "Connect, bind and support",
    ["Cover and line surfaces", "Control the body", "Produce movement"], "Epithelium covers; CT supports; muscle moves; nervous controls.", "L5, slides 3, 47")
add(9, "The main function of epithelial tissue is to:", "Cover and line body surfaces",
    ["Connect and support", "Contract", "Send electrical signals"], "Epithelium = covering.", "L5, slides 3, 11")

# ---------- 10. Epidermis layers (Come Let's Get Sun Burned) ----------
add(10, "In 'Come Let's Get Sun Burned,' what does 'Let's' stand for?", "Stratum lucidum",
    ["Stratum basale", "Stratum granulosum", "Stratum spinosum"], "Corneum, Lucidum, Granulosum, Spinosum, Basale.", "L6, slide 28")
add(10, "In 'Come Let's Get Sun Burned,' what does 'Get' stand for?", "Stratum granulosum",
    ["Stratum germinativum", "Stratum lucidum", "Stratum corneum"], "G = granulosum (the grainy layer).", "L6, slide 28")
add(10, "In 'Come Let's Get Sun Burned,' what does 'Sun' stand for?", "Stratum spinosum",
    ["Stratum basale", "Stratum lucidum", "Subcutaneous layer"], "S = spinosum (the spiny layer).", "L6, slide 28")
add(10, "The correct order of the epidermis from superficial to deep is:", "Corneum, lucidum, granulosum, spinosum, basale",
    ["Basale, spinosum, granulosum, lucidum, corneum", "Corneum, granulosum, lucidum, spinosum, basale", "Lucidum, corneum, spinosum, granulosum, basale"], "Come Let's Get Sun Burned.", "L6, slides 28, 36")
add(10, "Which layer lies directly beneath the stratum granulosum?", "Stratum spinosum",
    ["Stratum lucidum", "Stratum corneum", "Papillary layer"], "...Get (granulosum) Sun (spinosum) Burned (basale).", "L6, slide 28")
add(10, "Which layer is called the 'spiny layer' and contains Langerhans cells?", "Stratum spinosum",
    ["Stratum granulosum", "Stratum basale", "Stratum corneum"], "Spines = pre-keratin bundles; Langerhans = phagocytic WBCs.", "L6, slide 32")
add(10, "Which layer is called the 'grainy layer'?", "Stratum granulosum",
    ["Stratum spinosum", "Stratum lucidum", "Stratum basale"], "Granules = pieces of dead organelles; cells filling with keratin.", "L6, slide 31")
add(10, "Melanocytes, which produce melanin, are found in the:", "Stratum basale",
    ["Stratum corneum", "Stratum spinosum", "Reticular layer"], "Melanocytes are in the basale.", "L6, slide 33")
add(10, "Which layer lies directly above the stratum basale?", "Stratum spinosum",
    ["Stratum granulosum", "Stratum lucidum", "Papillary layer"], "Sun (spinosum) sits just above Burned (basale).", "L6, slide 28")

# ---------- 11. Sudoriferous, ceruminous, sebaceous glands ----------
add(11, "Sudoriferous glands produce:", "Sweat",
    ["Oil (sebum)", "Earwax (cerumen)", "Mucus"], "Sudoriferous = sweat glands (eccrine and apocrine).", "L6, slide 46")
add(11, "Sebaceous glands produce:", "Sebum (oil)",
    ["Sweat", "Earwax", "Melanin"], "Sebaceous = oil glands; lubricate hair and skin.", "L6, slide 45")
add(11, "Ceruminous glands produce:", "Cerumen (earwax)",
    ["Sebum", "Sweat", "Serous fluid"], "Modified sweat glands in the ear canal.", "L6, slide 49")
add(11, "Which glands are attached to and empty into hair follicles and contain antibacterial lysozymes?", "Sebaceous glands",
    ["Eccrine glands", "Ceruminous glands", "Goblet cells"], "Sebaceous: oil into the follicle; lysozymes kill bacteria.", "L6, slide 45")
add(11, "All cutaneous glands are what type of gland?", "Exocrine (have ducts)",
    ["Endocrine (ductless)", "Serous", "Synovial"], "Exocrine glands have ducts and live mostly in the dermis.", "L6, slide 44")
add(11, "Which sweat glands are small, very numerous, and open onto the skin through pores?", "Eccrine",
    ["Apocrine", "Ceruminous", "Sebaceous"], "Eccrine = temperature control.", "L6, slide 47")
add(11, "Which sweat glands are large, found in the axillary and urogenital regions, and become active at puberty?", "Apocrine",
    ["Eccrine", "Ceruminous", "Sebaceous"], "Apocrine: protein-rich sweat, opens into hair follicles.", "L6, slide 48")
add(11, "Ceruminous glands are a modified type of:", "Sweat gland",
    ["Oil gland", "Mucous gland", "Endocrine gland"], "Modified (apocrine) sweat glands in the external ear canal.", "L6, slide 49")
add(11, "Which is a function of earwax (cerumen)?", "Natural insect repellent and lubricates the ear canal",
    ["Cools the body", "Waterproofs the palms", "Makes vitamin D"], "Cerumen lubricates and repels insects.", "L6, slide 49")
add(11, "The main function of sudoriferous (sweat) glands is:", "Thermoregulation",
    ["Lubricating hair", "Producing earwax", "Making melanin"], "Sweat evaporates to cool the body.", "L6, slide 46")

# ---------- 12. Thick skin's extra layer ----------
add(12, "Which epidermal layer is found ONLY in thick skin?", "Stratum lucidum",
    ["Stratum granulosum", "Stratum spinosum", "Stratum basale"], "Lucidum = the extra 5th layer.", "L6, slides 30, 34")
add(12, "Where is thick skin found?", "Palms of the hands and soles of the feet",
    ["Scalp and face", "Back and abdomen", "Eyelids and lips"], "Thick skin = palms & soles only.", "L6, slide 34")
add(12, "Thick skin has how many epidermal layers?", "5",
    ["4", "3", "6"], "Thick = 5 (adds lucidum); thin = 4.", "L6, slide 34")
add(12, "Thin skin has how many epidermal layers?", "4",
    ["5", "3", "2"], "Thin skin: corneum, granulosum, spinosum, basale.", "L6, slide 35")
add(12, "The stratum lucidum sits between which two layers?", "Corneum and granulosum",
    ["Granulosum and spinosum", "Spinosum and basale", "Basale and dermis"], "Come (corneum) Let's (lucidum) Get (granulosum).", "L6, slide 36")
add(12, "What does the stratum lucidum do?", "Adds protection and 'grip' so palms and soles don't slide",
    ["Produces new skin cells", "Produces melanin", "Forms the fingerprints"], "Extra protection and grip for high-friction areas.", "L6, slide 30")
add(12, "A microscope slide shows a clear band between the corneum and granulosum. This skin is from:", "A palm or sole (thick skin)",
    ["The back (thin skin)", "The scalp", "The lip"], "A visible lucidum means thick skin.", "L6, slide 36 (notes)")
add(12, "'Lucidum' means:", "Clear",
    ["Grainy", "Spiny", "Horny"], "Stratum lucidum = the 'clear layer'.", "L6, slide 30 (notes)")

# ---------- 13. Corpuscles and receptors ----------
add(13, "Which receptor detects DEEP pressure? ('Think Pacific Ocean')", "Pacinian corpuscle",
    ["Meissner's corpuscle", "Merkel disc", "Krause end bulb"], "Pacific Ocean is deep → Pacinian = deep pressure.", "L6, slide 17")
add(13, "Which receptor is responsible for two-point discrimination and light pressure?", "Meissner's corpuscle",
    ["Pacinian corpuscle", "Nociceptor", "Ruffini corpuscle"], "Meissner's: light touch, 2-point discrimination, in dermal papillae.", "L6, slide 17")
add(13, "Which receptor detects edges or points with light pressure?", "Merkel disc",
    ["Pacinian corpuscle", "Krause end bulb", "Nociceptor"], "Merkel discs: edges/points, light pressure.", "L6, slide 17")
add(13, "Which receptor detects pain?", "Nociceptor (free nerve ending)",
    ["Merkel disc", "Pacinian corpuscle", "Meissner's corpuscle"], "Nociceptors = free nerve endings for painful stimuli.", "L6, slide 18")
add(13, "Per the lecture, which receptor detects HEAT? ('Sounds Italian; Italy is hot')", "Ruffini corpuscle",
    ["Krause end bulb", "Merkel disc", "Pacinian corpuscle"], "Ruffini = hot (class pairing).", "L6, slide 18")
add(13, "Per the lecture, which receptor detects COLD? ('Sounds like Santa Claus')", "Krause end bulb (corpuscle)",
    ["Ruffini corpuscle", "Meissner's corpuscle", "Nociceptor"], "Krause = cold (class pairing).", "L6, slide 18")
add(13, "How many skin receptors were covered in lecture?", "6",
    ["4", "3", "8"], "Meissner, Merkel, Pacinian, nociceptor, Ruffini, Krause.", "L6, slides 17–18")
add(13, "Which receptor sits deepest in the skin?", "Pacinian (lamellar) corpuscle",
    ["Meissner's corpuscle", "Merkel disc", "Langerhans cell"], "Deep dermis/hypodermis; light-touch receptors sit high.", "L6, slides 19, 40")
add(13, "A light, feathery massage stroke mainly stimulates:", "Meissner's corpuscles and Merkel discs",
    ["Pacinian corpuscles", "Krause end bulbs", "Langerhans cells"], "Light touch receptors sit near the epidermis.", "L6, slide 17 (notes)")
add(13, "Meissner's corpuscles are housed in the:", "Dermal papillae (papillary layer)",
    ["Hypodermis", "Stratum corneum", "Reticular layer"], "Papillae house touch receptors.", "L6, slide 39")

# ---------- 14. Transitional epithelium ----------
add(14, "Transitional epithelium is found in the:", "Urinary bladder and ureters",
    ["Lungs and capillaries", "Stomach and intestines", "Kidney tubules and ovaries"], "Urinary system: bladder, ureters.", "L5, slide 43")
add(14, "What makes transitional epithelium unique?", "It is the only epithelium capable of stretching",
    ["It is only one cell thick", "It has no nuclei", "It is found only in the skin"], "Cells change shape as the bladder fills.", "L5, slide 43")
add(14, "When transitional epithelium is NOT stretched, the apical cells are:", "Rounded / dome-shaped",
    ["Flat and squamous", "Tall and columnar", "Absent"], "Relaxed = dome (umbrella) cells.", "L5, slide 43")
add(14, "When the bladder is full and transitional epithelium is stretched, the apical cells become:", "Flat (squamous-like)",
    ["Dome-shaped", "Tall columnar", "Ciliated"], "Stretched = flat surface cells.", "L5, slide 43")
add(14, "The function of transitional epithelium is:", "Protection and stretching to hold fluid",
    ["Rapid diffusion", "Producing mucus", "Absorbing nutrients"], "Lets the bladder hold urine.", "L5, slide 43")
add(14, "Transitional epithelium has how many layers?", "Two or more",
    ["Exactly one", "None", "One, but appears layered"], "It is a stratified (multi-layer) epithelium.", "L5, slide 43")
add(14, "The dome-shaped apical cells of transitional epithelium are sometimes called:", "Umbrella cells",
    ["Goblet cells", "Langerhans cells", "Chondrocytes"], "Umbrella-shaped cells at the apical surface.", "L5, slide 45")
add(14, "Why is the bladder lined with transitional epithelium?", "So it can fill with urine without tearing",
    ["To absorb nutrients from urine", "To make mucus", "To allow gas exchange"], "Stretches like a rubber band.", "L5, slide 43 (notes)")

# ---------- 15. Biggest vs. smallest layers ----------
add(15, "Which is thicker, the epidermis or the dermis?", "The dermis",
    ["The epidermis", "They are equal", "Neither; the stratum corneum is thickest"], "The dermis is much thicker than the epidermis.", "L6, slide 38")
add(15, "The thickest layer of the EPIDERMIS is the:", "Stratum corneum",
    ["Stratum basale", "Stratum lucidum", "Stratum granulosum"], "About 30–40 cells thick, ~3/4 of the epidermis.", "L6, slide 29")
add(15, "The stratum corneum makes up about how much of the epidermis?", "About 3/4",
    ["About 1/5", "About 1/2", "About 1/10"], "Corneum ≈ 3/4 of epidermal thickness.", "L6, slide 29")
add(15, "Which dermal layer is the larger (thicker) one?", "Reticular layer (deep 4/5)",
    ["Papillary layer (superficial 1/5)", "They are equal", "Stratum spinosum"], "Reticular = 4/5; papillary = 1/5.", "L6, slides 39–40")
add(15, "Which dermal layer is the smaller (thinner) one?", "Papillary layer (superficial 1/5)",
    ["Reticular layer (deep 4/5)", "Hypodermis", "Stratum corneum"], "Papillary = superficial 1/5.", "L6, slide 39")
add(15, "Which epidermal layers are described as only 'a few cells thick'?", "Stratum lucidum and stratum granulosum",
    ["Stratum corneum and stratum basale", "Papillary and reticular", "Stratum corneum only"], "Lucidum: a few cells thick. Granulosum: only a few cells thick.", "L6, slides 30–31")
add(15, "How many cells thick is the stratum corneum (per the slides)?", "About 30–40",
    ["About 2–3", "About 5–10", "About 100–200"], "Slide: 30–40 cells (Marieb says 20–30 rows).", "L6, slide 29")
add(15, "What is the largest organ of the body?", "The skin",
    ["The liver", "The lungs", "The brain"], "The skin (cutaneous membrane) is the largest organ.", "L6, slide 14")

# ---------- 16. Layers of the dermis and epidermis ----------
add(16, "The dermis has two layers. They are:", "Papillary and reticular",
    ["Corneum and basale", "Visceral and parietal", "Spinosum and granulosum"], "Dermis: papillary (superficial), reticular (deep).", "L6, slide 38")
add(16, "The papillary layer of the dermis is made of:", "Areolar CT",
    ["Dense irregular CT", "Stratified squamous epithelium", "Adipose tissue"], "Papillary = areolar (loose) CT.", "L6, slide 39")
add(16, "The reticular layer of the dermis is made of:", "Dense irregular CT",
    ["Areolar CT", "Dense regular CT", "Hyaline cartilage"], "Reticular = dense irregular CT, strong in all directions.", "L6, slide 40")
add(16, "Hair follicles, sweat glands, oil glands and lamellar corpuscles are found in which layer?", "Reticular layer of the dermis",
    ["Papillary layer of the dermis", "Stratum corneum", "Stratum lucidum"], "Reticular layer contains epidermal derivatives.", "L6, slide 40")
add(16, "The epidermis is made mostly of:", "Keratinized stratified squamous epithelium",
    ["Dense irregular CT", "Simple squamous epithelium", "Transitional epithelium"], "Epidermis = KSS; avascular.", "L6, slide 25")
add(16, "Which is vascular (has blood vessels)?", "Dermis",
    ["Epidermis", "Stratum corneum", "Stratum lucidum"], "Epidermis is avascular; dermis is vascular.", "L6, slide 25")
add(16, "Dermal papillae project from the dermis into the:", "Epidermis",
    ["Hypodermis", "Reticular layer", "Muscle"], "Papillae push up into the epidermis.", "L6, slide 39")
add(16, "Thin skin, superficial to deep, is:", "Corneum, granulosum, spinosum, basale",
    ["Corneum, lucidum, granulosum, spinosum, basale", "Basale, spinosum, granulosum, corneum", "Corneum, spinosum, granulosum, basale"], "Thin skin has no lucidum.", "L6, slide 35")
add(16, "Which statement about the hypodermis is TRUE?", "It is NOT a layer of skin; it is subcutaneous fat",
    ["It is the deepest layer of the epidermis", "It is part of the dermis", "It is the papillary layer"], "Hypodermis = subcutaneous layer below the dermis.", "L6, slide 42")

# ---------- 17. Phases of mitosis ----------
add(17, "The four phases of mitosis, in order, are:", "Prophase, metaphase, anaphase, telophase",
    ["Metaphase, prophase, telophase, anaphase", "Prophase, anaphase, metaphase, telophase", "G1, S, G2, M"], "PMAT.", "L4, slide 58")
add(17, "In which phase do chromosomes line up in the middle of the cell?", "Metaphase",
    ["Prophase", "Anaphase", "Telophase"], "'Meet in the Middle in Metaphase.'", "L4, slide 61")
add(17, "In which phase are chromosomes pulled to opposite ends of the cell?", "Anaphase",
    ["Metaphase", "Prophase", "Telophase"], "'Away in Anaphase.'", "L4, slide 62")
add(17, "In which phase does the nuclear membrane fall apart and chromatin condense into chromosomes?", "Prophase",
    ["Telophase", "Anaphase", "Metaphase"], "Prophase: membrane & nucleolus break down, spindle forms, centrioles move apart.", "L4, slide 59")
add(17, "In which phase does the nuclear membrane reform and cytokinesis occur?", "Telophase",
    ["Prophase", "Metaphase", "Anaphase"], "Telophase is like prophase in reverse.", "L4, slide 63")
add(17, "Which is the LONGEST phase of mitosis?", "Prophase",
    ["Metaphase", "Anaphase", "Telophase"], "Prophase = 1st and longest phase of mitosis.", "L4, slide 59")
add(17, "Cytokinesis is the:", "Division of the cytoplasm that splits the cell in two",
    ["Copying of DNA", "Lining up of chromosomes", "Making of proteins"], "Cyto = cell; kinesis = motion.", "L4, slide 63")
add(17, "The pinch in the middle of a dividing cell during telophase is the:", "Cleavage furrow",
    ["Centromere", "Mitotic spindle", "Nuclear pore"], "Cleavage furrow pinches the cell in two.", "L4, slide 64")
add(17, "Mitosis turns one mother cell into:", "Two identical daughter cells",
    ["Four different daughter cells", "One larger cell", "Two cells with half the DNA each"], "1 mother cell → 2 daughter cells with the same genes.", "L4, slide 58")
add(17, "During prophase, the centrioles:", "Move to opposite ends of the cell",
    ["Line up in the middle", "Are destroyed", "Copy the DNA"], "Each pair of centrioles moves to opposite poles and forms the spindle.", "L4, slide 59")

# ---------- 18. Lysosomes, ribosomes, Golgi, peroxisomes ----------
add(18, "Which organelle is called the 'suicide sac' of the cell?", "Lysosome",
    ["Peroxisome", "Golgi body", "Ribosome"], "If lysosomes rupture, the cell digests itself.", "L4, slide 18")
add(18, "Lysosomes contain which type of enzymes?", "Hydrolytic (digestive) enzymes",
    ["Oxidase enzymes", "DNA helicase", "RNA polymerase"], "Lysosomes = digestive enzyme sacs; peroxisomes = oxidase sacs.", "L4, slides 18, 20")
add(18, "Which organelle breaks down bacteria, viruses, dirt and worn-out cell parts?", "Lysosome",
    ["Ribosome", "Golgi body", "Centriole"], "Lysosomes 'break things down'.", "L4, slide 18")
add(18, "Lysosomes are packaged by the:", "Golgi body",
    ["Ribosome", "Nucleolus", "Peroxisome"], "The Golgi packages enzymes, hormones and lysosomes.", "L4, slide 16")
add(18, "Peroxisomes are similar to lysosomes, but they:", "Neutralize toxins and alcohol with oxidase enzymes",
    ["Make proteins", "Package hormones", "Make ATP"], "Peroxisome = detox; lysosome = digestion.", "L4, slide 20")
add(18, "Which organelle has NO membrane and makes protein?", "Ribosome",
    ["Lysosome", "Golgi body", "Peroxisome"], "Ribosomes are tiny protein + rRNA bodies; site of protein synthesis.", "L4, slide 11")
add(18, "What keeps a lysosome's enzymes from destroying the cell?", "Its membrane",
    ["Its cristae", "Its ribosomes", "The cytosol"], "Membrane keeps the hydrolytic enzymes contained.", "L4, slide 18")
add(18, "Lysosomes are especially abundant in:", "Phagocytes (white blood cells that eat bacteria)",
    ["Red blood cells", "Fat cells", "Sperm cells"], "Phagocytes rely on lysosomes to digest what they engulf.", "L4, slide 18 (notes)")
add(18, "Match: 'packages' → ?, 'makes protein' → ?, 'detoxifies' → ?, 'digests' → ?", "Golgi, ribosome, peroxisome, lysosome",
    ["Ribosome, Golgi, lysosome, peroxisome", "Peroxisome, ribosome, Golgi, lysosome", "Golgi, lysosome, ribosome, peroxisome"], "Golgi packages; ribosome makes protein; peroxisome detoxifies; lysosome digests.", "L4, slides 11, 16, 18, 20")

# ---------- 19. Collagen, elastic, reticular fibers ----------
add(19, "Which fiber is the STRONGEST, with very high tensile strength?", "Collagen",
    ["Elastic", "Reticular", "Fibrin"], "Collagen resists pulling, compression and deformity.", "L5, slide 7")
add(19, "Which fiber can stretch and RECOIL to its original shape?", "Elastic",
    ["Collagen", "Reticular", "Keratin"], "Elastic = stretch and recoil like a rubber band.", "L5, slide 7")
add(19, "Which fibers are skinny, highly branched collagen fibers that form a support network for soft organs?", "Reticular",
    ["Elastic", "Collagen", "Connexon"], "Reticular: internal 'skeleton' of spleen, lymph nodes.", "L5, slide 8")
add(19, "Which cells make and secrete the fibers into the matrix?", "Fibroblasts",
    ["Chondrocytes", "Melanocytes", "Goblet cells"], "Fibroblasts secrete fibers into the ground substance.", "L5, slide 6")
add(19, "The intercellular matrix has two components:", "Ground substance and fibers",
    ["Cells and plasma", "Collagen and elastin", "Cytosol and organelles"], "Matrix = ground substance + fibers.", "L5, slide 6")
add(19, "Reticular fibers compared to regular collagen fibers are:", "Thinner and not as strong",
    ["Thicker and stronger", "Able to recoil", "Made of keratin"], "'Skinny collagen fibers'; not as strong.", "L5, slide 8")
add(19, "Elastic connective tissue (rich in elastic fibers) is found in the:", "Vocal cords, lungs and large blood vessels",
    ["Tendons and ligaments", "Intervertebral discs", "Stratum corneum"], "Structures that must stretch and spring back.", "L5, slide 54")
add(19, "Tendons and ligaments are made primarily of which fiber?", "Collagen",
    ["Elastic", "Reticular", "Fibrin"], "Dense regular CT: parallel collagen bundles.", "L5, slide 52")
add(19, "Which tissue contains all three fiber types and is the body's 'packing material'?", "Areolar CT",
    ["Adipose tissue", "Dense regular CT", "Hyaline cartilage"], "Areolar has collagen, elastic and reticular fibers.", "L5, slide 55")
add(19, "The three fiber types are:", "Collagen, elastic, reticular",
    ["Collagen, keratin, melanin", "Actin, myosin, tubulin", "Elastic, fibrin, cartilage"], "Collagen, reticular, elastic.", "L5, slide 6")

# ---------- 20. Living vs. dead skin layers ----------
add(20, "In which epidermal layer are ALL of the cells dead?", "Stratum corneum",
    ["Stratum basale", "Stratum spinosum", "Stratum granulosum"], "Corneum: all cells dead, keratinized.", "L6, slide 29")
add(20, "In which layer do some cells start to die as they fill with keratin and move away from the blood supply?", "Stratum granulosum",
    ["Stratum basale", "Stratum spinosum", "Papillary layer"], "Granulosum: some alive, some beginning to die.", "L6, slide 31")
add(20, "Why do epidermal cells die as they move upward?", "They get farther from the blood supply in the dermis",
    ["They are attacked by Langerhans cells", "They run out of melanin", "They divide too fast"], "The epidermis is avascular; nutrients diffuse up from the dermis.", "L6, slides 25, 31")
add(20, "Which layer is made of living cells actively dividing?", "Stratum basale",
    ["Stratum corneum", "Stratum lucidum", "Stratum granulosum"], "Basale: mitosis, nearest the blood supply.", "L6, slide 33")
add(20, "Which of these layers is made of DEAD cells?", "Stratum lucidum",
    ["Stratum spinosum", "Stratum basale", "Papillary layer"], "Lucidum = a few rows of flat, dead cells.", "L6, slide 30 (notes)")
add(20, "Which two layers contain living cells?", "Stratum spinosum and stratum basale",
    ["Stratum corneum and stratum lucidum", "Stratum lucidum and stratum granulosum", "Stratum corneum and stratum spinosum"], "Deep layers near the blood supply are alive.", "L6, slides 32–33")
add(20, "Dead cells of the stratum corneum are filled with which protein?", "Keratin",
    ["Carotene", "Melanin", "Collagen"], "Keratin makes the corneum tough and waterproof.", "L6, slide 29")
add(20, "Going from deep to superficial, epidermal cells go from:", "Alive and dividing to dead and keratinized",
    ["Dead to alive", "Flat to cuboidal", "Keratinized to unkeratinized"], "Born in the basale, shed from the corneum.", "L6, slides 28, 35")

# ---------- 21. What happens in G1, S, G2, M ----------
add(21, "In which phase does DNA replication occur?", "S phase",
    ["G1", "G2", "Mitosis"], "S = Synthesis; DNA is doubled.", "L4, slide 56")
add(21, "In which phase does the cell grow to its mature size?", "G1",
    ["S", "G2", "Anaphase"], "G1 = Growth 1, the first and longest phase.", "L4, slide 55")
add(21, "In which phase does the cell do 'housekeeping' and final preparation before mitosis?", "G2",
    ["G1", "S", "Telophase"], "G2 = final preparation.", "L4, slide 57")
add(21, "What happens in the M phase?", "The cell divides (mitosis)",
    ["DNA is copied", "The cell grows to mature size", "Proteins are packaged"], "M = mitosis (cell division).", "L4, slide 58")
add(21, "At the end of G1, which structures replicate?", "Centrioles",
    ["Chromosomes", "Lysosomes", "Ribosomes"], "Centrioles replicate at the end of G1.", "L4, slide 55")
add(21, "A cell that never divides (does not do mitosis) stays in which phase?", "G1",
    ["S", "G2", "Metaphase"], "Some cells never leave G1.", "L4, slide 55")
add(21, "What does 'S' stand for in the S phase?", "Synthesis",
    ["Separation", "Spindle", "Structure"], "S = synthesis of DNA.", "L4, slide 56")
add(21, "A cell enters S phase with 46 chromosomes. When it leaves S phase it has:", "Twice the DNA (each chromosome copied)",
    ["Half the DNA", "The same DNA", "23 chromosomes"], "DNA is doubled into sister chromatids.", "L4, slide 56")
add(21, "Why must DNA replication happen BEFORE mitosis?", "So each daughter cell gets a full set of 46 chromosomes",
    ["So the cell can grow", "So the nucleus can disappear", "So proteins can be made"], "Each daughter cell needs the right number of chromosomes (23 pairs).", "L4, slide 42")

# ---------- 22. The germinating layer ----------
add(22, "Which layer of the epidermis makes new cells?", "Stratum basale",
    ["Stratum corneum", "Stratum granulosum", "Stratum lucidum"], "The epidermis grows from the basale.", "L6, slide 33")
add(22, "The stratum basale is also known as the:", "Stratum germinativum",
    ["Stratum lucidum", "Stratum spinosum", "Papillary layer"], "Germinativum = germinating, where new cells form.", "L6, slides 28, 33")
add(22, "Cells in the stratum basale are undergoing:", "Mitosis",
    ["Keratinization and death", "Shedding", "Cytokinesis only in thick skin"], "Constantly dividing by mitosis.", "L6, slide 33")
add(22, "The epidermis grows in which direction?", "From the bottom up",
    ["From the top down", "From the sides inward", "From the hypodermis outward"], "New cells form in the basale and are pushed toward the surface.", "L6, slide 35")
add(22, "Cells of the stratum basale are what shape?", "Cuboidal",
    ["Squamous", "Dome-shaped", "Spindle-shaped"], "Cells are cuboidal (to columnar).", "L6, slide 33")
add(22, "Why is the germinating layer the deepest layer of the epidermis?", "It is closest to the blood supply in the dermis",
    ["It is farthest from the blood supply", "It is filled with keratin", "It contains no nuclei"], "Dividing cells need nutrients diffusing from the dermis.", "L6, slide 33 (notes)")
add(22, "Which pair is located in the germinating layer?", "Dividing cells and melanocytes",
    ["Dead cells and keratin", "Langerhans cells and pre-keratin spines", "Hair follicles and sweat glands"], "Basale: mitosis + melanocytes.", "L6, slide 33")
add(22, "Cutaneous glands form from cells of which layer that push down into the dermis?", "Stratum basale",
    ["Stratum corneum", "Stratum lucidum", "Hypodermis"], "Glands come from basale cells growing down.", "L6, slide 44 (notes)")

# ---------- 23. Fingerprints ----------
add(23, "Which layer is responsible for fingerprints?", "Papillary layer of the dermis",
    ["Reticular layer of the dermis", "Stratum corneum", "Stratum basale"], "Dermal papillae form the fingerprint ridges.", "L6, slide 39")
add(23, "Fingerprints are formed by:", "Dermal papillae",
    ["Hair follicles", "Sebaceous glands", "Melanocytes"], "Projections of the dermis into the epidermis.", "L6, slide 39")
add(23, "Besides forming fingerprints, dermal papillae:", "Bring capillaries close to the epidermis and house touch receptors",
    ["Produce sweat", "Make melanin", "Produce earwax"], "Papillae: fingerprints, grip, capillaries, touch receptors.", "L6, slide 39")
add(23, "The fingerprint ridges help with:", "Friction for gripping",
    ["Temperature regulation", "Vitamin D synthesis", "Excreting urea"], "Ridges create friction for grip.", "L6, slide 39")
add(23, "The papillary layer, which forms fingerprints, makes up how much of the dermis?", "The superficial 1/5",
    ["The deep 4/5", "One half", "All of it"], "Papillary = superficial 1/5.", "L6, slide 39")
add(23, "The papillary layer that forms fingerprints is made of which tissue?", "Areolar CT",
    ["Dense irregular CT", "Keratinized stratified squamous epithelium", "Adipose"], "Papillary layer = areolar CT.", "L6, slide 39")
add(23, "Fingerprints are part of which main skin region?", "Dermis",
    ["Epidermis", "Hypodermis", "Stratum lucidum"], "They come from the papillary layer of the dermis.", "L6, slide 39")
add(23, "Footprints on the soles are formed the same way as fingerprints, by the:", "Dermal papillae",
    ["Stratum lucidum", "Arrector pili", "Reticular layer"], "Papillae form ridge patterns on palms and soles.", "L6, slide 39 (notes)")

# ---------- 24. Goblet cells ----------
add(24, "What do goblet cells produce?", "Mucus",
    ["Sweat", "Sebum", "Serous fluid"], "Goblet cells make mucus.", "L5, slide 27")
add(24, "Goblet cells are associated with which two epithelia?", "Simple columnar and pseudostratified columnar",
    ["Simple squamous and simple cuboidal", "Transitional and stratified cuboidal", "Keratinized and non-keratinized stratified squamous"], "Both columnar epithelia have goblet cells.", "L5, slides 27, 30")
add(24, "Goblet cells are named for their:", "Cup (goblet) shape",
    ["Location in the gut", "Ability to stretch", "Dark color"], "The cup-shaped cell that secretes mucus.", "L5, slide 28 (notes)")
add(24, "In the respiratory tract, mucus from goblet cells acts as a:", "Sticky trap for dust, swept away by cilia",
    ["Waterproof barrier", "Source of oxygen", "Lubricant for joints"], "Pseudostratified ciliated epithelium: goblet cells + cilia.", "L5, slide 30 (notes)")
add(24, "Where would you expect to find goblet cells?", "Lining the small intestine",
    ["In the stratum corneum", "In the urinary bladder lining", "In the capillary walls"], "Simple columnar epithelium of the digestive tract.", "L5, slide 29")
add(24, "Goblet cells are found in which type of tissue?", "Epithelial tissue",
    ["Connective tissue", "Nervous tissue", "Bone tissue"], "They sit within columnar epithelium.", "L5, slide 27")
add(24, "The upper respiratory tract is lined with pseudostratified columnar epithelium with cilia and:", "Goblet cells",
    ["Melanocytes", "Chondrocytes", "Umbrella cells"], "Goblet cells make the mucus the cilia sweep.", "L5, slide 30")
add(24, "Which statement about goblet cells is TRUE?", "They secrete lubricating mucus",
    ["They produce earwax", "They anchor cells to the basement membrane", "They make melanin"], "Goblet = mucus.", "L5, slide 27")

# ---------- 25. Cytosol, nucleus, ribosomes, ER ----------
add(25, "The watery (liquid) portion of the cytoplasm is the:", "Cytosol",
    ["Nucleoplasm", "Matrix", "Inclusion"], "Cytosol = watery portion; in the Jello analogy it is the Jello.", "L4, slide 4")
add(25, "Which structure is the 'brain' of the cell and contains DNA?", "Nucleus",
    ["Ribosome", "Cytosol", "Endoplasmic reticulum"], "The nucleus directs all cellular functions.", "L4, slide 6")
add(25, "Which organelle is a 'tubular transport system' connected to the nuclear envelope?", "Endoplasmic reticulum (ER)",
    ["Golgi body", "Cytosol", "Lysosome"], "ER = membrane canals for intracellular transport.", "L4, slide 13")
add(25, "Rough ER is 'rough' because it is:", "Studded with ribosomes",
    ["Covered in cilia", "Folded into cristae", "Filled with keratin"], "Rough ER makes proteins; smooth ER has no ribosomes.", "L4, slide 14")
add(25, "Smooth ER is responsible for:", "Lipid and carbohydrate synthesis and breaking down drugs",
    ["Making proteins", "Making ribosomes", "Producing ATP"], "No ribosomes, so no protein; lipids and detox.", "L4, slide 14")
add(25, "A cell with 2 nuclei is described as:", "Binucleate",
    ["Anucleate", "Uninucleate", "Multinucleate"], "Binucleate ≠ multinucleate (3+).", "L4, slide 6")
add(25, "A mature red blood cell has no nucleus. It is:", "Anucleate",
    ["Uninucleate", "Binucleate", "Multinucleate"], "Anucleate = no nucleus.", "L4, slide 6")
add(25, "In the 'Jello fruit salad' analogy for cytoplasm, the fruit represents the:", "Organelles",
    ["Cytosol", "Cell membrane", "Nucleus"], "Jello = cytosol; fruit = organelles.", "L4, slide 4")
add(25, "The nucleus is surrounded by the:", "Nuclear envelope (double membrane with pores)",
    ["Cell wall", "Golgi body", "Basement membrane"], "Double phospholipid bilayer with nuclear pores.", "L4, slide 7")
add(25, "Ribosomes are:", "The site of protein synthesis",
    ["The site of ATP production", "The liquid in the cytoplasm", "The cell's control center"], "Ribosomes make protein, free or on the rough ER.", "L4, slide 11")

QUIZ = {"id": "q2", "title": "A&P Quiz #2", "lectures": "Lectures 4–6",
        "units": {"L4": "Cells", "L5": "Tissues", "L6": "Skin & Body Membranes"},
        "topics": TOPICS, "questions": B.Q}
