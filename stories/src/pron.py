"""Pronunciation fixes: IPA for words the default phonemizer gets wrong.
Used by build_story.py on the spoken text only."""
import re
IPA = {
 "abdominopelvic": "æbdˌɑːmɪnoʊpˈɛlvɪk", "acetylcholine": "əsˌiːɾəlkˈoʊliːn", "acromegaly": "ˌækɹoʊmˈɛɡəli",
 "adenosine": "ədˈɛnəsˌiːn", "antebrachial": "ˌæntibɹˈeɪkiəl", "brachial": "bɹˈeɪkiəl",
 "apocrine": "ˈæpəkɹɪn", "eccrine": "ˈɛkɹɪn", "exocrine": "ˈɛksəkɹɪn", "basale": "bəsˈeɪli",
 "biaxial": "baɪˈæksiəl", "bilayer": "bˈaɪleɪɚ", "calcaneal": "kælkˈeɪniəl", "calcaneus": "kælkˈeɪniəs",
 "calcitonin": "kˌælsɪtˈoʊnɪn", "capitis": "kˈæpɪɾɪs", "carpometacarpal": "kˌɑːɹpoʊmˌɛɾəkˈɑːɹpəl",
 "columnar": "kəlˈʌmnɚ", "conchae": "kˈɑːŋkiː", "condyle": "kˈɑːndaɪl", "condyles": "kˈɑːndaɪlz",
 "condyloid": "kˈɑːndɪlˌɔɪd", "epicondyle": "ˌɛpɪkˈɑːndaɪl", "epicondyles": "ˌɛpɪkˈɑːndaɪlz",
 "corneum": "kˈɔːɹniəm", "cuneiforms": "kjuːnˈiːəfˌɔːɹmz", "dermis": "dˈɜːmɪs", "diaphysis": "daɪˈæfɪsɪs",
 "disaccharides": "daɪsˈækəɹˌaɪdz", "monosaccharides": "mˌɑːnoʊsˈækəɹˌaɪdz", "polysaccharides": "pˌɑːlisˈækəɹˌaɪdz",
 "distal": "dˈɪstəl", "epiphyseal": "ɪpˌɪfɪsˈiːəl", "epiphyses": "ɪpˈɪfɪsˌiːz",
 "erythropoietin": "ɪɹˌɪθɹoʊpˈɔɪɪtɪn", "exocytosis": "ˌɛksoʊsaɪtˈoʊsɪs", "fascia": "fˈæʃiə",
 "foramen": "fɚɹˈeɪmən", "foramina": "fɚɹˈæmɪnə", "glycogenolysis": "ɡlˌaɪkoʊdʒənˈɑːlɪsɪs",
 "granulosum": "ɡɹˌænjʊlˈoʊsəm", "hemidesmosomes": "hˌɛmidˈɛzməsˌoʊmz", "hemidesmosome": "hˌɛmidˈɛzməsˌoʊm",
 "homeostasis": "hˌoʊmioʊstˈeɪsɪs", "intramembranous": "ˌɪntɹəmˈɛmbɹənəs", "lacunae": "ləkjˈuːniː",
 "lamellae": "ləmˈɛliː", "lucidum": "lˈuːsɪdəm", "mediastinum": "mˌiːdiəstˈaɪnəm", "medulla": "mɪdˈʌlə",
 "meniscus": "mɪnˈɪskəs", "mortis": "mˈɔːɹɾɪs", "nociceptors": "nˌoʊsɪsˈɛptɚz",
 "norepinephrine": "nˌɔːɹɛpɪnˈɛfɹɪn", "nuclei": "nˈuːkliaɪ", "obturator": "ˈɑːbtʃɚɹˌeɪɾɚ",
 "odontoid": "oʊdˈɑːntɔɪd", "olecranal": "oʊlˈɛkɹənəl", "olecranon": "oʊlˈɛkɹənˌɑːn",
 "osteoblasts": "ˈɑːstiəblˌæsts", "osteoblast": "ˈɑːstiəblˌæst", "osteoclasts": "ˈɑːstiəklˌæsts",
 "osteoclast": "ˈɑːstiəklˌæst", "osteomalacia": "ˌɑːstioʊməlˈeɪʃə", "osteoporosis": "ˌɑːstioʊpɚɹˈoʊsɪs",
 "osteoprogenitor": "ˌɑːstioʊpɹoʊdʒˈɛnɪɾɚ", "patellar": "pətˈɛlɚ", "periosteum": "pˌɛɹiˈɑːstiəm",
 "periosteum's": "pˌɛɹiˈɑːstiəmz", "peroxisomes": "pɚɹˈɑːksɪsˌoʊmz", "phalanges": "fəlˈændʒiːz",
 "pleurae": "plˈʊɹiː", "polymerase": "pəlˈɪmɚɹˌeɪs", "popliteal": "pˌɑːplɪtˈiːəl", "prolactin": "pɹoʊlˈæktɪn",
 "sarcolemma": "sˌɑːɹkəlˈɛmə", "spinosum": "spaɪnˈoʊsəm", "synchondroses": "sˌɪŋkɑːndɹˈoʊsiːz",
 "syndesmoses": "sˌɪndɛzmˈoʊsiːz", "talocrural": "tˌeɪloʊkɹˈʊɹəl", "trabeculae": "tɹəbˈɛkjʊliː",
 "triquetrum": "tɹaɪkwˈiːtɹəm", "trochanter": "tɹoʊkˈæntɚ", "tropomyosin": "tɹˌoʊpəmˈaɪəsɪn",
 "troponin": "tɹˈoʊpənɪn", "wolff's": "wˈʊlfs",
 "amphiarthrotic": "ˌæmfiɑːɹθɹˈɑːɾɪk",
 "angiotensin": "ˌændʒioʊtˈɛnsɪn",
 "aspera": "ˈæspɚɹə",
 "avascular": "eɪvˈæskjʊlɚ",
 "calciferol": "kælsˈɪfɚɹˌɔːl",
 "cholecalciferol": "kˌoʊləkælsˈɪfɚɹˌɔːl",
 "cisternae": "sɪstˈɜːniː",
 "comminuted": "kˈɑːmɪnˌuːɾɪd",
 "covalent": "koʊvˈeɪlənt",
 "creatine": "kɹˈiːətˌiːn",
 "diarthrotic": "dˌaɪɑːɹθɹˈɑːɾɪk",
 "endochondral": "ˌɛndoʊkˈɑːndɹəl",
 "epiglottis": "ˌɛpɪɡlˈɑːɾɪs",
 "glenohumeral": "ɡlˌiːnoʊhjˈuːmɚɹəl",
 "gonadotropins": "ɡoʊnˌædəɹtɹˈoʊpɪnz",
 "hypertrophy": "haɪpˈɜːtɹəfi",
 "incus": "ˈɪŋkəs",
 "labrum": "lˈeɪbɹəm",
 "langerhans": "lˈɑːŋɚhˌɑːnz",
 "lunula": "lˈuːnjʊlə",
 "meatus": "miˈeɪɾəs",
 "papillae": "pəpˈɪliː",
 "parietal": "pəɹˈaɪəɾəl",
 "parietals": "pəɹˈaɪəɾəlz",
 "piriformis": "pˌɪɹɪfˈɔːɹmɪs",
 "prophase": "pɹˈoʊfeɪz",
 "metaphase": "mˈɛɾəfˌeɪz",
 "symphyses": "sˈɪmfɪsˌiːz",
 "trochlea": "tɹˈɑːkliə",
 "trochlear": "tɹˈɑːkliɚ",
 "thymine": "θˈaɪmiːn",
 "trachea": "tɹˈeɪkiə",
 "tracheal": "tɹˈeɪkiəl",
 "stapes": "stˈeɪpiːz",
 "squamous": "skwˈeɪməs",
 "serous": "sˈɪɹəs",
 "nucleic": "nuːklˈeɪɪk",
 "patella": "pətˈɛlə",
 "meissner's": "mˈaɪsnɚz",
 "krause": "kɹˈaʊz",
 "lysis": "lˈaɪsɪs",
 "atp": "ˌeɪtˌiːpˈiː", "pth": "ˌpiːˌtiːˈeɪtʃ", "epo": "ˌiːˌpiːˈoʊ", "adh": "ˌeɪˌdiːˈeɪtʃ",
 "adp": "ˌeɪdˌiːpˈiː",
 "er": "ˌiːˈɑːɹ",
 "ism": "ˌaɪˌɛsˈɛm",
}
_RX = re.compile(r"(?<![A-Za-z'])(" + "|".join(sorted(map(re.escape, IPA), key=len, reverse=True)) + r")(?![A-Za-z'])", re.I)

def to_phonemes(text, phonemize):
    """Return a phoneme string with dictionary words swapped in, or None if no word matched."""
    parts = _RX.split(text)
    if len(parts) == 1:
        return None
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(IPA[p.lower()])
        elif p.strip():
            out.append(phonemize(p).strip())
    return " ".join(x for x in out if x)
