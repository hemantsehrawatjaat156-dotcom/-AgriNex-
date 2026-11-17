"""
Indian Crop Disease & Health Solutions Knowledgebase
Comprehensive Organic, Chemical, and Cultural Remedies for Indian Farmers
"""

INDIAN_CROP_SOLUTIONS = {
    "Wheat_Yellow_Rust": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Yellow Rust / Stripe Rust (पीला रतुआ)",
        "scientific_name": "Puccinia striiformis f. sp. tritici",
        "category": "Fungal Disease (फफूंद जनित रोग)",
        "severity": "High (गंभीर)",
        "severity_color": "danger",
        "description": "Yellow rust is a devastating fungal disease characterized by bright yellow, powdery pustules arranged in prominent linear stripes along leaf veins. Spores spread rapidly in cool, humid morning conditions.",
        "symptoms": [
            "Yellow to orange-yellow powdery pustules forming parallel stripes on leaf blades",
            "Yellow powder easily rubs off on fingers or white cloth",
            "Leaves turn brown and dry prematurely, reducing grain filling by up to 50%",
            "Severe infection spreads to leaf sheaths and ears (spikes)"
        ],
        "organic_remedies": [
            "Foliar spray of cold-pressed Neem Oil (1500 ppm) @ 5 ml per litre of water with a mild surfactant (liquid soap).",
            "Spray fermented sour buttermilk (खट्टी छाछ) @ 5 litres mixed with 150 litres water per acre to inhibit fungal spore germination.",
            "Soil application of Trichoderma viride or T. harzianum @ 2.5 kg mixed with 100 kg well-rotted cow dung manure per acre at sowing.",
            "Spray Cow Urine (गोमूत्र) @ 10% dilution (1 litre cow urine in 10 litres water) as a natural immune booster."
        ],
        "chemical_remedies": [
            "Propiconazole 25% EC (Tilt / Bumper / Radar) @ 200 ml mixed in 200 litres of water per acre at the first appearance of yellow stripes.",
            "Tebuconazole 25.9% EC (Folicur) @ 200 ml in 200 litres of water per acre for strong curative action.",
            "Azoxystrobin 18.2% + Difenoconazole 11.4% SC (Amistar Top) @ 200 ml per acre for persistent protection.",
            "Repeat chemical spray after 12-15 days if cool, cloudy weather persists."
        ],
        "farm_management": [
            "Halt excessive irrigation; avoid evening watering to minimize leaf wetness duration.",
            "Avoid excessive urea / nitrogenous fertilizer application (excess nitrogen makes crop foliage tender and susceptible to rust).",
            "Plant resistant wheat varieties recommended for your zone (e.g., HD-3086, PBW-725, DBW-187, DBW-222).",
            "Destroy wild grasses and volunteer wheat plants along field borders that harbor overwintering rust spores."
        ]
    },
    "Wheat_Brown_Rust": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Brown Rust / Leaf Rust (भूरा रतुआ)",
        "scientific_name": "Puccinia triticina",
        "category": "Fungal Disease (फफूंद जनित रोग)",
        "severity": "Moderate to High (मध्यम से गंभीर)",
        "severity_color": "warning",
        "description": "Brown rust produces small, round to oval, dark brownish-orange pustules scattered randomly over the upper surface of leaf blades. It appears later in the season as temperatures rise (20-25°C).",
        "symptoms": [
            "Small, scattered circular orange-brown pustules on upper leaf surface (not in linear stripes)",
            "Pustules turn dark brown to black as crop matures (teliospore stage)",
            "Premature drying and defoliation of flag leaves, reducing 1000-grain weight",
            "Spreads rapidly under warm, sunny days and cool nights with dew"
        ],
        "organic_remedies": [
            "Spray Neem Seed Kernel Extract (NSKE 5%) @ 25 kg kernel extract in 500 litres water per 2.5 acres.",
            "Bio-fungicide spray of Bacillus subtilis (Serenade) @ 2 ml per litre water.",
            "Foliar application of Jeevamrit (जीवामृत) @ 10% dilution to strengthen natural plant immunity."
        ],
        "chemical_remedies": [
            "Mancozeb 75% WP (Dithane M-45 / Indofil M-45) @ 600-800 grams in 200 litres of water per acre as a protectant spray.",
            "Propiconazole 25% EC @ 200 ml per acre at initial symptom onset.",
            "Hexaconazole 5% EC (Contaf) @ 300 ml in 200 litres water per acre."
        ],
        "farm_management": [
            "Maintain optimal plant spacing to allow adequate sunlight penetration and airflow.",
            "Balanced fertilizer application: ensure adequate potassium (MOP - Muriate of Potash) to build strong leaf cell walls.",
            "Early sowing in the first fortnight of November to avoid late-season high temperature rust pressure."
        ]
    },
    "Wheat_Foliar_Blight": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Foliar Blight / Spot Blotch (पत्ती झुलसा रोग)",
        "scientific_name": "Bipolaris sorokiniana (Helminthosporium)",
        "category": "Fungal Disease (फफूंद जनित रोग)",
        "severity": "Moderate to High (मध्यम से गंभीर)",
        "severity_color": "warning",
        "description": "Spot blotch / leaf blight causes small oval-to-elliptical brownish lesions that enlarge and coalesce into large necrotic blighted patches, especially prominent during the post-flowering grain-filling stage in warm regions.",
        "symptoms": [
            "Small oval dark brown spots on lower leaves with chlorotic yellow margins",
            "Spots merge together forming large irregular scorched, dead leaf patches",
            "Blackish fungal growth visible on lesions under humid weather",
            "Infected seed heads produce shriveled, discolored black-point grains"
        ],
        "organic_remedies": [
            "Seed treatment with Trichoderma harzianum @ 8-10 grams per kg of wheat seed before sowing.",
            "Foliar application of Copper Soap or Bordeaux Mixture (1%) at early heading stage.",
            "Spray Garlic + Neem leaf extract (5%) as a broad-spectrum natural anti-fungal."
        ],
        "chemical_remedies": [
            "Tebuconazole 50% + Trifloxystrobin 25% WG (Nativo) @ 120 grams in 200 litres of water per acre.",
            "Carbendazim 12% + Mancozeb 63% WP (Saaf / Sixer) @ 400-500 grams in 200 litres water per acre.",
            "Propiconazole 25% EC @ 200 ml in 200 litres water per acre."
        ],
        "farm_management": [
            "Deep summer ploughing to bury crop residues harboring fungus.",
            "Use certified disease-free, seed-treated wheat seed.",
            "Avoid water stagnation in fields after flowering."
        ]
    },
    "Wheat_Powdery_Mildew": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Powdery Mildew (चूर्णिल आसिता रोग)",
        "scientific_name": "Blumeria graminis f. sp. tritici",
        "category": "Fungal Disease (फफूंद जनित रोग)",
        "severity": "Moderate (मध्यम)",
        "severity_color": "info",
        "description": "Characterized by white, fluffy, cottony fungal patches on leaf surfaces, stems, and heads. In severe cases, the entire canopy appears as if dusted with white talcum powder.",
        "symptoms": [
            "White, cottony powder patches on lower leaves progressing up the plant",
            "Patches turn dull grayish-brown with tiny black dots (cleistothecia)",
            "Infected leaves turn yellow, wither, and die prematurely",
            "Poor head development and unfilled grains"
        ],
        "organic_remedies": [
            "Wettable Sulfur (Sulfur 80% WDG) @ 2 to 3 grams per litre of water.",
            "Baking soda (Sodium bicarbonate) spray @ 5 grams + 2 ml liquid soap per litre of water.",
            "Milk spray (1 part milk : 9 parts water) creates natural antiseptic film on leaf surfaces."
        ],
        "chemical_remedies": [
            "Propiconazole 25% EC @ 200 ml per acre in 200 litres of water.",
            "Triadimefon 25% WP (Bayleton) @ 150-200 grams in 200 litres water per acre.",
            "Hexaconazole 5% SC @ 300 ml per acre."
        ],
        "farm_management": [
            "Avoid dense sowing; maintain recommended seed rate of 40 kg/acre.",
            "Ensure proper drainage so soil does not stay overly damp in shady tree borders.",
            "Do not over-apply nitrogenous fertilizers."
        ]
    },
    "Moisture_Waterlogging_Stress": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Waterlogging & Poor Drainage Stress (जलभराव व अत्यधिक नमी)",
        "scientific_name": "Abiotic Root Hypoxia (अजैविक जड़ हाइपोक्सिया)",
        "category": "Abiotic Environmental Stress (अजैविक तनाव)",
        "severity": "High (गंभीर)",
        "severity_color": "danger",
        "description": "Excess standing water or poor soil drainage displaces oxygen in soil pores, suffocating wheat roots. Wheat is highly sensitive to water stagnation, resulting in root rot, yellowing of lower foliage, and stunted tillers.",
        "symptoms": [
            "General yellowing (chlorosis) beginning uniformly on lower canopy leaves",
            "Roots turn dark brown, mushy, and foul-smelling instead of fibrous white",
            "Plants appear stunted with thin, fragile tillers",
            "Standing muddy water or crusty waterlogged soil surface"
        ],
        "organic_remedies": [
            "Aerate soil surface by shallow inter-cultivation (hoeing / गुड़ाई) as soon as soil is workable.",
            "Soil drenching around root zone with Trichoderma viride @ 2.5 kg/acre to protect oxygen-starved roots from opportunistic soil rots.",
            "Apply well-decomposed vermicompost (500 kg/acre) to restore beneficial soil aerobic microbes."
        ],
        "chemical_remedies": [
            "DO NOT SPRAY FUNGICIDES on leaves unless secondary fungal infection is confirmed; chemical sprays on waterlogged plants increase phytotoxic stress.",
            "Foliar spray of 19:19:19 (NPK water soluble fertilizer) @ 1 kg in 100 litres water per acre once water drains to bypass damaged roots and provide immediate nutrition.",
            "If root rot develops, apply Carbendazim 50% WP @ 2 grams per litre water as drench."
        ],
        "farm_management": [
            "IMMEDIATE ACTION: Dig surface drainage channels (नाली) to drain out standing water within 24 hours.",
            "Construct raised beds or broad-bed furrows (BBF) in fields prone to water stagnation.",
            "Avoid flood irrigation; switch to sprinkler or furrow irrigation on laser-leveled fields."
        ]
    },
    "Wheat_Lodging_Damage": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Crop Lodging & Wind-Rain Damage (फसल का गिरना / झुकना)",
        "scientific_name": "Mechanical / Weather Abiotic Damage",
        "category": "Abiotic Mechanical Damage (प्राकृतिक क्षति)",
        "severity": "High (गंभीर)",
        "severity_color": "danger",
        "description": "Heavy rainfall, hail, or high-velocity winds causing wheat stems to bend or break at the base, flattening the crop canopy to the ground and exposing grains to moisture damage.",
        "symptoms": [
            "Wheat plants flattened and resting directly on the soil surface",
            "Bent or buckled lower stem internodes",
            "Damp microclimate at soil level leading to earhead mold and sprouted grains",
            "Difficulty during mechanical combine harvesting"
        ],
        "organic_remedies": [
            "Spray silica-rich rice husk ash extract or potassium silicate (2 ml/litre) at tillering to strengthen stem lignification.",
            "Apply Bio-Potash to enhance straw strength and stem rigidity."
        ],
        "chemical_remedies": [
            "Prophylactic spray of Mancozeb 75% WP @ 600 grams/acre if flattened crop is moist, to prevent secondary ear mold (Fusarium/Aspergillus).",
            "Apply Chlormequat chloride (Cycocel / Lihocin) @ 1.5 to 2.0 ml per litre water at first node stage in tall varieties to reduce internode length."
        ],
        "farm_management": [
            "Do not irrigate wheat crop when strong winds (> 20 km/h) are forecasted.",
            "Avoid excess nitrogen fertilizers which produce tall, weak, spongy stems.",
            "Drain any ponded water immediately to prevent grains from rotting on wet soil."
        ]
    },
    "Nutrient_Deficiency_Chlorosis": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Nitrogen / Zinc Nutrient Deficiency (पोषक तत्वों की कमी)",
        "scientific_name": "Nutritional Physiological Disorder",
        "category": "Nutritional Disorder (पोषक तत्व विकार)",
        "severity": "Mild to Moderate (हल्का से मध्यम)",
        "severity_color": "info",
        "description": "Lack of essential macro- or micro-nutrients (especially Nitrogen or Zinc) in alkaline or sandy soils, causing leaf chlorosis, pale yellowish foliage, and poor tillering.",
        "symptoms": [
            "Nitrogen deficiency: Uniform pale yellow-green color starting from tips of oldest leaves",
            "Zinc deficiency: White or yellow broad chlorotic bands on both sides of midrib on younger leaves (खैरा लक्षण)",
            "Stunted growth, delayed heading, and reduced earhead size"
        ],
        "organic_remedies": [
            "Foliar spray of enriched Cow Dung Wash or Panchagavya @ 3% (30 ml per litre water).",
            "Application of well-composted farmyard manure (FYM) @ 5 tonnes/acre before sowing.",
            "Foliar spray of Seaweed extract @ 2 ml per litre water for rapid micronutrient uptake."
        ],
        "chemical_remedies": [
            "For Nitrogen: Spray Urea (2% solution = 2 kg urea dissolved in 100 litres water per acre).",
            "For Zinc: Spray Zinc Sulphate (21% heptahydrate) @ 1 kg + 0.5 kg unslaked lime (चूना) in 200 litres water per acre.",
            "Spray water-soluble Chelated Zinc (Zn-EDTA 12%) @ 1 gram per litre of water for fast absorption."
        ],
        "farm_management": [
            "Conduct soil test to determine specific nutrient deficiencies before fertilizer application.",
            "Apply zinc sulphate (25 kg/acre) as basal dose once every 2-3 years at land preparation.",
            "Split nitrogen doses: 1/2 at sowing, 1/4 at first irrigation (CRI stage), and 1/4 at second irrigation."
        ]
    },
    "Healthy_Wheat_Crop": {
        "crop_name": "Wheat (गेहूँ)",
        "condition_name": "Healthy Wheat Crop (स्वस्थ गेहूँ की फसल)",
        "scientific_name": "Triticum aestivum - Optimal Health",
        "category": "Healthy / Non-Diseased (स्वस्थ फसल)",
        "severity": "Healthy (उत्कृष्ट स्वास्थ्य)",
        "severity_color": "success",
        "description": "The wheat crop displays excellent physiological vigor, deep emerald green foliage, sturdy upright tillers, and healthy root development with zero visible signs of fungal or bacterial pathogen damage.",
        "symptoms": [
            "Vibrant, uniform dark green leaf color across the entire canopy",
            "Erect, sturdy tillers with strong stem internodes",
            "Clean leaf surfaces without rust pustules, spots, or powdery mildew",
            "Strong, white fibrous root system and normal development stage"
        ],
        "organic_remedies": [
            "Continue routine preventative application of Jeevamrit (जीवामृत) with irrigation water every 20-25 days.",
            "Spray Seaweed Extract or Humic Acid (12%) @ 2 ml/litre at flag leaf stage to support optimal grain formation."
        ],
        "chemical_remedies": [
            "No chemical fungicide or pesticide spray is needed at this stage.",
            "Maintain standard fertility schedule: Apply 0:52:34 (Monopotassium phosphate) @ 1 kg/acre at boot leaf stage to enhance grain filling."
        ],
        "farm_management": [
            "Maintain scheduled light irrigation at critical crop stages (Crown Root Initiation - 21 DAS, Tillering - 40 DAS, Booting - 60 DAS, Milking - 85 DAS).",
            "Scout field borders weekly during cool, dewy mornings to detect any early signs of yellow rust early.",
            "Keep field borders clean of weeds."
        ]
    }
}

CLASS_NAMES = list(INDIAN_CROP_SOLUTIONS.keys())
