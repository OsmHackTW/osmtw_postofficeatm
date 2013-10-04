osmtw_postofficeatm
===================
資料來源為 dat.gov.tw 的中華郵政公司郵務業務全國郵局 ATM 位址[1]，檢查方法是利用 data.gov.tw 的 CSV 檔案中的經緯度，去查詢 OpenStreetMap 鄰近是否已經有人編輯 ATM[2]。

結果是全國郵局 ATM 位址中的經緯度是不可靠的。例如臺灣大學校內幾個 ATM 位址，明顯有誤。

* 如臺大郵局位於小福樓， CSV 的經緯度顯示為 25.017169999999997,121.53365)，接近校門。
* 另外如臺大大一女生宿舍餐廳門口旁 ATM，亦錯誤顯示為臺大校門口。
* 至於離島如馬祖等，GPS 位址則被列於海上。

因此我們無法直接將該筆資料匯入 OpenStreetMap 的圖資。只能可以用補足已經上傳之資料[3]。

 [1] 政府資料開放平臺>資料分類>服務分類>交通及通訊>rawData <http://data.gov.tw/opendata/Details?sno=315830000M-00004>
 [2] Tag:amenity=atm - OpenStreetMap Wiki <http://wiki.openstreetmap.org/wiki/Atm>
 [3] OpenStreetMap | 變更組合 | 18146099 <http://www.openstreetmap.org/browse/changeset/18146099>
