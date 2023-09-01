# docker-compose並載入addons測試的環境

注意：ARM處理器(Mac M系列)無法運行，因為套件wkhtmltopdf無法在ARM上運行([見](https://github.com/wkhtmltopdf/packaging/issues/98))

## 步驟：

1. 把需要測試的addons放入addons資料夾
2. 把addons所需的額外套件加入addons_requrements.txt
3. 建立.env檔案，並設定所需的odoo.conf
4. 執行指令以啟動測試環境：

```shell
docker-compose up
```

## 注意事項：

- dockerfile有進行過修改，會複製addons資料夾中的檔案進行build，並且使用20230825版本
- volume有連接config/odoo.conf，所以運行過後設定會被加入密鑰和初始不一樣

## 參考資料：

- [感謝twtrubiks的系列教學](https://github.com/twtrubiks/odoo-docker-tutorial)
- [官方的dockerfile](https://github.com/odoo/docker)