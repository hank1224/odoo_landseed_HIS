# Odoo addons Automate CI branch

## 步驟：
1. 將完成的addons上傳至addons資料夾中
2. 把addons所需的額外套件加入addons_requrements.txt
3. Github Actions將會自動執行測試
4. 檢視結果

## Github Actions會執行步驟：
1. build 20230825的odoo環境
2. 用odoo主程式初始化資料庫後停止
3. 重新啟動odoo，並安裝addons資料夾內的套件，安裝時會自動執行測試
4. 結束