from datetime import datetime
from tableauhyperapi import Connection, HyperProcess, SqlType, TableDefinition, Inserter, CreateMode, TableName, Telemetry

current_date = datetime.now()

hyper = HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU)
hyper_conn = Connection(hyper.endpoint, 'BACDEMO.hyper', CreateMode.CREATE_AND_REPLACE)
hyper_conn.catalog.create_schema('Extract')

table = TableDefinition(TableName('Extract','BACDEMO'), [
    TableDefinition.Column('row_id', SqlType.big_int()),
    TableDefinition.Column('row_name', SqlType.varchar(100)),
    TableDefinition.Column('row_update', SqlType.timestamp()),
])


hyper_conn.catalog.create_table(table)

with Inserter(hyper_conn, table) as inserter:
    for i in range (1, 101):
        inserter.add_row(
            [ i, "Row " + str(i) , current_date]
    )
    inserter.execute()


print("Hyper File BACDEMO.hyper Created !")

hyper_conn.close()
hyper.close()



