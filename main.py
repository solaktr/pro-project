meme_dict = {
            "CRINGE": "GARİP YA DA UTANDIRICI BİR ŞEY",
            "LOL": "KOMİK BİR ŞEYE VERİLEN CEVAP",
            }

kelime = input("anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_dict.keys():
     print(meme_dict[kelime])
else:
    print("henüz bu kelimeye sahip değiliz... ama üzerinde çalışıyoruz!")
