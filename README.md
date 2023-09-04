# Odoo addons Automate CI branch

## 步驟：
1. 將完成的addons上傳至addons資料夾中
2. 把addons所需的額外套件加入addons_requrements.txt
3. Github Actions將會自動執行測試
4. 檢視結果

## 程式：

## 注意事項：


- dockerfile有進行過修改，會複製addons資料夾中的檔案進行build，並且使用20230825版本
- volume有連接config/odoo.conf，所以運行過後設定會被加入密鑰和初始不一樣
- odoo.conf可以參考[這裡](https://www.cybrosys.com/odoo/odoo-books/odoo-16-development/setup-development-environment/conf-file/)

## 參考資料：
- [感謝twtrubiks的系列教學](https://github.com/twtrubiks/odoo-docker-tutorial)
- [官方的dockerfile](https://github.com/odoo/docker)