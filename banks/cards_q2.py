# Flashcards for A&P Quiz #2 (Lectures 4-6). Each card: (topic, front, back, source).
CARDS = [
    # 1. Cell cycle
    (1, "Two main stages of the cell cycle", "Interphase, then mitosis (M phase)", "L4, slide 53"),
    (1, "Order of the cell cycle", "G1 → S → G2 → Mitosis", "L4, slides 53–54"),
    (1, "Sub-phases of interphase", "G1, S, G2", "L4, slide 53"),
    (1, "Longest part of the cell cycle", "Interphase (G1 is its longest phase)", "L4, slides 53, 55"),
    (1, "Is interphase a 'resting' phase?", "No: the cell is growing, working and preparing to divide", "L4, slide 53"),
    # 2. Cell junctions
    (2, "Tight junction", "Leak-proof seal, like a zipper; nothing passes BETWEEN cells", "L5, slide 14"),
    (2, "Gap junction", "Hollow channels (connexons) that let cells COMMUNICATE", "L5, slide 15"),
    (2, "Desmosome", "'Spot welds' that resist mechanical stress", "L5, slide 16"),
    (2, "Hemidesmosome", "'Half' desmosome; anchors the BASAL surface to the basement membrane", "L5, slide 16"),
    (2, "Connexon", "The hollow protein channel of a gap junction", "L5, slide 15"),
    # 3. Body membranes
    (3, "Cutaneous membrane", "The skin; the ONLY dry membrane", "L6, slide 5"),
    (3, "Serous membrane", "Lines cavities CLOSED to the exterior (Serous = Sealed)", "L6, slide 6"),
    (3, "Mucous membrane", "Lines cavities OPEN to the exterior (respiratory, digestive, urogenital)", "L6, slide 8"),
    (3, "Synovial membrane", "Lines joints, bursae, tendon sheaths; NO epithelium (connective tissue only)", "L6, slides 4, 10"),
    # 4. Epithelium types
    (4, "Simple squamous", "One thin, flat layer; rapid diffusion and filtration (alveoli, capillaries)", "L5, slide 21"),
    (4, "Simple cuboidal", "One layer of cubes; secretion and absorption (kidney tubules, ovaries)", "L5, slide 24"),
    (4, "Simple columnar", "Tall cells with goblet cells; digestive tract stomach → rectum", "L5, slide 27"),
    (4, "Transitional", "Stretches; lines the urinary bladder and ureters", "L5, slide 43"),
    # 5. DNA / RNA base pairing
    (5, "DNA base pairs", "A–T and G–C", "L4, slides 33, 39"),
    (5, "RNA base pairs", "A–U and G–C", "L4, slides 36, 39"),
    (5, "Base only in DNA", "Thymine (T)", "L4, slide 38"),
    (5, "Base only in RNA", "Uracil (U), replaces thymine", "L4, slide 38"),
    (5, "Nucleotide", "Phosphate + sugar + nitrogenous base", "L4, slide 31"),
    # 6. Golgi, peroxisome, ribosome
    (6, "Golgi body", "Packages and ships proteins, hormones, enzymes and lysosomes; stack of flat sacs", "L4, slide 16"),
    (6, "Ribosome", "Site of PROTEIN synthesis", "L4, slide 11"),
    (6, "Peroxisome", "Neutralizes toxins and alcohol (oxidase enzymes); abundant in the liver", "L4, slide 20"),
    # 7. Skin layers top vs. bottom
    (7, "Top (most superficial) epidermal layer", "Stratum corneum", "L6, slide 28"),
    (7, "Bottom (deepest) epidermal layer", "Stratum basale", "L6, slides 28, 33"),
    (7, "Skin layers, superficial → deep", "Epidermis, dermis, hypodermis", "L6, slide 24"),
    (7, "Top dermal layer", "Papillary layer (just under the epidermis)", "L6, slide 39"),
    # 8. Mesenchyme
    (8, "Mesenchyme", "Embryonic CT that ALL adult connective tissue develops from", "L5, slides 48–49"),
    (8, "Two embryonic connective tissues", "Mesenchyme and Wharton's jelly", "L5, slide 48"),
    (8, "Wharton's jelly", "In the umbilical cord; keeps it from kinking", "L5, slide 48"),
    (8, "Where is mesenchyme found?", "Only in the embryo", "L5, slide 48"),
    # 9. Epithelium vs. connective tissue
    (9, "Epithelium", "Many cells, little matrix; avascular; highly mitotic", "L5, slide 12"),
    (9, "Connective tissue", "Few cells, lots of matrix; very vascular (except cartilage); not mitotic", "L5, slide 47"),
    (9, "Avascular", "Little or no blood supply of its own; fed by diffusion", "L5, slide 12"),
    # 10. Epidermis layers
    (10, "Come Let's Get Sun Burned", "Corneum, Lucidum, Granulosum, Spinosum, Basale (superficial → deep)", "L6, slide 28"),
    (10, "'Let's'", "Stratum lucidum", "L6, slide 28"),
    (10, "'Get'", "Stratum granulosum (grainy)", "L6, slide 28"),
    (10, "'Sun'", "Stratum spinosum (spiny)", "L6, slide 28"),
    (10, "Layer directly under the granulosum", "Stratum spinosum", "L6, slide 28"),
    # 11. Glands
    (11, "Sudoriferous glands", "SWEAT glands (eccrine and apocrine)", "L6, slide 46"),
    (11, "Sebaceous glands", "OIL (sebum); empty into hair follicles; lysozymes kill bacteria", "L6, slide 45"),
    (11, "Ceruminous glands", "EARWAX (cerumen); modified sweat glands", "L6, slide 49"),
    (11, "Cutaneous glands are…", "Exocrine (have ducts)", "L6, slide 44"),
    # 12. Thick skin
    (12, "Extra layer in thick skin", "Stratum lucidum", "L6, slides 30, 34"),
    (12, "Where is thick skin?", "Palms and soles only", "L6, slide 34"),
    (12, "Thick vs. thin skin layers", "Thick = 5 epidermal layers; thin = 4", "L6, slides 34–35"),
    (12, "Lucidum sits between…", "Corneum and granulosum", "L6, slide 36"),
    # 13. Corpuscles and receptors
    (13, "Pacinian corpuscle", "DEEP pressure ('Pacific Ocean is deep')", "L6, slide 17"),
    (13, "Meissner's corpuscle", "Light touch, two-point discrimination; in dermal papillae", "L6, slide 17"),
    (13, "Merkel disc", "Edges/points, light pressure", "L6, slide 17"),
    (13, "Nociceptor", "PAIN (free nerve ending)", "L6, slide 18"),
    (13, "Ruffini corpuscle", "HEAT ('sounds Italian; Italy is hot')", "L6, slide 18"),
    # 14. Transitional epithelium
    (14, "Transitional epithelium location", "Urinary bladder and ureters", "L5, slide 43"),
    (14, "What's unique about transitional epithelium?", "The only epithelium that STRETCHES", "L5, slide 43"),
    (14, "Transitional, relaxed", "Apical cells rounded / dome-shaped", "L5, slide 43"),
    (14, "Transitional, stretched", "Apical cells flat (squamous-like)", "L5, slide 43"),
    # 15. Biggest vs. smallest layers
    (15, "Thicker: epidermis or dermis?", "Dermis", "L6, slide 38"),
    (15, "Thickest epidermal layer", "Stratum corneum (~3/4 of the epidermis)", "L6, slide 29"),
    (15, "Reticular layer size", "Deep 4/5 of the dermis (the larger layer)", "L6, slides 39–40"),
    (15, "Papillary layer size", "Superficial 1/5 of the dermis (the smaller layer)", "L6, slide 39"),
    # 16. Layers of dermis and epidermis
    (16, "Two layers of the dermis", "Papillary (superficial) and reticular (deep)", "L6, slide 38"),
    (16, "Papillary layer tissue", "Areolar (loose) CT", "L6, slide 39"),
    (16, "Reticular layer tissue", "Dense irregular CT; holds hair follicles, glands, lamellar corpuscles", "L6, slide 40"),
    (16, "Epidermis tissue", "Keratinized stratified squamous epithelium; avascular", "L6, slide 25"),
    # 17. Phases of mitosis
    (17, "Phases of mitosis", "Prophase, metaphase, anaphase, telophase (PMAT)", "L4, slide 58"),
    (17, "Prophase", "Nuclear membrane breaks down; chromatin condenses; spindle forms", "L4, slide 59"),
    (17, "Metaphase", "Chromosomes line up in the MIDDLE ('Meet in the Middle')", "L4, slide 61"),
    (17, "Anaphase", "Chromosomes pulled to opposite ends ('Away')", "L4, slide 62"),
    (17, "Telophase", "Nuclear membrane reforms; cytokinesis; prophase in reverse", "L4, slide 63"),
    # 18. Lysosomes etc.
    (18, "Lysosome", "'Suicide sac'; digestive (hydrolytic) enzymes break down bacteria and worn-out parts", "L4, slide 18"),
    (18, "Lysosome vs. peroxisome", "Lysosome = digestion; peroxisome = detox (oxidase)", "L4, slides 18, 20"),
    (18, "What packages lysosomes?", "The Golgi body", "L4, slide 16"),
    # 19. Fibers
    (19, "Collagen fibers", "STRONGEST; high tensile strength", "L5, slide 7"),
    (19, "Elastic fibers", "Stretch and RECOIL like a rubber band", "L5, slide 7"),
    (19, "Reticular fibers", "Skinny, branched collagen; support network (spleen, lymph nodes)", "L5, slide 8"),
    (19, "Fibroblasts", "Cells that make and secrete fibers into the matrix", "L5, slide 6"),
    (19, "Matrix components", "Ground substance + fibers", "L5, slide 6"),
    # 20. Living vs. dead layers
    (20, "Layer where ALL cells are dead", "Stratum corneum", "L6, slide 29"),
    (20, "Layer where cells START to die", "Stratum granulosum", "L6, slide 31"),
    (20, "Why epidermal cells die moving up", "They get farther from the blood supply in the dermis", "L6, slides 25, 31"),
    (20, "Living, dividing layer", "Stratum basale", "L6, slide 33"),
    (20, "Stratum lucidum: alive or dead?", "Dead (a few rows of flat, dead cells)", "L6, slide 30"),
    # 21. G1, S, G2, M
    (21, "G1", "Growth 1: cell grows to mature size; longest phase; centrioles replicate at the end", "L4, slide 55"),
    (21, "S phase", "Synthesis: DNA replication", "L4, slide 56"),
    (21, "G2", "Final preparation / housekeeping before mitosis", "L4, slide 57"),
    (21, "M phase", "Mitosis: the cell divides", "L4, slide 58"),
    # 22. Germinating layer
    (22, "Stratum germinativum", "Another name for the stratum basale; makes new cells", "L6, slides 28, 33"),
    (22, "Stratum basale cells are doing…", "Mitosis (constantly dividing)", "L6, slide 33"),
    (22, "Direction the epidermis grows", "From the bottom up", "L6, slide 35"),
    (22, "Stratum basale cell shape", "Cuboidal (to columnar)", "L6, slide 33"),
    # 23. Fingerprints
    (23, "What forms fingerprints?", "Dermal papillae of the papillary layer", "L6, slide 39"),
    (23, "Fingerprint ridges help with…", "Friction for gripping", "L6, slide 39"),
    (23, "Dermal papillae also…", "Bring capillaries close to the epidermis; house touch receptors", "L6, slide 39"),
    # 24. Goblet cells
    (24, "Goblet cells", "Cup-shaped cells that secrete MUCUS", "L5, slide 27"),
    (24, "Epithelia with goblet cells", "Simple columnar and pseudostratified columnar", "L5, slides 27, 30"),
    (24, "Goblet cells in the airway", "Mucus traps dust; cilia sweep it away", "L5, slide 30"),
    # 25. Cytosol, nucleus, ribosomes, ER
    (25, "Cytosol", "Watery portion of the cytoplasm (the 'Jello')", "L4, slide 4"),
    (25, "Nucleus", "Contains DNA; the cell's 'brain'; surrounded by the nuclear envelope", "L4, slides 6–7"),
    (25, "Rough ER", "Studded with ribosomes; makes proteins", "L4, slide 14"),
    (25, "Smooth ER", "No ribosomes; makes lipids and carbs, breaks down drugs", "L4, slide 14"),
    (25, "Anucleate / binucleate / multinucleate", "No nucleus (RBC) / 2 nuclei / 3+ nuclei", "L4, slide 6"),
]
