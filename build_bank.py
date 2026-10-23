# Builds questions.json for the A&P Quiz #1 practice app.
# Format per question: topic, q (prompt), a (correct answer), w (wrong answers), e (explanation), s (source)
import json

TOPICS = {
    1: "Planes of the body",
    2: "Anatomy vs. physiology",
    3: "Oxidation vs. reduction",
    4: "Atomic mass vs. atomic number",
    5: "Types of bonds",
    6: "Terms for head and tail",
    7: "Smallest unit of matter / life",
    8: "Homeostasis",
    9: "Acid vs. base",
    10: "What the cell membrane is made of",
    11: "Charges: proton, neutron, electron",
    12: "Kinetic vs. potential energy",
    13: "Molecule vs. compound",
    14: "Positive vs. negative feedback",
    15: "Internal components of the cell",
    16: "Mono-, di- and polysaccharides",
    17: "Sharing vs. stealing electrons",
    18: "Synthesis, exchange and reversible reactions",
    19: "The universal solvent",
    20: "All the words for head / tail",
    21: "pH scale",
    22: "Diffusion vs. osmosis",
    23: "Coronal, sagittal and other planes",
    24: "Directional terms",
    25: "Synthesis reactions",
}

Q = []
def add(t, q, a, w, e, s):
    assert len(w) == 3, q
    assert a not in w, q
    Q.append({"topic": t, "q": q, "a": a, "w": w, "e": e, "s": s})

# ---------- 1. Planes of the body ----------
add(1, "Which plane divides the body into front (anterior) and back (posterior) portions?", "Coronal",
    ["Sagittal", "Transverse", "Oblique"], "The coronal (frontal) plane splits front from back.", "L1, slide 34")
add(1, "Which plane is also called the horizontal plane?", "Transverse",
    ["Coronal", "Midsagittal", "Frontal"], "Transverse = horizontal plane; it divides top from bottom.", "L1, slide 35")
add(1, "Which plane divides the body into EQUAL left and right halves?", "Midsagittal (median)",
    ["Sagittal (off-center)", "Coronal", "Transverse"], "The midsagittal (median) plane runs directly through the center.", "L1, slide 33")
add(1, "The transverse plane divides the body into:", "Top and bottom portions",
    ["Left and right portions", "Front and back portions", "Angled portions"], "Transverse (horizontal) = superior vs. inferior.", "L1, slide 35")
add(1, "The coronal plane is also known as the:", "Frontal plane",
    ["Horizontal plane", "Median plane", "Angular plane"], "Coronal a.k.a. frontal.", "L1, slide 34")
add(1, "A plane that divides the body into UNEQUAL left and right pieces is a:", "Sagittal plane",
    ["Midsagittal plane", "Coronal plane", "Transverse plane"], "Sagittal = left/right pieces; midsagittal is the special case that makes equal halves.", "L1, slide 33")
add(1, "The midsagittal plane is a special type of which plane?", "Sagittal",
    ["Coronal", "Transverse", "Oblique"], "Midsagittal (median) = a sagittal plane through the exact center.", "L1, slide 33")
add(1, "Which plane divides the body at various angles?", "Oblique",
    ["Transverse", "Coronal", "Midsagittal"], "Oblique (angular) plane cuts at various angles.", "L1, slide 36")

# ---------- 2. Anatomy vs. physiology ----------
add(2, "Anatomy is the study of the body's:", "Structure",
    ["Function", "Chemical reactions", "Diseases"], "Anatomy = STRUCTURE (names of parts and regions).", "L1, slide 3")
add(2, "Physiology is the study of:", "How the body functions",
    ["The names of body parts", "Body regions and landmarks", "The shape of bones"], "Physiology = how the body FUNCTIONS and how parts work together.", "L1, slide 3")
add(2, "Describing HOW the kidneys filter waste from blood is an example of:", "Physiology",
    ["Anatomy", "Histology", "Cytology"], "How something works = function = physiology.", "L1, slide 3")
add(2, "Learning the names of the bones of the skull is an example of:", "Anatomy",
    ["Physiology", "Homeostasis", "Biochemistry"], "Names of parts = structure = anatomy.", "L1, slide 3")
add(2, "Explaining how the heart pumps blood through the body is:", "Physiology",
    ["Anatomy", "Cytology", "Histology"], "Pumping is a function, so it's physiology.", "L1, slide 3")
add(2, "Identifying the four chambers of the heart is:", "Anatomy",
    ["Physiology", "Homeostasis", "Metabolism"], "Identifying parts = structure = anatomy.", "L1, slide 3")
add(2, "Why are anatomy and physiology studied together?", "Structure determines function",
    ["They are the same subject", "Function determines the names of parts", "Both only study cells"], "The lecture's spoon/fork/knife example: a part's structure determines what it can do.", "L1, slide 3")
add(2, "Which statement is correct?", "Anatomy = structure; physiology = function",
    ["Anatomy = function; physiology = structure", "Both mean the study of function", "Both mean the study of structure"], "Anatomy = STRUCTURE; physiology = FUNCTION.", "L1, slide 3")

# ---------- 3. Oxidation vs. reduction ----------
add(3, "Losing electrons in a chemical reaction is called:", "Oxidation",
    ["Reduction", "Hydrolysis", "Synthesis"], "LEO: Lose Electrons = Oxidation.", "L2, slides 44–45")
add(3, "Gaining electrons in a chemical reaction is called:", "Reduction",
    ["Oxidation", "Decomposition", "Ionization only"], "GER: Gain Electrons = Reduction.", "L2, slides 44–45")
add(3, "When sodium (Na) loses an electron and becomes Na⁺, sodium has been:", "Oxidized",
    ["Reduced", "Neutralized", "Hydrolyzed"], "Na loses an electron, so it is oxidized (LEO).", "L2, slide 46")
add(3, "When chlorine (Cl) gains an electron and becomes Cl⁻, chlorine has been:", "Reduced",
    ["Oxidized", "Neutralized", "Decomposed"], "Cl gains an electron, so it is reduced (GER).", "L2, slide 46")
add(3, "In the memory aid 'LEO the lion goes GER', what does LEO stand for?", "Lose Electrons = Oxidation",
    ["Lose Energy = Oxidation", "Lose Electrons = Osmosis", "Lose Elements = Oxidation"], "LEO = Lose Electrons = Oxidation; GER = Gain Electrons = Reduction.", "L2, slide 45")
add(3, "Which statement about oxidation and reduction is TRUE?", "They always occur together (coupled)",
    ["They never occur in the same reaction", "Oxidation only happens in acids", "Reduction means losing electrons"], "An oxidation must be coupled with a reduction, and vice versa.", "L2, slide 44")
add(3, "In GER, the 'R' stands for:", "Reduction",
    ["Reaction", "Release", "Reversible"], "Gain Electrons = Reduction.", "L2, slide 45")
add(3, "An atom that becomes more NEGATIVE by picking up an electron has undergone:", "Reduction",
    ["Oxidation", "Hydrolysis", "Filtration"], "Gaining an electron (more negative charge) = reduction.", "L2, slides 44–46")

# ---------- 4. Atomic mass vs. atomic number (static; app also generates calculation questions) ----------
add(4, "Atomic number is equal to the number of:", "Protons",
    ["Neutrons", "Protons + neutrons", "Electron shells"], "Atomic number = # of protons.", "L2, slides 11–12")
add(4, "Atomic mass is equal to the number of:", "Protons + neutrons",
    ["Protons only", "Protons + electrons", "Electrons only"], "Atomic mass = protons + neutrons.", "L2, slides 11–12")
add(4, "How do you calculate the number of neutrons in an atom?", "Atomic mass − atomic number",
    ["Atomic number − atomic mass", "Atomic mass + atomic number", "Atomic number × 2"], "# neutrons = atomic mass − atomic number.", "L2, slides 11–12")
add(4, "An element has an atomic number of 20. How many electrons are in a neutral atom of it?", "20",
    ["10", "40", "It cannot be determined"], "Neutral atoms have equal protons and electrons, so 20.", "L2, slide 14")
add(4, "An atom has 11 protons. How many electrons does a neutral atom of it have?", "11",
    ["12", "22", "1"], "# electrons = # protons in a neutral atom.", "L2, slide 17")

# ---------- 5. Types of bonds ----------
add(5, "Which type of bond forms when a metal gives electrons to a nonmetal?", "Ionic",
    ["Polar covalent", "Nonpolar covalent", "Hydrogen"], "Ionic bonds: electrons given by a metal and received by a nonmetal.", "L2, slide 22")
add(5, "Which type of bond is described as STRONG?", "Covalent",
    ["Ionic", "Hydrogen", "They are all equally strong"], "Covalent bonds are STRONG bonds where nonmetals share electrons.", "L2, slide 25")
add(5, "Which relatively WEAK bond forms between water molecules and between DNA bases?", "Hydrogen bond",
    ["Nonpolar covalent bond", "Polar covalent bond", "Peptide bond"], "Hydrogen bonds are relatively weak attractions between H atoms of different molecules.", "L2, slide 28")
add(5, "A bond formed between a cation (+) and an anion (−) is a(n):", "Ionic bond",
    ["Covalent bond", "Hydrogen bond", "Peptide bond"], "Ionic bonds form between oppositely charged ions.", "L2, slide 22")
add(5, "Which type of bond falls apart (dissociates) easily in water?", "Ionic",
    ["Nonpolar covalent", "Polar covalent", "Peptide"], "Ionic bonds dissociate easily in water (e.g., NaCl).", "L2, slide 22")
add(5, "NaCl (table salt) is held together by which type of bond?", "Ionic",
    ["Covalent", "Hydrogen", "Peptide"], "NaCl is the lecture's example of an ionic bond.", "L2, slide 22")
add(5, "A covalent bond in which electrons are shared EQUALLY (e.g., CO₂) is:", "Nonpolar covalent",
    ["Polar covalent", "Ionic", "Hydrogen"], "Nonpolar covalent = equal sharing; atoms close to the same size.", "L2, slide 25")
add(5, "Hydrogen bonds form between:", "Hydrogen atoms of different molecules",
    ["A metal and a nonmetal", "Two atoms sharing electrons equally", "Atoms inside one nucleus"], "Hydrogen bonds: adjacent hydrogen atoms of DIFFERENT molecules.", "L2, slide 28")

# ---------- 6. Terms for head and tail ----------
add(6, "Which term means 'toward the head'?", "Cephalic",
    ["Caudal", "Distal", "Inferior"], "Superior, cranial and cephalic all mean toward the head.", "L1, slide 23")
add(6, "'Caudal' means:", "Toward the tail/feet",
    ["Toward the head", "Toward the front", "Toward the midline"], "Caudal (caudad) = toward the tail, same as inferior.", "L1, slide 23")
add(6, "Which pair of terms BOTH mean 'toward the head'?", "Superior and cephalic",
    ["Inferior and cranial", "Caudal and cephalic", "Superior and caudad"], "Head: superior/cranial/cephalic. Tail: inferior/caudal/caudad.", "L1, slide 23")
add(6, "'Superior' is also called:", "Cranial or cephalic",
    ["Caudal or caudad", "Ventral or anterior", "Proximal or medial"], "Superior (cranial/cephalic) = toward the head.", "L1, slide 23")
add(6, "'Inferior' is also called:", "Caudal or caudad",
    ["Cranial or cephalic", "Dorsal or posterior", "Distal or lateral"], "Inferior (caudal/caudad) = toward the tail/feet.", "L1, slide 23")
add(6, "The term 'cranial' comes from cranium, which means:", "Skull",
    ["Tail", "Neck", "Spine"], "Cranium = skull → 'cranial'.", "L1, slide 27")
add(6, "Which term means the OPPOSITE of caudal?", "Cranial",
    ["Inferior", "Caudad", "Distal"], "Caudal = toward tail; cranial = toward head.", "L1, slide 23")
add(6, "Which pair of terms BOTH mean 'toward the tail'?", "Inferior and caudal",
    ["Superior and caudal", "Cranial and caudad", "Cephalic and inferior"], "Inferior, caudal and caudad all mean toward the tail/feet.", "L1, slide 23")

# ---------- 7. Smallest unit of matter / life ----------
add(7, "The smallest unit of matter is the:", "Atom",
    ["Cell", "Molecule", "Organelle"], "Atoms are the smallest unit of matter.", "L1, slide 5; L2, slide 5")
add(7, "The smallest unit of life is the:", "Cell",
    ["Atom", "Tissue", "Macromolecule"], "Cells are the smallest unit of life.", "L1, slide 6; L3, slide 42")
add(7, "Which pairing is correct?", "Matter: atom · Life: cell",
    ["Matter: cell · Life: atom", "Matter: molecule · Life: tissue", "Matter: atom · Life: organelle"], "Atom = smallest unit of matter; cell = smallest unit of life.", "L1, slides 5–6")
add(7, "The study of cells, the smallest unit of life, is called:", "Cytology",
    ["Histology", "Physiology", "Anatomy"], "Cytology = study of cells. Histology = study of tissues.", "L1, slide 6")
add(7, "Atoms are made of which three subatomic particles?", "Protons, neutrons, electrons",
    ["Cells, tissues, organs", "Molecules, ions, compounds", "Protons, ions, cells"], "Atoms (smallest unit of matter) are made of protons, neutrons and electrons.", "L2, slide 5")
add(7, "Which is the correct order from smallest to largest?", "Atom → molecule → cell → tissue",
    ["Cell → atom → tissue → molecule", "Molecule → atom → cell → tissue", "Tissue → cell → molecule → atom"], "Levels of organization build from atoms up to the organism.", "L1, slides 4–8")
add(7, "The human body is made of roughly how many cells?", "~35 trillion",
    ["~35 thousand", "~35 million", "~35 billion"], "The body is made of ~35 trillion cells, the smallest units of life.", "L3, slide 42")
add(7, "Which of these is NOT alive on its own, but is the smallest unit of matter?", "Atom",
    ["Cell", "Tissue", "Organism"], "Atoms are matter, not life. The cell is the smallest living unit.", "L1, slides 5–6")

# ---------- 8. Homeostasis ----------
add(8, "Homeostasis is best defined as:", "Maintaining a stable internal environment",
    ["The breakdown of food into nutrients", "The movement of water across a membrane", "The production of offspring"], "Homeostasis = the process of maintaining a stable internal environment.", "L1, slide 50")
add(8, "Homeostasis is also known as:", "Dynamic equilibrium",
    ["Metabolism", "Positive feedback", "Osmosis"], "a.k.a. dynamic equilibrium or state of balance.", "L1, slide 50")
add(8, "In a homeostatic feedback loop, which part SENSES the change?", "Receptor",
    ["Effector", "Control center", "Stimulus"], "Stimulus → receptor (senses) → control center → effector.", "L1, slide 51")
add(8, "In a feedback loop, which part interprets the signal and decides how to respond?", "Control center",
    ["Receptor", "Effector", "Stimulus"], "The control center interprets the signal and sends instructions.", "L1, slide 51")
add(8, "In a feedback loop, which part carries out the response (a cell, tissue or organ)?", "Effector",
    ["Receptor", "Control center", "Stimulus"], "The effector brings about the response; it is always a cell, tissue or organ.", "L1, slide 51")
add(8, "In a feedback loop, a 'stimulus' is:", "A deviation from normal",
    ["The part that responds", "The brain only", "A hormone that restores balance"], "Stimulus = deviation from normal.", "L1, slide 51")
add(8, "Which organ systems help maintain homeostasis?", "Virtually every organ system",
    ["Only the nervous system", "Only the endocrine system", "Only the cardiovascular system"], "Virtually every organ system plays a role.", "L1, slide 50")
add(8, "What is the correct order of a feedback loop?", "Stimulus → receptor → control center → effector",
    ["Receptor → stimulus → effector → control center", "Control center → stimulus → receptor → effector", "Effector → receptor → stimulus → control center"], "Stimulus is sensed by a receptor, interpreted by the control center, and carried out by an effector.", "L1, slide 51")

# ---------- 9. Acid vs. base ----------
add(9, "An acid is a substance that:", "Donates hydrogen ions (H⁺)",
    ["Accepts hydrogen ions (H⁺)", "Donates hydroxide ions (OH⁻)", "Has a pH above 7"], "Acids are H⁺ donors.", "L3, slide 9")
add(9, "A base is a substance that:", "Donates OH⁻ / accepts hydrogen ions",
    ["Donates hydrogen ions (H⁺)", "Has a sour taste", "Has a pH below 7"], "Bases donate OH⁻ and can be defined as H⁺ acceptors.", "L3, slide 10")
add(9, "In the reaction HCl → H⁺ + Cl⁻, HCl is acting as:", "An acid",
    ["A base", "A buffer", "A salt"], "HCl releases H⁺, so it's an acid.", "L3, slide 9")
add(9, "In the reaction NaOH → Na⁺ + OH⁻, NaOH is acting as:", "A base",
    ["An acid", "A buffer", "A solvent"], "NaOH releases OH⁻, so it's a base.", "L3, slide 10")
add(9, "Which characteristics describe a BASE?", "Bitter taste, slippery, pH above 7",
    ["Sour taste, burns metal, pH below 7", "Neutral taste, pH exactly 7", "Sour taste, slippery, pH below 7"], "Bases: bitter, slippery, high pH.", "L3, slide 10")
add(9, "Which characteristics describe an ACID?", "Sour taste, burns through metal, pH below 7",
    ["Bitter taste, slippery, pH above 7", "No taste, pH exactly 7", "Bitter taste, pH below 7"], "Acids: sour, burn through metal, low pH.", "L3, slide 9")
add(9, "Which substance ACCEPTS hydrogen ions?", "A base",
    ["An acid", "Water only", "A salt"], "Bases can be defined as hydrogen ion acceptors.", "L3, slide 10")
add(9, "Compounds that resist dramatic changes in pH by adding or removing H⁺ are called:", "Buffers",
    ["Salts", "Solvents", "Enzymes"], "Buffers act as acids when pH is high and as bases when pH is low.", "L3, slide 13")

# ---------- 10. Cell membrane ----------
add(10, "What is the MAJOR component of the cell membrane?", "Phospholipids arranged in a bilayer",
    ["Triglycerides", "Glycogen", "Membrane sugars"], "Phospholipids (bilayer) are the major component.", "L3, slides 25, 46")
add(10, "Which TWO types of lipids are found in the cell membrane?", "Phospholipids and cholesterol",
    ["Triglycerides and phospholipids", "Triglycerides and cholesterol", "Waxes and oils"], "Membrane lipids: phospholipids and cholesterol (a steroid).", "L3, slides 45, 51")
add(10, "Which is NOT a component of the cell membrane?", "Glycogen",
    ["Phospholipids", "Cholesterol", "Membrane proteins"], "Membrane = phospholipids, proteins, sugars, cholesterol. Glycogen is stored in liver and muscle.", "L3, slides 20, 45")
add(10, "The phospholipid head is ______ and the tail is ______.", "Hydrophilic; hydrophobic",
    ["Hydrophobic; hydrophilic", "Hydrophilic; hydrophilic", "Hydrophobic; hydrophobic"], "Head loves water (hydrophilic); tail fears water (hydrophobic).", "L3, slides 25, 46")
add(10, "What role does cholesterol play in the cell membrane?", "Holds phospholipids together; gives flexible rigidity",
    ["Forms channels for ions", "Stores energy for the cell", "Determines blood type"], "Cholesterol sits between phospholipids and gives 'flexible' rigidity.", "L3, slide 51")
add(10, "The 'fluid mosaic model' means membrane components:", "Are free to move within the membrane",
    ["Are locked in fixed positions", "Are made only of water", "Dissolve in water"], "Components are not locked in place; they move within the membrane.", "L3, slide 45")
add(10, "Which membrane component is used for blood typing?", "Membrane sugars",
    ["Cholesterol", "Phospholipid tails", "Peripheral proteins only"], "Membrane sugars: cell recognition, receptors, blood typing.", "L3, slide 50")
add(10, "Which membrane proteins span the entire membrane and form channels?", "Integral proteins",
    ["Peripheral proteins", "Membrane sugars", "Cholesterol"], "Integral proteins touch both inside and outside; only they form channels.", "L3, slide 48")

# ---------- 11. Charges ----------
add(11, "What is the charge of a neutron?", "Neutral (no charge)",
    ["Positive", "Negative", "Depends on the element"], "Neutrons have no charge.", "L2, slide 6")
add(11, "Which subatomic particle carries a NEGATIVE charge?", "Electron",
    ["Proton", "Neutron", "Nucleus"], "Electrons are negative.", "L2, slide 6")
add(11, "Which subatomic particle carries a POSITIVE charge?", "Proton",
    ["Electron", "Neutron", "Ion"], "Protons are positive.", "L2, slide 6")
add(11, "Which correctly matches particle and charge?", "Proton: positive",
    ["Proton: negative", "Electron: positive", "Neutron: positive"], "Proton +, neutron 0, electron −.", "L2, slide 6")
add(11, "Which particles are found in the nucleus?", "Protons and neutrons",
    ["Electrons only", "Protons and electrons", "Neutrons and electrons"], "Nucleus = protons + neutrons; electrons are in the electron cloud.", "L2, slide 6")
add(11, "Where are electrons found?", "In the electron cloud (shells/orbits) around the nucleus",
    ["Inside the nucleus", "Bound to neutrons", "Between protons"], "Electrons circle the nucleus in shells, orbits or rings.", "L2, slide 6")
add(11, "An atom that LOSES an electron becomes a:", "Cation (positive ion)",
    ["Anion (negative ion)", "Neutral atom", "Neutron"], "Losing electrons leaves more protons, so the atom is positive (cation).", "L2, slide 21")
add(11, "An atom that GAINS an electron becomes a(n):", "Anion (negative ion)",
    ["Cation (positive ion)", "Neutral atom", "Isotope"], "Gaining electrons makes it negative (anion).", "L2, slide 21")

# ---------- 12. Kinetic vs. potential energy ----------
add(12, "Energy of motion is called:", "Kinetic energy",
    ["Potential energy", "Activation energy", "Stored energy"], "Kinetic = energy of motion.", "L2, slide 34")
add(12, "Stored energy is called:", "Potential energy",
    ["Kinetic energy", "Thermal energy", "Mechanical energy"], "Potential = stored energy.", "L2, slide 34")
add(12, "Heat, light and the movement of large objects are examples of:", "Kinetic energy",
    ["Potential energy", "Stored energy", "Activation energy"], "All are energy of motion.", "L2, slide 34")
add(12, "The energy held in chemical bonds is:", "Potential energy",
    ["Kinetic energy", "Light energy", "Heat energy"], "Chemical bonds store energy, so it's potential.", "L2, slide 34")
add(12, "A charged battery sitting on a shelf contains:", "Potential energy",
    ["Kinetic energy", "No energy", "Only heat energy"], "A battery is the lecture's example of stored (potential) energy.", "L2, slide 34")
add(12, "Energy is defined as:", "The ability to do work",
    ["The movement of electrons only", "Stored heat", "The mass of an object"], "Energy is the ability to do work.", "L2, slide 34")
add(12, "A muscle actively contracting and moving the arm shows:", "Kinetic energy",
    ["Potential energy", "Stored energy", "Chemical bonds only"], "Movement = energy of motion = kinetic.", "L2, slide 34")
add(12, "Which pairing is correct?", "Kinetic = motion · Potential = stored",
    ["Kinetic = stored · Potential = motion", "Both = stored", "Both = motion"], "Kinetic is motion; potential is stored.", "L2, slide 34")

# ---------- 13. Molecule vs. compound ----------
add(13, "H₂ (two hydrogen atoms bonded together) is a:", "Molecule",
    ["Compound", "Ion", "Salt"], "A molecule is one type of element only.", "L2, slide 31")
add(13, "A compound is made of:", "Two or more different elements",
    ["Only one type of element", "Only charged atoms", "Only carbon atoms"], "Compound = 2+ different elements.", "L2, slide 31")
add(13, "Methane (CH₄), made of carbon and hydrogen, is a:", "Compound",
    ["Molecule of a single element", "Ion", "Element"], "Two different elements make it a compound.", "L2, slide 31")
add(13, "O₂ (two oxygen atoms) is best classified as a:", "Molecule",
    ["Compound", "Salt", "Mixture"], "Only one type of element (oxygen), so it's a molecule.", "L2, slide 31")
add(13, "Water (H₂O) contains hydrogen and oxygen. It is a:", "Compound",
    ["Molecule of one element", "Element", "Ion"], "Two different elements, so it's a compound.", "L2, slide 31")
add(13, "Which is the key difference between a molecule and a compound (as taught in lecture)?", "Molecule = one type of element; compound = two or more different elements",
    ["Molecule = charged; compound = neutral", "Molecule = large; compound = small", "There is no difference"], "Molecule = same element; compound = multiple elements.", "L2, slide 31")
add(13, "Glucose (C₆H₁₂O₆) is a:", "Compound",
    ["Molecule of one element", "Element", "Ion"], "Three different elements (C, H, O), so it's a compound.", "L2, slides 31–32")
add(13, "N₂ (two nitrogen atoms) is a:", "Molecule",
    ["Compound", "Salt", "Acid"], "One type of element only, so it's a molecule.", "L2, slide 31")

# ---------- 14. Positive vs. negative feedback ----------
add(14, "Which is an example of POSITIVE feedback?", "Childbirth contractions",
    ["Sweating when hot", "Shivering when cold", "Insulin lowering blood sugar"], "Positive feedback examples: childbirth (oxytocin) and blood clotting.", "L1, slides 54–55")
add(14, "In NEGATIVE feedback, the response:", "Moves in the opposite direction of the change",
    ["Moves in the same direction as the change", "Amplifies the stimulus", "Only happens in unusual circumstances"], "Negative feedback counteracts the stimulus.", "L1, slide 52")
add(14, "Shivering to warm up when you are cold is an example of:", "Negative feedback",
    ["Positive feedback", "Osmosis", "Hydrolysis"], "The response opposes the change, so it's negative feedback.", "L1, slides 52–53")
add(14, "Most feedback mechanisms in the body are:", "Negative",
    ["Positive", "Neither", "Equally positive and negative"], "Most feedback is negative.", "L1, slide 52")
add(14, "In POSITIVE feedback, the response:", "Amplifies the change (same direction)",
    ["Counteracts the change", "Returns the body to normal", "Stops the stimulus"], "Positive feedback amplifies and drives farther from normal.", "L1, slide 54")
add(14, "Blood clotting is an example of:", "Positive feedback",
    ["Negative feedback", "Diffusion", "Homeostatic sweating"], "Blood clotting is a positive feedback example.", "L1, slide 54")
add(14, "Sweating when body temperature rises is an example of:", "Negative feedback",
    ["Positive feedback", "Active transport", "Synthesis"], "Sweating cools the body, opposing the rise.", "L1, slide 52")
add(14, "Which hormone drives the positive feedback loop of childbirth?", "Oxytocin",
    ["Insulin", "Glucagon", "Cholesterol"], "The pituitary releases oxytocin, amplifying contractions.", "L1, slide 55")

# ---------- 15. Internal components of the cell ----------
add(15, "The liquid portion of the cytoplasm is the:", "Cytosol",
    ["Nucleus", "Inclusion", "Organelle"], "Cytoplasm includes cytosol (liquid), organelles, inclusions.", "L3, slide 43")
add(15, "Which is NOT part of the cytoplasm?", "Nucleus",
    ["Cytosol", "Organelles", "Inclusions"], "The nucleus is its own component.", "L3, slide 43")
add(15, "The three main components of a cell are:", "Cell membrane, cytoplasm, nucleus",
    ["Cytosol, organelles, inclusions", "Phospholipids, proteins, cholesterol", "Tissue, organ, organ system"], "Membrane ('skin'), cytoplasm ('guts'), nucleus ('brain').", "L3, slide 43")
add(15, "The cytoplasm is described as the cell's:", "'Guts'",
    ["'Skin'", "'Brain'", "'Bouncer'"], "Cytoplasm = the 'guts' of the cell.", "L3, slide 43")
add(15, "The nucleus is described as the cell's:", "'Brain' or command center",
    ["'Skin' or outer boundary", "'Guts'", "Liquid portion"], "Nucleus = 'brain' / command center.", "L3, slide 43")
add(15, "Tiny 'organs' inside the cell are called:", "Organelles",
    ["Inclusions", "Cytosol", "Tissues"], "Organelles = tiny organs within the cytoplasm.", "L3, slide 43")
add(15, "Things inside the cytoplasm that do NOT dissolve in water, like fat and pigments, are:", "Inclusions",
    ["Organelles", "Cytosol", "Nuclei"], "Inclusions = undissolved things like fat and pigment.", "L3, slide 43")
add(15, "The cytoplasm includes which three things?", "Cytosol, organelles, inclusions",
    ["Nucleus, membrane, cytosol", "Phospholipids, cholesterol, proteins", "DNA, RNA, ATP"], "Cytoplasm = cytosol + organelles + inclusions.", "L3, slide 43")

# ---------- 16. Saccharides ----------
add(16, "Glucose is classified as a:", "Monosaccharide",
    ["Disaccharide", "Polysaccharide", "Lipid"], "Glucose, fructose, galactose = monosaccharides.", "L3, slide 16")
add(16, "Sucrose (glucose + fructose) is a:", "Disaccharide",
    ["Monosaccharide", "Polysaccharide", "Protein"], "Disaccharides: sucrose, lactose, maltose.", "L3, slide 18")
add(16, "Glycogen, the storage form of glucose in animals, is a:", "Polysaccharide",
    ["Monosaccharide", "Disaccharide", "Triglyceride"], "Polysaccharides: starch (plants), glycogen (animals).", "L3, slide 20")
add(16, "Lactose is made of:", "Glucose + galactose",
    ["Glucose + fructose", "Glucose + glucose", "Fructose + galactose"], "Lactose = glucose + galactose.", "L3, slide 18")
add(16, "Maltose is made of:", "Glucose + glucose",
    ["Glucose + fructose", "Glucose + galactose", "Galactose + fructose"], "Maltose = glucose + glucose.", "L3, slide 18")
add(16, "Starch, the storage form of carbohydrate in plants, is a:", "Polysaccharide",
    ["Monosaccharide", "Disaccharide", "Lipid"], "Starch = plant polysaccharide.", "L3, slide 20")
add(16, "A disaccharide is made of how many monosaccharides?", "2",
    ["1", "3 or more", "20"], "Di = 2.", "L3, slide 18")
add(16, "Which chemical reaction joins monosaccharides into a disaccharide?", "Dehydration synthesis",
    ["Hydrolysis", "Oxidation", "Filtration"], "Monosaccharides are combined by dehydration synthesis.", "L3, slide 18")
add(16, "Where is glycogen stored in the body?", "Skeletal muscle and liver",
    ["Brain and spinal cord", "Skin and hair", "Bones and cartilage"], "Glycogen is stored in skeletal muscle and liver.", "L3, slide 20")
add(16, "Which is a monosaccharide?", "Fructose",
    ["Sucrose", "Lactose", "Glycogen"], "Fructose is a simple sugar; the others are di- or polysaccharides.", "L3, slide 16")

# ---------- 17. Sharing vs. stealing electrons ----------
add(17, "In which type of bond are electrons SHARED?", "Covalent",
    ["Ionic", "Hydrogen", "Metallic only"], "Covalent bonds: nonmetals share electrons.", "L2, slide 25")
add(17, "In which type of bond does one atom take ('steal') electrons from another?", "Ionic",
    ["Nonpolar covalent", "Polar covalent", "Hydrogen"], "Ionic: electrons are given by one atom and received by another.", "L2, slide 22")
add(17, "In water, oxygen and hydrogen share electrons UNEQUALLY. This is a:", "Polar covalent bond",
    ["Nonpolar covalent bond", "Ionic bond", "Hydrogen bond"], "Polar covalent = unequal sharing (e.g., water).", "L2, slide 25")
add(17, "Sharing electrons equally between atoms of about the same size is a:", "Nonpolar covalent bond",
    ["Polar covalent bond", "Ionic bond", "Hydrogen bond"], "Nonpolar covalent = equal sharing (e.g., CO₂).", "L2, slide 25")
add(17, "Covalent bonds form between:", "Nonmetal atoms sharing electrons",
    ["A metal and a nonmetal transferring electrons", "Molecules of water only", "A cation and an anion"], "Covalent = two or more nonmetals sharing.", "L2, slide 25")
add(17, "Polar covalent bonds share electrons unequally because:", "The atoms are very different in size",
    ["The atoms are the same size", "One atom is a metal", "No electrons are involved"], "Large difference in atom size → unequal sharing.", "L2, slide 25")
add(17, "When Na gives its electron to Cl to form NaCl, the bond formed is:", "Ionic",
    ["Covalent", "Hydrogen", "Peptide"], "Electron transferred (not shared), so it's ionic.", "L2, slides 22, 46")
add(17, "A chemical bond is an attraction between atoms created by:", "Sharing, losing or gaining electrons",
    ["Sharing protons", "Combining nuclei", "Losing neutrons"], "Bonds form by sharing, losing or gaining electrons.", "L2, slide 20")

# ---------- 18. Synthesis, exchange, reversible ----------
add(18, "AB + CD → AC + BD is an example of:", "Exchange (double displacement)",
    ["Synthesis", "Decomposition", "Reversible reaction"], "Partners are swapped, so it's an exchange reaction.", "L2, slide 41")
add(18, "A + B + energy ⇄ AB is an example of a:", "Reversible reaction",
    ["Single replacement", "Decomposition", "Double displacement"], "The double arrow means either direction.", "L2, slide 43")
add(18, "A + B → AB is an example of:", "Synthesis",
    ["Decomposition", "Exchange", "Single replacement"], "Putting pieces together = synthesis.", "L2, slide 37")
add(18, "A + BC → AC + B is an example of:", "Single replacement (exchange)",
    ["Synthesis", "Decomposition", "Double displacement"], "One element replaces another in a compound.", "L2, slide 42")
add(18, "AB → A + B + energy is an example of:", "Decomposition",
    ["Synthesis", "Exchange", "Reversible reaction"], "Breaking down, releasing energy = decomposition (catabolic).", "L2, slide 39")
add(18, "A double displacement reaction is actually a combination of which two reactions?", "Decomposition and synthesis",
    ["Oxidation and osmosis", "Synthesis and synthesis", "Diffusion and filtration"], "AB + CD breaks apart (catabolic) and then recombines (anabolic).", "L2, slide 41")
add(18, "Metal on a car slowly rusting is the lecture's example of a:", "Reversible reaction",
    ["Synthesis reaction only", "Double displacement", "Hydrolysis reaction"], "Most reactions in nature are reversible, even if it takes years.", "L2, slide 43")
add(18, "Which statement about reversible reactions is TRUE?", "Most reactions in nature are reversible",
    ["They can only go forward", "They never involve energy", "They only occur in acids"], "Most natural reactions are reversible.", "L2, slide 43")

# ---------- 19. Universal solvent ----------
add(19, "Which substance is known as the 'universal solvent'?", "Water",
    ["Blood plasma", "Hydrochloric acid", "Saline"], "Water is the universal solvent.", "L3, slide 6")
add(19, "Water makes up about how much of your body weight?", "About 2/3",
    ["About 1/4", "About 1/3", "About 9/10"], "~2/3 of body weight.", "L3, slide 6")
add(19, "A solvent is a substance that:", "Dissolves other substances",
    ["Resists changes in pH", "Speeds up chemical reactions", "Stores energy"], "Solvent: dissolves things.", "L3, slide 6")
add(19, "Water is held together by which type of bond?", "Polar covalent",
    ["Ionic", "Nonpolar covalent", "Peptide"], "Water is an inorganic compound with polar covalent bonds.", "L3, slide 6")
add(19, "Water is classified as a(n):", "Inorganic compound",
    ["Organic compound", "Lipid", "Element"], "Water contains no carbon, so it is inorganic.", "L3, slides 5–6")
add(19, "Which is NOT a function of water in the body?", "Storing genetic information",
    ["Lubrication and cushioning", "Temperature regulation", "Transportation (blood)"], "Water: solvent, lubrication/cushioning, temperature regulation, transport. DNA stores genetic info.", "L3, slide 6")
add(19, "Water helps regulate body temperature through:", "Sweat and its high heat capacity",
    ["Storing fat", "Producing ATP", "Forming ionic bonds"], "Temperature regulator: sweat and high heat capacity.", "L3, slide 6")
add(19, "Why is water called the 'universal solvent'?", "It dissolves more substances than any other liquid",
    ["It is found everywhere in the universe", "It never dissolves anything", "It is a strong acid"], "Water's polarity lets it dissolve a huge range of substances.", "L3, slide 6")

# ---------- 20. Words for head / tail ----------
add(20, "Which term does NOT refer to the head?", "Caudal",
    ["Superior", "Cranial", "Cephalic"], "Caudal = toward the tail.", "L1, slide 23")
add(20, "Which term means 'toward the tail'?", "Caudad",
    ["Cephalic", "Cranial", "Superior"], "Caudad/caudal/inferior = tail.", "L1, slide 23")
add(20, "'Cephalic' refers to the:", "Head",
    ["Tail", "Back", "Midline"], "Cephalon = head.", "L1, slides 23, 27")
add(20, "Which term does NOT refer to the tail/feet?", "Cranial",
    ["Inferior", "Caudal", "Caudad"], "Cranial = toward the head.", "L1, slide 23")
add(20, "Which group contains ONLY 'head' words?", "Superior, cranial, cephalic",
    ["Superior, caudal, cephalic", "Inferior, cranial, cephalic", "Cranial, caudad, superior"], "Head: superior, cranial, cephalic.", "L1, slide 23")
add(20, "Which group contains ONLY 'tail' words?", "Inferior, caudal, caudad",
    ["Inferior, cranial, caudad", "Superior, caudal, caudad", "Caudal, cephalic, inferior"], "Tail: inferior, caudal, caudad.", "L1, slide 23")
add(20, "'Cephalon' is the Latin/Greek word for:", "Head",
    ["Skull", "Neck", "Face"], "Cephalon (head) → 'cephalic'. Cranium = skull.", "L1, slide 27")
add(20, "The feet are ______ to the head.", "Inferior (caudal)",
    ["Superior (cranial)", "Cephalic", "Medial"], "Toward the tail/feet = inferior/caudal.", "L1, slide 23")

# ---------- 21. pH (static; app also generates questions) ----------
add(21, "The pH scale ranges from:", "0 to 14",
    ["1 to 10", "0 to 100", "−7 to 7"], "pH range is 0–14.", "L3, slide 11")
add(21, "The normal pH of human blood is:", "7.35–7.45",
    ["6.35–6.45", "7.0 exactly", "8.35–8.45"], "Blood pH = 7.35–7.45 (slightly basic).", "L3, slide 11")
add(21, "As H⁺ concentration INCREASES, a solution becomes more:", "Acidic (lower pH)",
    ["Basic (higher pH)", "Neutral", "Salty"], "More H⁺ = more acidic = lower pH.", "L3, slides 11–12")
add(21, "As OH⁻ concentration INCREASES, a solution becomes more:", "Basic (higher pH)",
    ["Acidic (lower pH)", "Neutral", "Polar"], "More OH⁻ = more basic = higher pH.", "L3, slides 11–12")
add(21, "Human blood (pH 7.35–7.45) is:", "Slightly basic",
    ["Strongly acidic", "Slightly acidic", "Exactly neutral"], "Just above 7 = slightly basic.", "L3, slide 11")

# ---------- 22. Diffusion vs. osmosis ----------
add(22, "Osmosis is the movement of:", "Water only",
    ["Gases from high to low concentration", "Large particles using ATP", "Particles through holes driven by blood pressure"], "Osmosis = 'the diffusion of water'.", "L3, slide 57")
add(22, "Simple diffusion is the movement of molecules:", "From high to low concentration without energy",
    ["From low to high concentration using ATP", "Of water only", "Only through a carrier molecule"], "Diffusion: high → low, down a concentration gradient, no energy.", "L3, slide 56")
add(22, "What is the key difference between diffusion and osmosis?", "Osmosis moves only water; diffusion moves other molecules",
    ["Diffusion requires ATP; osmosis does not", "Diffusion moves low to high; osmosis high to low", "Osmosis is active; diffusion is passive"], "Both are passive and high → low; osmosis is water only.", "L3, slides 56–57")
add(22, "Diffusion and osmosis are both examples of:", "Passive transport (no ATP)",
    ["Active transport", "Endocytosis", "Exocytosis"], "Both are passive.", "L3, slides 55–57")
add(22, "A cell placed in a HYPOTONIC solution will:", "Swell and may burst (hemolysis)",
    ["Shrink (crenation)", "Stay the same size", "Pump water out using ATP"], "Water rushes in, so the cell swells.", "L3, slide 59")
add(22, "A cell placed in a HYPERTONIC solution will:", "Shrink (crenation)",
    ["Swell and burst", "Stay the same size", "Divide"], "Water moves out, so the cell shrinks.", "L3, slide 60")
add(22, "In an ISOTONIC solution, a cell will:", "Stay the same size",
    ["Swell", "Shrink", "Burst"], "Same concentration inside and out, so water moves evenly.", "L3, slide 58")
add(22, "Simple diffusion is driven by:", "A concentration gradient",
    ["ATP", "Blood pressure", "A carrier molecule"], "Diffusion is driven by a concentration gradient.", "L3, slide 56")

# ---------- 23. Coronal, sagittal and other planes ----------
add(23, "The sagittal plane divides the body into:", "Left and right portions",
    ["Front and back portions", "Top and bottom portions", "Angled portions"], "Sagittal = left/right.", "L1, slide 33")
add(23, "The frontal plane is another name for the:", "Coronal plane",
    ["Sagittal plane", "Transverse plane", "Oblique plane"], "Coronal a.k.a. frontal.", "L1, slide 34")
add(23, "Which plane is also called the angular plane?", "Oblique",
    ["Coronal", "Sagittal", "Transverse"], "Oblique = angular.", "L1, slide 36")
add(23, "A cut that separates the face from the back of the head is along the:", "Coronal plane",
    ["Sagittal plane", "Transverse plane", "Midsagittal plane"], "Front vs. back = coronal (frontal).", "L1, slide 34")
add(23, "A cut that separates the right eye from the left eye is along a:", "Sagittal plane",
    ["Coronal plane", "Transverse plane", "Horizontal plane"], "Left vs. right = sagittal.", "L1, slide 33")
add(23, "A cut at the waist separating the upper body from the lower body is along the:", "Transverse plane",
    ["Coronal plane", "Sagittal plane", "Frontal plane"], "Top vs. bottom = transverse (horizontal).", "L1, slide 35")
add(23, "The median plane is another name for the:", "Midsagittal plane",
    ["Coronal plane", "Transverse plane", "Oblique plane"], "Midsagittal (median).", "L1, slide 33")
add(23, "Which pairing is correct?", "Coronal = front/back · Sagittal = left/right",
    ["Coronal = left/right · Sagittal = front/back", "Coronal = top/bottom · Sagittal = left/right", "Coronal = front/back · Sagittal = top/bottom"], "Coronal splits front/back; sagittal splits left/right.", "L1, slides 33–34")

# ---------- 24. Directional terms ----------
add(24, "'Medial' means:", "Toward the midline",
    ["Away from the midline", "Close to the point of attachment", "Toward the surface"], "Medial = toward the midline.", "L1, slide 24")
add(24, "The wrist is ______ to the elbow.", "Distal",
    ["Proximal", "Medial", "Superior"], "Distal = farther from the point of attachment.", "L1, slide 24")
add(24, "The ears are ______ to the nose.", "Lateral",
    ["Medial", "Proximal", "Deep"], "Lateral = away from the midline.", "L1, slide 24")
add(24, "The elbow is ______ to the wrist.", "Proximal",
    ["Distal", "Lateral", "Inferior"], "Proximal = closer to the point of attachment.", "L1, slide 24")
add(24, "'Superficial' means:", "Toward the surface",
    ["Away from the surface", "Toward the midline", "Toward the back"], "Superficial (external) = toward the surface.", "L1, slide 25")
add(24, "The skin is ______ to the muscles.", "Superficial",
    ["Deep", "Proximal", "Medial"], "The skin is closer to the surface.", "L1, slide 25")
add(24, "'Anterior' is also called:", "Ventral",
    ["Dorsal", "Caudal", "Lateral"], "Anterior (ventral) = toward the front.", "L1, slide 23")
add(24, "'Posterior' is also called:", "Dorsal",
    ["Ventral", "Cranial", "Medial"], "Posterior (dorsal) = toward the back.", "L1, slide 23")
add(24, "The nose is ______ to the eyes.", "Medial",
    ["Lateral", "Distal", "Posterior"], "The nose is closer to the midline.", "L1, slide 24")
add(24, "The term for 'between superficial and deep' is:", "Intermediate",
    ["Medial", "Proximal", "Lateral"], "Intermediate = between superficial and deep.", "L1, slide 25")

# ---------- 25. Synthesis reactions ----------
add(25, "Which statement about synthesis reactions is TRUE?", "They build larger molecules and require energy",
    ["They break molecules apart", "They release energy", "They are catabolic"], "Synthesis (anabolic) = construction; requires energy.", "L2, slide 37")
add(25, "Dehydration synthesis creates a bond by:", "Removing water",
    ["Adding water", "Adding oxygen", "Releasing energy"], "Dehydration = removal of water.", "L2, slide 38")
add(25, "Synthesis reactions are also called:", "Anabolic",
    ["Catabolic", "Hydrolysis", "Exchange"], "Synthesis = anabolic; decomposition = catabolic.", "L2, slides 37, 39")
add(25, "Which equation represents a synthesis reaction?", "A + B (+ energy) → AB",
    ["AB → A + B + energy", "AB + CD → AC + BD", "A + BC → AC + B"], "Synthesis puts A and B together into AB.", "L2, slide 37")
add(25, "The lecture describes synthesis as:", "Construction",
    ["Demolition", "Exchange", "Filtration"], "Synthesis = construction; decomposition = demolition.", "L2, slides 37, 39")
add(25, "Energy for a synthesis reaction usually comes in the form of:", "Heat",
    ["Light only", "Sound", "Nothing; no energy is needed"], "Requires energy input, usually heat.", "L2, slide 37")
add(25, "Forming functional proteins from amino acids is an example of:", "Synthesis (anabolic)",
    ["Decomposition (catabolic)", "Hydrolysis", "Single replacement"], "Building proteins = synthesis.", "L2, slide 38")
add(25, "The OPPOSITE of dehydration synthesis is:", "Hydrolysis (breaking a bond by adding water)",
    ["Oxidation", "Osmosis", "Double displacement"], "Hydrolysis = break by adding water.", "L2, slide 40")

# sanity
from collections import Counter
c = Counter(q["topic"] for q in Q)
for t in TOPICS:
    assert c[t] >= 5, (t, c[t])
out = {"title": "A&P Quiz #1 Practice", "topics": TOPICS, "questions": Q}
json.dump(out, open("questions.json", "w"), ensure_ascii=False, indent=1)
print(len(Q), "questions;", dict(sorted(c.items())))
