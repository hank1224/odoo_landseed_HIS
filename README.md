# odoo16的source code安裝方式

**！！務必閱讀官方文檔，三個系統安裝方式皆不同！！**

- [source安裝](https://www.odoo.com/documentation/16.0/administration/install/source.html)

## 先docker建psql和hapi：

```bash
docker compose up -f docker-compose.yml
```
volume會建立在本地的.docker-volumes資料夾

## 安裝odoo依賴：
基本都必須用

```bash
pip install -r requirements.txt
```

視系統不同需要額外步驟，請參考官方文檔

## 選擇安裝odoo：
1. 直接用這包repo，繼續下一步

2. 僅windows可使用exe拆包方式，完美避雷（[教學文章已遺失](https://stackoverflow.com/questions/75569858how-to-install-odoo-on-windows-along-with-other-version-and-run-it-without-error)）

## 啟動：
首次啟動odoo請使用：`python odoo-bin --db_host=localhost --db_user 資料庫帳號 --db_password 資料庫密碼`

（若odoo使用UNIX socket就不設定 --db_host=localhost ）

用此指令第一次進入後他會叫你建資料庫名稱和admin帳號

**如果直接給予db_name，odoo會自動建立資料庫，並且帳號密碼預設admin**

之後進入可以搭配下面的參數一起使用

開發時可以善用以下啟動參數：

- `--dev=all`： 啟動開發模式，會有debug模式和開發者模式
- `--init=模組名稱`： 安裝某個模組
- `--update=模組名稱`： 更新某個模組
- 若要刪除模組僅能進去用手刪除

也可以建立odoo.conf來存放多個啟動參數，使用 `-c odoo.conf` 啟動時載入，見odoo.conf.example
- `--db_user=資料庫帳號`
- `--db_password=資料庫密碼`
- `--db_host=localhost`
- `--without-demo=all`： 初次建立資料庫時不安裝demo資料

## 其他
若要刪除odoo資料庫：

```bash
docker compose down
docker volume rm odoo-db-data
```

嫌麻煩建議改使用docker方式安裝，良心建議

## Reference：

- [source安裝](https://www.odoo.com/documentation/16.0/administration/install/source.html)
- [啟動參數](https://www.odoo.com/documentation/16.0/developer/reference/cli.html)