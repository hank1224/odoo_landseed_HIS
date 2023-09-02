# docker-compose並載入addons測試的環境
注意：ARM處理器(Mac M系列)無法運行，因為套件wkhtmltopdf無法在ARM上運行([見](https://github.com/wkhtmltopdf/packaging/issues/98))

## 步驟：
1. 把需要測試的addons放入addons資料夾
2. 把addons所需的額外套件加入addons_requrements.txt
3. 執行指令以啟動測試環境：

```shell
docker compose up
```

## 注意事項：
- 由於抓不到你建立的db名稱，所以healthcheck時可能會報錯：
```bash
FATAL:  database "odoo" does not exist #在docker-compose.yml中設定你指定的名稱即可
```


- dockerfile有進行過修改，會複製addons資料夾中的檔案進行build，並且使用20230825版本
- volume有連接config/odoo.conf，所以運行過後設定會被加入密鑰和初始不一樣
- odoo.conf可以參考[這裡](https://www.cybrosys.com/odoo/odoo-books/odoo-16-development/setup-development-environment/conf-file/)

## 參考資料：
- [感謝twtrubiks的系列教學](https://github.com/twtrubiks/odoo-docker-tutorial)
- [官方的dockerfile](https://github.com/odoo/docker)