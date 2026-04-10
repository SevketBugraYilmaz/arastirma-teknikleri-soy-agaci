import matplotlib.pyplot as plt
import networkx as nx

def draw_colored_perfect_tree():
    G = nx.DiGraph()
    
     
    edges = [
        ("ARAŞTIRMA\nTEKNİKLERİ", "A. HAZIRLIK\nSÜRECİ"),
        ("ARAŞTIRMA\nTEKNİKLERİ", "B. ARAŞTIRMA\nSÜRECİ"),
        ("ARAŞTIRMA\nTEKNİKLERİ", "C. DEĞERLENDİRME\nSÜRECİ"),
        ("ARAŞTIRMA\nTEKNİKLERİ", "D. YAZIM\nSÜRECİ"),
        
        
        ("A. HAZIRLIK\nSÜRECİ", "Konu Belirleme\nSüreci"),
        ("A. HAZIRLIK\nSÜRECİ", "Okumalar"),
        ("Okumalar", "Kaynak Tespiti &\nMerkezler"), 
        ("Okumalar", "Literatür Tespiti"),
        ("A. HAZIRLIK\nSÜRECİ", "Sınırlandırma &\nSüre"),
        ("A. HAZIRLIK\nSÜRECİ", "Geçici Plan"),
        
        
        ("B. ARAŞTIRMA\nSÜRECİ", "Konuya Dair\nKaynak Araştırma"),
        ("Konuya Dair\nKaynak Araştırma", "Arşivler"), 
        ("Konuya Dair\nKaynak Araştırma", "Süreli\nYayınlar"), 
        ("Konuya Dair\nKaynak Araştırma", "Değerlendirme\nEserler"),
        ("Değerlendirme\nEserler", "Kitaplar"), 
        ("Değerlendirme\nEserler", "Anılar"),
        ("B. ARAŞTIRMA\nSÜRECİ", "Kaynakların\nToplanması"),
        ("Kaynakların\nToplanması", "Arşiv Belgeleri"), 
        ("Kaynakların\nToplanması", "Süreli\nYayınlar "), 
        ("Kaynakların\nToplanması", "Değerlendirme\nEserler "),
        
        
        ("C. DEĞERLENDİRME\nSÜRECİ", "Arşiv\nMalzemeleri"),
        ("C. DEĞERLENDİRME\nSÜRECİ", "Süreli\nYayınlar  "),
        ("C. DEĞERLENDİRME\nSÜRECİ", "Kitap ve Anı\nEserleri"),
        ("Arşiv\nMalzemeleri", "Kataloglama\n(Arşiv)"), ("Arşiv\nMalzemeleri", "Fişleme\n(Arşiv)"),
        ("Süreli\nYayınlar  ", "Kataloglama\n(Basın)"), ("Süreli\nYayınlar  ", "Fişleme\n(Basın)"),
        ("Kitap ve Anı\nEserleri", "Kataloglama\n(Eser)"), ("Kitap ve Anı\nEserleri", "Fişleme\n(Eser)"),
        
        
        ("D. YAZIM\nSÜRECİ", "Bölümler"),
        ("Bölümler", "Katalog ve Fiş\nYararlanma"), ("Bölümler", "Yeni Materyal\nKullanımı"),
        ("D. YAZIM\nSÜRECİ", "Yazım Kuralları"),
        ("Yazım Kuralları", "Katalog/Fiş\nKullanım Şekli"), ("Yazım Kuralları", "Alıntıların\nVerilmesi"),
        ("D. YAZIM\nSÜRECİ", "Dipnotlama\nTeknikleri"),
        ("D. YAZIM\nSÜRECİ", "Sonuç Bölümü"),
        ("D. YAZIM\nSÜRECİ", "Kaynakça\nOluşturma"),
        ("D. YAZIM\nSÜRECİ", "Önsöz/Giriş/Ekler")
    ]
    
    G.add_edges_from(edges)

    
    a_nodes = [node for node in G.nodes if "A. " in node or node in ["Konu Belirleme\nSüreci", "Okumalar", "Kaynak Tespiti &\nMerkezler", "Literatür Tespiti", "Sınırlandırma &\nSüre", "Geçici Plan"]]
    b_nodes = [node for node in G.nodes if "B. " in node or node in ["Konuya Dair\nKaynak Araştırma", "Arşivler", "Süreli\nYayınlar", "Değerlendirme\nEserler", "Kitaplar", "Anılar", "Kaynakların\nToplanması", "Arşiv Belgeleri", "Süreli\nYayınlar ", "Değerlendirme\nEserler "]]
    c_nodes = [node for node in G.nodes if "C. " in node or node in ["Arşiv\nMalzemeleri", "Süreli\nYayınlar  ", "Kitap ve Anı\nEserleri", "Kataloglama\n(Arşiv)", "Fişleme\n(Arşiv)", "Kataloglama\n(Basın)", "Fişleme\n(Basın)", "Kataloglama\n(Eser)", "Fişleme\n(Eser)"]]
    d_nodes = [node for node in G.nodes if "D. " in node or node in ["Bölümler", "Katalog ve Fiş\nYararlanma", "Yeni Materyal\nKullanımı", "Yazım Kuralları", "Katalog/Fiş\nKullanım Şekli", "Alıntıların\nVerilmesi", "Dipnotlama\nTeknikleri", "Sonuç Bölümü", "Kaynakça\nOluşturma", "Önsöz/Giriş/Ekler"]]

    color_map = []
    for node in G.nodes:
        if node == "ARAŞTIRMA\nTEKNİKLERİ": color_map.append("lightgray")
        elif node in a_nodes: color_map.append("#FFFF99") 
        elif node in b_nodes: color_map.append("#FF9999") 
        elif node in c_nodes: color_map.append("#99CCFF") 
        elif node in d_nodes: color_map.append("#FFCC99") 
        else: color_map.append("white")

    
    pos = {
        "ARAŞTIRMA\nTEKNİKLERİ": (0, 20),
        "A. HAZIRLIK\nSÜRECİ": (-45, 15), "B. ARAŞTIRMA\nSÜRECİ": (-15, 15), 
        "C. DEĞERLENDİRME\nSÜRECİ": (15, 15), "D. YAZIM\nSÜRECİ": (45, 15),
        "Konu Belirleme\nSüreci": (-54, 10), "Okumalar": (-48, 10), "Sınırlandırma &\nSüre": (-42, 10), "Geçici Plan": (-36, 10),
        "Kaynak Tespiti &\nMerkezler": (-50, 5), "Literatür Tespiti": (-46, 5),
        "Konuya Dair\nKaynak Araştırma": (-22, 10), "Kaynakların\nToplanması": (-8, 10),
        "Arşivler": (-26, 5), "Süreli\nYayınlar": (-22, 5), "Değerlendirme\nEserler": (-18, 5),
        "Kitaplar": (-20, 0), "Anılar": (-16, 0),
        "Arşiv Belgeleri": (-12, 5), "Süreli\nYayınlar ": (-8, 5), "Değerlendirme\nEserler ": (-4, 5),
        "Arşiv\nMalzemeleri": (5, 10), "Süreli\nYayınlar  ": (15, 10), "Kitap ve Anı\nEserleri": (25, 10),
        "Kataloglama\n(Arşiv)": (3, 5), "Fişleme\n(Arşiv)": (7, 5),
        "Kataloglama\n(Basın)": (13, 5), "Fişleme\n(Basın)": (17, 5),
        "Kataloglama\n(Eser)": (23, 5), "Fişleme\n(Eser)": (27, 5),
        "Bölümler": (35, 10), "Yazım Kuralları": (43, 10), "Dipnotlama\nTeknikleri": (50, 10), 
        "Sonuç Bölümü": (56, 10), "Kaynakça\nOluşturma": (62, 10), "Önsöz/Giriş/Ekler": (68, 10),
        "Katalog ve Fiş\nYararlanma": (33, 5), "Yeni Materyal\nKullanımı": (37, 5),
        "Katalog/Fiş\nKullanım Şekli": (41, 5), "Alıntıların\nVerilmesi": (45, 5)
    }

    plt.figure(figsize=(90, 35))
    nx.draw(G, pos, with_labels=True, node_size=16500, node_color=color_map, 
            node_shape="s", edgecolors="black", linewidths=2.5, font_size=13, 
            font_weight="bold", edge_color="gray", arrows=True, arrowsize=35)
    
    plt.title("Araştırma Teknikleri Soy Ağacı ", size=35, pad=60)
    plt.show()

draw_colored_perfect_tree()
