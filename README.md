# x86架構下的版本
於x86/AMD64運行版本，請檢查運行電腦的晶片架構

M系列mac 或 arm架構電腦 無法運行，請使用另一個banch

## 步驟：
1. 把需要測試的addons放入extra-addons資料夾
2. 把addons所需的額外套件加入extra-addons_requrements.txt
3. 執行指令以啟動測試環境：

```shell
docker compose up
```

## 注意事項：
- 由於抓不到你建立的db名稱，所以healthcheck時可能會報錯：
```bash
FATAL:  database "odoo" does not exist #在docker-compose.yml中設定你指定的名稱即可
```

- dockerfile有進行過修改，會複製extra-addons資料夾中的檔案進行build，並且使用20230825版本
- 並且首次啟動過程中會重新啟動並自動安裝extra-addons內的套件
- volume有連接config/odoo.conf，所以運行過後設定會被加入密鑰和初始不一樣
- odoo.conf可以參考[這裡](https://www.cybrosys.com/odoo/odoo-books/odoo-16-development/setup-development-environment/conf-file/)

## 參考資料：
- [感謝twtrubiks的系列教學](https://github.com/twtrubiks/odoo-docker-tutorial)
- [官方的dockerfile](https://github.com/odoo/docker)
