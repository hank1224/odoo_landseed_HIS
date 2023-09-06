# odoo16的source code安裝方式

先安裝psql，可用 docker 或 直接安裝

- docker：需要把port映射出來，映射出來的話是localhost:5432
- 直接安裝：注意odoo預設使用UNIX socket連線，在odoo.conf設定 --db_host=localhost 即可更改

再安裝odoo：

- source code：需要先pip安裝環境，不同平台套件容易不支援
- exe拆包：不需要安裝環境，但只能在Windows上使用（[參考連結](https://stackoverflow.com/questions/75569858how-to-install-odoo-on-windows-along-with-other-version-and-run-it-without-error)）

## Dev環境安裝建議：

odoo使用：

- Windows: exe安裝後拆來用(完美避雷)
- MacOS: source code
- Linux/Ubuntu: source code

psql使用：

- docker 或 直接安裝 都可以看習慣

用docker啟動psql：

```bash
# 位置psql_docker
docker compose up
```

若要刪除或重建資料庫：

```bash
# 位置psql_docker
docker compose down
docker volume rm psql_docker_odoo-db-data
```

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

## Reference：

- [source安裝](https://www.odoo.com/documentation/16.0/administration/install/source.html)
- [啟動參數](https://www.odoo.com/documentation/16.0/developer/reference/cli.html)