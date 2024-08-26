from datetime import datetime
from tableauhyperapi import Connection, HyperProcess, SqlType, TableDefinition, Inserter, CreateMode, TableName, Telemetry
current_date = datetime.now()

hyper = HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU)
hyper_conn = Connection(hyper.endpoint, 'BACDEMO.hyper', CreateMode.NONE)

with Inserter(hyper_conn, TableName('Extract','BACDEMO')) as inserter:
    for i in range (101, 106):
        inserter.add_row(
            [ i, "Row " + str(i) , current_date]
    )
    inserter.execute()


print("Hyper File BACDEMO.hyper Updated !")

inserter.close()
hyper_conn.close()
hyper.close()