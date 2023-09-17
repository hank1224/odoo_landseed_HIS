# Odoo addons Automate CICD branch

**注意：ARM處理器(Mac M系列)無法運行**，因為套件wkhtmltopdf無法在ARM上運行([見](https://github.com/wkhtmltopdf/packaging/issues/98))

## 步驟：
1. 將完成的套件上傳至extra-addons資料夾中
2. 把extra-addons所需的額外套件加入addons_requrements.txt
3. Github Actions將會自動執行測試
4. 檢視結果


## Github Actions會執行步驟：
1. build 20230825的odoo環境
2. 用odoo主程式初始化資料庫後停止
3. 重新啟動odoo，並安裝extra-addons資料夾內的套件，安裝時會自動執行測試
4. 結束


## 注意事項：
- dockerfile有進行過修改，會複製addons資料夾中的檔案進行build，並且使用20230825版本
- volume有連接config/odoo.conf，所以運行過後設定會被加入密鑰
- odoo.conf可以參考[這裡](https://www.cybrosys.com/odoo/odoo-books/odoo-16-development/setup-development-environment/conf-file/)


## 參考資料：
- [感謝twtrubiks的系列教學](https://github.com/twtrubiks/odoo-docker-tutorial)
- [官方的dockerfile](https://github.com/odoo/docker)