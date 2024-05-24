from flask import Flask
import random
import math

app = Flask(__name__)

factlist = [
    "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
    "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
    "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
    "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
    "Sosyal ağlar, dünya genelindeki insanları birbirine bağlayarak uzak mesafedeki akrabalar ve arkadaşlarla iletişim kurmayı kolaylaştırır.",
    "Sosyal medyada geçirilen fazla zaman, yüz yüze iletişimi azaltabilir ve sosyal becerilerin zayıflamasına yol açabilir.",
    "Sosyal ağlar, iş dünyasında ve kariyer gelişiminde önemli fırsatlar sunar.",
    "Sosyal medya platformları, yanlış bilgi ve dedikoduların hızla yayılmasına neden olabilir.",
    "Çoğu sosyal medya platformu, kullanıcılarına kişisel bilgilerini gizli tutma ve paylaşım kontrolü sağlama imkanı verir.",
    "Sosyal ağlar, kişisel ve profesyonel yaşamda kendini ifade etme ve görünürlüğü artırma fırsatları sunar.",
    "Sosyal medya, kullanıcıları için yaratıcı içerik oluşturma ve paylaşma fırsatları sunar.",
    "Sosyal ağlar, reklam ve pazarlama için etkili bir platform sağlar.",
    "Sosyal medya bağımlılığı, uyku düzeni ve genel sağlık üzerinde olumsuz etkilere yol açabilir.",
    "Sosyal medya, önemli sosyal ve politik hareketlerin organize edilmesine ve yayılmasına yardımcı olabilir.",
    "Sosyal medya kullanımı, bazı bireylerde depresyon ve anksiyeteye yol açabilir.",
    "Sosyal ağlar, kullanıcıların yeni bilgi ve beceriler öğrenmesine yardımcı olabilir.",
    "Sosyal medya, kişisel veri güvenliği ve gizlilik konusunda endişeler yaratabilir.",
    "Sosyal medya, sahte hesaplar ve kimlik hırsızlığı gibi güvenlik tehditleri içerebilir.",
    "Sosyal ağlar, kullanıcıların çeşitli konularda bilgi edinmelerini ve farkındalık kazanmalarını sağlar.",
    "Sosyal medya platformları, kullanıcıların kültürel ve sosyal farklılıkları keşfetmelerine olanak tanır.",
    "Sosyal medya, işletmelerin ve bireylerin geniş kitlelere ulaşmasını sağlar.",
    "Sosyal medya, gerçek zamanlı bilgi paylaşımı ve haber takibi için kullanışlı bir araçtır.",
    "Sosyal ağlar, kullanıcıların destek gruplarına ve topluluklara katılmalarını sağlar.",
    "Sosyal medya, bireylerin ve organizasyonların kriz durumlarında hızlı bir şekilde bilgi yaymalarına yardımcı olabilir.",
    "Sosyal medya platformları, kullanıcıların yaratıcı projelerini ve çalışmalarını sergilemelerine olanak tanır.",
    "Sosyal medya, kişisel markalaşma ve kariyer gelişimi için önemli bir araçtır.",
    "Sosyal ağlar, dijital pazarlama stratejilerinin önemli bir parçasıdır.",
    "Sosyal medya, kullanıcılara etkileşimli ve görsel içerik sunarak eğlenceli bir deneyim sağlar.",
    "Sosyal medya platformları, kullanıcıların çeşitli etkinliklere katılmalarına ve haber almalarına yardımcı olur.",
    "Sosyal ağlar, kullanıcıların yeni arkadaşlıklar ve profesyonel bağlantılar kurmalarını sağlar.",
    "Sosyal medya, kişisel ve profesyonel gelişim için kaynaklar ve fırsatlar sunar.",
    "Sosyal medya platformları, kullanıcıların hobilerini ve ilgi alanlarını paylaşmalarına olanak tanır.",
    "Sosyal medya, kullanıcıların çeşitli konularda geri bildirim ve yorum almasını sağlar.",
    "Sosyal ağlar, kullanıcıların çeşitli topluluklara katılmalarına ve destek bulmalarına olanak tanır.",
    "Sosyal medya platformları, kullanıcıların çevrimiçi alışveriş yapmalarına olanak tanır.",
    "Sosyal medya, kullanıcıların yerel ve küresel olaylardan haberdar olmalarını sağlar.",
    "Sosyal medya platformları, kullanıcıların seyahat ve gezi deneyimlerini paylaşmalarına olanak tanır.",
    "Sosyal ağlar, kullanıcıların sağlık ve yaşam tarzı konularında bilgi edinmelerine yardımcı olur.",
    "Sosyal medya, kullanıcıların eğitici ve öğretici içeriklere erişim sağlamalarına olanak tanır.",
    "Sosyal medya platformları, kullanıcıların müzik, film ve sanat gibi kültürel içerikleri keşfetmelerine olanak tanır.",
    "Sosyal medya, kullanıcıların çeşitli etkinlik ve organizasyonlara katılmalarını sağlar.",
    "Sosyal ağlar, kullanıcıların çeşitli konularda bilgi ve deneyim paylaşmalarına olanak tanır.",
    "Sosyal medya platformları, kullanıcıların çeşitli sosyal sorumluluk projelerine katılmalarına yardımcı olur.",
    "Sosyal medya, kullanıcıların güncel olaylar ve trendler hakkında bilgi sahibi olmalarını sağlar.",
    "Sosyal ağlar, kullanıcıların dil öğrenme ve kültürel değişim programlarına katılmalarına yardımcı olur.",
    "Sosyal medya platformları, kullanıcıların çevrimiçi topluluklara katılmalarına ve destek bulmalarına olanak tanır."
]

k = 100000
asallar = []

for a in range(2, k):
    is_asal = True
    for i in range(2, int(math.sqrt(a)) + 1): 
        if a % i == 0:
            is_asal = False
            break
    if is_asal:
        asallar.append(a)

def separate(asallar, separated="\n"):
    return separated.join(map(str, asallar))

asallar2 = separate(asallar, separated="\n")

@app.route("/")
def anasayfa():
    return '''<h1>Rastgele Gerçekler!!!</h1>                
              <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a>
              <h1>Asal Sayılar!!!</h1>                        
              <a href="/asallar">Asalları görüntüle!</a>'''

@app.route("/rastgele_gercek")
def rastgele_gercek():
    return f'''<h1>{random.choice(factlist)}</h1>  
              <a href="/rastgele_gercek">Birtane daha?</a>                                                       
              <a href="/">Geri dön?</a>'''

@app.route("/asallar")
def asallar_route():
    return f'''<h1>{asallar2}</h1>
            <a href="/">Geri dön?</a'''

if __name__ == "__main__":
    app.run(debug=True)
