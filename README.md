# PyQt4 Graphics
## Qt Designer ile Form oluşturma
Qt Designer ile bir form oluşturuyoruz<br>
![Qt Designer Form](https://github.com/urkera/PyQt4-Graphics/blob/master/images/00%20Qt%20Designer%20-%20Create%20Window.PNG)<br>
(Resim 1)<br>
![Qt Designer Form](https://github.com/urkera/PyQt4-Graphics/blob/master/images/01%20Qt%20Designer%20-%20Main%20Window.PNG)<br>
(Resim 2)<br>
Forma varsayılan olarak eklenen statusbar ve menubar'ı siliyoruz bunlarla işimiz yok. Daha sonra oluşturduğumuz forma Widget Box kısmından GraphicsView ekliyoruz ve formu Layout Vertically butonuna basarak içindeki nesneler alt alta ve formun tümünü kaplayacak şekilde düzenlenmesini sağlıyoruz.<br>
Sonuç aşağıdaki gibi olacaktır.<br>
![Qt Designer Form](https://github.com/urkera/PyQt4-Graphics/blob/master/images/02%20Qt%20Designer%20-%20Graphicsview.PNG)<br>
(Resim 3)<br>
Dosyayı form.ui ismiyle kaydediyoruz.<br>
## pyuic4
CMD ile kaydettiğimiz konuma giderek yada benim yaptığım gibi windows explorer üzerinden "pyuic4 form.ui -x -o form.py" komutuyla python scripti haline çeviriyoruz.<br>
![pyuic4](https://github.com/urkera/PyQt4-Graphics/blob/master/images/03%20pyuic4.png)<br>
(Resim 4)<br>
Bu Komutu çalıştırdıktan sonra form.ui dosyasının yanında form.py isimli dosyamız oluşturuluyor. "form.py" dosyasını çalıştırarak Qt Designer'de oluşturduğumuz pencerenin hatasız çalışıp çalışmadığını görebilirsiniz.<br>
![form.py](https://github.com/urkera/PyQt4-Graphics/blob/master/images/04%20run%20form_py.png)<br>
(Resim 5)<br>
## GView.py
Yakınlaştırma/uzaklaştırma, sürükleme vs gibi özellikleri tanımlayabilmek için QGraphicsView'i kendi isteğimize göre özelleştirmemiz gerekiyor, bundan dolayı "GView.py" isimli bir python dosyası oluşturup kendi QGraphicsView'imizi oluşturuyoruz. (Kodlar üzerinde açıklamalar mevcut dolayısıyla tüm kodları açıklamıyorum)<br>
![GView.py](https://github.com/urkera/PyQt4-Graphics/blob/master/images/05%20GraphicsView.PNG)<br>
(Resim 6)<br>
Oluşturmuş olduğumuz MyView isimli nesneyi "form.py"de import edip varsayılan olarak QGraphicsView'e atanmış olan değişkene atıyoruz.<br>
![form.py import GView](https://github.com/urkera/PyQt4-Graphics/blob/master/images/06%20form_py%20import.PNG)<br>
(Resim 7)<br>
## main.py
pyuic ile otomatik oluşturulan form.py dosyasında çalışmaktansa kendi oluşturacağımız "main.py" isimli dosya ile çalışmak daha açık ve anlaşılır olacaktır, bu sebeple "main.py" isimli bir dosya açıp PyQt kütüphanesini ve "form.py" dosyasında işimize yarayacak nesne/fonksiyonları import ediyoruz. (Aşağıda gördüğünüz üzere gerekli yerlerde kodların ne işe yaradığı açıklanmış detaya girmiyorum)<br>
![main.py](https://github.com/urkera/PyQt4-Graphics/blob/master/images/07%20main_py.PNG)<br>
(Resim 8)<br>
## items.py PolygonItem
PyQt4'ün içinde bir çok nesne önceden tanımlanmış (QGraphicsRectItem, QGraphicsTextItem, QGraphicsLineItem...) bunları kullanabileceğimiz gibi istediğimiz gibi kendimizde türlü nesneler oluşturabiliriz. QGraphicsView (Bizim oluşturduğumuz sınıf adıyla GView) üzerinde çizim yapmak yada tanımladığımız nesneleri gösterebilmek için PyQt4'te QGraphicsItem türünde nesneler oluşturmamız gerekiyor. PolygonItem isminde kullanıcının belirlediği sayıda kenarı olan çokgenler oluşturan bir nesne tanımlayalım. Bunun için geometri bilgilerimizi kullanacağız.<br>
![Polygon](https://github.com/urkera/PyQt4-Graphics/blob/master/images/08%20Polygon.png)<br>
(Resim 9)<br>
Yukarıda gördüğümüz şekil bizim çokgen oluşturmamız için gereken temel bilgiyi aslında veriyor, ihtiyacımız olan kenar (yada köşe) sayısı ve "r" ile gösterilen değerler. Kenar sayısı ile "θ" ile gösterilen açıyı hesaplayıp daha sonra sinüs ve cosinüs fonksiyonlarını kullanarak çokgenin her köşesinin koordinatlarını hesaplayacağız. Bunun için öncelikle items.py isimli python dosyası açıp gerekli fonksiyon ve sınıfları import ederek PolygonItem ismiyle kendi nesnemizi oluşturuyoruz.(Gerekli açıklamalar kodlar üzerinde mevcut)<br>
![PolygonItem](https://github.com/urkera/PyQt4-Graphics/blob/master/images/09%20PolygonItem.PNG)<br>
(Resim 10)<br>
## PolygonItem oluşturup GraphicsView'de gösterme
main.py dosyamıza yeni oluşturduğumuz items.py dosyasından PolygonItem nesnesini import edip üçgen ve beşgen oluşturalım sonrasında da bunları ekranda görelim. Oluşturduğumuz nesneleri QGraphicsView'e değil de QGraphicsScene'ye eklediğimize dikkat edin. (QGraphicsView'i tiyatro, QGraphicsScene'yi de sahne olarak düşünebilirsiniz :) benzetmeyi ben yaptım yanlış olduysa düzeltin lütfen)<br>
![Üçgen Beşgen](https://github.com/urkera/PyQt4-Graphics/blob/master/images/10%20Add%20PolygonItem.PNG)<br>
(Resim 11)<br>
Elde ettiğimiz sonuca bakmak için main.py dosyasını çalıştıralım.<br>
![main.py üçgen beşgen](https://github.com/urkera/PyQt4-Graphics/blob/master/images/11%20main_py%20ucgen%20besgen.PNG)<br>
(Resim 12)<br>
Burada şunu sorabilirsiniz; oluşturduğumuz çokgenleri setPos(...) fonksiyonuyla belirli konumlara hangi noktası esas alınarak yerleştiriliyor? Herhangi bir köşe noktası esas alınmıyor Resim 9 a baktığınızda çok genin merkezindeki (0,0) noktası bizim setPos(...) ile belirlediğimiz noktaya taşınıyor.<br>
Şimdi de oluşturduğumuz bu şekilleri biraz renklendirelim :)<br><br>
items.py dosyasına geri dönüp PolygonItem nesnemize pen ve brush property'leri ekleyelim bu sayede oluşturacağımız çokgenlerin hangi renkte çizilip hangi renkte boyanacağını belirleyebileceğiz.<br>
![items.py pen brush](https://github.com/urkera/PyQt4-Graphics/blob/master/images/12%20PolygonItem%20Pen%20Brush.PNG)<br>
(Resim 13)<br>
Şimdi de main.py dosyasında PolygonItem oluşturduğumuz kısma gidip kırmızı ve mavi renkli kalemler (QPen) oluşturalım ve bu kalemleri üçgen ve beşgen nesnelerimize gönderelim.<br>
![main.py red_pen blue_pen](https://github.com/urkera/PyQt4-Graphics/blob/master/images/13%20red_pen%20blue_pen.PNG)<br>
(Resim 14)<br>
main.py dosyasını çalıştıralım.<br>
![main.py run red blue](https://github.com/urkera/PyQt4-Graphics/blob/master/images/14%20red%20triangle%20blue%20pentagon.PNG)<br>
(Resim 15)<br>
Sonuç tahmin ettiğimiz gibi. Şimdide kırmızı ve mavi fırçalar (QBrush) oluşturup bunları yine üçgen ve beşgen nesnelerine gönderelim.<br>
![main.py red_brush blue_brush](https://github.com/urkera/PyQt4-Graphics/blob/master/images/15%20red_brush%20blue_brush.PNG)<br>
(Resim 16)<br>
main.py dosyasını tekrar çalıştıralım.<br>
![main.py red blue polygon](https://github.com/urkera/PyQt4-Graphics/blob/master/images/16%20red%20triangle%20blue%20pentagon.PNG)<br>
(Resim 17)<br>
Ve sonuçta sadece kenarları değil içi de istediğimiz renkte olan çokgenler oluşturmuş olduk.<br>
