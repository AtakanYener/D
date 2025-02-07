meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GOAT" : "Greatest of all time yani tüm zamanların en iyisi",
            "Based" : "Bir düşüncenin doğru olduğunu belirtmek",
            "W" : "Bir şeyi iyi olarak değerlendirmek",
            "L" : "Bir şeyi kötü olarak değerlendirmek",
            "NPC" : "Sıkıcı veya özgün olmayan insanlar için kullanılır."
            }
while True:
            for i in range(len(meme_dict)):
                        print(meme_dict[i])
            word = input("Anlamadığınız bir kelime yazın (yukarıdaki gibi yazın!): ")
            if word in meme_dict.keys():
                # Kelime eşleşiyorsa ne yapmalıyız?
                print(meme_dict[word] , "anlamına gelmektedir.")
            else:
                # Kelime eşleşmiyorsa ne yapmalıyız?
                print("böyle bir kelime yok.")
