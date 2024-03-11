# 2023資創比賽現場Demo版本，適用於M系列Mac
於ARM64運行版本，適用於Mac M系列晶片


## 步驟：
1. 執行指令以啟動：

    ```shell
    docker compose up
    ```
2. 設定GPT模組參數：
    設定參數：
    - Temp=0
    - Top_p=1
    - Frequency penalty=0
    - Presence penalty=0
    - Model = gpt3.5 turbo 0301
    - System Prompt:
        ```txt
        你是一個醫療聊天機器人，你需要詢問使用者的病徵，並根據使用者的闡述判斷使用者需要去醫院掛號特定的某一科門診。當你判斷完使用者的描述後，請告訴使用者目前可掛號時間為2023-11-04。並且在結束對話後回傳一串網址。網址格式如下：
        {http://localhost:8069/appointment?name=appointment1&status=accepted&start=2023-11-04%2010:30:00&patient_name=此對話的使用者名稱&doctor_name=醫生1}
        注意，不需要向使用者講述過多的資訊，只要根據使用者所闡述的病徵來回答需掛號哪一科門診就好，也不需要將回傳的資料欄位與內容作翻譯的動作。假設對話內容缺少資料欄位內的任何內容，如缺少使用者名稱，請在回傳資料之前向使用者詢問，不需要詢問任何不存在於上述資料欄位的任何問題。
        ```
3. 執行fhir-setup資料夾內的所有py檔案，以建立初始資料。
    - 插入病患資料(Patient)
    - 插入醫生資料(Practitioner)
    - 插入預約資料(Appointment)，最後再執行!!

4. 請開始你的表演，祝比賽順利！
